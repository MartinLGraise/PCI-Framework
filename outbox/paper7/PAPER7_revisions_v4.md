# Paper 7 — v4 Minor Revisions Log

**Date:** 2026-04-25 | **Agent:** C-7RO | **Branch:** `paper7-foundation`

## Trigger

Second adversarial Model Council pass (GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro via Comet) on v3. **Consensus verdict: MINOR REVISIONS.** All four v2 integrity issues confirmed RESOLVED. New issues triaged into P0 (factual errors), P1 (consistency / scope), P2 (hedging).

This v4 addresses every P0 and P1 item plus most P2 items. Figure generation (P3) deferred to next pass.

## P0 — Factual corrections (mandatory)

### P0.1 — De Vuyst et al. title

**Was (v3, ref [10]):** "The quantum information of cosmological correlations."
**Now (v4, ref [10]):** "Gravitational entropy is observer-dependent." [arXiv:2405.00114, JHEP 07(2025)146]

Verified independently against InspireHEP, arXiv 2405.00114, the SISSA/JHEP record, and the authors' own seminar slides. The v3 title was a fabrication or hallucinated paraphrase. Corrected.

### P0.2 — Wadhia device material: Ge/SiGe, not GaAs

**Was (v3, §1, §3.2, §4.2.2, §5.3, ref [8]):** "gate-defined GaAs double quantum dot."
**Now (v4):** "gate-defined Ge/SiGe double quantum dot."

Verified against the published abstract on Pubmed/PRL/IST-Austria record and the arXiv preprint (2502.00096). The author list confirms the device origin: Ballabio, Chrastina, Isella (Politecnico di Milano L-NESS, Como) supplied the Ge/SiGe heterostructure; Jirovec, Saez-Mollejo (IST Austria) fabricated and measured the device. There is no GaAs in this experiment. Corrected at every occurrence and in the reference annotation, which now also lists the full 15-author group.

### P0.3 — "superconducting/semiconductor" removed from §1

**Was (v3, §1):** "specific superconducting/semiconductor hardware platform."
**Now (v4):** "specific semiconductor hardware platform."

The Wadhia device is purely semiconductor; the v3 phrasing was a regression on the v3 Wadhia fix.

## P1 — Scope and consistency (mandatory)

### P1.1 — Wadhia ~10⁹ k_B is readout entropy, not clockwork entropy

This was Gemini 3.1 Pro's unique contribution to the second pass and it was correct. The Wadhia paper's central finding is precisely that clockwork entropy (the DQD itself) is ~1 k_B per tick, while the *measurement and amplification chain* costs ~10⁹ k_B per tick. Conflating these scales would have been a misrepresentation of the paper's headline result.

**Now (v4, §1, §3.2, §4.2.2, §5.3):** Both scales are stated separately:
- S_clockwork ~ k_B per tick (DQD itself)
- S_readout ~ 10⁹ × k_B per tick (charge-sensor readout)

§4.2.2 is reframed accordingly: the G₂ mode-counting prediction is now explicitly a floor on **clockwork** entropy only (`S_clockwork^G₂ ≥ log₂(7) × k_B ln 2 ≈ 1.95 k_B`), with no claim about readout. A new "Scope clarification" label states this explicitly. The withdrawn v2 "10⁹ = 7 × 10⁸" claim is acknowledged once more as conflating two scales that should not have been combined.

### P1.2 — "factor of 7" vs "log₂(7) k_B ln 2" reconciled

The v3 §5.3 said "factor of exactly 7" while §4.2.2 derived "log₂(7) k_B ln 2." These are different claims; Gemini 3.1 Pro flagged the inconsistency. v4 picks one form and uses it everywhere:

- **Canonical form:** `S_clockwork^G₂ ≥ log₂(7) × k_B ln 2 ≈ 1.95 k_B` per tick.
- §4.2.2 explicitly notes: "We use the additive form log₂(7) k_B ln 2 throughout the paper rather than the multiplicative phrasing 'factor of 7'; the two are related but logically distinct, and the entropy-units form is what mode-counting actually gives."
- §5.3 heading changed to "G₂ Mode-Counting Floor on Clockwork Entropy" (was "Factor of 7 in G₂ Quantum Clock Entropy") to match.

