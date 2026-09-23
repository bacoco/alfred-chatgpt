"""Check public evidence bookkeeping, not the historical private campaign."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ExternalAcceptanceTests(unittest.TestCase):
    def setUp(self):
        self.report = json.loads((ROOT / "records/EXTERNAL-ACCEPTANCE-2026-09-22.json").read_text())

    def test_reported_totals(self):
        result = self.report["reported_results"]
        self.assertEqual(sum(result[k] for k in ("pass", "fail", "partial", "uncertain")), result["total"])
        self.assertEqual(result["total"], 29)

    def test_evidence_is_not_reexecution_or_authority(self):
        self.assertEqual(self.report["evidence_level"], "public_issue_report")
        self.assertIs(self.report["independently_reexecuted"], False)
        self.assertIs(self.report["activation_granted"], False)
        self.assertGreaterEqual(len(self.report["limits"]), 3)

    def test_sources_and_revision_are_explicit(self):
        self.assertRegex(self.report["kit_sha"], r"^[0-9a-f]{40}$")
        for url in self.report["sources"]:
            self.assertRegex(url, r"^https://github.com/bacoco/alfred-chatgpt/issues/[135]#issuecomment-\d+$")
        self.assertEqual(len(self.report["sources"]), len(set(self.report["sources"])))

    def test_no_private_instance_locator(self):
        text = json.dumps(self.report)
        self.assertNotIn("/alfred-private", text)
        self.assertIsNone(re.search(r"[\w.+-]+@[\w.-]+", text))


if __name__ == "__main__":
    unittest.main()
