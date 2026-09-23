"""Synthetic onboarding observations, including Only select repositories."""
import copy
import unittest
from tools.installation_diagnostics import diagnose_repository


class InstallationDiagnosticsTests(unittest.TestCase):
    def facts(self, **changes):
        data = dict(exists=True, accessible=True, private=True, owner_matches=True,
                    can_write=True, empty=False, scaffold="complete", storage_readback_verified=True)
        data.update(changes)
        return data

    def test_absent_repository_creation_is_distinct_from_file_write(self):
        data = self.facts(exists=False, accessible=False, absence_verified=True)
        self.assertEqual(diagnose_repository(data)["actor"], "owner")
        data["can_create_repository"] = True
        self.assertEqual(diagnose_repository(data)["actor"], "chat")

    def test_ambiguous_404_does_not_create_repository(self):
        data = self.facts(exists=False, accessible=False, absence_verified=False)
        self.assertEqual(diagnose_repository(data)["state"], "access_unknown")

    def test_public_target_blocks(self):
        p = diagnose_repository(self.facts(private=False))
        self.assertEqual(p["state"], "public_repository")
        self.assertEqual(p["actor"], "owner")
        self.assertFalse(p["change_permissions"])

    def test_only_select_repositories_requires_positive_evidence(self):
        p = diagnose_repository(self.facts(accessible=False, github_app_excluded=True))
        self.assertEqual(p["state"], "private_not_selected")
        p = diagnose_repository(self.facts(accessible=False, github_app_excluded=None))
        self.assertEqual(p["state"], "access_unknown")

    def test_empty_private_repository_is_recoverable(self):
        for capability, actor in ((True, "chat"), (False, "owner")):
            p = diagnose_repository(self.facts(empty=True, can_initialize=capability))
            self.assertEqual(p["state"], "empty_private_repository")
            self.assertEqual(p["actor"], actor)

    def test_partial_and_missing_readback_never_activate(self):
        for data, expected in ((self.facts(scaffold="partial"), "partial_scaffold"),
                               (self.facts(storage_readback_verified=False), "readback_required")):
            p = diagnose_repository(data)
            self.assertEqual(p["state"], expected)
            self.assertFalse(p["activate_business"])

    def test_verified_storage_resumes_without_reset(self):
        p = diagnose_repository(self.facts())
        self.assertEqual(p["next_action"], "resume_or_request_only_missing_scope")
        self.assertFalse(p["activate_business"])

    def test_unknown_identity_and_missing_write_are_distinct(self):
        self.assertEqual(diagnose_repository(self.facts(owner_matches=None))["state"], "identity_unknown")
        self.assertEqual(diagnose_repository(self.facts(can_write=False))["state"], "write_unavailable")
        self.assertEqual(diagnose_repository(self.facts(owner_matches=False))["state"], "wrong_owner")

    def test_refusals_do_not_change_connectors_or_permissions(self):
        self.assertEqual(diagnose_repository(self.facts(security_blocked=True))["state"], "blocked")
        p = diagnose_repository(self.facts(conversation_refused=True))
        self.assertEqual(p["next_action"], "same_connector_chat_branch_then_read")
        self.assertFalse(p["change_permissions"])

    def test_contradictory_observations_do_not_create(self):
        p = diagnose_repository(self.facts(exists=False, absence_verified=True))
        self.assertEqual(p["state"], "observations_conflict")

    def test_inputs_unchanged(self):
        data = self.facts()
        before = copy.deepcopy(data)
        diagnose_repository(data)
        self.assertEqual(data, before)


if __name__ == "__main__":
    unittest.main()
