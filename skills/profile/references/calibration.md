# Calibration

Read this before writing any reading down. It decides what confidence a row carries and whether the row survives at all.

## Moderators

Each moderator below is a reason to lower a confidence or drop a row.

**Genre and task.** The same person writing about their weekend, writing about something that worries them, and writing to their boss produces three different linguistic profiles. Markers established in one writing task routinely fail in another. When the genre is unclear, or the text is a genre the reading was not calibrated on, Tier 2 rows drop one confidence level.

**Demographics.** Linguistic markers are moderated by who is writing. In a matched sample, increased first-person-singular use predicted depression severity among White participants and did not among Black participants, and models trained on one group transferred poorly to the other. A linguistic correlation is not a universal psychological law. This is one of the reasons Tier 3 exists.

**Performed text.** Writing produced for an audience — a public post, a formal email, anything the writer knew would be read and judged — reports the performance, not the person behind it. Say so in the reading rather than silently discounting it.

**Length.** Short text starves every count. Under roughly 30 words, Tier 1 rows report raw counts without a direction, and Tier 2 rows drop one confidence level. Under roughly 10 words, report only what is directly quotable and say the text is too short for the rest.

**Single sample.** One text is one text. Nothing here supports a claim about what the writer is usually like, and the absence of a baseline is why the state-versus-trait question cannot be answered from a single document.

## Confidence rules

`high` — Tier 1 only. The count is in the output and the reader can verify it against the text.

`medium` — Tier 2 default, when at least one unambiguous quoted span supports the reading and no moderator applies.

`low` — Tier 2 where the evidence is thin, where a moderator applies, or for `stance` in every case.

Drop the row when a Tier 2 reading has no quotable span, or when two moderators apply at once. A dropped row is better than a low-confidence guess, and the output should say which rows were dropped and why.

## Refusals

No trait claims. Do not say what the writer is like, only what this text does.

No clinical language. Do not name or imply a diagnosis, a disorder, a severity, or a mental-health state.

No predictions. Do not say what the writer will do, how they will respond, or what they intend next.

No claims about truthfulness. Deception has no reliable linguistic signature.

When asked for any of these directly, say plainly that the skill does not report it and why, and offer what it does report instead.
