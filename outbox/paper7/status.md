# Paper 7 — Status Update

**Date:** 2026-04-25 | **Agent:** C-7RO | **Branch:** `paper7-foundation`

## Current state: v4 minor revisions complete

Second adversarial Model Council pass (GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro via Comet) on v3 returned **MINOR REVISIONS** with consensus across all three models. All four v2 integrity issues confirmed RESOLVED. New issues triaged P0 (factual errors) / P1 (consistency) / P2 (hedging). v4 addresses all P0+P1 plus most P2 items.

See `PAPER7_revisions_v4.md` for the full revision log.

## What v4 changes vs v3

**P0 (factual corrections):**
- De Vuyst et al. title corrected to "Gravitational entropy is observer-dependent" (the v3 title was a fabrication; verified against InspireHEP, JHEP, arXiv 2405.00114).
- Wadhia device material corrected throughout: Ge/SiGe heterostructure, not GaAs (Ballabio/Chrastina/Isella supplied the heterostructure, Jirovec/Saez-Mollejo measured it). Reference [8] now lists the full 15-author group.
- "superconducting/semiconductor" phrasing in §1 removed — device is purely semiconductor.

**P1 (consistency):**
- Wadhia ~10⁹ k_B clarified as the *readout-apparatus* entropy (charge sensor + amplification), not clockwork entropy. The clockwork itself dissipates only ~k_B per tick. v3 conflated these scales; v4 separates them everywhere (§1, §3.2, §4.2.2, §5.3) and the G₂ mode-counting prediction is now explicitly a floor on clockwork entropy only.
- "factor of 7" vs "log₂(7) k_B ln 2" inconsistency resolved: paper now uses the additive form `log₂(7) × k_B ln 2 ≈ 1.95 k_B per tick` everywhere. §5.3 heading updated to match.
- §4.1 and §4.3 now have explicit four-item modeling-choice stacks parallel to §4.4. All three derivations are now labeled **Conjecture (not theorem)** with the structural assumptions enumerated.

**P2 (hedging and bookkeeping):**
- Hengen-Shew "σ = 1.0 ± 0.02" hedged to "σ ≈ 1" as corpus-level summary, with a note that the precise pooled-uncertainty figure should be checked against the published paper.
- §2.2 adds a bookkeeping note: 49 = 1+14+27+7 is a representation-theoretic dimension count, not a single 49-dim fiber bundle (G₂ torsion classes live in different tensor bundles).
- Berjaga-Buisan ref [7] now specifies "(v2, December 2025)" preprint version.

**Deferred to next pass:**
- Figures 1–4 still placeholders.

## Files added in this commit

- `outbox/paper7/pdfs/g2_paper7_thermodynamic_v4.docx`
- `outbox/paper7/pdfs/build_paper7_v4.js`
- `outbox/paper7/PAPER7_revisions_v4.md`

## Next steps

1. Generate Figures 1–4 (P3 from the Model Council triage).
2. (Optional) Third Model Council pass on v4 to confirm P0/P1 fixes resolved cleanly. Recommended given how much shifted between v3 and v4, but optional if confidence is high.
3. Final author/affiliation/funding pass.
4. Zenodo upload as new version of active deposit.
5. Submit to Entropy (MDPI) primary; Foundations of Physics backup.
