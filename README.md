# Idea Court

An open Agent Skill that puts an idea or competing solutions on trial. Two advocates argue the case, you get to respond, 12 AI jurors vote in separate contexts, and a judge explains the verdict and what could change it.

## When to use it

- **You have an idea.** Put a specific decision on trial, such as whether to spend a week validating demand for a new app.
- **You have a problem.** A board of relevant roles proposes two or three ways forward. You can also submit proposals you've already received. The same jury evaluates each proposal on its own merits.

Your advocate brings material objections and any proposed settlement back to you before the vote. An agreed settlement closes the dispute. Otherwise each juror submits both a reason for and a reason against, a vote, and a condition that could change it. Seven votes decide a proposal and a 6–6 split stays unresolved.

## Install

Download or clone the repository. Copy the entire [`skills/idea-court`](skills/idea-court/) directory into a skill location below. Keep `SKILL.md`, `references/`, and `scripts/` together.

| Client | Inside one project | Across local projects | Invoke |
| --- | --- | --- | --- |
| Codex | `.agents/skills/idea-court/` | `~/.agents/skills/idea-court/` | `$idea-court` |
| Claude Code | `.claude/skills/idea-court/` | `~/.claude/skills/idea-court/` | `/idea-court` |

Open a new session in the relevant project and try a [sample case](examples/pilot.md). A full hearing uses the host's native fresh-context subagents. Hosts without that capability can prepare the case and leave voting pending. The optional ballot counter uses the Python 3 standard library. The skill itself uses your existing agent session and has no dedicated server or additional API key.

An isolated run keeps the jurors from reading one another's votes. They are simulated perspectives, and runs may share a model and its blind spots. Treat the reasons and the proposed real-world test as part of the result.

[Codex skill locations](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) · [Claude Code skill locations](https://code.claude.com/docs/en/skills#choose-where-skills-load) · [Agent Skills format](https://agentskills.io/specification)

## Verify

From the repository root, run the ballot counter tests with Python 3.

```sh
python -B -m unittest discover -s tests -v
```

For a live check or a comparison with a shorter critical prompt, use the [pilot cases](examples/pilot.md).

## עברית

**בית משפט לרעיונות.** מביאים רעיון או בעיה פתוחה. עורך הדין שלך והצד השני מציגים טיעונים, ויש לך הזדמנות לענות או לאשר פשרה. אם ממשיכים למשפט, 12 מושבעי AI רלוונטיים מצביעים בהקשרים נפרדים, והשופט מסביר מה הכריע ומה כדאי לבדוק.

אחרי ההתקנה, נסה לכתוב ב־Codex ״`$idea-court` יש לי רעיון לתוסף. תעמיד אותו למשפט״. ב־Claude Code השתמש ב־`/idea-court`. הסקיל ינהל את הדיון בשפה שלך.

## License

[MIT](LICENSE)
