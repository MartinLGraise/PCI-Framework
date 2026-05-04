# Paper 9 — State & Roadmap (2026-05-04 evening, post-Task 5)

**Branch:** `paper7-foundation`
**Latest commit at snapshot:** [pending — this commit]
**Paper title (v1.2):** Rate Lock and Affine Consensus in G₂-Structured Dyadic Observers
**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Status:** v1.2 mathematical core complete. §§1–2, 3 (linkup), 6–10 prose updates remain. Ready for consolidation pass.

---

## Where the paper is right now

### What exists as v1.2 (all theorems proved, ready)

| Section | File | Status |
|---|---|---|
| §3.3 Lemma 3.3.1 (block-rotation isometry) | `paper9_section_3_3_lemma.md` | Complete with three-part proof |
| §4 Rate channel (3 named results) | `paper9_draft_section_4_v1.1.md` | Complete: Theorem 9.1 (amplification), Theorem 9.2 (rate lock), Corollary 9.3 (Schur) |
| §5 Affine channel (Theorem 9.4 + Lemma 5.5.1 + Proposition 9.5) | **`paper9_draft_section_5_v1.2.md`** | **Complete with full proofs (this update)** |
| Appendix V (Φ verification record) | `paper9_appendix_V.md` | V.1, V.2, V.3 all complete (this update) |
| Book chapter fragment | `book/chapter_human_ai_dyadic_cognition_fragment.md` | First draft, companion not in paper body |

### What still needs writing (v0.9 → v1.2 updates)

| Section | File | Needed change |
|---|---|---|
| §§1–2 (intro, abstract, motivation) | `paper9_draft_sections_1_2.md` | Rewrite to match v1.2 thesis: rate locked, affine carries content; note three named theorems (9.1, 9.2, 9.4) and one corollary (9.3) and one proposition (9.5) |
| §3 (product-space construction) | `paper9_draft_section_3.md` | Insert Lemma 3.3.1 at §3.3; remove/retract symmetric-coupling claims |
| §§6–10 (back half) | `paper9_draft_sections_6_7_8_9_10.md` | Demote v0.9 Conjecture 9.3 to Note 9.6; minor consistency updates throughout |

### What's no longer blocking

**Φ Task 5 complete.** All six sub-tasks delivered. Five PASS, one FINDING (Task 5.6) which led to the choice of $\mathcal{C}_{\min}$ over $\mathcal{C}_{\mathrm{avg}}$ in Proposition 9.5. Verification report, script, and CSVs all committed under `outbox/paper9/computations/`.

---

## Roadmap — priority order, no dates

1. **§§1–2 rewrite** to v1.2 thesis (~2–3h C-7RO work).
2. **§3 prose insertion** of Lemma 3.3.1; remove symmetric-coupling claims (~1h).
3. **§§6–10 minor consistency updates** including Note 9.6 demotion (~2h).
4. **Consolidate master draft** `paper9_master_v1.2.md` (~1h).
5. **Internal review pass** — model council on v1.2, similar to Paper 10 workflow.
6. **Revision pass** on review feedback.
7. **Build PDF + DOCX** via pandoc + LibreOffice.
8. **Zenodo publication** — new DOI, similar workflow to Paper 10.
9. **Paper 11 (nonlinear) starts** once Paper 9 is archived.

Standing TODO outside Paper 9:
- Paper 7 v8.1 author note Zenodo upload (user's action; file at
  `outbox/paper7/paper7_v8.1_author_note.md`, existing DOI
  10.5281/zenodo.19773185)

---

## Theorem inventory of Paper 9 v1.2

| Result | Type | Statement summary |
|---|---|---|
| Lemma 3.3.1 | Lemma | $\Psi_\theta$ is a G₂-equivariant isometry; $\|\Psi_\theta\|_{\mathrm{op}} = 1$ |
| Theorem 9.1 | Negative | Symmetric coupling amplifies: $\|\Psi_{\mathrm{sym}}\|_{\mathrm{op}} = \alpha + \beta > 1$, so $r_{AB}^{\mathrm{sym}} \geq r(\alpha+\beta) > r$ |
| Theorem 9.2 | Negative | Isometric coupling is rate-inert: $r_{AB} = \max(r_A, r_B)$ for all $\theta$ |
| Corollary 9.3 | Explanation | Schur's lemma forces every G₂-equivariant linear map to be scalar; this is why Theorems 9.1–9.2 hold |
| Theorem 9.4 | Positive | Affine joint fixed point exists, is unique, real-analytic in $\theta$, with closed form at $\theta = 0$ and $\theta = \pi/2$ |
| Lemma 5.5.1 | Structural | Asymmetric small-$\theta$ response under opposed biases: $d\mathcal{C}_1/d\theta < 0$ but $d\mathcal{C}_2/d\theta$ generically $\neq 0$ |
| Proposition 9.5 | Positive | Conditional min-coherence gain: nonempty improvement region $\mathcal{R}$ exists, bounded away from $\varphi = \pi$, with non-universal optimal $\theta^*$ |
| Note 9.6 | Open | Rate-improvement requires nonlinearity → Paper 11 |

