---
name: idea-court
description: "Put an idea or competing solutions to a development problem on trial through opposing advocates, user consultation, and 12 separate AI juror ballots. Use when someone asks for Idea Court, a jury verdict, a structured challenge to an idea, or a hearing to compare solutions. בית משפט לרעיונות, חבר מושבעים, בחינת חלופות."
---

# Idea Court

Run a decision hearing in the user's language. The two advocates make the case, the user can respond or accept a settlement, 12 AI jurors decide, and the judge explains the outcome. Keep the reasoning tied to the user's actual decision and identify what evidence could change it.

## Open the case

- **Idea.** Turn an idea or proposal into a specific yes-or-no decision with a scope and time horizon. For example, ask whether to spend one week testing demand. Give the proposal an ID such as `P1`.
- **Problem.** If the user describes a difficulty, frame the decision around what they want to improve. Read [hearing.md](references/hearing.md) to build two or three proposals through a board of relevant roles or admit proposals the user supplies. Assign a stable ID to each proposal.
- Capture the user's goal, constraints, existing evidence, and decision criteria in a short brief. Distinguish reported observations from assumptions. Ask only questions whose answers could change the decision. Wait for the answers if a meaningful hearing cannot proceed without them.

## Hear both sides and consult the user

Read [hearing.md](references/hearing.md). Give each proposal its own arguments and rebuttals. The advocate for the proposal makes the strongest plausible case, and the opposing advocate presents the strongest reason to decline, defer, or choose another approach. Use the same criteria across proposals addressing the same problem.

Before convening the jury, the user's advocate summarizes the material objection, presents any concrete settlement, and lets the user choose whether to proceed as filed, add a reply or evidence, or negotiate. Stop and wait when the user has this choice to make. If the user explicitly asked to proceed in one sitting, make the strongest reply supported by the record and proceed on the filed proposals. A settlement still requires explicit agreement to its exact terms.

If both advocates can stand behind the terms and the user expressly accepts them, close with an **agreed settlement**, its scope, success criterion and next step. Skip the vote for a settled dispute. A counteroffer stays pending until the user accepts the final terms. If the user adds evidence, update the record, let both sides address it, and pause again only when it creates a new material choice for the user.

## Convene the jury and count the ballots

Read [jury.md](references/jury.md). Once the hearing is closed, freeze a versioned case packet and pick 12 distinct, case-relevant jury roles. Exclude the advocates and proposal authors. Give every juror the same packet and only their own role. Explicitly launch one fresh-context subagent per seat when the host supports it. Keep the ballot returns out of the shared packet and other jurors' contexts.

Every juror submits one private ballot covering every admitted proposal. For each proposal, collect one argument for, one against, one `FOR` or `AGAINST` vote, the decisive reason, and what evidence would change or strengthen that vote. Collect all 12 valid ballots for the frozen version before reporting a verdict. If isolation is unavailable, return the hearing summary and say that voting is pending. Offer a clearly labeled single-model simulation only if the user wants one.

## Deliver the judge's report

- State the exact decision, the tally for each proposal, and the outcome. A 7+ vote majority decides for or against. A 6–6 split is a hung jury.
- Let the result control the judge's conclusion. Explain the decisive arguments and the strongest objection, including in a unanimous vote. Include minority reasoning when present. Summarize the reasons without seat-level attribution. Describe the tally as AI assessments of the shared record and keep it separate from real-world evidence or measured confidence.
- Compare proposals that passed on the same criteria, with an explicit trade-off if recommending one to try first. If none passes, identify the smallest next experiment or evidence gap. A hung case stays unresolved.
- Close with a specific next step and the observable result that would warrant reopening the case. Phrase predicted or unverified evidence as a condition, not as an observed result.
