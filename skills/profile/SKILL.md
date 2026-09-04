---
name: profile
description: Use when reading a piece of writing - an email, message, post or transcript - to report what its language is doing across affect, attention, certainty, temporal focus, stance and style, with per-dimension confidence. Reports readings of the text, never trait claims about its writer.
---

# Profile

Read a piece of writing and report what its language is doing.

Every row of the output describes a text. No row describes a person. If that distinction blurs, the output becomes a psychological verdict on someone who did not consent to one, which is the thing this skill exists to avoid.

## Getting the text

The text arrives three ways: pasted after the command, given as a file path, or referred to from earlier in the conversation. Read what you are pointed at. Do not go looking for text on your own, and do not profile a person's writing gathered from somewhere they did not put in front of you.

## Procedure

**1. Read it once for sense.** Before any counting or scoring, understand what the text is saying and what it is for. This ordering is not optional. The dominant failure mode in this domain is scoring that fires on subject matter instead of expression — a text about fear scored as fearful, a message containing "dead" scored as negative. Knowing what the text means is what prevents it.

**2. Count the Tier 1 dimensions.** These are counts you take directly from the text: attention, temporal, certainty, agency, analytic, complexity. See `references/dimensions.md` for what each one counts and how to report it.

**3. Read the Tier 2 dimensions.** Valence, emotion, arousal, stance. Each one anchored to a span you can quote. A reading you cannot quote for is a reading you do not have.

**4. Check against `references/calibration.md`.** Apply the moderators, set each confidence, and drop the rows that do not survive. Do this before writing anything down, not after.

**5. Write the output.**

## Output contract

Table first, evidence underneath.

| dimension | reading           | conf   |
| --------- | ----------------- | ------ |
| attention | self-focused 8:2  | high   |
| temporal  | past-oriented     | high   |
| certainty | hedged (4 hedges) | high   |
| valence   | negative          | medium |
| emotion   | frustration       | medium |
| stance    | deferential       | low    |

Then, under a horizontal rule, the evidence for each row:

```
attention — self-focused
  8 first-person vs 2 second-person references
temporal — past-oriented
  "I've asked", "you said", "we agreed" — 6 past, 1 present
valence — negative
  "still nothing back", "three times now"
  counter-evidence: "whenever you get a chance" softens it
```

Three rules govern the output.

Counter-evidence is required wherever it exists in the text. A reading that lists only the spans confirming it is not a reading, it is a case being made. If a text cuts against your conclusion somewhere, that span goes in the output.

Every Tier 2 row carries at least one quoted span. A row with no quotable evidence does not appear in the table at all.

Confidence is one of `high`, `medium` or `low`, set by the rules in `references/calibration.md`. Tier 1 rows are high because the reader can verify the count. Nothing else is high.

Close with any rows you dropped and why, and with any moderator that applied to the text as a whole — an unclear genre, a very short sample, writing that was plainly performed for an audience.

## What this does not report

Personality traits, including the Big Five. Mental-health state. Deception. Predictions about what the writer will do next.

These are unavailable, not uncertain. When measured against labelled data, trait inference did not beat guessing the majority class. The mental-health markers are documented as varying by the writer's demographics and by the writing task, neither of which this skill knows.

When asked for one of them directly, say plainly that the skill does not report it, say why in a sentence, and offer what it does report.
