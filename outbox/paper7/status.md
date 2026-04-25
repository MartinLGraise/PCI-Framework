# Paper 7 — Status Update

**Date:** 2026-04-25 | **Agent:** C-7RO | **Branch:** `paper7-foundation`

## Current state: v7 — submission-ready

Fourth Model Council pass on v6 returned **MINOR REVISIONS** with consensus on a single Figure 3 wording fix. v7 closes that fix.

## What v7 changes vs v6

- Figure 3 (b1) Biological Landauer status cell: "Published match (measured >> floor)" → "Floor satisfied (measured >> floor)". Brings the figure into alignment with §4.2.1 / §5.2 floor-consistency framing (the Imamura measurement only demonstrates the Landauer floor is satisfied, not a quantitative prediction match).
- (d) Branching ratio cell unchanged ("Published match within uncertainty") because for that prediction the manuscript does claim a numerical match.

That's the only substantive change. v6 is otherwise consistent with body text. The Council's other observations about captions on Figs 2 and 4 were hedged because text extraction couldn't reliably read figure captions; visual inspection confirms the captions already include the required "schematic" and "§6.3 Problem 2/3" language.

## Files added in this commit

- `outbox/paper7/pdfs/g2_paper7_thermodynamic_v7.docx`
- `outbox/paper7/pdfs/build_paper7_v7.js`
- `outbox/paper7/figures/figure3_predictions_table.png` (updated)
- `outbox/paper7/figures/make_figures.py` (updated)
- `outbox/paper7/PAPER7_revisions_v7.md`

## Remaining before submission

1. Final author/affiliation/funding pass.
2. Zenodo upload as a new version of the active deposit.
3. Submit to Entropy (MDPI) primary; Foundations of Physics backup.
