# Idea Court

An open Agent Skill that puts an idea or competing solutions on trial. Two advocates argue the case, you get to respond, 12 AI jurors vote in separate contexts, and a judge explains the verdict and what could change it.

[הסבר והוראות התקנה בעברית](#עברית)

## Why use it?

Use Idea Court when a decision deserves more than a quick reaction. The hearing makes each side respond to the other's strongest evidence, gives you a chance to correct assumptions before the vote, and records which objections were answered. You leave with a reasoned recommendation and a clear view of what could change it.

## Two ways to open a case

| What you bring | What happens first | What the jury decides |
| --- | --- | --- |
| **Idea.** “Is it worth building an extension that saves quotes from articles?” | Define the intended user and the problem the extension would solve. | Whether the idea is worth building. |
| **Problem.** “Users leave during onboarding.” | The board proposes two or three solutions, or uses alternatives you bring. | Whether each solution merits the proposed action. The same jury assesses all of them on the same criteria. |

## Who does what

| Role | Responsibility |
| --- | --- |
| Board | Proposes alternatives when you start with a problem. |
| Defense | Makes the strongest evidence-backed case for the proposal. The clerk relays material objections and settlement offers to you. |
| Challenging advocate | Tests the claims and evidence, and can accept the reply or change position. |
| 12 jurors | Consider both sides. Each submits a private vote, the reasoning both ways, and what could change the decision. |
| Judge | Pairs each material objection with its reply, states what remains open, and explains the decision and the tally. |

The advocates present evidence, challenge each other's claims, and respond to those challenges in front of you. You can add your own reply, continue to the jury, or accept a settlement. If voting proceeds, you see which perspectives are on the panel and the totals per proposal. Seven votes decide a proposal and a 6–6 split stays unresolved.

The clerk keeps the original chat private from the court roles. The advocates and jurors receive the proposal, constraints and relevant evidence in fresh contexts. The judge receives the same case and the validated result in another fresh context. The submitter's identity, personal motive, wanted outcome, and earlier verdicts stay with the clerk.

A verdict in favor of development ends with a short brief you can give to a planning skill. It carries forward the scope, requirements, and unresolved objections.

## Install

1. On GitHub, open **Code → Download ZIP** and extract it. If you prefer Git, run `git clone https://github.com/bs1601/idea-court.git`.
2. Copy the entire [`skills/idea-court`](skills/idea-court/) folder into the matching skills directory below. Create the parent directory if needed. At the destination, `idea-court/SKILL.md` should be next to the `references/` and `scripts/` folders.
3. Start a new session in the project you want to work on and use the command in the last column, followed by your idea or problem.

| Client | Inside one project | Across local projects | Invoke |
| --- | --- | --- | --- |
| Codex | `.agents/skills/idea-court/` | `~/.agents/skills/idea-court/` | `$idea-court` |
| Claude Code | `.claude/skills/idea-court/` | `~/.claude/skills/idea-court/` | `/idea-court` |

Try `$idea-court Is an extension that saves article quotes worth building?` in Codex, or start the same prompt with `/idea-court` in Claude Code. There are [more cases to try](examples/pilot.md).

A full hearing requires a host that can launch fresh-context subagents. If they are unavailable, the skill can prepare the case and leave voting pending. Python 3 is optional and runs the ballot counter. The skill uses your existing agent session and requires no separate account, server, or API key.

An isolated run keeps the jurors from reading one another's votes. They are simulated perspectives, and runs may share a model and its blind spots. Treat the reasons and the proposed real-world test as part of the result.

[Codex skill locations](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) · [Claude Code skill locations](https://code.claude.com/docs/en/skills#choose-where-skills-load) · [Agent Skills format](https://agentskills.io/specification)

## Verify

From the repository root, run the ballot counter tests with Python 3.

```sh
python -B -m unittest discover -s tests -v
```

For a live check or a comparison with a shorter critical prompt, use the [pilot cases](examples/pilot.md).

## עברית

**בית משפט לרעיונות** עוזר לך להחליט אם שווה להתקדם עם רעיון, או מה לעשות כשיש לך בעיה וכמה פתרונות אפשריים. שני עורכי דין בוחנים את הטענות ואת הראיות. אתה יכול לענות לפני ההצבעה, ובסוף אתה מקבל החלטה מנומקת והסבר מה עשוי לשנות אותה.

### מסלול 1 — יש לי רעיון

> יש לי רעיון לתוסף ששומר ציטוטים ממאמרים. האם כדאי לבנות אותו?

עורך הדין שלך מציג למה כדאי לבנות את הרעיון, הצד השני בוחן את ההנחות והראיות שלו, ושני הצדדים מגיבים זה לזה לפני שהמושבעים מצביעים.

### מסלול 2 — יש לי בעיה פתוחה

> משתמשים נוטשים בהרשמה כשמבקשים מהם לחבר שלושה חשבונות. מה כדאי לנסות?

הבורד יכול להציע להתחיל מחשבון אחד, להציג הדגמה או לאפשר למשתמש להמשיך את ההרשמה מאוחר יותר. שני עורכי הדין בוחנים כל חלופה, ואותם 12 מושבעים מצביעים בנפרד על כל אחת.

בשני המסלולים תראה את שאלת ההכרעה, מה ידוע ומה עוד חסר. עורך הדין שלך נותן לך הזדמנות לענות או לקבל פשרה. בסיום השופט מציג **טיעונים בעד, התנגדויות והתשובה לכל התנגדות מהותית, והחלטה מנומקת**. אם המושבעים בעד פיתוח, אפשר להעביר לסקיל תכנון את תקציר ההחלטה, הדרישות והסיכונים שנשארו פתוחים.

מנהל הדיון מכין לשופט ולמושבעים תיק עם השאלה, ההצעה, הטיעונים והראיות. הפרטים על מי הגיש את הרעיון, מה האינטרס שלו ואיזו תשובה הוא רוצה נשארים בשיחה עם מנהל הדיון. השופט מקבל את התיק בהקשר נפרד ומסביר את הכרעת המושבעים.

### התקנה והרצה

1. בראש הריפו ב־GitHub לוחצים **Code → Download ZIP** ומחלצים את הקובץ.
2. מעתיקים את התיקייה `skills/idea-court` בשלמותה לתיקיית הסקילים בפרויקט. ב־Codex מעתיקים ל־`.agents/skills/`. ב־Claude Code מעתיקים ל־`.claude/skills/`. אם תיקיית היעד חסרה, יוצרים אותה. אחרי ההעתקה הנתיב צריך להסתיים ב־`idea-court/SKILL.md`.
3. פותחים שיחה חדשה בפרויקט. ב־Codex כותבים `$idea-court` וב־Claude Code כותבים `/idea-court`, ואחר כך מוסיפים את הרעיון או את הבעיה בשפה שלכם.

למשל, אפשר להדביק ב־Codex את ההודעה הזאת. ב־Claude Code משתמשים ב־`/idea-court` בתחילת ההודעה.

```text
$idea-court יש לי רעיון לתוסף ששומר ציטוטים ממאמרים. האם כדאי לבנות אותו?
```

להתקנה בכל הפרויקטים אפשר להעתיק את אותה תיקייה למיקום האישי לפי הטבלה למעלה. משפט מלא דורש שהכלי יוכל להפעיל סוכנים בהקשרים נפרדים.

## License

[MIT](LICENSE)
