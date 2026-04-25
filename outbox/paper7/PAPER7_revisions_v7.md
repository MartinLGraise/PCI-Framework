# Paper 7 — v7 Final Polish (Council MINOR REVISIONS, addressed)

**Date:** 2026-04-25 | **Agent:** C-7RO | **Branch:** `paper7-foundation`

## Trigger

Fourth Model Council pass on v6 (figures-verification). Verdict: **MINOR REVISIONS**, consensus among GPT-5.5 Thinking and Claude Opus 4.7 Thinking on a single substantive issue. Gemini's pass not delivered separately but the two-model consensus is sufficient to act.

## What v7 changes

### Single substantive fix: Figure 3 (b1) status cell

**Was (v6):** "Published match (measured >> floor)"
**Now (v7):** "Floor satisfied (measured >> floor)"

GPT-5.5 (MAJOR) and Claude Opus 4.7 (MINOR) both flagged this. The manuscript §4.2.1 and §5.2 frame the Imamura et al. 2009 anchor as a *floor-consistency* result — the measured biological dissipation (~5 × 10⁵ zJ per G₂/M event) exceeds the Landauer floor (16 zJ) by ~3 × 10⁴, demonstrating only that the floor is *satisfied*, not that there is a quantitative match between prediction and measurement. The v6 wording "Published match" risked overstating the evidential status by suggesting numerical agreement where the manuscript only claims a one-sided bound.

The (d) Branching ratio cell remains "Published match (within uncertainty)" because for that prediction the manuscript does claim a numerical match between σ_pred ≈ 0.9796 and Wilting & Priesemann's σ ≈ 0.98, within the published uncertainty.

This change is two words and brings Figure 3 into exact alignment with the manuscript's body-text epistemic discipline.

## What was NOT changed

The Council also flagged caption-language concerns about Figs 2 and 4 — that captions should *explicitly* say "schematic" and direct readers to §6.3 Problem 2 (Fig 2) and Problem 3 (Fig 4). On visual inspection, both captions already include exactly that language:

- Figure 2 caption: "Schematic Cayley-graph distance structure on the 8 cosets of PSL(2,7)/F₂₁. The exact graph depends on the choice of generators and octonion multiplication-table convention (open computation, §6.3 Problem 2); the four-level entropy structure depicted here is a conjectured representation-theoretic ansatz (§4.3 modeling-choice stack), not a derived theorem."
- Figure 4 caption: "Figure 4. The G₂ prediction σ_pred ≈ 0.9796 against an illustrative distribution centered at the Wilting & Priesemann (2018) awake-rat-cortex value σ ≈ 0.98 (subsampling-corrected, multiscale regression estimator). The histogram is a schematic representation of the published value and its stated uncertainty, not raw data; current measurement precision does not yet distinguish σ_pred from σ = 1 with high confidence. Per-dataset reanalysis of the Hengen-Shew corpus (§6.3 Problem 3) is the strongest test."

The two reviewing models hedged on these because their text-extraction pipeline did not reliably read the figure captions; the captions themselves are correct.

The Council's other "MINOR" observations — figure placement after References (acceptable for both Entropy and Foundations of Physics), accent-color semantic consistency (verified visually) — are not gating.

## Files

- `outbox/paper7/pdfs/g2_paper7_thermodynamic_v7.docx` — manuscript with corrected Fig 3
- `outbox/paper7/pdfs/build_paper7_v7.js` — build script (unchanged from v6)
- `outbox/paper7/figures/figure3_predictions_table.png` — corrected Fig 3
- `outbox/paper7/figures/make_figures.py` — corrected (b1) status string

## Status

Manuscript is now submission-ready. Council-flagged residuals all addressed.

## Next steps

1. Final author/affiliation/funding pass.
2. Zenodo upload as new version of active deposit.
3. Submit to Entropy (MDPI) primary; Foundations of Physics backup.
