"""Pure read-back planner. No I/O, writes, retries, permissions or scheduler calls."""
from __future__ import annotations

import re
from collections.abc import Mapping


def plan_recovery(expected: Mapping[str, str], observed: Mapping[str, Mapping], *,
                  repository_verified: bool = False, write_authorized: bool = False,
                  safety_blocked: bool = False) -> dict:
    """Compare frozen expected SHA-256 digests with fresh, same-repository reads.

    An 'absent' observation must be a verified absence, not an ambiguous 404.
    Calling this function does not obtain any of those proofs or execute its plan.
    """
    if not expected or any(not isinstance(k, str) or not k for k in expected):
        raise ValueError("Expected a nonempty manifest with string destinations")
    if any(not isinstance(v, str) or not re.fullmatch(r"[0-9a-f]{64}", v)
           for v in expected.values()):
        raise ValueError("Expected lowercase SHA-256 digests")
    if any(type(v) is not bool for v in
           (repository_verified, write_authorized, safety_blocked)):
        raise ValueError("Evidence flags must be booleans")
    files = {}
    for path, digest in sorted(expected.items()):
        observation = observed.get(path, {})
        state = observation.get("state", "unknown")
        if state == "present":
            actual = observation.get("sha256")
            if not isinstance(actual, str) or not re.fullmatch(r"[0-9a-f]{64}", actual):
                files[path] = "unknown"
            else:
                files[path] = "verified" if actual == digest else "conflict"
        elif state == "absent" and observation.get("absence_verified") is True:
            files[path] = "missing"
        else:
            files[path] = "unknown"
    states = set(files.values())
    if safety_blocked or not repository_verified or not write_authorized:
        status = "blocked"
    elif "conflict" in states:
        status = "conflict"
    elif "unknown" in states:
        status = "uncertain"
    elif "missing" in states:
        status = "resume_missing"
    else:
        status = "complete"
    return {"status": status, "files": files,
            "create_only": [p for p, s in files.items() if s == "missing"]
            if status == "resume_missing" else [],
            "overwrite": [], "automatic_retry": False}
