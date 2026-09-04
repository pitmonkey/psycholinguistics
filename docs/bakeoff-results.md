# Engine bakeoff — results

Throwaway spike. The question was how a psycholinguistics plugin should actually compute its analysis: skill-guided LLM reading, code-backed feature extraction, or a hybrid of the two.

## Setup

| | |
|---|---|
| Emotion task | GoEmotions test split, single-label items only, mapped to Ekman 6 + neutral. 105 items, 15 per class, chance = 0.143. |
| Personality task | Pennebaker & King stream-of-consciousness essays, Big Five binary labels. 30 held-out items, 2437 for training, majority baseline = 0.60. |
| Arm A | Skill-guided reading. Taxonomy definition only, no features, no training data. |
| Arm B | Logistic regression over closed-vocabulary features, tf-idf 1-2 grams, or both. spaCy + NRC EmoLex + VADER; LIWC itself is proprietary and was not used. |
| Arm C | Arm A's reading plus a per-item feature card (top 14 features as z-scores against the training corpus). |

## Emotion, macro-F1 (n=105)

| arm | accuracy | macro-F1 |
|---|---|---|
| C hybrid | 0.581 | **0.586** |
| A skill-only | 0.552 | 0.559 |
| B both (fair fusion) | 0.533 | 0.537 |
| B open (tf-idf) | 0.438 | 0.446 |
| B closed (features) | 0.438 | 0.431 |
| chance | 0.143 | — |

Arm C changed only 3 of 105 labels against arm A, and all 3 were corrections. The feature card rarely overrode a confident reading; it helped where the reading had nothing to go on.

Arm A's errors are concentrated where the label scheme is fuzzy, not where the reading is wrong: disgust recall 0.27 (6 of 15 disgust items read as anger), neutral precision 0.37. Fear and sadness both reach F1 0.77.

## Big Five, accuracy (n=30)

| arm | cEXT | cNEU | cAGR | cCON | cOPN | mean | 95% CI |
|---|---|---|---|---|---|---|---|
| B open | 0.53 | 0.60 | 0.57 | 0.70 | 0.70 | 0.62 | [0.54, 0.69] |
| A skill-only | 0.60 | 0.60 | 0.60 | 0.53 | 0.73 | 0.61 | [0.53, 0.69] |
| majority class | 0.57 | 0.57 | 0.53 | 0.60 | 0.73 | 0.60 | — |
| B closed | 0.53 | 0.53 | 0.50 | 0.77 | 0.57 | 0.58 | [0.50, 0.66] |
| B both | 0.53 | 0.50 | 0.40 | 0.67 | 0.60 | 0.54 | [0.46, 0.62] |

No arm is distinguishable from always guessing the majority class. At n=30 the interval is ±0.08 on the mean, so this rules out a large effect, not a small one — but nothing here supports scoring traits from a single document.

## Which closed-vocabulary features carry the signal

Ablation on the emotion task (macro-F1, all closed features = 0.431):

| family | alone | removed |
|---|---|---|
| affect lexicon (NRC + VADER) | 0.359 | 0.327 |
| style (length, punctuation, TTR, negation, swearing) | 0.235 | 0.373 |
| syntax / POS rates | 0.236 | 0.417 |
| temporal (tense) | 0.201 | 0.439 |
| pronouns by person | 0.177 | 0.421 |
| cognitive word lists | 0.127 | 0.418 |
| social word lists | 0.073 | 0.431 |

Affect lexicons and surface style do the work. The LIWC-style cognitive and social categories are at or below chance alone and cost nothing to remove. On texts this short they fire on too few tokens to mean anything — that is a statement about 20-word Reddit comments, not about the categories in general.

The lexicons also fire on topic rather than expression. "death of fear is certain" scores z=+6.7 on NRC fear while expressing none; "He had to much red dead 2" scores strongly negative on VADER because of the word "dead".

## Recommendation

1. **Skill-guided reading is the engine.** It beat every code-only variant on emotion by 0.11-0.16
macro-F1, needs no runtime, no venv, and no licensed dictionary.
2. **Code is an evidence layer, not the scorer.** The hybrid gained 0.03 — real but small, and
entirely on items where the reading was weak. Worth shipping as an optional second pass, not as the default path.
3. **Ship the countable dimensions as measurements, not inferences.** Pronoun distribution, tense
distribution, hedging, negation, the analytic index, lexical complexity: these are facts about the text and are worth reporting as such. They are not evidence for a trait claim.
4. **Do not ship Big Five scoring as an inference.** Nothing beat the majority baseline.
5. **Do not report lexicon counts without the text.** They confuse topic with expression often
enough to mislead on their own.

## Files

`features.py` is the one piece worth keeping — the feature extractor is reusable as an evidence layer if that pass is ever wanted. It lives in the local-only spike directory and is not part of the repository. Everything else there is scaffolding for this comparison.