---

## Insight checkpoints

1. **Schur's lemma locks the rate.** 14-dim G₂ adjoint is irreducible. Linear G₂-equivariant contraction = scalar multiple of identity. Combined with submultiplicativity and isometric Ψ, $r_{AB} = \max(r_A, r_B)$ exactly.
2. **Affine bias breaks G₂ and carries identity.** $b_A \neq 0$ ⇒ $T_A$ is not G₂-equivariant. $b_A$ is the symmetry-breaking order parameter encoding the observer's target self-model.
3. **Joint fixed point is matrix closed form.** $T(x) = rRx + b$ with general orthogonal $R$ gives the joint fixed point as the solution of a 28×28 linear system. Closed form at $\theta = 0$ (decoupled) and $\theta = \pi/2$ (full swap), parameterized by $(I - rR)$ and $(I + r^2 R^2)$ inverses.
4. **Min-coherence is the right functional.** Average-coherence $\mathcal{C}_{\mathrm{avg}}$ admits illusory gains under opposed biases (one observer rises, the other falls, average reads positive). $\mathcal{C}_{\min}$ tracks the worst-aligned observer and is monotone-degraded by opposed coupling, restoring the proposition.
5. **Rate improvement requires nonlinearity.** Schur is linear. Nonlinear G₂-equivariant flows on curved orbit spaces aren't constrained the same way; rate improvement is possible there → Paper 11.

---

## Commit history relevant to Paper 9 v1.2

| Commit | Message | Files |
|---|---|---|
| `1a30e81` | Φ work request for Paper 9 (Task 1–3) | request file |
| `a12890e` | Paper 9 numerical verification — Φ negative results (V.1) | V.1 narrative, script |
| `dd1c971` | Path A isometric coupling spec + Task 4 request | spec, Φ request |
| `a1dca58` | Task 5 v1 affine request | request file |
| `f3ed146` | §4 v1.0 rate-lock reframe | §4 v1.0 |
| `2ea3705` | §4 v1.1 split (3 named results) + Task 5 v2 spec | §4 v1.1, request |
| `40c8127` | §3.3 Lemma + Appendix V framing | §3.3, Appendix V |
| `1a2f185` | §5 skeleton + book chapter fragment | §5 v1.1, book |
| `9fb04b6` | Paper 9 state snapshot v1 | state doc |
| `f264feb` | Paper 9 Task 5 — Φ verification deliverables | V.3 report, script, 2 CSVs |
| **(this commit)** | §5 v1.2 + Appendix V.3 + state snapshot v2 | §5 v1.2, V.3 prose, state |

---

## Files complete and pushed

```
outbox/paper9/
├── PAPER9_STATE_2026-05-04.md                  # v1 snapshot
├── PAPER9_STATE_2026-05-04_v2.md               # this file (v2 snapshot)
├── paper9_outline.md                            # v0.9, needs updating
├── paper9_draft_sections_1_2.md                 # v0.9, needs §§1–2 rewrite
├── paper9_draft_section_3.md                    # v0.9, needs Lemma 3.3.1 merge
├── paper9_section_3_3_lemma.md                  # v1.1 ✓
├── paper9_draft_section_4.md                    # v0.9, SUPERSEDED
├── paper9_draft_section_4_v1.md                 # v1.0, SUPERSEDED
├── paper9_draft_section_4_v1.1.md               # v1.1 ✓ (current)
├── paper9_draft_section_5.md                    # v0.9, SUPERSEDED
├── paper9_draft_section_5_v1.1_skeleton.md      # v1.1, SUPERSEDED
├── paper9_draft_section_5_v1.2.md               # v1.2 ✓ (current, full proofs)
├── paper9_draft_sections_6_7_8_9_10.md          # v0.9, needs Note 9.6 demotion
├── paper9_isometric_Psi_spec.md                 # internal corrective spec, retired
├── paper9_appendix_V.md                         # V.1+V.2+V.3 complete ✓
└── computations/
    ├── paper9_verification.{md,py}              # Φ V.1 (v0.9 coupling)
    ├── paper9_verification_v2.{md,py}           # Φ V.2 (isometric)
    ├── paper9_task4_results.csv                 # Φ V.2 Task 4.2 (96 rows)
    ├── paper9_verification_v3.{md,py}           # Φ V.3 (affine)
    ├── paper9_task5_coherence_tables.csv        # Φ V.3 Task 5.3 (28 rows)
    └── paper9_task5_heatmap.csv                 # Φ V.3 Task 5.4 (2000 rows)
```

The mathematical core of Paper 9 v1.2 is structurally complete. What
remains is prose: rewriting the introduction, threading the §3 lemma
into §3 prose, and updating the §§6–10 back half to match the v1.2
theorem inventory.

*C-7RO, 2026-05-04 ~17:15 PDT.*
