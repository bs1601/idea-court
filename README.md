# Idea Court

An open Agent Skill that puts an idea or competing solutions on trial. Two advocates argue the case, you get to respond, 12 AI jurors vote in separate contexts, and a judge explains the verdict and what could change it.

[הסבר ושתי דוגמאות בעברית](#עברית)

## Two ways to open a case

| What you bring | What happens first | What the jury decides |
| --- | --- | --- |
| **Idea.** “I want to build an extension that saves quotes from articles.” | Define the scope, for example one week to build a prototype. | Whether to take that specific step. |
| **Problem.** “Users leave during onboarding.” | The board proposes two or three solutions, or uses alternatives you bring. | Whether each solution merits the proposed action. The same jury assesses all of them on the same criteria. |

## Who does what

| Role | Responsibility |
| --- | --- |
| Board | Proposes alternatives when you start with a problem. |
| Your advocate | Presents the case for the proposal and brings the strongest objection or a settlement offer back to you. |
| Opposing advocate | Presents the strongest reason to reject or defer the proposal and responds to your side. |
| 12 jurors | Consider both sides. Each submits a private vote, the reasoning both ways, and what could change the decision. |
| Judge | Reports the count and explains the jury's conclusion, the strongest objection, and the next step. |

The hearing opens with the question, proposals, and evidence and shows both advocates' positions. You can reply, continue to the jury, or accept a settlement. If voting proceeds, you see which perspectives are on the panel and the totals per proposal. Seven votes decide a proposal and a 6–6 split stays unresolved.

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

### מסלול 1 — יש לי רעיון

> יש לי רעיון לתוסף ששומר ציטוטים ממאמרים. האם שווה להשקיע שבוע בבניית אב־טיפוס?

מנסחים שאלה אחת ברורה. עורך הדין שלך מציג את הטיעון בעד, הצד השני מציג את הטיעון נגד, ובסוף המושבעים מצביעים על הצעד שהוגדר.

### מסלול 2 — יש לי בעיה פתוחה

> משתמשים נוטשים בהרשמה כשמבקשים מהם לחבר שלושה חשבונות. מה כדאי לנסות?

הבורד יכול להציע להתחיל מחשבון אחד, להציג הדגמה או לאפשר למשתמש להמשיך את ההרשמה מאוחר יותר. שני עורכי הדין בוחנים כל חלופה, ואותם 12 מושבעים מצביעים בנפרד על כל אחת.

בשני המסלולים תראה את שאלת ההכרעה, מה ידוע, מה עוד חסר ומי טוען בכל צד. עורך הדין שלך נותן לך הזדמנות לענות או לקבל פשרה. אם מגיעים להצבעה, יוצג הרכב המושבעים לפי תפקידים, והקולות ייספרו במצטבר. השופט מסביר מה הכריע ומה כדאי לעשות עכשיו.

אחרי ההתקנה, אפשר להעתיק אחת מהדוגמאות ולהתחיל אותה ב־`$idea-court` ב־Codex או ב־`/idea-court` ב־Claude Code. הסקיל ינהל את הדיון בשפה שלך.

## License

[MIT](LICENSE)
