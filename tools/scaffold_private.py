"""Render ALFRED's private scaffold offline; never call GitHub or a scheduler."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Mapping

KIT = "bacoco/alfred-chatgpt"
VARIABLES = {"PRIVATE_REPO", "PRIVATE_BRANCH", "KIT_SHA", "INSTALLATION_ID", "RENDERED_AT_UTC"}
MARKER = re.compile(r"\{\{([A-Z_]+)\}\}")
REPO = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]{0,38}/[A-Za-z0-9_.-]{1,100}")
BRANCH = re.compile(r"[A-Za-z0-9][A-Za-z0-9_./-]{0,150}")


def _path(value: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value or ":" in value:
        raise ValueError("Invalid relative path")
    parts = value.split("/")
    if any(x in ("", ".", "..") or x.casefold() in (".git", ".github") for x in parts):
        raise ValueError("Unsafe path")
    if str(PurePosixPath(value)) != value:
        raise ValueError("Non-canonical path")
    return value


def validate_parameters(parameters: Mapping[str, str]) -> None:
    if set(parameters) != VARIABLES or any(not isinstance(v, str) for v in parameters.values()):
        raise ValueError("Provide exactly the five documented string parameters")
    repo = parameters["PRIVATE_REPO"]
    if not REPO.fullmatch(repo) or repo.split("/")[1] in (".", "..") or repo.casefold() == KIT.casefold():
        raise ValueError("Invalid private repository, or target equals public kit")
    branch = parameters["PRIVATE_BRANCH"]
    if (not BRANCH.fullmatch(branch) or ".." in branch or "//" in branch
            or branch.endswith((".", "/"))
            or any(p.startswith(".") or p.endswith(".lock") for p in branch.split("/"))):
        raise ValueError("Invalid branch")
    if not re.fullmatch(r"[0-9a-f]{40}", parameters["KIT_SHA"]):
        raise ValueError("KIT_SHA must be a resolved 40-character lowercase SHA")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{7,79}", parameters["INSTALLATION_ID"]):
        raise ValueError("Invalid installation ID")
    timestamp = parameters["RENDERED_AT_UTC"]
    if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d{1,6})?Z", timestamp):
        raise ValueError("Use a UTC ISO 8601 timestamp ending in Z")
    if datetime.fromisoformat(timestamp.replace("Z", "+00:00")).tzinfo != timezone.utc:
        raise ValueError("Expected UTC")


def render(root: Path, parameters: Mapping[str, str]) -> dict[str, str]:
    """Return validated UTF-8 target files, without filesystem or account writes."""
    validate_parameters(parameters)
    root = root.resolve()
    manifest = json.loads((root / "templates/private/manifest.json").read_text(encoding="utf-8"))
    if (manifest.get("schema_version") != 1 or manifest.get("required_visibility") != "private"
            or set(manifest.get("variables", [])) != VARIABLES):
        raise ValueError("Unsupported scaffold manifest")
    prefix = _path(manifest["source_root"]) + "/"
    if prefix != "templates/private/files/":
        raise ValueError("Unexpected template root")
    outputs: dict[str, str] = {}
    folded: set[str] = set()
    for entry in manifest["files"]:
        source, target = _path(entry["source"]), _path(entry["target"])
        if source != prefix + target or target.casefold() in folded:
            raise ValueError("Invalid mapping or duplicate destination")
        path = root / source
        if any((root / Path(*Path(source).parts[:i])).is_symlink() for i in range(1, len(Path(source).parts)+1)):
            raise ValueError("Symlinks are not supported")
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != entry["sha256"]:
            raise ValueError("Template integrity mismatch: " + source)
        text = MARKER.sub(lambda match: parameters[match[1]], data.decode("utf-8"))
        if "{{" in text or "}}" in text:
            raise ValueError("Unresolved template variable")
        if target.endswith(".json"):
            json.loads(text)
        outputs[target] = text
        folded.add(target.casefold())
    control = json.loads(outputs["state/control.json"])
    if control["mode"] != "storage_only" or any(control[k] for k in
            ("live_processing_enabled", "scheduler_enabled", "external_actions_enabled")):
        raise ValueError("Scaffold must be inactive")
    if control["source_accounts"] or control["active_mandates"]:
        raise ValueError("No real accounts or mandates in a template")
    if any(path not in outputs for path in control["state_paths"].values()):
        raise ValueError("Missing referenced private file")
    for path, key in (("state/cases.json", "cases"), ("state/decisions.json", "decisions"),
                      ("state/subscriptions.json", "subscriptions")):
        if json.loads(outputs[path])[key]:
            raise ValueError("Business registers must start empty")
    if any(t["enabled"] for t in json.loads(outputs["state/tasks.json"])["tasks"]):
        raise ValueError("Initial task must be inactive")
    return outputs


def write_new(outputs: Mapping[str, str], destination: Path) -> None:
    """Use a new directory only. On a partial failure, leave evidence, never reset."""
    destination = Path(destination)
    for path in outputs:
        _path(path)
    destination.mkdir(parents=True, exist_ok=False)
    for relative, text in outputs.items():
        path = destination / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parameters", required=True, type=Path, help="JSON file with the five technical variables")
    parser.add_argument("--output", required=True, type=Path, help="New local directory; never an existing instance")
    args = parser.parse_args()
    try:
        parameters = json.loads(args.parameters.read_text(encoding="utf-8"))
        outputs = render(Path(__file__).resolve().parents[1], parameters)
        write_new(outputs, args.output)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print("Scaffold not completed: " + str(exc), file=sys.stderr)
        return 1
    print(json.dumps({"status": "RENDERED_LOCALLY", "file_count": len(outputs),
                      "github_repository_created": False, "scheduler_created": False}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
