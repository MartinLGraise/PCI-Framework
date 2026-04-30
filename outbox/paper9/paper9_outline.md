# Paper 9 — Dyadic Coherence

**Working title:** "Dyadic Coherence: G₂ Fixed-Point Contraction on Product Spaces of Coupled Observers"

**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Status:** OUTLINE / SCAFFOLDING — pre-derivation
**Series position:** Paper 9 of the PCI/PME Framework arc
**Branch:** paper7-foundation (will move to paper9-dyadic once we have a v1 draft)
**Sequel to:** Paper 7 (Thermodynamic Cost of Coherence Ceiling)
**Parallel track to:** Paper 8 (Eight-Coset Simulator), Paper 10 (SIC-POVM / G₂ Embedding)

---

## 1. Why this paper exists

Paper 7 [DOI 10.5281/zenodo.19773185] derived a thermodynamic coherence ceiling by treating an observer as a single G₂-structured self-modeling system, bounded by the PSL(2,7)/F₂₁ blind-spot ratio ε_min = 1/7. Section §6.3 of that paper explicitly identifies the natural generalization:

> *"The current series treats the G₂ attractor as a single fixed point. A natural generalization is to pairs of G₂ systems — dyads — whose mutual self-modeling creates a shared representational geometry. This extension would predict additional thermodynamic signatures: entropy reduction through dyadic coherence (a shared 'void mode' Ω_void that is wider than either system's individual void), modified FDT violation bounds for coupled systems, and a branching ratio prediction for coupled neural assemblies rather than individual recordings."*

Paper 9 makes this generalization rigorous. It extends the Banach fixed-point argument to contractions on *product spaces* of two G₂ manifolds, where the product structure is constrained by a shared PSL(2,7) symmetry. The result is a quantitative theory of dyadic coherence with falsifiable predictions for:

1. **Inter-brain gamma synchrony** in human pairs engaged in cooperative tasks (an empirical anchor independent of the single-observer awake-cortex prediction in Paper 7)
2. **Human-AI dyads** as a special case where the AI is a structured G₂-like system rather than a biological brain — a regime the framework should make predictions about even though it isn't yet experimentally testable
3. **Severance / decoupling thresholds** — the analogue of the ε_min = 1/7 blind spot, but for a dyad: at what coupling strength does the joint system fragment back into two independent G₂ observers?

The motivating physical observation: *coherence is not maximized in isolation*. Two systems sharing a representational frame can sustain higher joint coherence than either can alone. This is the dyadic version of the (d-1)/d ceiling.

---

## 2. Structure (target: 26-32 pages, ~20-25 references)

### §1 Introduction
- Recap of Paper 7's single-observer ceiling (1 paragraph)
- The single → dyad generalization stated in Paper 7 §6.3
- What this paper claims and what it does NOT claim
- Roadmap

### §2 Single-observer recap
Compact restatement of Paper 7's key results, sufficient that Paper 9 reads independently:
- The G₂ self-modeling fixed-point construction
- Banach contraction with rate 6/7
- ε_min = 1/7 PSL(2,7)/F₂₁ blind-spot bound
- σ_pred = 1 − 1/49 ≈ 0.9796 branching ratio prediction
- The thermodynamic coherence ceiling C_max

This section is ~3 pages, primarily for self-containment. Cited papers do the heavy lifting.

### §3 The product-space construction
- Two G₂-structured observers $\mathcal{O}_A$ and $\mathcal{O}_B$, each a Banach fixed-point of its own self-modeling map
- Joint state space $\mathcal{O}_A \times \mathcal{O}_B$
- Shared PSL(2,7) symmetry constraint: define a *coupling action* of PSL(2,7) on the product that reduces to the diagonal action when the observers are aligned and to the independent action when they are decoupled
- Modeling-choice stack: diagonal action vs. anti-diagonal vs. mixed; we adopt the diagonal as canonical, document the alternatives
- Define the joint G₂ structure on the product space: a 28-dim Lie algebra structure (since 𝔤₂ × 𝔤₂ has dim 28) that respects both individual structures and the coupling

