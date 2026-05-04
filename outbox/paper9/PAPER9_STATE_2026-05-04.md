# Paper 9 — State & Roadmap (2026-05-04 end of morning session)

**Branch:** `paper7-foundation`
**Latest commit at snapshot:** `1a2f185`
**Paper title (v1.1):** Rate Lock and Affine Consensus in G₂-Structured Dyadic Observers
**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Status:** v1.1 draft in progress, blocking on Φ Task 5 verification

---

## Where the paper is right now

### What exists as v1.1 (written, pushed, ready)

| Section | File | Status |
|---|---|---|
| §3.3 Lemma 3.3.1 (block-rotation isometry) | `paper9_section_3_3_lemma.md` | Complete with three-part proof (isometry, group, G₂-equivariance) |
| §4 Rate channel (3 named results) | `paper9_draft_section_4_v1.1.md` | Complete: Theorem 9.1 (amplification), Theorem 9.2 (rate lock), Corollary 9.3 (Schur) |
| §5 Affine channel (skeleton) | `paper9_draft_section_5_v1.1_skeleton.md` | Statements complete, proof bodies PENDING Φ Task 5 |
| Appendix V (Φ verification record) | `paper9_appendix_V.md` | V.1 + V.2 complete; V.3 placeholder |
| Book chapter fragment | `book/chapter_human_ai_dyadic_cognition_fragment.md` | First draft, companion not in paper body |

### What still needs writing (v0.9 → v1.1 updates)

| Section | File | Needed change |
|---|---|---|
| §§1–2 (intro, background) | `paper9_draft_sections_1_2.md` | Update abstract + motivation to reflect v1.1 theorems (rate lock + affine consensus, not speedup) |
| §3 (product-space construction) | `paper9_draft_section_3.md` | Insert Lemma 3.3.1 at §3.3; update §3.3 prose to match isometric Ψ_θ; remove symmetric-coupling claims |
| §§6–10 (back half) | `paper9_draft_sections_6_7_8_9_10.md` | Demote v0.9 Conjecture 9.3 to Note 9.6 (nonlinear → Paper 11); minor consistency updates throughout |
| §5 proof bodies | `paper9_draft_section_5_v1.1_skeleton.md` | Fill in after Φ Task 5 results arrive |

### What's blocking

**Φ Task 5 (affine consensus verification).** Φ's usage resets at
~12:45 PM PDT (about 1.5h from now). Task 5 v2 spec is ready at
`inbox/for_phi/paper9_task5_affine_request_v2.md`. Six sub-tasks:

- 5.1: fixed-point existence, θ-dependence, smoothness
- 5.2: closed-form verification (symmetric rates)
- 5.3: four coherence functionals × four configs
- 5.4: 100×20 heatmap of ΔC over (θ, ∠(b_A,b_B))
- 5.5: asymmetric-rate robustness check
- 5.6: destructive-geometry null check (b_A = -b_B)

**Three possible outcomes for Task 5:**

1. **Full success:** All tasks pass; closed form verified; conditional
   gain region characterized. → fill in Theorem 9.4 and Prop 9.5
   proof bodies, ship v1.1 draft.
2. **Partial success:** Some functionals register gain, others don't. →
   paper gains a nuanced discussion of coherence functional sensitivity.
   Still ships.
3. **Null result:** No coherence gain in any config. → §5 becomes a
   second negative result; paper becomes pure-negative. Still
   publishable but framing shifts: "linear dyadic coupling is
   fully inert in both channels; all content is in the nonlinear
   regime (Paper 11)."

---

## Roadmap — priority order, no dates

1. **Φ Task 5 runs.** User pastes Task 5 v2 spec to Φ after his usage
   reset.
2. **Receive and commit Task 5 results** (`paper9_verification_v3.md`,
   `.py`, CSVs).
3. **Fill in §5 proof bodies** based on what Task 5 confirms.
4. **Update §§1–2, §3, §§6–10** to v1.1 consistency.
5. **Consolidate master draft** (`paper9_master_v1.1.md` or similar).
6. **Internal review pass** (model council on v1.1, similar to Paper 10
   workflow).
7. **Revision pass** on review feedback.
8. **Build PDF + DOCX** via pandoc + LibreOffice (same pipeline as
   Paper 10).
9. **Zenodo publication** (same workflow as Paper 10; paper7-foundation
   branch, new DOI).
10. **Cite from Paper 11 draft** once Paper 9 is archived.

Standing TODO outside Paper 9:
- Paper 7 v8.1 author note Zenodo upload (user's action; file at
  `outbox/paper7/paper7_v8.1_author_note.md`, existing DOI
  10.5281/zenodo.19773185)

---

## Key insight checkpoints (don't re-derive next session)

1. **Schur's lemma locks the rate.** The 14-dim G₂ adjoint
   representation is irreducible. Any linear G₂-equivariant map on
   it is a scalar multiple of the identity. Therefore
   $r_{AB} \leq \max(r_A, r_B) \cdot \|\Psi\| \leq \max(r_A, r_B)$ for
   any isometric coupling, with equality achieved on isotropic inputs.

