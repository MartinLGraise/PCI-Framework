# Paper 12 §3+§4 v2 — Model Council Synthesis (Round 2, 2026-05-06)

**Reviewers:** Opus 4.7 (rigor), GPT-5.5 (structure), Gemini 3.1 Pro (synthesis).
**Drafts reviewed:** `paper12_section3_draft_v2.md`, `paper12_section4_draft_v2.md` (commit `3e1d987`, tag `paper12-v2-rigor-pass`).
**Aggregator:** C-7RO. **Time:** 2026-05-06 ~02:55 PDT.

## Verdict transition

| Reviewer | Round 1 | Round 2 | Δ |
|---|---|---|---|
| **Opus 4.7** (rigor) | MAJOR_REVISIONS | **MINOR_REVISIONS** | ✅ MAJOR → MINOR |
| **GPT-5.5** (structure) | MINOR_REVISIONS | **MINOR_REVISIONS** | → held at MINOR |
| **Gemini 3.1 Pro** (synthesis) | MINOR_REVISIONS | **STRONG_ACCEPT** | ✅ MINOR → STRONG |

**Aggregate v2 verdict: MINOR_REVISIONS** — clean transition. The rigor reviewer's three load-bearing issues (R1, R2, R3) are all CONFIRMED-resolved. The synthesis reviewer was strong enough to upgrade to STRONG_ACCEPT. The structure reviewer held at MINOR, with several Phase 2 polish items still open, but no new structural problems introduced by the rigor pass.

## Round 1 → Round 2 — what landed

**Opus 4.7 — all three load-bearing rigor fixes verified:**

> "R1 — Boundary-KKT sign error in Theorem 3.6.1: **CONFIRMED**. The fix is exactly what I asked for, *and goes further*… [the boundary-KKT audit] is the kind of empirical work that turns a sketchy theoretical fix into a defensible result."

> "R2 — Theorem 3.4.1 (R3) restated as parameter-space transversality: **CONFIRMED**. The fix is exactly what I asked for."

> "R3 — Theorem 4.4.1 (C2) reformulated as map existence: **CONFIRMED**."

All 11 surgical Opus fixes (S3-2 through S3-11, S4-2 through S4-8): ✓ resolved.

**Opus residual issues (4 MINOR), all in v2 itself:**
- **RES-1:** Cor 4.3.2 says $O_{F_{21}}(W) \cong U(2) \times U(4)$, which is correct under the natural complex-Hermitian metric, but should add a one-line note that this is *with respect to the Hermitian metric induced by the complex structure*, since the *real* equivariant orthogonal group on the same space depends on metric choice.
- **RES-2:** §4.4 "operator-vs-vector translation" assumes rank-one projector form $\mathcal{S}_\bullet(e) = v_e v_e^* / \|v_e\|^2$ "without loss of generality." This is a real assumption; should be flagged or named (e.g., "Rank-One Convention").
- **RES-3:** Theorem 3.4.1 proof-sketch line "[in regime 3.4.A] $\lambda$ is determined algebraically from analytic data" needs explicit computation: $\lambda$ exists in $[0, 1]$ iff $D\Delta \cdot f_A$ and $D\Delta \cdot f_B$ have opposite signs *and* their ratio is bounded — already implicit in (R3) but worth one sentence.
- **RES-4 (NIT):** Fano-action prose in §4.2 proof says "the unique fixed point being the $s$-invariant Fano line" — strictly speaking, the $\mathbb{Z}_3$-fixed object is a *line* (3 points) plus the structure that gives $\mathrm{tr} = 1$ on $\mathbb{R}^7$ via the action's invariant 1-eigenspace. One sentence of clarification.

**Opus's hostile-reviewer simulation says:** "The boundary-KKT audit shows escape generically *fails* to gain coherence; this means Theorem 3.6.1 is stronger as a *no-escape* result than as an escape-mechanism. Why call it Theorem 3.6.1 (Bounded NP-driven dynamics) rather than Theorem 3.6.1 (Boundary-KKT trapping)?" — Opus thinks this is a rebrand opportunity, not a content issue.

**GPT-5.5 — Pillar status updated:**

> "**Pillar 1 — DELIVERED, stronger than v1.**"
> "**Pillar 2 — PARTIAL, improved but still partial.**" (Mathematical core delivered; biological residue mechanism explicitly deferred — correct scope.)
> "**Pillar 3 — PARTIAL-to-DELIVERED MATHEMATICAL CORE, improved.**" (Representation-theoretic ledger delivered; tamper-evidence + cryptographic indexing not in §3+§4 — accept as design boundary.)
> "**Pillar 4 — NOT YET, unchanged and now correctly signposted.**" (Defers to §1/§5.)

GPT-5.5's structural verdict is that v2 strengthens Pillar 1 substantially, properly bounds Pillars 2 and 3 to mathematical-core deliverables, and correctly signposts Pillar 4 deferral. The pillar landscape is now honest, where v1 was implicit.