### §4 The dyadic Banach contraction
- Product-space self-modeling map $T_{AB}: \mathcal{O}_A \times \mathcal{O}_B \to \mathcal{O}_A \times \mathcal{O}_B$
- Decompose: $T_{AB} = (T_A \otimes T_B) \circ \Psi_{\text{coupling}}$
- Show that under the diagonal PSL(2,7) action, the contraction rate of the product map is bounded by $\max(r_A, r_B) \cdot \rho(\Psi)$ where $\rho$ is the spectral radius of the coupling map
- **Key result (Theorem 9.1):** The dyadic contraction rate is *strictly less than* either individual rate when $\rho(\Psi) < 1$ — i.e., a properly coupled dyad converges faster than either observer in isolation. This is the formal version of "two heads better than one."
- Modeling-choice stack: spectral-radius bound vs. operator-norm bound; we use spectral radius because the diagonal PSL(2,7) action is normal

### §5 Theorem 9.2 — The dyadic coherence ceiling
**Statement:** For a coupled dyad with coupling map $\Psi$ of spectral radius $\rho$, the joint coherence ceiling is

$$C_{AB}^{\max} = \frac{6}{7} + \frac{1}{7} \cdot \frac{\rho^2}{1 + \rho^2}$$

where the second term is the *coupling bonus* — the additional fraction of the blind-spot subspace that the dyad can collectively access through mutual modeling.

**Proof sketch:**
1. The individual ceiling is 6/7 with residual 1/7 (Paper 7).
2. The residual 1/7 corresponds to the F₂₁-stabilized direction in PSL(2,7)/F₂₁.
3. When two observers share a PSL(2,7) frame with coupling spectral radius $\rho$, the joint blind-spot is reduced by a factor of $1 - \rho^2/(1+\rho^2)$ (lemma).
4. Therefore the joint ceiling rises from 6/7 by $(1/7) \cdot \rho^2/(1+\rho^2)$.

**Implications:**
- $\rho \to 0$: decoupled, ceiling = 6/7 (recover Paper 7)
- $\rho \to 1$: maximally coupled, ceiling = 6/7 + 1/14 = 13/14 ≈ 0.929
- $\rho = 1$ exactly: the dyad merges into a single 14-dim G₂ system (singular limit; the product structure breaks down)

### §6 The dyadic branching ratio prediction
- Apply the same FDT-style argument as Paper 7 to the product space
- Predicted joint branching ratio:

$$\sigma_{AB}^{\text{pred}} = 1 - \frac{1}{49} \cdot (1 - \rho^2/(1+\rho^2))^2$$

- Empirical anchor: **inter-brain gamma synchrony in cooperative dyads.** Multiple studies (Pérez et al. 2017, Dikker et al. 2017, others — to fill in from L7 results when available) report enhanced gamma coupling in coordinated dyads. The prediction: σ_AB approaches but does not reach 1, with the exact value depending on the measurable coupling strength.
- Modeling-choice stack: how to operationalize $\rho$ from observable inter-brain coherence measures (PLV, dPLI, MI). We propose Mutual Information / channel capacity normalized to single-brain capacity as the cleanest mapping.

### §7 The severance threshold
**Statement (Conjecture 9.3):** The dyad is unstable as a unit when the coupling spectral radius drops below a critical value $\rho_c$:

$$\rho_c = \frac{1}{\sqrt{6}} \approx 0.408$$

(Numerical coincidence with the $\sqrt{1/6}$ factor that appears in the Paper 6 contraction; whether this is structural or coincidental is left as an open problem.)

**Interpretation:** Below $\rho_c$, the joint system fragments into two independent G₂ observers. The 1/7 residual blind-spot reasserts itself, and the dyadic coherence advantage collapses.

