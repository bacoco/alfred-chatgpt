"""Validate identity projections only; do not infer semantic matches or write state."""
from __future__ import annotations

from collections.abc import Mapping, Sequence


def identity_errors(cases: Sequence[Mapping], previous: Sequence[Mapping] = (), *,
                    authorized_reopens: frozenset[str] = frozenset()) -> list[str]:
    """Check a proposed projection of existing cases and its provenance continuity.

    Each projection has case_id, canonical_case_id, source_refs (namespaced strings),
    aliases and status. Permission and semantic evidence are checked by Chat first.
    This function does not obtain or grant authority through authorized_reopens.
    """
    errors, by_id = [], {}
    for case in cases:
        if not isinstance(case, Mapping):
            errors.append("Invalid case projection")
            continue
        identifier = case.get("case_id")
        if not isinstance(identifier, str) or not identifier:
            errors.append("Missing case_id")
            continue
        if identifier in by_id:
            errors.append("Duplicate case_id: " + identifier)
        by_id[identifier] = case
        for field in ("source_refs", "aliases"):
            values = case.get(field)
            if (not isinstance(values, list) or
                    any(not isinstance(v, str) or not v for v in values)):
                errors.append(identifier + ": invalid " + field)
            elif len(values) != len(set(values)):
                errors.append(identifier + ": duplicate " + field)
        if not isinstance(case.get("status"), str) or not case["status"]:
            errors.append(identifier + ": missing status")
    if errors:
        return sorted(set(errors))
    for identifier, case in by_id.items():
        root_id = case.get("canonical_case_id")
        root = by_id.get(root_id) if isinstance(root_id, str) else None
        if root is None or root.get("canonical_case_id") != root_id:
            errors.append(identifier + ": dangling or noncanonical target")
            continue
        if root_id != identifier:
            if not isinstance(case.get("identity_reason"), str) or not case["identity_reason"].strip():
                errors.append(identifier + ": merge reason required")
            if identifier not in root["aliases"]:
                errors.append(identifier + ": missing canonical alias")
            if not set(case["source_refs"]) <= set(root["source_refs"]):
                errors.append(identifier + ": provenance missing at canonical case")
        for alias in case["aliases"]:
            target = by_id.get(alias)
            if (alias == identifier or target is None or
                    target.get("canonical_case_id") != identifier or root_id != identifier):
                errors.append(identifier + ": invalid alias " + alias)
    old_errors = identity_errors(previous) if previous else []
    if old_errors:
        return sorted(set(errors + ["Invalid previous projection: " + e for e in old_errors]))
    all_refs = {ref for case in cases for ref in case["source_refs"]}
    for old in previous:
        identifier = old["case_id"]
        current = by_id.get(identifier)
        if current is None:
            errors.append(identifier + ": identity removed; preserve an audit record")
        elif (old["status"] in ("resolved", "dropped", "snoozed") and
              current["status"] != old["status"] and identifier not in authorized_reopens):
            errors.append(identifier + ": protected decision changed without authority")
        if not set(old["source_refs"]) <= all_refs:
            errors.append(identifier + ": source provenance lost")
    return sorted(set(errors))
