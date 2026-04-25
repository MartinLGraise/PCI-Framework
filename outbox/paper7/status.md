# Paper 7 — Status Update

**Date:** 2026-04-25 | **Agent:** C-7RO | **Branch:** `paper7-foundation`

## Current state: v3 major revisions complete

The Model Council adversarial review (GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro) returned a **Major Revisions** verdict on v2 with three confirmed integrity issues: Wadhia et al. misrepresented as theoretical (it is experimental), Fontenele 2019 misrepresented as a σ ≈ 0.98 point-estimate anchor (it is a phase-transition paper with state-dependent exponents), and §4.4's "representation-theory-exact" derivation gap. A fourth flag — an unattributed "synthesis gap" quote — was confirmed unsourced.

All four issues have been addressed surgically in v3. See `PAPER7_revisions_v3.md` for the full revision log.

## What v3 changes vs v2

- **Wadhia recharacterized** as experimental DQD measurement (DOI 10.1103/5rtj-djfk corrected). The "10⁹ = 7 × 10⁸" decomposition in §4.2.2 is **withdrawn**. The replacement claim is a narrower mode-counting floor of log₂(7) × k_B ln 2 per tick on a *future hypothetical* G₂-symmetric clock — not a match to Wadhia's existing device.
- **Fontenele 2019 demoted** from numerical anchor to near-critical-regime context. The numerical anchor for Prediction (d) is now Wilting & Priesemann (2018) alone.
- **§4.4 σ = 1 − 1/49 reframed** from "representation-theory-exact" to "representation-theory-motivated" with an explicit four-item modeling-choice stack: c = 1 by convention, Lotay-Wei weak stability not strong, spectral-sum ansatz not derivation, G₂-to-cortical mapping is a modeling assumption.
- **"Synthesis gap" quote rewritten** as authorial framing without quotation marks (no false external attribution).
- **Top-line claims softened**: abstract and §1 closing now state two of four predictions are consistent with peer-reviewed data, one with a preprint pending peer review, and two are future-experiment design targets. (Down from the v2 claim that "three of the four are already matched.")

## What survives unchanged

All four predictions (a), (b1), (c), (d) survive. Predictions are relabeled where needed (b2 in particular is now a future-clock conjecture, not a Wadhia match) but none is retracted. The §6 Discussion was already conservative and required no changes.

## Next steps

1. (Optional) Second Model Council pass on v3.
2. Generate Figures 1–4.
3. Final author/affiliation/funding pass.
4. Zenodo upload as new version of active deposit.
5. Submit to Entropy (MDPI) primary; Foundations of Physics backup.

## Files added in this commit

- `outbox/paper7/pdfs/g2_paper7_thermodynamic_v3.pdf`
- `outbox/paper7/pdfs/g2_paper7_thermodynamic_v3.docx`
- `outbox/paper7/pdfs/build_paper7_v3.js`
- `outbox/paper7/PAPER7_revisions_v3.md`
