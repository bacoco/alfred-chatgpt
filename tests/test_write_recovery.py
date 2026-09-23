"""Synthetic recovery decisions; never exercise a real platform safety refusal."""
import copy
import unittest
from tools.write_recovery import plan_recovery

A, B = "a" * 64, "b" * 64


class WriteRecoveryTests(unittest.TestCase):
    def plan(self, observed, **flags):
        options = dict(repository_verified=True, write_authorized=True)
        options.update(flags)
        return plan_recovery({"state/cases.json": A}, observed, **options)

    def test_matching_write_is_not_replayed(self):
        p = self.plan({"state/cases.json": {"state": "present", "sha256": A}})
        self.assertEqual(p["status"], "complete")
        self.assertEqual(p["create_only"], [])

    def test_verified_absence_is_only_create_candidate(self):
        p = self.plan({"state/cases.json": {"state": "absent", "absence_verified": True}})
        self.assertEqual(p["create_only"], ["state/cases.json"])
        self.assertFalse(p["automatic_retry"])
        self.assertEqual(p["overwrite"], [])

    def test_changed_existing_file_blocks_all_writes(self):
        p = self.plan({"state/cases.json": {"state": "present", "sha256": B}})
        self.assertEqual(p["status"], "conflict")
        self.assertEqual(p["create_only"], [])

    def test_unknown_unreadable_or_ambiguous_absence_is_not_missing(self):
        for observation in ({}, {"state": "unreadable"}, {"state": "absent"},
                            {"state": "present", "sha256": None}):
            with self.subTest(observation=observation):
                p = self.plan({"state/cases.json": observation})
                self.assertEqual(p["status"], "uncertain")
                self.assertEqual(p["create_only"], [])

    def test_safety_refusal_is_not_retry_authority(self):
        p = self.plan({"state/cases.json": {"state": "absent", "absence_verified": True}},
                      safety_blocked=True)
        self.assertEqual(p["status"], "blocked")
        self.assertEqual(p["create_only"], [])

    def test_default_and_revoked_authority_block(self):
        for flags in ({"repository_verified": False}, {"write_authorized": False}):
            self.assertEqual(self.plan({}, **flags)["status"], "blocked")
        self.assertEqual(plan_recovery({"x": A}, {})["status"], "blocked")

    def test_partial_manifest_preserves_existing_and_input(self):
        actual = {"a": {"state": "present", "sha256": A},
                  "b": {"state": "absent", "absence_verified": True}}
        before = copy.deepcopy(actual)
        p = plan_recovery({"b": B, "a": A}, actual,
                          repository_verified=True, write_authorized=True)
        self.assertEqual(p["create_only"], ["b"])
        self.assertEqual(actual, before)
        self.assertEqual(list(p["files"]), ["a", "b"])

    def test_invalid_inputs_are_rejected(self):
        for expected in ({}, {"x": "not-a-digest"}):
            with self.assertRaises(ValueError):
                plan_recovery(expected, {})
        with self.assertRaises(ValueError):
            self.plan({}, safety_blocked="false")


if __name__ == "__main__":
    unittest.main()