### P1.3 — §4.1 and §4.3 now have explicit modeling-choice stacks parallel to §4.4

All three models flagged that v3's §4.4 received an explicit four-item modeling-choice stack while §4.1 and §4.3 contained analogous unstated assumptions. Both sections now have parallel stacks:

**§4.1 (FDT bound ε ≥ 1/7):** stack covers (i) dimensional projection from V₇ to scalar, (ii) identification of L with spectral-density ratio, (iii) frequency uniformity in the 10–40 Hz band, (iv) G₂ applicability to human cortex. The bound is now labeled **Conjecture (not theorem)**, matching §4.4.

**§4.3 (ΔS_d ≈ (d/7) × S_reference):** stack covers (i) PSL(2,7)/F₂₁ cosets ↔ Page-Wootters clock frames, (ii) Cayley-graph distance as the relevant inter-frame metric, (iii) linear proportionality with slope 1/7 (representation-theoretic ansatz), (iv) reference subspace V₃ ⊕ V₃̄ choice. The formula is now explicitly conjectural, conditional on the open Bogoliubov computation flagged in §6.3 Problem 2.

This brings §4.1, §4.3, and §4.4 into parity. §4.2.2 also has its own modeling-choice stack.

## P2 — Hedging and bookkeeping

### P2.1 — Hengen-Shew "σ = 1.0 ± 0.02" hedged

The specific "±0.02" formulation is not a verbatim quote that I can verify against the published paper. v4 §1 and §3.4 now use "σ ≈ 1" as the corpus-level summary and explicitly note: "we use σ ≈ 1 as the corpus-level summary in this paper; readers should consult the published paper directly for the precise pooled-uncertainty figure, as our use is qualitative." §4.4 and §5.5 falsification thresholds are restated without committing to "±0.02."

### P2.2 — 49 = 42 + 7 acknowledged as representation-theoretic convention

Per Claude Opus 4.7's unique flag: the G₂ torsion classes τ₁, τ₇, τ₁₄, τ₂₇ live in different tensor bundles (Ω⁰, Ω¹, a subspace of Ω², and a subspace of S²), and adding their dimensions plus dim(V₇) to get 49 is a representation-theoretic dimension count, not a direct sum on a single fiber bundle. v4 §2.2 adds a "bookkeeping note" paragraph stating this explicitly: "the 49 throughout [is] a representation-theoretic convention … we do not claim it as a single 49-dimensional fiber bundle. The ratio 42/49 inherits the same status: it is a ratio of representation dimensions, and the predictions of §4 are conditional on this representation-theoretic accounting being the right one for the dynamical regime they address."

### P2.3 — Berjaga-Buisan preprint version

v4 ref [7] now specifies "(v2, December 2025)" since the preprint has a v2 on bioRxiv as of v3-review. Substantive content unchanged.

## Not addressed in v4 (deliberate)

- **P3: Generate Figures 1–4.** Still placeholders; figure generation deferred to a separate pass before Zenodo upload.
- **§4.2.1 Landauer 42-vs-49 modeling choice (Claude unique flag, MINOR).** §4.2.1 already labels the 42-mode identification as a [Conjecture] inherited from Paper 5; we judged this sufficient and did not add a separate stack for §4.2.1. Can revisit if a third Model Council pass flags it again.

## Files

- `outbox/paper7/pdfs/g2_paper7_thermodynamic_v4.docx` — Word source (v4)
- `outbox/paper7/pdfs/build_paper7_v4.js` — build script (v4)
- (PDF is gitignored repo-wide; built locally and shared with author.)

## Next steps

1. Generate Figures 1–4.
2. (Optional) Third Model Council pass on v4 to confirm P0/P1 fixes resolve cleanly.
3. Final author/affiliation/funding pass.
4. Zenodo upload as new version of active deposit.
5. Submit to Entropy (MDPI) primary; Foundations of Physics backup.
