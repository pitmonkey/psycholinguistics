# psycholinguistics

A Claude Code plugin that reads a piece of writing and reports what its language is doing — affect, attention, certainty, temporal focus, stance and style — with a confidence on each dimension that reflects how reliably it can actually be read.

## Use

`/profile` with the text pasted after it, a path to a file, or a reference to something earlier in the conversation.

The output is a table of dimensions with confidences, then the quoted evidence underneath, including evidence that cuts against the reading.

## What it does not do

It does not report personality traits, mental-health state, deception, or predictions about what the writer will do. These are refused rather than reported with a caveat.

The reason is measurement. Against labelled essays, no method beat guessing the majority class on Big Five traits — 0.61 for model reading, 0.62 for n-grams, 0.58 for hand-designed features, against a 0.60 baseline. The mental-health markers in the literature vary by the writer's demographics and by the writing task, neither of which this plugin knows.

Every row it does report describes a text. No row describes a person.

## Evidence

The engine choice and the dimension tiering come from a three-arm bakeoff run before any of this was designed: `docs/bakeoff-results.md`.

The design that follows from it: `docs/superpowers/specs/2026-09-04-psycholinguistics-plugin-design.md`.

## Tests

```
uv run --with pytest pytest tests/ -v
```

These check structure and content — that the manifest parses, the frontmatter is well formed, every named reference resolves, and the required content anchors are present. They cannot check whether a reading is any good. That is what `evals/cases.md` is for, and it is run by hand.
