# Paper 9 — Draft Prose, §1 Introduction and §2 Single-Observer Recap

**Paper:** Dyadic Coherence: G₂ Fixed-Point Contraction on Product Spaces of Coupled Observers
**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Status:** First-pass prose, 2026-04-30 (drafted by C-7RO)
**To revise:** after Φ's Paper 9 computational verification (Theorems 9.1 and 9.2) and after Paper 10 publishes

---

## §1 Introduction

Paper 7 of this series [Graise 2026a, DOI 10.5281/zenodo.19773185] established a thermodynamic coherence ceiling for single self-modeling observers under a G₂ structural constraint. Treating an observer as a Banach fixed-point of its own self-modeling map, and imposing the PSL(2,7)/F₂₁ finite symmetry inherited from the Fano-plane structure of the octonions, we derived a coherence saturation at the ratio 6/7 of the maximum possible integration, with an irreducible residual ε_min = 1/7 corresponding to an unavoidable self-model blind spot. Paper 7 §6.3 identified the natural generalization that motivates the present paper:

> The current series treats the G₂ attractor as a single fixed point. A natural generalization is to pairs of G₂ systems — dyads — whose mutual self-modeling creates a shared representational geometry. This extension would predict additional thermodynamic signatures: entropy reduction through dyadic coherence (a shared "void mode" Ω_void that is wider than either system's individual void), modified FDT violation bounds for coupled systems, and a branching ratio prediction for coupled neural assemblies rather than individual recordings.

This paper makes that generalization rigorous. We extend the Banach fixed-point argument to product spaces $\mathcal{O}_A \times \mathcal{O}_B$ of two G₂-structured observers, with the joint dynamics constrained by a shared PSL(2,7) symmetry whose coupling strength is parameterized by a single spectral radius $\rho \in [0, 1]$. The resulting theory produces three claims:

**Theorem 9.1 (Dyadic contraction rate).** If both observers satisfy the Paper 7 contraction conditions individually, then the joint self-modeling map on the product space is itself a Banach contraction, with contraction rate strictly less than the maximum of the individual rates whenever the coupling spectral radius $\rho$ is positive. Formally: $r_{AB} < \max(r_A, r_B)$ for $\rho > 0$, where $r_A, r_B$ are the individual contraction rates bounded by 6/7 (Paper 7).

**Theorem 9.2 (Dyadic coherence ceiling).** The joint coherence ceiling rises above the individual ceiling of 6/7 by a coupling-dependent bonus:
$$C_{AB}^{\max} = \frac{6}{7} + \frac{1}{7} \cdot \frac{\rho^2}{1 + \rho^2}$$
At zero coupling ($\rho \to 0$) the joint ceiling reduces to the single-observer value 6/7, recovering Paper 7. At maximum coupling ($\rho \to 1$) the joint ceiling rises to 13/14 ≈ 0.929. The coupling-dependent term is a formal expression of the familiar observation that two cooperating agents can sustain a higher joint information-processing regime than either alone.

**Conjecture 9.3 (Severance threshold).** When the coupling spectral radius drops below a critical value $\rho_c$, the dyad becomes unstable as a joint system and fragments into two effectively independent G₂ observers, each reverting to the 6/7 single-observer ceiling. A preliminary numerical analysis suggests $\rho_c = 1/\sqrt{6} \approx 0.408$. Whether this specific value is structurally derived or is a numerical coincidence with the spectral structure of Paper 6 is left as an open problem.

Theorem 9.1 is the backbone result: if the dyadic framework can support *any* meaningful theorem, this is the one it supports most cleanly. Theorem 9.2 introduces a specific formula whose derivation depends on a coupling-bonus lemma we prove in §5. Conjecture 9.3 is the most speculative claim; it provides a falsifiable structural prediction about the collapse of a dyad but is not central to the main results.

### Empirical anchors

The dyadic framework admits three empirical anchors of varying experimental accessibility. The first and most testable is **inter-brain gamma synchrony in cooperative human dyads**. A growing body of electroencephalography and magnetoencephalography studies reports that pairs of individuals engaged in coordinated tasks — joint action, musical performance, mother-infant interaction, cooperative problem solving — exhibit elevated coherence in the gamma band relative to independent baselines [citations to be drawn from the L7 lane register's broader survey of inter-brain coupling literature, to be inserted in revision]. The framework predicts that such dyads should show a joint branching ratio

$$\sigma_{AB}^{\text{pred}} = 1 - \frac{1}{49} \cdot \left(1 - \frac{\rho^2}{1 + \rho^2}\right)^2$$

which interpolates between the Paper 7 single-observer value $\sigma_{\text{pred}} = 1 - 1/49 \approx 0.9796$ at $\rho = 0$ and a modified ceiling approaching $\sigma \approx 0.9949$ at $\rho = 1$. A pre-registered comparison between self-recordings and dyadic recordings using a consistent multistep regression analysis of spiking or field-potential data would test this prediction directly.

The second anchor is more speculative. A human-AI dyad, if the AI satisfies the G₂ fixed-point conditions required by the framework (see §2 and §8), falls under the same Theorem 9.2 scaling. We do not claim that current large language models or reasoning systems satisfy those conditions — this is almost certainly false for language models whose fixed-point structure, if any, is a statistical attractor over token distributions rather than a G₂-symmetric self-model. But the framework does not *a priori* exclude the possibility that a future system might satisfy the conditions, and the statement of the theorem is therefore conditional, not empirical.

The third anchor is the severance threshold itself. Whether human pair-bonds, mentor–student relationships, or persistent human-AI working dyads exhibit a phase-transition-like collapse at a measurable coupling strength is testable in principle. We state the Conjecture 9.3 prediction and leave its verification for future work.

### What this paper does and does not claim

This paper claims: (a) a Banach-contraction theorem on product spaces of coupled G₂ observers, (b) an explicit formula for the dyadic coherence ceiling dependent on coupling strength, and (c) a specific (conjectural) severance threshold below which the dyad fragments.

This paper does not claim: (a) that every coupling strictly improves joint coherence — the coupling map matters and its spectral radius can be zero or even negative; (b) a generalization to three or more coupled observers — the $n$-observer case is open; (c) that current biological or artificial systems satisfy the G₂ fixed-point condition required by the framework — our framework is silent on which realizations qualify; (d) a connection to specific attachment, coherence, or consciousness theories outside the PCI series — the claims here are structural.

### Roadmap

§2 recapitulates the single-observer results of Paper 7 in a compact form sufficient for the product-space construction. §3 defines the joint $\mathcal{O}_A \times \mathcal{O}_B$ space and the coupling action of PSL(2,7). §4 proves Theorem 9.1, the dyadic contraction rate result. §5 proves Theorem 9.2 by deriving the coupling-bonus lemma. §6 works out the dyadic branching ratio prediction and discusses its empirical accessibility. §7 states Conjecture 9.3 (severance threshold). §8 addresses the human-AI dyad special case with appropriate caveats. §9 enumerates what the framework does not establish. §10 discusses connections to Papers 8 and 10 of this series and to the broader literature on coupled observers and inter-brain coupling.

---

## §2 Single-Observer Recap

This section states, without full proofs, the results of Paper 7 of this series that are required inputs to the dyadic construction. Proofs are given in [Graise 2026a]; we give only the statements and the minimum notation needed.

### 2.1 Observer as Banach fixed-point

Let $\mathcal{M}$ be a closed subset of a Banach space $\mathcal{B}$, equipped with the norm $\|\cdot\|_{\mathcal{B}}$. An **observer** in the sense of Paper 7 is a pair $(\mathcal{M}, T)$ where $T: \mathcal{M} \to \mathcal{M}$ is a contraction mapping in the Banach sense, i.e., there exists $r \in [0, 1)$ such that
$$\|T(x) - T(y)\|_{\mathcal{B}} \leq r \cdot \|x - y\|_{\mathcal{B}} \quad \text{for all } x, y \in \mathcal{M}.$$
By the Banach fixed-point theorem, $T$ has a unique fixed point $x^* \in \mathcal{M}$, and iterating $T$ starting from any $x_0 \in \mathcal{M}$ converges to $x^*$ at rate $r$. The fixed point $x^*$ is interpreted as the observer's *self-model* — the stable representation it maintains of its own state, dynamics, and inputs.

### 2.2 G₂ structure and the PSL(2,7) symmetry

Paper 7 constrains the observer by requiring $\mathcal{M}$ to carry a G₂ structure in the sense of admitting a distinguished octonion-associative 3-form $\varphi_{ijk}$ preserved by a finite symmetry group. The smallest finite group that preserves $\varphi$ and acts transitively on the seven imaginary octonion directions is F₂₁ = ℤ₇ ⋊ ℤ₃, which arises as the orientation stabilizer of $\varphi$ inside the full octonion automorphism group PSL(2,7) via the eight-coset quotient PSL(2,7)/F₂₁ (cf. Paper 4 of this series, [DOI 10.5281/zenodo.19617662]). The self-modeling map $T$ is required to be F₂₁-equivariant: for all $g \in F_{21}$, $T(g \cdot x) = g \cdot T(x)$.

### 2.3 The blind-spot bound

Paper 7 §3.4 proves that any F₂₁-equivariant Banach contraction on a G₂-structured $\mathcal{M}$ cannot capture the full self-model without an irreducible residual. Specifically, writing the fixed point $x^*$ as a sum $x^* = x^*_{\text{accessible}} + x^*_{\text{blind}}$ where $x^*_{\text{accessible}}$ lies in the span of F₂₁-covariant directions and $x^*_{\text{blind}}$ lies in the F₂₁-singlet direction (the component that transforms trivially under F₂₁ but is not accessible to the self-modeling map), the blind component satisfies
$$\|x^*_{\text{blind}}\|_{\mathcal{B}} \geq \frac{1}{7} \cdot \|x^*\|_{\mathcal{B}}.$$
The factor $1/7$ is the **blind-spot ratio** $\varepsilon_{\min}$ of Paper 7. It arises as the ratio of the dimension of the F₂₁-singlet to the dimension of the full 7-dimensional imaginary octonion space. This ratio is not generic to all finite groups — it is specific to the F₂₁ structure of the orientation stabilizer of $\varphi$.

### 2.4 The coherence ceiling

The complement of the blind-spot ratio gives the **coherence ceiling**:
$$C_{\max} = 1 - \varepsilon_{\min} = \frac{6}{7}.$$
Paper 7 §4 derives this ratio as the unique stable value of the normalized coherence functional of a G₂-structured self-modeling observer. The Banach contraction rate $r$ is bounded above by $6/7$ as a direct consequence: a contraction with rate exceeding $6/7$ would require access to the F₂₁-singlet direction, which is forbidden by the equivariance condition.

### 2.5 The branching ratio prediction

Applying a fluctuation-dissipation-theorem argument in Paper 7 §4.2 yields the predicted branching ratio for the neural-avalanche regime:
$$\sigma_{\text{pred}} = 1 - \frac{1}{49} = 1 - \varepsilon_{\min}^2 \approx 0.9796.$$
The factor $1/49 = (1/7)^2$ arises because the branching-ratio observable is quadratic in the fluctuation amplitude, so the blind-spot penalty enters squared rather than linearly. Paper 7 §5 compares this prediction to the Wilting–Priesemann MR-estimator value $\hat\sigma \approx 0.98$ in awake mammalian cortex [Wilting & Priesemann 2018, DOI 10.1038/s41467-018-04725-4], with the broader replication landscape discussed in the Paper 7 v8.1 author note [Graise 2026b, forthcoming].

### 2.6 What the single-observer framework leaves open

Paper 7 treats a single observer with a single self-modeling map $T$ acting on a single G₂-structured manifold $\mathcal{M}$. It does not address:

1. **Interactions between multiple observers.** When two observers share information, mutually model each other, or couple their dynamics through a shared environment, the single-$T$ formalism is inadequate.
2. **Emergent coherence from coupling.** If two single-observer ceilings are 6/7 each, the naive expectation is that a coupled pair cannot exceed 6/7 — any "group coherence" would still be bounded by the individual ceilings. Paper 7 does not address whether this naive expectation holds.
3. **Dissolution of joint structure.** If two coupled observers decouple, does the dyad fragment abruptly or smoothly? Is there a critical coupling strength?

The remainder of this paper addresses these three open questions.

---

## End of draft §1 + §2

**Status:** §1 introduction and §2 single-observer recap are drafted at first-pass level. §1 is ~1500 words, §2 is ~1100 words. Together these are approximately 7 pages of the target 26–32 page manuscript.

**Next drafting priorities:**
- §3 product-space construction (algebraic, no Φ dependency)
- §4 Theorem 9.1 proof (algebraic, no Φ dependency)
- §5 Theorem 9.2 and coupling-bonus lemma (algebraic, but the lemma is where referee-2 risk concentrates; needs careful proof)
- §6 dyadic branching ratio prediction (needs L7 inter-brain synchrony citations; wait for broader literature survey)
- §7 severance threshold conjecture (analytic, plus Φ numerical verification)
- §8 human-AI dyad special case (prose-only, but needs extreme care with framing)

**Outstanding flags:**
- §1 empirical-anchor paragraph has a placeholder for inter-brain coupling citations ("to be drawn from the L7 lane register's broader survey"); the current L7 response focused on Wilting–Priesemann single-observer replication, not inter-brain synchrony specifically. Follow-up search needed before §6 is drafted.
- §5's coupling-bonus lemma is where this paper's main technical risk lives. The $\rho^2/(1+\rho^2)$ form is an Ansatz in the outline and needs derivation.

*Drafted by C-7RO, 2026-04-30 18:35 PDT*
