# Dimensions

Each dimension belongs to a tier, and the tier sets the confidence it may be reported at.

## Tier 1 — countable

Facts about the text. Anyone re-reading it can check them. Report at high confidence, and show the count in the reading column.

### attention

Count first-person singular and plural, second-person, and third-person references. Report as a balance, for example `self-focused 8:2`, giving the first-person and second-person counts.

Pronouns carry this, and so do naming choices: "the team" and "you people" are both second and third-person orientation without a pronoun.

### temporal

Count past, present and future verb constructions. Report the dominant orientation and the counts, for example `past-oriented, 6 past : 1 present`.

Future includes "will", "going to", "shall" and the present-tense-for-future construction ("I fly out Tuesday").

### certainty

Count hedges ("maybe", "I think", "sort of", "probably", "seems"), negations, and absolutes ("always", "never", "definitely", "obviously"). Report the balance and the raw counts, for example `hedged, 4 hedges : 0 absolutes`.

This row reports the counts only. The stance those counts imply is the Tier 2 `certainty` reading, which lives under `stance`.

### agency

Count active against passive constructions, and note who is placed as the actor. Report as, for example, `active, writer as actor` or `passive, 3 of 5 clauses agentless`.

Agentless passives matter more than the raw ratio: "mistakes were made" removes an actor that "I made mistakes" supplies. An agentless passive is a construction, not an intention. Report that the actor is absent from the sentence; do not report why.

### analytic

Pennebaker's contrast: high article and preposition use against high pronoun, auxiliary verb, conjunction, adverb and negation use. High values read as formal, categorical and detached; low values read as narrative, personal and immediate.

Report as a direction with the evidence, for example `analytic, article and preposition dense` or `narrative, pronoun and auxiliary dense`. Do not report a numeric score — the published formula is scaled against a corpus this skill does not have.

### complexity

Sentence length, word length, lexical variety and register. Report as, for example, `semi-formal, 18 words per sentence` or `terse, fragments throughout`.

## Tier 2 — read

Judgement calls. Defensible from quoted evidence, never from a count alone. Report at medium confidence by default, dropping to low for `stance`, and for any row where a calibration moderator applies or the quoted evidence is thin.

Every Tier 2 row carries at least one quoted span or it does not appear in the table.

### valence

Positive, negative, mixed or neutral, as expressed by the writer.

The trap here is topic. A text can discuss a terrible subject in level language, and level language is what the row reports. "The death of fear is certain" expresses no fear; a lexicon scoring it fires at more than six standard deviations above the mean on fear, which is exactly the error this skill exists to avoid. Read expression, not subject matter.

Words that are negative out of context are frequently not negative in context: "red dead 2" is a game title, "sick" and "insane" are often praise.

### emotion

The dominant emotion the writer expresses, if any. Anger, disgust, fear, joy, sadness, surprise, or none.

Measured performance on this dimension is macro-F1 0.56 against a chance floor of 0.14, so it is worth reporting and is not close to certain. That was measured on short social-media comments; on email, transcripts or anything longer the figure is an estimate, not a result.

The weak seam is disgust against anger: in the measurement, 6 of 15 disgust items were read as anger. When a text expresses revulsion at a thing rather than grievance against an agent, check disgust before settling on anger. "Everyone in this thread is disgusting" is disgust; "everyone in this thread is wrong" is anger.

Mark `none` freely. Informational and transactional writing carries no emotion, and inventing one is the most common way this dimension goes wrong.

### arousal

Activation level, independently of valence. Calm against activated.

Punctuation density, capitalisation, repetition, sentence fragmentation and intensifiers carry this. Note that this dimension was not measured — treat it as the least evidenced Tier 2 row after `stance`.

### stance

Orientation toward the reader: affiliative, deferential, dominant, distant, or neutral. Includes the certainty stance implied by the Tier 1 `certainty` counts.

Report at low confidence. This dimension was not directly measured, and its closed-vocabulary analogue scored below the chance floor in the ablation.

## Tier 3 — not reported

These are unavailable. Name them as unavailable when asked; do not produce a hedged reading.

Big Five personality traits — openness, conscientiousness, extraversion, agreeableness, neuroticism — are not inferable here. In measurement against labelled essays, no method beat the majority-class baseline: 0.61 for reading, 0.62 for n-grams, 0.58 for hand-designed features, against a 0.60 baseline.

Mental-health state, including depression and anxiety severity, is not reported. The markers are documented as varying by the writer's demographics and by the writing task, and this skill has neither piece of context.

Deception is not reported. There is no reliable linguistic signature of it.

A hedged number in any of these areas gets quoted without its hedge. That is why they are refused outright rather than softened.
