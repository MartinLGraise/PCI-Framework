# Paper 7 — v5 Final Polish Log

**Date:** 2026-04-25 | **Agent:** C-7RO | **Branch:** `paper7-foundation`

## Trigger

Third Model Council pass on v4 returned **ACCEPT (submission-ready pending figures)** unanimously. Five residual MINOR items flagged across the three models. v5 fixes all five so the prose is clean before figure generation.

## What changed in v5

### 1. Abstract — additive form for Prediction (b2) (consensus flag, all 3 models)

**Was (v4 abstract):** "(b2) a conjectured factor of exactly 7 = dim(V₇) contributed by the G₂ fundamental representation to the mode-counting structure of any future G₂-symmetric quantum-clock readout"

**Now (v5 abstract):** "(b2) a conjectured G₂ mode-counting floor of S_clockwork ≥ log₂(7) × k_B ln 2 ≈ 1.95 k_B per tick on the clockwork entropy of any future G₂-symmetric quantum-clock register, where dim(V₇) = 7 is the dimension of the G₂ fundamental representation"

The body of §4.2.2 and §5.3 already used the additive form; the abstract was the last "factor of exactly 7" residual.

### 2. §6.3 Problem 1 — heading and body match additive form (GPT-5.5 + Claude flag)

**Was (v4 §6.3 Problem 1):** "Full Lindblad derivation of the factor-of-7 … identifies a factor of 7 in the entropy cost of a G₂-symmetric quantum clock"

**Now (v5 §6.3 Problem 1):** "Full Lindblad derivation of the G₂ mode-counting floor … identifies a clockwork entropy floor of log₂(7) × k_B ln 2 ≈ 1.95 k_B per tick for a G₂-symmetric clockwork register"

### 3. Wadhia clockwork value corrected to ~60 k_B per tick (GPT-5.5 unique flag, verified)

This was a real factual error. GPT-5.5 cross-checked the actual PRL paper and found the clockwork entropy is reported as **~60 k_B per tick** (estimated as a maximum from Fig. 2(a)), not "~k_B per tick" as v3/v4 stated. I verified directly against the published manuscript.

The actual measured values from Wadhia et al. (2025):
- **Clockwork (DQD itself):** of order tens of k_B per tick; ~60 k_B max from Fig. 2(a). (Theoretical expression: Σ_tick = β·e·|V_DQD|.)
- **Readout apparatus:** ~10⁹ k_B (RF reflectometry) to ~10¹¹ k_B (DC) per tick. Three orders of magnitude depending on readout method.
- **Gap:** "the second contribution … is, in fact, the dominant one by 9 orders of magnitude" (authors' own framing).

v5 corrects every occurrence in §1, §3.2, §4.2.2, §5.3, ref [8] annotation. The two-line scale display in §3.2 is now:

```
S_clockwork ~ 10¹–10² × k_B   (per tick, DQD itself; ~60 k_B max from Fig. 2(a))
S_readout   ~ 10⁹–10¹¹ × k_B  (per tick, charge-sensor readout, RF–DC range)
```

The 9-order-of-magnitude framing remains correct because the gap goes from ~60 k_B clockwork to ~10⁹–10¹¹ k_B readout — that is what "approximately nine orders of magnitude" measures, just as the authors state.

### 4. De Vuyst arXiv version specified (Claude + Gemini flag)

Ref [10] now reads "[arXiv:2405.00114v3]" reflecting the published JHEP version (final v3 from April 2025), not just "[arXiv:2405.00114]."

### 5. §4.2.2 qualitative-consistency observation added (Gemini Pass-2C flag)

Per Gemini's "don't water down" call: v4 refused any comparison between log₂(7) k_B ln 2 ≈ 1.95 k_B and the existing Wadhia clockwork measurement, which Gemini judged as over-softening. v5 adds one paragraph in §4.2.2 making a qualitative observation only, explicitly not a prediction match:

> As a qualitative observation — not a prediction match — we note that the G₂ mode-counting floor of ≈1.95 k_B per tick lies well below the clockwork entropy of order tens of k_B per tick observed in Wadhia et al.'s Ge/SiGe DQD. This is consistent with the structural expectation that mode-counting from G₂ representation theory imposes a floor far below the dissipation actually paid by a non-G₂ clockwork dominated by tunneling thermodynamics: a G₂-symmetric clockwork engineered to approach the floor would dissipate substantially less per tick than a generic DQD does. We make no quantitative match to the Wadhia number; we record only the qualitative scale relationship.

This honors the standing "don't water down" instruction without rolling back v3/v4's epistemic discipline.

## Council verdict tracking

| Item | v4 status | v5 status |
|---|---|---|
| Abstract "factor of exactly 7" | flagged MINOR by all 3 | RESOLVED |
| §6.3 Problem 1 heading | flagged MINOR by 2 of 3 | RESOLVED |
| Wadhia clockwork ~60 k_B (factual) | flagged MINOR by GPT-5.5; verified true | RESOLVED |
| De Vuyst arXiv version | flagged MINOR by 2 of 3 | RESOLVED |
| §4.2.2 under-claiming (Pass 2C) | flagged by Gemini | RESOLVED |
| Figures 1–4 | deferred (P3) | deferred (next pass) |

Council recommendation was **ACCEPT pending figures** even with these residuals present. v5 closes them. Manuscript text is now submission-ready.

## Files

- `outbox/paper7/pdfs/g2_paper7_thermodynamic_v5.docx`
- `outbox/paper7/pdfs/build_paper7_v5.js`
- (PDF gitignored repo-wide; built locally and shared with author.)

## Next steps

1. Generate Figures 1–4.
2. Final author/affiliation/funding pass.
3. Zenodo upload as new version of the active deposit.
4. Submit to Entropy (MDPI) primary; Foundations of Physics backup.
