"""Offline scaffold tests: fictitious identities; no connected-account actions."""
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from tools.scaffold_private import render, validate_parameters, write_new

ROOT = Path(__file__).resolve().parents[1]
PARAMS = {"PRIVATE_REPO": "example-user/alfred-memory", "PRIVATE_BRANCH": "main",
          "KIT_SHA": "a" * 40, "INSTALLATION_ID": "synthetic-install-001",
          "RENDERED_AT_UTC": "2026-09-22T00:00:00Z"}


class ScaffoldTests(unittest.TestCase):
    def test_all_sixteen_files_render(self):
        outputs = render(ROOT, PARAMS)
        self.assertEqual(len(outputs), 16)
        for path, text in outputs.items():
            self.assertNotIn("{{", text)
            if path.endswith(".json"):
                self.assertIsInstance(json.loads(text), dict)

    def test_initial_permissions_and_registers_empty(self):
        out = render(ROOT, PARAMS)
        control = json.loads(out["state/control.json"])
        self.assertFalse(control["live_processing_enabled"])
        self.assertFalse(control["scheduler_enabled"])
        self.assertFalse(control["external_actions_enabled"])
        self.assertEqual(control["active_mandates"], [])
        self.assertEqual(control["source_accounts"], [])
        self.assertEqual(json.loads(out["memory/profile.json"])["confirmed_preferences"], [])
        self.assertEqual(json.loads(out["state/checkpoints.json"])["sources"], {})

    def test_no_fabricated_verification(self):
        out = render(ROOT, PARAMS)
        setup = json.loads(out["state/setup.json"])
        for key, value in setup.items():
            if key.endswith("verified") or key in ("scope_approved", "scheduler_created"):
                self.assertIs(value, False)
        self.assertIsNone(json.loads(out["state/tasks.json"])["native_scheduler"]["task_id"])
        self.assertTrue(json.loads(out["tests/fixtures/storage-probe.json"])["synthetic"])

    def test_parameters_used_consistently(self):
        out = render(ROOT, PARAMS)
        self.assertIn(PARAMS["PRIVATE_REPO"], out["README.md"])
        self.assertEqual(json.loads(out["state/control.json"])["private_storage"]["repository"], PARAMS["PRIVATE_REPO"])
        self.assertEqual(json.loads(out["state/setup.json"])["kit_commit"], PARAMS["KIT_SHA"])

    def test_reject_public_kit_as_destination(self):
        with self.assertRaises(ValueError):
            render(ROOT, {**PARAMS, "PRIVATE_REPO": "BaCoCo/ALFRED-CHATGPT"})

    def test_parameter_injection_rejected(self):
        for value in ('owner/repo\"', '../repo', 'owner/repo;curl', 'owner/repo\n', 'owner/..'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_parameters({**PARAMS, "PRIVATE_REPO": value})

    def test_bad_branches_rejected(self):
        for branch in ('../main', '/main', 'main.lock', 'a//b', 'a/../b', 'a/.hidden'):
            with self.subTest(branch=branch), self.assertRaises(ValueError):
                validate_parameters({**PARAMS, "PRIVATE_BRANCH": branch})

    def test_bad_sha_time_and_extra_variable_rejected(self):
        for patch in ({"KIT_SHA": "main"}, {"RENDERED_AT_UTC": "yesterday"},
                      {"RENDERED_AT_UTC": "2026-02-30T00:00:00Z"}, {"EXTRA": "x"}):
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                validate_parameters({**PARAMS, **patch})

    def changed_copy(self, directory):
        copy = Path(directory) / "kit"
        shutil.copytree(ROOT / "templates", copy / "templates")
        return copy, copy / "templates/private/manifest.json"

    def test_integrity_tampering_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            copy, _ = self.changed_copy(directory)
            (copy / "templates/private/files/state/control.json").write_text("{}")
            with self.assertRaises(ValueError):
                render(copy, PARAMS)

    def test_duplicate_and_unsafe_paths_rejected(self):
        for target in ("../escape", "/absolute", ".github/workflows/run.yml", "README.md"):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as directory:
                copy, manifest_path = self.changed_copy(directory)
                manifest = json.loads(manifest_path.read_text())
                entry = dict(manifest["files"][0], target=target)
                manifest["files"].append(entry)
                manifest_path.write_text(json.dumps(manifest))
                with self.assertRaises(ValueError):
                    render(copy, PARAMS)

    def test_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            copy, _ = self.changed_copy(directory)
            path = copy / "templates/private/files/README.md"
            saved = copy / "outside.md"
            path.rename(saved)
            path.symlink_to(saved)
            with self.assertRaises(ValueError):
                render(copy, PARAMS)

    def test_initial_files_can_be_written_and_read_back(self):
        with tempfile.TemporaryDirectory() as directory:
            out = render(ROOT, PARAMS)
            destination = Path(directory) / "new-instance"
            write_new(out, destination)
            for path, text in out.items():
                self.assertEqual((destination / path).read_text(), text)

    def test_existing_instance_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "instance"
            out = render(ROOT, PARAMS)
            write_new(out, destination)
            target = destination / "state/cases.json"
            target.write_text('{"cases":["keep-existing"]}')
            with self.assertRaises(FileExistsError):
                write_new(out, destination)
            self.assertEqual(target.read_text(), '{"cases":["keep-existing"]}')

    def test_manifest_covers_state_paths_and_disabled_template(self):
        out = render(ROOT, PARAMS)
        control = json.loads(out["state/control.json"])
        self.assertTrue(set(control["state_paths"].values()) <= set(out))
        task = json.loads(out["state/tasks.json"])["tasks"][0]
        self.assertEqual(task["template_id"], "briefing")
        self.assertFalse(task["enabled"])
        self.assertIsNone(task["source_account_id"])
        self.assertIsNone(task["schedule"]["timezone"])


if __name__ == "__main__":
    unittest.main()
