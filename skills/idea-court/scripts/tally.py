"""Validate and count the 12 ballots for a frozen Idea Court case."""

import argparse
import json
from pathlib import Path
import sys


JURORS = {f"J{seat:02d}" for seat in range(1, 13)}
REASONS = ("for_reason", "against_reason", "decisive_reason", "change_condition")


def tally(record):
    if not isinstance(record, dict):
        raise ValueError("The case record must be a JSON object.")

    case_id = record.get("case_id")
    if not isinstance(case_id, str) or not case_id.strip():
        raise ValueError("A nonempty case_id is required.")

    proposal_ids = record.get("proposal_ids")
    if not isinstance(proposal_ids, list) or not proposal_ids:
        raise ValueError("At least one proposal ID is required.")
    if any(not isinstance(key, str) or not key.strip() for key in proposal_ids):
        raise ValueError("Proposal IDs must be nonempty strings.")
    if len(proposal_ids) != len(set(proposal_ids)):
        raise ValueError("Proposal IDs must be unique.")

    ballots = record.get("ballots")
    if not isinstance(ballots, list):
        raise ValueError("Ballots must be a list.")

    seen = set()
    proposal_keys = set(proposal_ids)
    counts = {key: {"FOR": 0, "AGAINST": 0} for key in proposal_ids}
    for ballot in ballots:
        if not isinstance(ballot, dict) or ballot.get("case_id") != case_id:
            raise ValueError("Every ballot must match the frozen case_id.")

        juror_id = ballot.get("juror_id")
        if not isinstance(juror_id, str) or juror_id not in JURORS:
            raise ValueError("Each juror_id must be within J01 and J12.")
        if juror_id in seen:
            raise ValueError(f"Duplicate ballot from {juror_id}.")
        seen.add(juror_id)

        votes = ballot.get("votes")
        if not isinstance(votes, dict) or votes.keys() != proposal_keys:
            raise ValueError(f"{juror_id} must vote once on every admitted proposal.")
        for key, entry in votes.items():
            if not isinstance(entry, dict) or entry.get("vote") not in ("FOR", "AGAINST"):
                raise ValueError(f"{juror_id}/{key} needs a FOR or AGAINST vote.")
            for field in REASONS:
                reason = entry.get(field)
                if not isinstance(reason, str) or not reason.strip():
                    raise ValueError(f"{juror_id}/{key} needs a nonempty {field}.")
            counts[key][entry["vote"]] += 1

    if seen != JURORS:
        missing = ", ".join(sorted(JURORS - seen))
        raise ValueError(f"Voting is incomplete. Missing ballots from {missing}.")

    proposals = {}
    for key, votes in counts.items():
        outcome = "HUNG"
        if votes["FOR"] >= 7:
            outcome = "FOR"
        elif votes["AGAINST"] >= 7:
            outcome = "AGAINST"
        proposals[key] = {"for": votes["FOR"], "against": votes["AGAINST"], "outcome": outcome}
    return {"case_id": case_id, "ballots_counted": len(seen), "proposals": proposals}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON field {key!r}.")
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", type=Path, help="UTF-8 JSON file (default is stdin)")
    args = parser.parse_args()
    try:
        raw = args.file.read_bytes() if args.file else sys.stdin.buffer.read()
        record = json.loads(raw, object_pairs_hook=unique_object)
        result = tally(record)
    except (OSError, ValueError) as error:
        parser.exit(2, f"Invalid case record: {error}\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
