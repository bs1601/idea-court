---
name: idea-court
description: "Put an idea or competing solutions to a development problem on trial through opposing advocates, user consultation, and 12 separate AI juror ballots. Use when someone asks for Idea Court, a jury verdict, a structured challenge to an idea, or a hearing to compare solutions. בית משפט לרעיונות, חבר מושבעים, בחינת חלופות."
---

# Idea Court

Run a decision hearing in the user's language. Act as clerk. Take the request, prepare a neutral case, and relay replies. Two advocates test the merits, 12 AI jurors decide, and a judge in a separate fresh context explains the result.

## Open the case

- **Idea.** Frame a yes-or-no question at the scope the user asked for. If they ask whether an idea is worth building, put that decision to the jury. Present a smaller step as an alternative in the debate or as a settlement the user can accept. Give the proposal an ID such as `P1`.
- **Problem.** If the user describes a difficulty, frame the decision around what they want to improve. Read [hearing.md](references/hearing.md) to build two or three proposals through a board of relevant roles or admit proposals the user supplies. Assign a stable ID to each proposal.
- Prepare a neutral case brief. Include the decision, the proposal's intended outcome, constraints, material evidence, and evaluation criteria. Keep the submitter's identity, personal motives, preferred result, private chat, and previous verdicts with the clerk. Read the [case brief rules](references/hearing.md#prepare-a-neutral-case-brief) before sharing it. Ask only questions whose answers could change the decision.

Show the opening brief to the user. Name the route, quote the exact decision question, and list what is known and what remains uncertain. In the problem route, show which board role or source proposed each alternative and what it would do.

## Hear both sides and consult the user

Read [hearing.md](references/hearing.md). Start each advocate in a fresh context using only the neutral brief and their role. Defense builds the strongest supported case. The challenging advocate examines claims and evidence, accepts a supported reply, and can conclude the proposal merits proceeding. Hear opening cases, challenges, direct replies, and closing positions. Use the same criteria across proposals addressing the same problem.

Show the core hearing with named speakers. Use **Defense** and **Challenging advocate** or local equivalents, and include the most consequential disagreement. If the host cannot display the brief and arguments while the hearing runs, present them before the verdict in the user-facing report.

Before convening the jury, the clerk relays the defense's summary of the material objection and any concrete settlement offer. Let the user choose whether to proceed as filed, add a reply or evidence, or negotiate. Stop and wait when the user has this choice to make. If the user explicitly asked to proceed in one sitting, let defense finish its reply from the case record and proceed on the filed proposals. A settlement still requires explicit agreement to its exact terms.

If both advocates can stand behind the terms and the user expressly accepts them, relay the accepted terms and record the **agreed settlement**, its scope, success criterion and next step in the closing protocol. Skip the vote for a settled dispute. A counteroffer stays pending until the user accepts the final terms. If the user adds evidence, pass only the relevant fact or rebuttal, anonymized and accurately attributed. Let both sides explain which objections it answers and which remain.

## Convene the jury and count the ballots

Read [jury.md](references/jury.md). Once the hearing is closed, freeze the versioned neutral case with both advocates' actual arguments and replies. Give all 12 jurors that same record, with each juror's own role. Explicitly launch one fresh-context subagent per seat. Keep ballot returns out of the shared packet and other jurors' contexts.

Give the user the panel's role names in a compact roster before voting or alongside the result. Keep the role list separate from individual ballot contents.

Every juror submits one private ballot covering every admitted proposal. For each proposal, collect one argument for, one against, one `FOR` or `AGAINST` vote, the decisive reason, and what evidence would change or strengthen that vote. Collect all 12 valid ballots for the frozen version before reporting a verdict. If isolation is unavailable, return the hearing summary and say that voting is pending. Offer a clearly labeled single-model simulation only if the user wants one.

## Close with the judge's protocol

Start a fresh-context judge with the same neutral case, the validated tally and anonymized jury reasoning, or the agreed terms for a settlement. Use the [judge's brief](references/jury.md#brief-the-judge). If fresh contexts are unavailable, explain which stages are pending and label any requested single-context walkthrough as a simulation.

Start the protocol with the exact question that was heard. Use three clearly labeled sections in the user's language for every proposal, including when the dispute ends in settlement.

1. **Arguments for.** Summarize the strongest case for the proposal and the evidence or assumption it depends on.
2. **Objections and replies.** Pair each material objection with what supports it, the advocate's answer, and whether the issue was answered, partly answered, or remains open. Include serious objections in a unanimous vote and summarize minority reasoning when present. Keep individual ballots private.
3. **Decision.** Answer the question directly. Explain which objections affected the result and, if the vote was for, why the reasons to proceed outweighed the remaining objections. For a vote, give the count for and against, the total valid ballots, and whether jurors ran in fresh contexts. A 7+ vote majority decides for or against. A 6–6 split stays unresolved. The judge explains the result and does not cast a ballot. For a settlement, state the accepted terms and success criterion. If the jury is pending, mark it pending.

When several proposals pass, compare them on the same criteria and explain any trade-off behind the one to try first. End with a specific next step and the observable result that could change the decision. Treat the tally as the panel's assessment of the record, and present real-world evidence and untested assumptions separately.

When the verdict supports development, include a short **Brief for development planning** that the user can copy into a follow-up skill. Carry over the intended user and problem, the scope supported by the verdict, requirements and constraints, open objections or risks, and what would count as success. Leave sequencing and the implementation plan to the follow-up.