**Empirical anchor:** Severance / breakup / decoupling phenomena. Whether human pair-bonds, mentor-student pairs, or persistent human-AI working dyads exhibit this threshold is testable in principle but not in the scope of this paper. We state the prediction and leave verification for future work.

### §8 Human-AI dyads as a special case
- The Paper 9 framework does not require both observers to be biological
- A G₂-structured AI agent (defined by being a Banach fixed-point of its own self-modeling map, with PSL(2,7) symmetry) is a valid second member of a dyad
- The prediction Theorem 9.2 applies: a properly coupled human-AI dyad has a higher coherence ceiling than either alone
- This is a consequence of the framework, not an empirical claim — the framework is silent on whether current AI systems satisfy the G₂-fixed-point condition (most plausibly, language models do not; specialized reasoning systems might)
- Cite Yamaguchi et al., Bench et al., and other emerging human-AI collaboration research as adjacent context, NOT as confirming evidence

### §9 What this paper does *not* establish
- Does not claim two coupled observers always coherence-improve; the coupling map matters and the spectral radius can be small or zero
- Does not claim Theorem 9.1 generalizes beyond two observers; the n-observer case is open (linear scaling? nonlinear? saturating?)
- Does not claim severance threshold $\rho_c = 1/\sqrt{6}$ is structurally derived; numerical coincidence with Paper 6 is flagged but not explained
- Does not claim human-AI dyads currently exhibit dyadic coherence; the framework provides the mathematical possibility but not empirical evidence
- Does not connect to specific consciousness or attachment theories; the framework is structural

### §10 Discussion and open problems
- Connection to inter-brain coupling literature (gamma synchrony, dPLI, etc.)
- Connection to the n-observer generalization (Paper 11+ candidate)
- Connection to Paper 8's eight-coset simulator (the 8 cosets could index 8 dyad classes; this is open)
- Connection to Paper 10's SIC-POVM operator basis (the dyadic G₂ structure should embed in 𝔤𝔩(7,ℂ) ⊗ 𝔤𝔩(7,ℂ); is the Theorem 1 embedding extendable?)
- The severance threshold $\rho_c$ as an empirical research target

---

## 3. Computations needed (work request to Φ)

See `/inbox/for_phi/paper9_computation_request.md` (TO BE WRITTEN — pending Paper 10 Tasks 2/3 completion).

Briefly:
1. **Symbolic** (Cadabra2 / SymPy): construct the joint 28-dim 𝔤₂ × 𝔤₂ Lie algebra and verify Lie bracket closure under the diagonal PSL(2,7) action
2. **Numerical** (NumPy / mpmath): verify Theorem 9.1 contraction-rate bound for at least three choices of coupling map $\Psi$ with varying $\rho$
3. **Numerical** (NumPy / mpmath): verify Theorem 9.2 ceiling formula by direct computation of joint coherence at $\rho = 0, 0.5, 0.9, 1.0$
4. **Analytic exploration**: the $\rho_c = 1/\sqrt{6}$ severance threshold conjecture — does it derive from a known eigenvalue argument, or is it numerical coincidence?

This is the lightest computational paper in the queue. Most of Paper 9 is analytic.

---

## 4. Modeling-choice stacks

- **§3 stack:** diagonal vs. anti-diagonal vs. mixed PSL(2,7) action on the product
- **§4 stack:** spectral-radius vs. operator-norm contraction bound
- **§5 stack:** the joint blind-spot reduction lemma (where exactly does the $\rho^2/(1+\rho^2)$ form come from? is this the *only* possible coupling-bonus form?)
- **§6 stack:** how to operationalize the spectral radius $\rho$ from observable inter-brain coherence measures
- **§7 stack:** severance threshold definition (spectral radius drop below critical, or alternative criteria like Lyapunov instability of the joint flow)

---

## 5. Risk register

