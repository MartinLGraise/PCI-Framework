# Paper 7 — v6 Figure Generation Log

**Date:** 2026-04-25 | **Agent:** C-7RO | **Branch:** `paper7-foundation`

## Trigger

Third Model Council pass on v4 returned **ACCEPT (submission-ready pending figures)** unanimously. v5 closed the five MINOR text residuals. v6 generates and embeds Figures 1–4, completing the deferred P3 item.

## What v6 changes vs v5

The manuscript text is unchanged from v5. v6 only:
1. Generates four figures (Python/matplotlib, paper-academic style: minimal, monochrome with single rust accent #7A2818 matching the project's website palette, serif body font for figure text).
2. Embeds them in the manuscript via the new `figure()` helper added to `build_paper7.js` (uses `docx.ImageRun`).
3. Replaces the four "[Figure N: … To be added in next pass]" placeholders with a clean §Figures section at the end of the document, after References.

## The four figures

### Figure 1 — G₂ torsion decomposition schematic

A horizontal stacked-bar visualization of the 49 representation-theoretic dimensions broken into T₁ (1) + T₁₄ (14) + T₂₇ (27) torsion classes (in muted greys) plus V₇ (7) attractor (in rust accent). Brackets below the bar group the 42-dim torsion subspace and the 7-dim attractor; headline text states "Torsion fraction 42/49 = 6/7 ≈ 0.857 · Attractor fraction 7/49 = 1/7 ≈ 0.143". Caption explicitly notes that the 49 is a representation-theoretic dimension count combining different tensor bundles, mirroring the §2.2 bookkeeping note added in v4.

### Figure 2 — PSL(2,7)/F₂₁ Cayley graph

Schematic distance structure on the 8 cosets, with the reference observer at d=0 (rust accent), three nodes at d=1, three at d=2, and one at d=3, drawn on concentric distance rings. Edges show illustrative connections between adjacent shells. Caption explicitly disclaims that this is a schematic (the exact graph depends on octonion multiplication-table conventions; see §6.3 Problem 2) and notes that the four-level entropy structure is a conjecture (§4.3 modeling-choice stack), not a derived theorem.

### Figure 3 — Predictions × empirical anchors × evidential status table

Five-row summary table covering predictions (a), (b1), (b2), (c), (d) with their predicted quantities, empirical anchors, and evidential status. Status cells are subtly tinted (warm sand for preprint, sage for published match, terracotta for design target). All quantitative claims match the v5 manuscript text exactly: σ_pred = 0.9796, ε ≥ 1/7 ≈ 0.143, ΔE_min ≈ 16 zJ, S ≥ log₂(7) k_B ln 2 ≈ 1.95 k_B per tick (additive form), ΔS_d ≈ (d/7) × S_ref. Caption notes all four predictions are labeled Conjecture (not theorem) in the manuscript.

### Figure 4 — σ_pred vs awake-cortex distribution

Histogram of a schematic awake-cortex branching-ratio distribution centered at 0.98 (representing the published Wilting & Priesemann 2018 value with stated uncertainty), with the G₂ prediction σ_pred = 1 − 1/49 ≈ 0.9796 marked as a vertical rust line and the critical value σ = 1 marked as a dashed grey line. Caption explicitly notes that the histogram is a schematic representation of the published value and its stated uncertainty, not raw data, and that current measurement precision does not yet distinguish σ_pred from σ = 1 with high confidence — directing readers to the per-dataset Hengen-Shew reanalysis (§6.3 Problem 3) as the strongest test.

## Style discipline

- Single accent color (#7A2818, the rust used on pciframework.com) for all "G₂ prediction" / "reference observer" highlights; everything else in INK or muted grey.
- No decorative elements. No 3D charts, no pies. No gratuitous color.
- All quantitative annotations match the manuscript body text exactly.
- All "design target" / "schematic" disclaimers in figure captions match the §4 modeling-choice stacks and §6.3 open-problem labels.

## Files added in this commit

- `outbox/paper7/pdfs/g2_paper7_thermodynamic_v6.docx` — manuscript with figures embedded
- `outbox/paper7/pdfs/build_paper7_v6.js` — build script (adds `figure()` helper, ImageRun import, figure-section assembly)
- `outbox/paper7/figures/figure1_torsion_decomposition.png` — embedded in manuscript
- `outbox/paper7/figures/figure2_psl27_cayley.png` — embedded in manuscript
- `outbox/paper7/figures/figure3_predictions_table.png` — embedded in manuscript
- `outbox/paper7/figures/figure4_sigma_prediction.png` — embedded in manuscript
- `outbox/paper7/figures/make_figures.py` — figure-generation source

(PDF versions of each figure exist locally at the same paths but are gitignored repo-wide; PNGs are committed and are what the build script embeds.)

## Status

Manuscript is now feature-complete: all six published-paper sections with body content, four predictions with explicit modeling-choice stacks and Conjecture labels, full references with corrected metadata, and four embedded figures. Total 35 pages.

## Next steps

1. Final author/affiliation/funding pass.
2. Zenodo upload as new version of active deposit.
3. Submit to Entropy (MDPI) primary; Foundations of Physics backup.
4. Optional: brief fourth Model Council pass on v6 to confirm figures don't introduce any inconsistencies. Likely unnecessary — figures contain no claims not already in body text.