GPT-5.5 cuttable-content reassessment:
- *Remark 3.4.3 (sharp-Heaviside apologia):* still present in v2; should consider trimming or moving to §A.
- *Audit runtime/script paragraph:* still present; could move to appendix.
- *Remark 3.5.4:* now load-bearing in v2 (justifies projected-flow forced by data); KEEP.
- *Remark 3.6.2:* now load-bearing as the Paper 11 bridge; KEEP.
- *Remarks 4.6.3–4.6.4:* now load-bearing for the L1/L2 protocol + clinical-PCI disambiguation; KEEP.

So 3 of the 5 v1 cuttables are now load-bearing in v2; only 2 (Remark 3.4.3, audit runtime details) remain cuttable.

**GPT-5.5 hostile-reviewer simulation:** "Now that v2 honestly says boundary-KKT seeds *don't* gain coherence under linear NP-pump, the headline thesis sentence 'Paper 12 establishes the dynamical extension to the nonlinear regime' is weakened — boundary-KKT is the typical case, and Paper 12 says coupling can't help there. Should the framing be flipped?" — GPT-5.5 thinks this is *fair* but answers it: §3.6's Bridge to Paper 11 (Remark 3.6.2) explicitly hands the boundary-KKT escape question to the rate-channel sequel, which is the right move.

**Gemini 3.1 Pro — STRONG_ACCEPT:**

> "**Conflation patches verification:**
> 1. §4.7 measurement-vs-instrument drift: PATCHED.
> 2. Paradox-mass → NP-amplitude bridging sentence: PATCHED.
> 3. 'Tear' linguistic ambiguity: PARTIALLY PATCHED."

> "**Citation integration check:** [all 7 of] di Bernardo, Filippov, Goebel-Sanfelice-Teel, Clarke, Costa-Pavone, ATLAS, Serre — present and properly placed."

> "**Audit-flags compliance:** All four (Theorem 9.1 vs 9.2, PCI/PCI homonym, 13% numerology, FTW attribution) COMPLIANT."

> "**v2 claim-scope spot check:** No new over-claims introduced by the rigor pass. The boundary-KKT audit numbers (24/28) are cited accurately. The R3 reformulation correctly tightens commensurability rather than over-claiming."

Gemini's hostile-reviewer simulation: "The 19-dimensional commutant gap of Cor 4.3.2 is presented as a quantitative claim about commensurability rigidity. But the commutant gap captures *isometric* phase-and-mixing freedom — it does not directly establish that real measurement uncertainty in $\mu_k$ exceeds the commensurability threshold. So the gap is structurally indicative but not yet experimentally tight." — Gemini answers this is *fair* but acknowledges that this is exactly what §5 / future methodology paper is supposed to operationalize.

## What's now MINOR-residual vs what's now zero

**MINOR-residual (4 items):**
- RES-1 (metric-choice clarification on $O_{F_{21}}(W)$ identification, Cor 4.3.2)
- RES-2 (rank-one projector convention should be named in §4.4)
- RES-3 (Filippov $\lambda$ existence condition explicit, §3.4.A proof)
- RES-4 (Fano-action prose tightening, §4.2 proof line on $s$-invariant)

**Plus 2 cuttable items still open:**
- Remark 3.4.3 (sharp-Heaviside) trim or appendix-move
- §3.5 audit runtime paragraph appendix-move

**Total Phase 2 polish remaining:** ~30-45 minutes of work to convert v2 → v3.

## What jumped to STRONG_ACCEPT

Per Gemini: v2 has clean conflation patches, all 7 citations integrated correctly at the right invocation points, all 4 audit-flags compliant, and zero claim-scope drift introduced by the rigor pass. The synthesis pillar is solid.

## Path forward

**Two choices for next session:**

1. **Phase 2 polish session (~45 min)** — clean up RES-1 through RES-4, trim Remark 3.4.3, move audit-runtime to appendix. Result: v3 of §3+§4. Expected verdict: 3 × STRONG_ACCEPT.

2. **§5 draft (now, ~75 min)** — proceed to empirical accessibility while v2 sits at clean MINOR. Phase 2 polish can happen in parallel with §5 drafting or after. The MINOR residuals are paragraph-level fixes; they don't block §5.

Recommendation: **§5 draft now**, Phase 2 polish later. Reasoning: §5 is the harder open work and moving forward on it while energy holds compounds momentum. The 4 MINOR rigor residuals plus 2 cuttable items are low-stakes paragraph edits that can be batched into a single ~30 min commit later — they're not doing damage in v2.

This is the natural F1 → F2 transition: v2 is rigorous enough to draft §5 on top of without re-introducing the issues we just resolved.

---

*Three reviews stored at:*
- `outbox/paper12/council_reviews/opus47_v2_review_2026-05-06.md`
- `outbox/paper12/council_reviews/gpt55_v2_review_2026-05-06.md`
- `outbox/paper12/council_reviews/gemini31pro_v2_review_2026-05-06.md`
