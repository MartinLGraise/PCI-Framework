# Paper 7 — v3 Major Revisions Log

**Date:** 2026-04-25 | **Agent:** C-7RO | **Branch:** `paper7-foundation`

## Trigger

Adversarial Model Council review (GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro via Comet) returned a **Major Revisions** consensus on the v2 manuscript. Three of the four flags were independently verified via web search and confirmed as genuine integrity issues.

## Issues addressed in v3

### Issue 1 — Wadhia et al. misrepresentation (CONFIRMED)

**v2 framing (wrong):** Wadhia et al. (PRL 135:200407) presented as a *theoretical* result derived within the Lindblad master equation combined with a Penrose-threshold amplification model, yielding a 10⁹ k_B ln 2 lower bound on quantum-clock readout entropy.

**Verified reality:** Wadhia, Ares, et al. (PRL 135:200407, Nov 14 2025; DOI 10.1103/5rtj-djfk) is an *experimental* paper from the Natalia Ares group (Oxford). They measured entropy production on a gate-defined GaAs double quantum dot. The 10⁹ figure is an empirical observation about their specific device, not a derived universal lower bound, and the paper is not framed as Lindblad+Penrose.

**v3 fix:**
- §1, §3.2, §5.3, References [8]: Wadhia recharacterized as experimental DQD measurement with corrected DOI (10.1103/5rtj-djfk).
- §4.2.2: The unfounded "10⁹ = 7 × 10⁸" decomposition (factor 7 from G₂, factor 10⁸ from hardware) explicitly **withdrawn**. The replacement claim is narrower: G₂ representation theory imposes a *minimum mode-counting floor* of log₂(7) × k_B ln 2 per tick on a hypothetical future G₂-symmetric clock — a conjecture about a device that does not yet exist, not a match to Wadhia.
- Abstract claim "factor of exactly 7 to the mode-counting structure of quantum-clock entropy costs" softened to "any future G₂-symmetric quantum-clock readout."

### Issue 2 — Fontenele 2019 misrepresentation (CONFIRMED)

**v2 framing (wrong):** Cited as reporting σ ≈ 0.98 across awake-state cortical recordings, alongside Wilting & Priesemann 2018, as a numerical anchor for Prediction (d).

**Verified reality:** Fontenele et al. 2019 (PRL 122:208101) studies phase transitions between cortical states and reports critical exponents that differ from mean-field directed percolation. It does not report σ ≈ 0.98 as a point estimate.

**v3 fix:**
- Abstract, §1, §3.4, §4.4 testable-match label, §5.5, Figure 4 caption, References [13]: Fontenele restored to its actual content — near-critical regime with state-dependent exponents — and explicitly removed as a numerical σ anchor.
- The numerical anchor for Prediction (d) is now **Wilting & Priesemann (2018) alone** ("single-source published match").

### Issue 3 — §4.4 derivation gap (CONFIRMED)

**v2 framing (wrong):** σ = 1 − 1/49 ≈ 0.9796 presented as "representation-theory-exact." GPT-5.5 flagged this as numerology because the coupling constant c = 1 was assumed without proof and Lotay-Wei 2019 proves only weak stability (within the diffeomorphism orbit), not the computable eigenvalue spectrum the §4.4 argument requires.

**v3 fix:**
- §4.4 fully rewritten: σ_pred = 1 − 1/49 now labeled "representation-theory-motivated, not representation-theory-exact."
- Added explicit four-item modeling-choice stack:
  1. Coupling constant c = 1 fixed by convention, not derived.
  2. Lotay-Wei stability is weak (diffeomorphism orbit), not strong (computable spectrum).
  3. Spectral-sum factor 7/49 is a representation-theoretic ansatz, not a derivation.
  4. Map from G₂ flow to cortical branching is a modeling assumption, not a theorem.
- §4.4 epistemic labels: the σ_pred = 0.9796 claim is now labeled **Conjecture (not theorem)**, and the prior "Theorem given Lotay-Wei 2019" label is restricted to what Lotay-Wei actually proves (sign of the correction, weak stability).
- §2.2 supporting framing softened in parallel: "rigor here is conditional on those three inputs, not absolute."

### Issue 4 — Unattributed "synthesis gap" quote (CONFIRMED)

**v2 framing (wrong):** A passage was set in quotation marks in both the abstract and §1 and presented as a citation from "the review literature" / "a recent survey of consciousness thermodynamics," but the source could not be located.

**v3 fix:**
- Both occurrences (abstract paragraph 1, §1 paragraph 5) rewritten as authorial framing without quotation marks. The substance of the synthesis-gap argument is preserved as the paper's own claim, not falsely attributed to an external source.

## Honesty downgrades to top-line claims

- Abstract last paragraph: "Three of the four are already matched by published empirical data" → "Two of the four (b1 and d) are consistent with published peer-reviewed empirical data; one (a) is consistent with a current preprint whose peer review is pending; the remaining two (b2 and c) are design targets for future G₂-symmetric quantum-hardware experiments." (b2 is no longer claimed as a Wadhia match.)
- §1 closing paragraph: parallel softening.

## What was *not* changed

- Predictions (a), (b1), (c), (d) all survive — relabeled where needed but not retracted.
- §2 framework review unchanged in substance; only the §2.2 closing sentence softened.
- §6 Discussion (What This Paper Does Not Claim, What Remains Conditional, Open Problems, Series Arc) was already conservative and required no changes.
- All other references unchanged.

## Files

- `outbox/paper7/pdfs/g2_paper7_thermodynamic_v3.pdf` — revised manuscript
- `outbox/paper7/pdfs/g2_paper7_thermodynamic_v3.docx` — Word source
- `outbox/paper7/pdfs/build_paper7_v3.js` — build script (docx generator)

## Next steps

1. (Optional) Second Model Council pass on v3 to verify the integrity issues are resolved.
2. Generate Figures 1–4 (currently placeholders).
3. Final author/affiliation/funding pass.
4. Zenodo upload as a new version of the active deposit.
5. Submit to Entropy (MDPI) primary; Foundations of Physics backup.

## Discipline note

The Model Council caught real misrepresentations that would have surfaced in adversarial peer review at Entropy. The cost of the v3 revision (one week) is far less than the cost of a rejection or, worse, a post-publication citation-integrity flag. The paper remains ambitious; it just stops claiming more than the underlying mathematics supports. House rule "what we have not claimed" applied.
