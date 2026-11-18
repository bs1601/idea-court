"""Exercise complete, tied, and invalid ballots through the command line."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "skills" / "idea-court" / "scripts" / "tally.py"


def case_record(for_counts):
    case_id = "setup-v1"
    ballots = []
    for seat in range(1, 13):
        ballots.append({
            "case_id": case_id,
            "juror_id": f"J{seat:02d}",
            "votes": {
                key: {
                    "vote": "FOR" if seat <= count else "AGAINST",
                    "for_reason": "This could shorten setup.",
                    "against_reason": "The result may omit some data.",
                    "decisive_reason": "The test fits the stated scope.",
                    "change_condition": "A trial with new users could change my vote.",
                }
                for key, count in for_counts.items()
            },
        })
    return {"case_id": case_id, "proposal_ids": list(for_counts), "ballots": ballots}


def run_tally(raw, *args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        input=raw,
        capture_output=True,
        timeout=10,
    )


class TallyTests(unittest.TestCase):
    def test_same_panel_yields_three_independent_proposal_counts(self):
        result = run_tally(json.dumps(case_record({"P1": 7, "P2": 5, "P3": 6})).encode())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {
            "case_id": "setup-v1",
            "ballots_counted": 12,
            "proposals": {
                "P1": {"for": 7, "against": 5, "outcome": "FOR"},
                "P2": {"for": 5, "against": 7, "outcome": "AGAINST"},
                "P3": {"for": 6, "against": 6, "outcome": "HUNG"},
            },
        })

    def test_accepts_a_utf8_ballot_file_with_bom(self):
        record = case_record({"P1": 12})
        record["ballots"][0]["votes"]["P1"]["for_reason"] = "הפתרון מקצר את ההרשמה."
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ballots.json"
            path.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8-sig")
            result = run_tally(None, str(path))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["proposals"]["P1"]["for"], 12)

    def test_rejects_incomplete_or_inconsistent_records_without_a_tally(self):
        cases = {
            "missing seat": lambda case: case["ballots"].pop(),
            "duplicate seat": lambda case: case["ballots"].append(case["ballots"][0]),
            "other version": lambda case: case["ballots"][0].update(case_id="setup-v2"),
            "wrong seat": lambda case: case["ballots"][0].update(juror_id="J00"),
            "missing proposal": lambda case: case["ballots"][0]["votes"].pop("P2"),
            "duplicate proposal": lambda case: case["proposal_ids"].append("P2"),
            "abstention": lambda case: case["ballots"][0]["votes"]["P1"].update(vote="ABSTAIN"),
            "missing rationale": lambda case: case["ballots"][0]["votes"]["P1"].pop("against_reason"),
        }
        for issue, change in cases.items():
            with self.subTest(issue=issue):
                record = case_record({"P1": 8, "P2": 4})
                change(record)
                result = run_tally(json.dumps(record).encode())
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertEqual(result.stdout, b"")

    def test_rejects_duplicate_json_keys(self):
        result = run_tally(b'{"case_id": "setup-v1", "case_id": "setup-v2"}')
        self.assertEqual(result.returncode, 2)
        self.assertIn(b"Duplicate JSON field", result.stderr)


if __name__ == "__main__":
    unittest.main()
