"""Synthetic expected groupings and adversarial structural checks, not LLM scoring."""
import copy
import unittest
from tools.case_identity import identity_errors


def case(identifier, refs, **extra):
    return dict(case_id=identifier, canonical_case_id=identifier,
                source_refs=refs, aliases=[], status="open", **extra)


class CaseIdentityTests(unittest.TestCase):
    def test_five_notifications_one_incident_and_overlap(self):
        c = case("CI-A", ["gmail/test/m" + str(i) for i in range(5)])
        self.assertEqual(identity_errors([c], [c]), [])
        bad = copy.deepcopy(c)
        bad["source_refs"].append(bad["source_refs"][0])
        self.assertTrue(identity_errors([bad]))

    def test_similar_workflows_remain_distinct(self):
        cases = [case("CI-A", ["github/test/workflow-A/run-1"]),
                 case("CI-B", ["github/test/workflow-B/run-1"])]
        self.assertEqual(identity_errors(cases), [])

    def test_mail_and_calendar_same_appointment(self):
        refs = ["gmail/test/invite", "gmail/test/thread",
                "calendar/test/explicit", "calendar/test/automatic"]
        self.assertEqual(identity_errors([case("MEETING-A", refs)]), [])

    def test_same_title_different_dates_stays_separate(self):
        cases = [case("MEETING-A", ["calendar/test/day-1"]),
                 case("MEETING-B", ["calendar/test/day-2"])]
        self.assertEqual(identity_errors(cases, cases), [])

    def test_merge_requires_alias_reason_and_all_provenance(self):
        a, b = case("A", ["gmail/test/a"]), case("B", ["calendar/test/b"])
        b.update(canonical_case_id="A", identity_reason="Verified shared appointment UID")
        self.assertTrue(identity_errors([a, b]))
        a.update(aliases=["B"], source_refs=a["source_refs"] + b["source_refs"])
        self.assertEqual(identity_errors([a, b]), [])
        b.pop("identity_reason")
        self.assertTrue(identity_errors([a, b]))

    def test_manual_split_retains_ids_and_provenance(self):
        merged = [case("A", ["gmail/test/a", "calendar/test/b"]),
                  case("B", ["calendar/test/b"])]
        merged[0]["aliases"] = ["B"]
        merged[1].update(canonical_case_id="A", identity_reason="Former decision")
        split = [case("A", ["gmail/test/a"]), case("B", ["calendar/test/b"])]
        self.assertEqual(identity_errors(split, merged), [])
        split[1]["source_refs"] = []
        self.assertTrue(identity_errors(split, merged))

    def test_old_signal_does_not_reopen_resolved_dropped_or_snoozed(self):
        for state in ("resolved", "dropped", "snoozed"):
            old = case("A", ["gmail/test/old"])
            old["status"] = state
            current = copy.deepcopy(old)
            current["source_refs"].append("gmail/test/new")
            self.assertEqual(identity_errors([current], [old]), [])
            current["status"] = "open"
            self.assertTrue(identity_errors([current], [old]))
            self.assertEqual(identity_errors([current], [old],
                             authorized_reopens=frozenset({"A"})), [])

    def test_cycles_dangling_alias_and_duplicate_ids_rejected(self):
        a, b = case("A", []), case("B", [])
        a["canonical_case_id"], b["canonical_case_id"] = "B", "A"
        self.assertTrue(identity_errors([a, b]))
        a = case("A", [])
        a["aliases"] = ["missing"]
        self.assertTrue(identity_errors([a]))
        self.assertTrue(identity_errors([case("A", []), case("A", [])]))

    def test_deleted_identity_and_invalid_fields_rejected(self):
        self.assertTrue(identity_errors([], [case("A", ["gmail/test/a"])]))
        self.assertTrue(identity_errors([{"case_id": "A"}]))

    def test_input_unchanged_and_deterministic_errors(self):
        cases = [case("A", ["gmail/test/a"])]
        before = copy.deepcopy(cases)
        self.assertEqual(identity_errors(cases), identity_errors(cases))
        self.assertEqual(cases, before)


if __name__ == "__main__":
    unittest.main()
