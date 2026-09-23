"""Read-only occurrence classifier: no scheduling, retry, notification or I/O."""
from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
import re


def _time(value: str) -> datetime:
    if not isinstance(value, str):
        raise ValueError("Expected an explicit timestamp")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("Timestamp must include its timezone")
    return parsed


def observe_occurrence(expected: Mapping, native: Mapping, receipt: Mapping | None = None) -> dict:
    """Classify one immutable task/occurrence/kit identity from supplied evidence.

    Verification flags require real reads and validation outside this pure helper.
    An old last_run_time, an interactive receipt or a created task never proves PASS.
    """
    for key in ("task_id", "operation_id", "instruction_sha"):
        if not isinstance(expected.get(key), str) or not expected[key]:
            raise ValueError("Missing occurrence identity: " + key)
    if not re.fullmatch(r"[0-9a-f]{40}", expected["instruction_sha"]):
        raise ValueError("Expected a pinned instruction SHA")
    due, now = _time(expected["scheduled_for"]), _time(expected["observed_at"])

    def result(state, verified=False):
        return {"state": state, "scheduled_cycle_verified": verified,
                "automatic_retry": False, "automatic_reschedule": False,
                "create_replacement": False}

    if native.get("task_verified") is not True or native.get("task_id") != expected["task_id"]:
        return result("scheduler_configuration_unverified")
    if receipt is not None:
        same = (receipt.get("surface") == "scheduled" and all(
            receipt.get(key) == expected[key] for key in ("task_id", "operation_id", "instruction_sha")))
        if not same:
            return result("scheduler_evidence_mismatch")
        if receipt.get("receipt_validation_passed") is not True:
            return result("scheduler_run_uncertain")
        state = receipt.get("status")
        if state in ("blocked", "busy", "incomplete"):
            return result({"blocked": "scheduler_run_blocked", "busy": "scheduler_run_busy",
                           "incomplete": "scheduler_run_partial"}[state])
        if state == "complete" and all(receipt.get(key) is True for key in
                ("connectors_verified", "coverage_verified", "private_readback_verified")):
            return result("scheduled_cycle_verified", True)
        return result("scheduler_run_observed_unverified")
    last_run = native.get("last_run_time")
    if last_run is not None:
        timestamp = _time(last_run)
        if timestamp > now:
            return result("scheduler_evidence_mismatch")
        if native.get("occurrence_verified") is True:
            return result("scheduler_run_observed_unverified")
    return result("scheduler_run_uncertain" if now >= due else "scheduler_created")