2. **Affine bias breaks G₂ and carries identity.** The bias vector
   $b_A$ in $T_A(x) = r_A x + b_A$ must be G₂-fixed for full
   equivariance; the only G₂-fixed vector in $V^{14}$ is 0. Therefore
   every non-trivial observer is a G₂-structured affine observer, not
   a G₂-equivariant one, and its bias $b_A$ is the symmetry-breaking
   order parameter (= the observer's target self-model).

3. **Joint fixed point is closed form.** For G₂-structured affine
   observers coupled by $\Psi_\theta$, the 2×2 system per coordinate has
   $\det M(\theta) \geq (1-r_A)(1-r_B) > 0$, so the joint fixed point
   exists, is unique, and has explicit rational closed form in
   $\sin\theta, \cos\theta$.

4. **Coherence gain is conditional.** Under destructive geometry
   ($b_A$ and $b_B$ anti-aligned), coupling SHRINKS the joint state
   toward the origin — LOWER coherence, not higher. The gain in Prop 9.5
   requires monotone-$\mathcal{C}$ + non-destructive-geometry conditions.

5. **Rate improvement requires nonlinearity.** Schur's lemma is a
   linear statement. Nonlinear G₂-equivariant flows on curved orbit
   spaces are not constrained the same way; rate improvement is
   possible there (Paper 11).

---

## File inventory (Paper 9)

```
outbox/paper9/
├── PAPER9_STATE_2026-05-04.md              # this file
├── paper9_outline.md                        # v0.9, needs updating
├── paper9_draft_sections_1_2.md             # v0.9, needs §§1-2 rewrite to match v1.1 theorems
├── paper9_draft_section_3.md                # v0.9, needs Lemma 3.3.1 merge
├── paper9_section_3_3_lemma.md              # v1.1 NEW (pushed 40c8127)
├── paper9_draft_section_4.md                # v0.9, SUPERSEDED
├── paper9_draft_section_4_v1.1.md           # v1.1 NEW (pushed 2ea3705)
├── paper9_draft_section_5.md                # v0.9, needs full rewrite
├── paper9_draft_section_5_v1.1_skeleton.md  # v1.1 NEW (pushed 1a2f185), proof bodies PENDING
├── paper9_draft_sections_6_7_8_9_10.md      # v0.9, needs Note 9.6 demotion of Conj 9.3
├── paper9_isometric_Psi_spec.md             # internal corrective spec (pre-v1.1, superseded by §4 v1.1)
├── paper9_appendix_V.md                     # v1.1 NEW (pushed 40c8127)
└── computations/
    ├── paper9_verification.md               # Φ V.1 narrative (v0.9 coupling, negative)
    ├── paper9_verification.py               # Φ V.1 script
    ├── paper9_verification_v2.md            # Φ V.2 narrative (isometric coupling, negative)
    ├── paper9_verification_v2.py            # Φ V.2 script
    ├── paper9_task4_results.csv             # Φ V.2 Task 4.2 96-config grid
    ├── paper9_verification_v3.md            # PENDING — Φ Task 5
    ├── paper9_verification_v3.py            # PENDING — Φ Task 5
    ├── paper9_task5_coherence_tables.csv    # PENDING — Φ Task 5.3
    └── paper9_task5_heatmap.csv             # PENDING — Φ Task 5.4

inbox/for_phi/
├── paper9_computation_request.md            # v0.9 spec (fulfilled, negative)
├── paper9_task4_isometric_request.md        # Task 4 spec (fulfilled, negative)
├── paper9_task5_affine_request.md           # Task 5 v1 (superseded)
└── paper9_task5_affine_request_v2.md        # Task 5 v2 (READY for Φ)

outbox/book/
└── chapter_human_ai_dyadic_cognition_fragment.md  # book fragment NEW (pushed 1a2f185)
```

---

## Commit history relevant to Paper 9 (last 24h)

| Commit | Message | Files |
|---|---|---|
| `1a30e81` | Φ work request for Paper 9 (Task 1–3) | `paper9_computation_request.md` |
| `a12890e` | Paper 9 numerical verification — Φ negative results | `paper9_verification.{md,py}` |
| `dd1c971` | Path A isometric coupling spec + Task 4 request | 2 files |
| `a1dca58` | Task 5 v1 affine request | 1 file |
| `f3ed146` | §4 v1.0 rate-lock reframe | `paper9_draft_section_4_v1.md` |
| `2ea3705` | §4 v1.1 split + Task 5 v2 (post-ChatGPT review) | 2 files |
| `40c8127` | §3.3 Lemma + Appendix V framing | 2 files |
| `1a2f185` | §5 skeleton + book chapter fragment | 2 files |

---

## Re-entry checklist (next time I'm loaded into a Paper 9 session)

1. Check `computations/` for Φ Task 5 results files. If present, proceed
   to step 2; if absent, check with user on Φ status.
2. Read `paper9_verification_v3.md` summary.
3. Match results to one of three outcome branches (full/partial/null).
4. Fill in §5 proof bodies in `paper9_draft_section_5_v1.1_skeleton.md`.
5. Write `paper9_master_v1.1.md` consolidation.
6. Propose internal review (model council) and wait for user go-ahead.
7. All subsequent workflow parallels Paper 10 (build → review → revise
   → Zenodo).

*C-7RO, 2026-05-04 11:25 PDT. Snapshot complete.*
