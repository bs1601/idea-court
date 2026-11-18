# Jury protocol

## Select 12 seats

Use IDs `J01` through `J12`. Give each seat a distinct reason to care and a specific decision lens. For an app, useful roles might include a prospective customer, a first-time user, a UI/UX designer, a developer with relevant implementation experience, a startup founder at an early stage, an experienced founder, and an investor. Fill the other seats based on the case, such as a buyer, support lead, integration owner, accessibility specialist, or domain practitioner. A technical incident can call for a substantially different panel.

Use role descriptions as simulated perspectives. Avoid invented credentials, endorsements, or actual customer testimony. Keep role instructions neutral about the desired vote. The same 12 seats review all proposals in a case using the same decision criteria.

## Isolate each ballot

- **Codex.** Use native subagents. Select an empty or fresh context using the option exposed by the current host, such as `fork_turns: "none"` when available. Respect the open-agent limit. Collect and close a batch before convening the next, using the same frozen packet. A completed seat is never reused as another role.
- **Claude Code.** Use new non-fork subagents through the Agent tool. Use a foreground run when useful for reliably collecting one result at a time. A worktree controls file writes and is insufficient to establish a fresh conversation.
- **Other Agent Skills hosts.** Use an equivalent fresh-context operation if it supports one run per seat with private returns. Consider host settings, tool availability, and user permissions. An AI agent may still receive host or project instructions. This protocol isolates jury ballots from one another, and the host may retain separate run transcripts.

Send each juror only their seat ID, role, decision lens, the frozen packet, and the ballot instructions below. Direct each agent to evaluate from that record, use no tools or shared files, contact no other juror, and return only its ballot to the coordinator. Start every later seat or retry fresh without earlier outputs, even if the runs must be sequential. Do not report partial counts. Do not claim a vote was isolated if the host used shared history or its behavior is unknown.

If a ballot fails or is malformed, request one fresh retry with the same seat and packet. Keep successful ballots for that case version. If a seat remains unavailable, mark the vote pending and report how many valid ballots arrived. An explicitly requested single-model simulation may illustrate the process, with an unmistakable simulation label in its result and no claim of isolated voting.

## Ballot

Request a JSON object like this from each juror, with an entry for every proposal ID in the packet. A `FOR` vote means the proposal merits the action at the stated scope. Missing evidence can justify `AGAINST` without asserting the proposal can never succeed.

```json
{
  "case_id": "onboarding-v1",
  "juror_id": "J03",
  "votes": {
    "P1": {
      "vote": "FOR",
      "for_reason": "One connection reduces the work before a user sees data.",
      "against_reason": "One data source may leave the result too sparse to use.",
      "decisive_reason": "A limited experiment can measure usable first results.",
      "change_condition": "I would vote against deployment if one source cannot produce the core result."
    }
  }
}
```

## Count and report

Use [tally.py](../scripts/tally.py) when Python 3 is available. It accepts a UTF-8 JSON file path or reads JSON from standard input. Assemble a single object from trusted case metadata and the returned ballots.

```text
{
  "case_id": "<the frozen case version>",
  "proposal_ids": ["P1", "P2"],
  "ballots": [<the 12 actual ballot objects>]
}
```

```sh
python "<path-to-skill>/scripts/tally.py" "<path-to-ballots.json>"
```

Keep ballot data within the run. If a local file is necessary, use a temporary file outside the repository. The helper validates structure and counts votes. The coordinator is responsible for collecting independent runs and retaining the agreed proposal IDs and version.

If Python is unavailable, verify the same invariants before counting manually. There must be one return from each of `J01` through `J12`, one vote for every proposal per seat, a shared case version, valid vote values and all four nonempty rationale fields. Apply the same majority and tie rules. Never use a fabricated tally to fill a missing vote.
