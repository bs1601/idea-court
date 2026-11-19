# Idea Court

An open Agent Skill that puts your idea on trial. Two advocates argue the case, you get to respond, 12 AI jurors vote in separate contexts, and a judge explains the verdict and what could change it.

[הסבר והוראות התקנה בעברית](#עברית)

## Why use it?

Use Idea Court when a decision deserves more than a quick reaction. The hearing makes each side respond to the other's strongest evidence, gives you a chance to correct assumptions before the vote, and records which objections were answered. You leave with a reasoned recommendation and a clear view of what could change it.

## Put an idea on trial

Bring an idea, who it is for, and what you want to decide. For example, “Is it worth launching a weekly newsletter for freelance designers?” The jury votes on whether the idea is worth pursuing.

## Who does what

| Role | Responsibility |
| --- | --- |
| Defense | Makes the strongest evidence-backed case for the proposal. The clerk relays material objections and settlement offers to you. |
| Challenging advocate | Tests the claims and evidence, and can accept the reply or change position. |
| 12 jurors | Consider both sides. Each submits a private vote, the reasoning both ways, and what could change the decision. |
| Judge | Pairs each material objection with its reply, states what remains open, and explains the decision and the tally. |

The advocates present evidence, challenge each other's claims, and respond to those challenges in front of you. You can add your own reply, continue to the jury, or accept a settlement. If voting proceeds, you see which perspectives are on the panel and the totals per proposal. Seven votes decide a proposal and a 6–6 split stays unresolved.

The clerk keeps the original chat private from the court roles. The advocates and jurors receive the proposal, constraints and relevant evidence in fresh contexts. The judge receives the same case and the validated result in another fresh context. The submitter's identity, personal motive, wanted outcome, and earlier verdicts stay with the clerk.

## Install

1. On GitHub, open **Code → Download ZIP** and extract it. If you prefer Git, run `git clone https://github.com/bs1601/idea-court.git`.
2. Copy the entire [`skills/idea-court`](skills/idea-court/) folder into the matching skills directory below. Create the parent directory if needed. At the destination, `idea-court/SKILL.md` should be next to the `references/` and `scripts/` folders.
3. Start a new session in the project where you installed the skill. Use the command in the last column, followed by your idea.

| Client | Inside one project | Across local projects | Invoke |
| --- | --- | --- | --- |
| Codex | `.agents/skills/idea-court/` | `~/.agents/skills/idea-court/` | `$idea-court` |
| Claude Code | `.claude/skills/idea-court/` | `~/.claude/skills/idea-court/` | `/idea-court` |

Try `$idea-court Is it worth launching a weekly newsletter for freelance designers?` in Codex, or start the same prompt with `/idea-court` in Claude Code. [Example hearing](examples/pilot.md)

A full hearing requires a host that can launch fresh-context subagents. If they are unavailable, the skill can prepare the case and leave voting pending. Python 3 is optional and runs the ballot counter. The skill uses your existing agent session and requires no separate account, server, or API key.

An isolated run keeps the jurors from reading one another's votes. They are simulated perspectives, and runs may share a model and its blind spots. Treat the reasons and the proposed real-world test as part of the result.

[Codex skill locations](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) · [Claude Code skill locations](https://code.claude.com/docs/en/skills#choose-where-skills-load) · [Agent Skills format](https://agentskills.io/specification)

## Verify

From the repository root, run the ballot counter tests with Python 3.

```sh
python -B -m unittest discover -s tests -v
```

For a live check or a comparison with a shorter critical prompt, use the [example hearing](examples/pilot.md).

## עברית

**בית משפט לרעיונות** עוזר לך להחליט אם שווה להתקדם עם רעיון. שני עורכי דין בוחנים את הטענות ואת הראיות. אתה יכול לענות לפני ההצבעה, ובסוף אתה מקבל החלטה מנומקת והסבר מה עשוי לשנות אותה.

### איך זה עובד

אתה מציג את הרעיון, למי הוא מיועד ומה אתה רוצה להחליט. ההגנה מציגה את הטיעון בעד, הצד השני בוחן את ההנחות והראיות, ושניהם מגיבים זה לזה. יש לך הזדמנות לענות או לקבל פשרה. אם הדיון מגיע להצבעה, 12 המושבעים מצביעים בחשאי. השופט מציג **טיעונים בעד, תשובות להתנגדויות המהותיות והחלטה מנומקת**.

מנהל הדיון מכין לשופט ולמושבעים תיק עם השאלה, ההצעה, הטיעונים והראיות. הפרטים על מי הגיש את הרעיון, מה האינטרס שלו ואיזו תשובה הוא רוצה נשארים בשיחה עם מנהל הדיון. השופט מקבל את התיק בהקשר נפרד ומסביר את הכרעת המושבעים.

### התקנה והרצה

1. בראש הריפו ב־GitHub לוחצים **Code → Download ZIP** ומחלצים את הקובץ.
2. מעתיקים את התיקייה `skills/idea-court` בשלמותה לתיקיית הסקילים בפרויקט. ב־Codex מעתיקים ל־`.agents/skills/`. ב־Claude Code מעתיקים ל־`.claude/skills/`. אם תיקיית היעד חסרה, יוצרים אותה. אחרי ההעתקה הנתיב צריך להסתיים ב־`idea-court/SKILL.md`.
3. פותחים שיחה חדשה בפרויקט. ב־Codex כותבים `$idea-court` וב־Claude Code כותבים `/idea-court`, ואחר כך מוסיפים את הרעיון בשפה שלכם.

למשל, אפשר להדביק ב־Codex את ההודעה הזאת. ב־Claude Code משתמשים ב־`/idea-court` בתחילת ההודעה.

```text
$idea-court האם כדאי לפתוח ניוזלטר שבועי למעצבים עצמאיים?
```

להתקנה בכל הפרויקטים אפשר להעתיק את אותה תיקייה למיקום האישי לפי הטבלה למעלה. משפט מלא דורש שהכלי יוכל להפעיל סוכנים בהקשרים נפרדים.

## License

[MIT](LICENSE)