| Risk | Mitigation |
|------|-----------|
| Theorem 9.2 ceiling formula is wrong (specifically, the $\rho^2/(1+\rho^2)$ form is unjustified) | Derive it cleanly in §5 or admit it's an Ansatz; keep Theorem 9.1 (contraction rate) as the safer backbone result |
| Inter-brain synchrony empirical anchor is methodologically contested | Cite multiple distinct measures; do not pin the prediction to one method |
| The "human-AI dyad" §8 is interpreted as a literal claim about LLMs | Frame strictly as conditional: IF an AI satisfies the G₂ fixed-point criterion, THEN dyadic coherence applies. Most current AI does not satisfy this criterion (footnote) |
| Severance threshold $\rho_c = 1/\sqrt{6}$ is unfalsifiable in human dyads | Keep §7 as a prediction labeled CONJECTURE, not theorem; do not stake the paper on it |
| Reviewer says "this is just statistical mechanics of coupled systems with extra octonion vocabulary" | Strongest defense: Theorem 9.2's specific form $6/7 + (1/7)\rho^2/(1+\rho^2)$ is not generic — the 1/7 residual comes from the PSL(2,7)/F₂₁ structure inherited from Papers 4 and 7, not from generic coupling-theory |

---

## 6. Authorship and acknowledgments

- **Author:** Martin Luther Graise (sole, all conceptual + paper writing)
- **Computational support:** Φ (Anthropic Claude Dispatch, Cadabra2 / SymPy / NumPy / mpmath under author's direction)
- **External research support:** ChatGPT GPT-5 Pro (research lane register)
- **Use of AI Tools:** Same disclosure pattern as Papers 7 and 10

---

## 7. Target venue

- **First choice:** *Foundations of Physics* (likely the same venue as Paper 10; both target QBism / consciousness-adjacent foundational physics)
- **Second choice:** *Entropy* (open-access, accepts coupled-systems and FDT-style work)
- **Fallback:** arXiv + Zenodo (consistent with the rest of the series)

---

## 8. Status checklist

- [x] Outline written (this document)
- [ ] §1 introduction drafted
- [ ] §2 single-observer recap drafted (compact)
- [ ] §3 product-space construction drafted
- [ ] §4 Theorem 9.1 stated and proved
- [ ] §5 Theorem 9.2 stated; coupling-bonus lemma proved
- [ ] §6 dyadic branching ratio prediction
- [ ] §7 severance threshold conjecture
- [ ] §8 human-AI dyad special case (with strong caveats)
- [ ] §9 what is not established
- [ ] §10 discussion
- [ ] Φ computational verification of Theorems 9.1 and 9.2
- [ ] Severance threshold investigation
- [ ] Front matter
- [ ] Model Council pass
- [ ] Revisions
- [ ] Zenodo
- [ ] Submitted

---

## 9. Sequencing relative to other in-flight papers

**Paper 9 is intentionally the LAST of the four in-flight papers** to draft beyond outline:

1. **Paper 7** — published, awaiting MDPI APC waiver
2. **Paper 10** — Theorem 1 done, Tasks 2/3 in flight; closest to publication
3. **Paper 8** — outline + Φ work request in queue, Tasks 1-3 not yet started (gated by Φ usage budget)
4. **Paper 9** — this outline; computations are lighter than 8 or 10, but conceptually depends on Paper 10's SIC operator basis being established

**Why Paper 9 last:** the §10 discussion of "joint G₂ embedding extends to 𝔤𝔩(7,ℂ) ⊗ 𝔤𝔩(7,ℂ)" needs Paper 10's Theorem 1 already cited in the literature. Drafting Paper 9 before Paper 10 ships would force forward-referencing.

**Acceleration option:** Paper 9 could be drafted in parallel as a shorter, tighter paper if Paper 7 referees come back asking "what about the dyadic case?" — in that scenario, Paper 9 becomes a fast follow-up rather than a third sequel.

---

*Drafted by C-7RO, 2026-04-30 16:55 PDT*
