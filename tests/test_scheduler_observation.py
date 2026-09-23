"""Synthetic delayed-observation cases. No actual scheduler invocation."""
import copy
import unittest
from tools.scheduler_observation import observe_occurrence


class SchedulerObservationTests(unittest.TestCase):
    def setUp(self):
        self.expected = dict(task_id="TEST-TASK", operation_id="TEST-OCCURRENCE", instruction_sha="a" * 40,
                             scheduled_for="2026-01-01T10:00:00Z", observed_at="2026-01-01T10:09:00Z")
        self.native = dict(task_id="TEST-TASK", task_verified=True, is_enabled=True, last_run_time=None)
        self.receipt = dict(task_id="TEST-TASK", operation_id="TEST-OCCURRENCE", instruction_sha="a" * 40,
                            surface="scheduled", status="complete", receipt_validation_passed=True,
                            connectors_verified=True, coverage_verified=True, private_readback_verified=True)

    def observe(self, receipt=None):
        return observe_occurrence(self.expected, self.native, receipt)

    def test_due_without_run_is_uncertain_never_replayed(self):
        p = self.observe()
        self.assertEqual(p["state"], "scheduler_run_uncertain")
        self.assertFalse(p["scheduled_cycle_verified"])
        for field in ("automatic_retry", "automatic_reschedule", "create_replacement"):
            self.assertFalse(p[field])

    def test_not_due_is_only_created(self):
        self.expected["observed_at"] = "2026-01-01T09:59:00Z"
        self.assertEqual(self.observe()["state"], "scheduler_created")

    def test_valid_receipt_can_precede_native_observability(self):
        self.assertTrue(self.observe(self.receipt)["scheduled_cycle_verified"])
        self.native["is_enabled"] = False  # A finished one-shot may be inactive.
        self.assertTrue(self.observe(self.receipt)["scheduled_cycle_verified"])

    def test_native_timestamp_alone_is_not_occurrence_proof(self):
        self.native["last_run_time"] = "2026-01-01T10:03:00Z"
        self.assertEqual(self.observe()["state"], "scheduler_run_uncertain")
        self.native["occurrence_verified"] = True
        self.assertEqual(self.observe()["state"], "scheduler_run_observed_unverified")

    def test_old_task_occurrence_revision_or_interactive_receipt_rejected(self):
        for key, value in (("task_id", "OTHER"), ("operation_id", "OLD"),
                           ("instruction_sha", "b" * 40), ("surface", "chat")):
            receipt = dict(self.receipt, **{key: value})
            self.assertEqual(self.observe(receipt)["state"], "scheduler_evidence_mismatch")

    def test_each_required_proof_is_checked(self):
        for field in ("receipt_validation_passed", "connectors_verified",
                      "coverage_verified", "private_readback_verified"):
            receipt = dict(self.receipt, **{field: False})
            self.assertFalse(self.observe(receipt)["scheduled_cycle_verified"])

    def test_partial_busy_and_blocked_are_not_pass(self):
        for status in ("incomplete", "busy", "blocked"):
            self.assertFalse(self.observe(dict(self.receipt, status=status))["scheduled_cycle_verified"])

    def test_unverified_native_task_is_not_created_proof(self):
        self.native["task_verified"] = False
        self.assertEqual(self.observe(self.receipt)["state"], "scheduler_configuration_unverified")

    def test_timezones_and_future_evidence(self):
        self.expected["scheduled_for"] = "2026-01-01T11:00:00+01:00"
        self.assertEqual(self.observe()["state"], "scheduler_run_uncertain")
        self.native["last_run_time"] = "2026-01-01T12:00:00Z"
        self.assertEqual(self.observe()["state"], "scheduler_evidence_mismatch")
        self.expected["observed_at"] = "2026-01-01T10:09:00"
        with self.assertRaises(ValueError):
            self.observe()

    def test_inputs_unchanged(self):
        before = copy.deepcopy((self.expected, self.native, self.receipt))
        self.observe(self.receipt)
        self.assertEqual((self.expected, self.native, self.receipt), before)


if __name__ == "__main__":
    unittest.main()
