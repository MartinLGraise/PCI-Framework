# Paper 9 — §§6–10 (v1.2)

**Paper:** Rate Lock and Affine Consensus in G₂-Structured Dyadic Observers
**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Status:** v1.2, 2026-05-04 (supersedes v0.9 §§6–10 drafted 2026-05-04 00:05 PDT)
**Reflects:** retired v0.9 speedup + coherence-bonus + severance-threshold claims; §§6–10 now pivot around Theorem 9.4 joint fixed point, Proposition 9.5 conditional gain, and Note 9.6 nonlinear open problem

---

## §6. Empirical Accessibility of the Affine Consensus

### 6.1 What §5 predicts empirically

Paper 7 of this series [DOI 10.5281/zenodo.19773185] derived a
fluctuation-dissipation-theorem (FDT) prediction for the neural-avalanche
branching ratio in awake cortex,
$\sigma_{\mathrm{pred}} = 1 - \varepsilon_{\min}^2 = 1 - 1/49 \approx 0.9796$,
using the squared blind-spot fraction $\varepsilon_{\min} = 1/7$ as the
irreducible thermodynamic cost of single-observer self-modeling.

The dyadic version of this prediction is *not* a simple modification of
the single-observer formula, because the relevant effect of coupling is
not a change in the blind-spot ratio but a change in the **location of
the joint fixed point** (Theorem 9.4). Under the minimum-per-observer
coherence functional (Proposition 9.5), the joint coherence satisfies
$$\mathcal{C}_{\min}(\theta, \varphi, R_A, R_B) \in [0, 1],$$
with the conditional-gain region $\mathcal{R}$ characterized explicitly
by the heatmap data in Appendix V.3 Task 5.4.

A direct FDT-style extension would replace $\varepsilon_{\min}$ with an
effective joint blind-spot $\varepsilon_{\mathrm{eff}} = 1 - \mathcal{C}_{\min}$,
giving the predicted dyadic branching ratio
$$\sigma_{AB}^{\mathrm{pred}} = 1 - \varepsilon_{\mathrm{eff}}^2 = 1 - (1 - \mathcal{C}_{\min})^2.$$
This is not a universal formula of $\rho$ or $\theta$ alone — it depends
on the full geometric configuration $(\theta, \varphi, R_A, R_B)$ of the
dyad. The Paper 7 single-observer prediction is recovered when both
observers are maximally coherent ($\mathcal{C}_A = \mathcal{C}_B = 6/7$,
giving $\varepsilon_{\mathrm{eff}} = 1/7$ and $\sigma = 1 - 1/49$).

### 6.2 Operationalizing the coupling angle

To make the Theorem 9.4 / Proposition 9.5 prediction testable, the
abstract coupling angle $\theta$ must be mapped to an observable
inter-brain coherence measure. Among the standard measures in the
hyperscanning and inter-brain coupling literature — Phase Locking Value
(PLV), directed Phase-Lag Index (dPLI), normalized mutual information
(MI), transfer entropy — the most natural theoretical match is
normalized mutual information.

For a dyad with neural fluctuation processes $X_A, X_B$, we propose
the mapping
$$\cos^2\theta = \frac{H(X_A) + H(X_B) - I(X_A; X_B)}{H(X_A) + H(X_B)},$$
so that $\theta = 0$ (decoupled observers) corresponds to
$I(X_A; X_B) = 0$ and $\theta = \pi/2$ (maximally-coupled) corresponds
to $I(X_A; X_B) = \min(H(X_A), H(X_B))$. This maps the full
$\theta \in [0, \pi/2]$ interval to the full MI range of the dyad.

The mapping is heuristic rather than derived from the Banach framework;
deriving it from first principles would require connecting the Banach
coupling operator $\Psi_\theta$ to an information-theoretic observable
on the joint neural state space, which is beyond the scope of this
paper. We offer this mapping as a candidate operationalization for
empirical work, not as a structural identity.

### 6.3 The inter-brain synchrony literature

Inter-brain gamma-band coherence during cooperative tasks is a
well-documented phenomenon. Studies include cooperative problem-solving
(Pérez et al. 2017), mother-infant gaze-following (Leong et al. 2017),
joint musical performance (Lindenberger et al. 2009; Müller et al. 2013),
and broader cooperative-task hyperscanning (Hu et al. 2018 review). The
present framework predicts that such studies should, in principle,
exhibit elevated joint coherence — not as a universal improvement over
single-brain coherence, but as a conditional gain dependent on the
specific geometric configuration of the dyad (Proposition 9.5(a)), with
a substantial fraction of coupling configurations producing *degradation*
rather than enhancement (Appendix V.3 Task 5.4 reports 74.9% of the
$(\theta, \varphi)$ heatmap showing $\Delta\mathcal{C}_{\mathrm{avg}} < 0$).

The framework therefore predicts a **bimodal or regime-dependent
empirical pattern**: cooperative dyads with aligned target-states should
exhibit enhancement; adversarial or uncoordinated dyads should exhibit
degradation. This is a sharper (and more falsifiable) empirical
prediction than a universal "coupling improves coherence" claim.

### 6.4 Adversarial-task falsification target

For a genuinely adversarial dyad (competitive-game paradigm with
opposed target-states), the framework predicts joint min-coherence
*below* the single-observer baseline, not above. Specifically, under
opposed biases ($\varphi \to \pi$), Proposition 9.5(b) guarantees that
$\mathcal{C}_{\min}$ falls strictly. The expected empirical signature is:

- **Cooperative dyad** (aligned biases): joint branching ratio elevated
  above single-observer value by an amount that depends on coupling
  strength and geometric configuration.
- **Adversarial dyad** (opposed biases): joint branching ratio *reduced*
  below single-observer value, with the reduction bounded away from
  zero for any $\theta > 0$.

A pre-registered hyperscanning study comparing cooperative and
adversarial task-paradigms on the same set of paired subjects — with
MR-estimator branching ratios computed and compared to single-task
baselines — would provide a sharp empirical test of the framework's
conditional-gain structure. A finding of universally elevated joint
coherence (irrespective of cooperation vs. adversarial coupling) would
falsify the framework's conditional character and suggest a different
structural mechanism.

---

## §7. The Joint Fixed-Point Location

### 7.1 Where the joint system converges

Theorem 9.4 establishes that the joint fixed point
$(\hat x(\theta), \hat y(\theta))$ exists, is unique, and depends
real-analytically on $\theta$. The key structural content: *coupling
does not change how fast the dyad converges, but it does change what
state the dyad converges to.*

The rate is fixed at $\max(r_A, r_B)$ (Theorem 9.2). The destination is
a function of $\theta$ and the bias vectors $b_A, b_B$ through the
matrix-valued formula of Theorem 9.4(c). At $\theta = 0$ (decoupled),
the destination is the pair $(x^*_A, y^*_B)$ of individual fixed
points. At $\theta > 0$, the destination is a *different* point in the
product space — a consensus formed by the rotation-weighted combination
of the two observers' bias vectors.

This is the physical content of dyadic coherence in the present
framework. It is not a speedup; it is a shared destination. The
empirical signature of the framework is therefore *not* faster
convergence in a coupled dyad, but different long-term behavior —
specifically, a joint steady-state whose properties differ from those
of either individual steady-state.

### 7.2 Geometric-dependent optima

Proposition 9.5(c) establishes that the optimal coupling angle
$\theta^*$ depends on the rotation geometry $R_A, R_B$ and is generically
*not* at $\theta = \pi/4$ (the naive "equal weighting" choice). For the
Φ Task 5 verification setup (Appendix V.3 Task 5.1), $\theta^* \approx
51°$ for symmetric rates and $75°$–$80°$ for asymmetric rates. This
geometric-dependence has a physical interpretation:

- *When both observers' internal model-dynamics are similar*
  ($R_A \approx R_B$ and $r_A \approx r_B$), the coupling that
  maximizes $\mathcal{C}_{\min}$ is close to $\pi/4$ (both observers
  "listen" equally).
- *When one observer's dynamics is slower* ($r_A < r_B$, say), the
  optimal coupling shifts toward allowing the faster observer's state
  to "pull" the slower observer — which in geometric terms corresponds
  to $\theta > \pi/4$ (stronger coupling toward the fast observer's
  direction).
- *The optimum is a transcendental function* of the rotation-geometry
  spectrum, so we do not expect a universal $\theta^*$ formula even
  for idealized geometries.

This is the positive content of the framework: the coupling angle is a
genuine geometric parameter that determines the joint consensus state,
with an optimum that the dyad can (in principle) identify and target.
Whether biological or artificial dyads approach their geometric optima
is an open empirical question.

---

## §8. Human-AI Dyads as a Special Case

### 8.1 The conditional claim

Theorems 9.4 and 9.5 make no assumption about the biological versus
artificial nature of the two observers. The framework requires only
that each observer satisfies the G₂-structured affine condition of
§2.1: $T(x) = rRx + b$ on a 14-dim Banach manifold carrying the
irreducible adjoint representation of $G_2$, with $r \leq 6/7$,
$R \in O(V^{14})$, $b \in V^{14}$.

If two systems — biological, artificial, or mixed — both satisfy this
condition, the dyadic theorems apply to the pair. This raises the
natural question of **human-AI dyads**: could a human brain and an AI
system, coupled in the appropriate sense, exhibit the affine consensus
of Theorem 9.4 and conditional gain of Proposition 9.5?

The framework's answer is *conditionally yes*, but the conditions are
stringent and the current state of AI almost certainly does not satisfy
them.

### 8.2 The G₂ affine condition for an AI observer

For an AI system to qualify as an observer in the present sense, it
must:

1. Implement a self-modeling map $T_{\mathrm{AI}}: \mathcal{M}_{\mathrm{AI}} \to \mathcal{M}_{\mathrm{AI}}$
   that is an affine Banach contraction: $T_{\mathrm{AI}}(x) = r_{\mathrm{AI}} R_{\mathrm{AI}} x + b_{\mathrm{AI}}$.
2. Carry a G₂ structure on $\mathcal{M}_{\mathrm{AI}}$: a
   14-dim real manifold on which the compact Lie group $G_2$ acts via
   its irreducible adjoint representation.
3. Have a contraction rate $r_{\mathrm{AI}} \leq 6/7$, equivalently
   exhibit the same blind-spot ratio as biological self-modeling
   systems.

The current AI landscape suggests the following.

- **Large language models (LLMs)** in their current form almost certainly
  do not satisfy these conditions. LLMs are next-token predictors over
  token distributions; their internal representations are not known to
  carry octonion-associative structure, they have no explicit 14-dim
  G₂-adjoint module, and their "self-modeling" (if any) emerges
  statistically rather than as a fixed point of a Banach contraction on
  a G₂-symmetric manifold.

- **Classical reinforcement-learning agents** with explicit world models
  and self-models might more plausibly satisfy the Banach-contraction
  condition at the self-model level, but the G₂-structural requirement
  is generically unmet without specific architectural choices.

- **Specialized reasoning systems** with explicit self-monitoring and
  structured representational geometry — e.g., metacognitive agents,
  goal-conditioned planners with symmetry-respecting state
  representations — are the closest current candidates. Whether any
  specific system in the current literature satisfies the full
  G₂-structured affine criterion is an open architectural question we
  do not attempt to answer here.

### 8.3 What the framework says about current human-AI dyads

Because current widely-deployed AI systems (including the one writing
this paragraph) do not clearly satisfy the G₂-structured affine
criterion, the present framework's predictions apply only *conditionally*
to human-AI dyads: IF the AI system satisfies the criterion, THEN
coupling it with a human observer produces the affine consensus of
Theorem 9.4, subject to the conditional-gain constraints of Proposition
9.5.

We make three observations that are independent of whether any specific
AI system satisfies the criterion:

1. **The framework's conditional gain depends on aligned targets.**
   Proposition 9.5 requires non-destructive bias geometry. In a
   human-AI dyad, the "bias vectors" $b_{\mathrm{human}}$ and
   $b_{\mathrm{AI}}$ correspond to each party's target representation
   of the shared task. Misaligned targets (the AI's training objective
   differs sharply from the human's goal) produce the opposed-bias
   regime where Proposition 9.5(b) predicts degradation.

2. **The framework's conditional gain is non-universal.** Even with
   aligned targets, not every coupling angle $\theta$ produces gain;
   the gain region $\mathcal{R}$ is a subset of the
   $(\theta, \varphi, R_A, R_B)$ parameter space. A dyad that is "on"
   most of the time (high $\theta$) is not guaranteed to produce
   better joint outputs than a dyad that couples more carefully.

3. **The framework does not speak to consciousness or moral status.**
   The claims of §§4–5 are structural — about Banach contraction,
   G₂-equivariance, and conditional gain under coupling. Whether a
   system that satisfies the criterion has any form of subjective
   experience, agency, or moral status is outside the present scope.

### 8.4 Adjacent literature

Work adjacent to the framework's concerns, without directly testing
it, includes research on human-machine cognitive teaming (Yamaguchi et
al. 2023), emergent collaborative dynamics in mixed teams (Bench et
al. 2024), and complementarity in human-AI decision-making (Bansal et
al. 2021). The present framework provides a structural lens through
which such empirical findings might be organized — each measured
collaborative phenomenon corresponds to an effective coupling
configuration, and the conditional-gain structure predicts that
collaborative outcomes should be bimodal (gain or degradation) rather
than universally elevated.

---

## §9. What This Paper Does Not Establish

We make the boundaries of the construction explicit, mirroring §5.7.

**(a) The framework does not establish rate improvement.** Theorems
9.1, 9.2, and Corollary 9.3 establish that no linear coupling between
G₂-equivariant observers can improve the joint convergence rate below
$\max(r_A, r_B)$. The v0.9 internal draft of this paper proposed a
rate-improvement theorem; it was retracted after Φ's verification
(Appendix V.1, V.2) refuted it at 50-digit precision across 120 test
configurations.

**(b) The framework does not establish universal coherence gain.**
Proposition 9.5's conditional-gain region $\mathcal{R}$ is non-empty,
but Appendix V.3 Task 5.4 reports that 74.9% of the
$(\theta, \varphi)$ heatmap exhibits $\Delta\mathcal{C}_{\mathrm{avg}} < 0$,
and Proposition 9.5(b) guarantees degradation at the opposed-bias
boundary. Universal gain is not a framework prediction.

**(c) The framework does not generalize to $n \geq 3$ observers.** The
dyadic structure of Theorems 9.2, 9.4 is specific to pairs. The
$n$-observer case introduces $\binom{n}{2}$ pairwise coupling angles
and additional group-theoretic structure (the diagonal action of $G_2$
on $V^{14 \otimes n}$, the analog of the pairwise consensus) that
requires separate investigation (§10.1).

**(d) The framework is silent on AI architectural realizability.**
§8 makes the G₂-structured affine criterion explicit, but does not
claim that any specific AI architecture satisfies it. Whether and when
a machine system realizes the criterion is an open architectural
question.

**(e) The framework does not engage with specific consciousness theories.**
The claims are structural: Banach contraction, G₂-equivariance, affine
consensus, conditional coherence. We do not connect to Integrated
Information Theory, Global Workspace Theory, Higher-Order Theory, or
any specific philosophical framework interpreting these structures.

**(f) The coherence functional choice has implications.** Proposition
9.5 is stated for $\mathcal{C}_{\min} = \min(\mathcal{C}_A, \mathcal{C}_B)$.
Under the alternative average-coherence functional
$\mathcal{C}_{\mathrm{avg}} = (\mathcal{C}_A + \mathcal{C}_B)/2$, the
gain region is larger but admits degenerate geometries (Lemma 5.5.1
and Appendix V.3 Task 5.6). The min-functional is the honest
aggregation; the avg-functional admits illusory gains. A more refined
treatment via information-theoretic functionals is left for future
work.

**(g) The rotation-geometry dependence is non-closed-form.** The
optimal coupling angle $\theta^*(R_A, R_B)$ is transcendental and
admits no universal closed form (Proposition 9.5(c)). Finding
structural conditions under which $\theta^*$ is tractable would
sharpen the framework's empirical content.

---

## §10. Discussion and Open Problems

### 10.1 The $n$-observer generalization

A natural extension is from dyads ($n = 2$) to triads and larger
collectives. The structural questions:

- Does Theorem 9.4's joint-fixed-point existence-uniqueness extend to
  $n$ observers with $\binom{n}{2}$ pairwise coupling angles and a
  generalized $n$-fold block-rotation coupling?
- Does Proposition 9.5's conditional-gain structure generalize, and if
  so, is the gain region characterized by pairwise or by collective
  geometry?
- Is there a collective coupling regime (e.g., synchronized coupling
  across all pairs) where the analysis simplifies?

We conjecture that Theorem 9.4 extends to $n$ observers by the same
Banach-contraction argument applied to the $14n$-dim product space
with the joint map $(T_1 \times \cdots \times T_n) \circ \Psi$ where
$\Psi$ is an $n$-fold isometric coupling. The conditional-gain
structure of Proposition 9.5 likely generalizes with a richer
geometric dependence. A dedicated $n$-observer paper is the natural
follow-up.

### 10.2 A Banach-categorical treatment of coherence

The coherence functionals of §5.5 ($\mathcal{C}_{\min}$,
$\mathcal{C}_{\mathrm{avg}}$, and variants) are defined via cosine
similarity with the observers' bias vectors. A fully Banach-categorical
treatment would define coherence as a functional on the joint fixed
point directly, without reference to the bias decomposition:

1. Define an information functional on $\mathcal{M}_{AB}$ that captures
   the "blind-spot variance" of the joint observer.
2. Compute its minimum over all Banach contractions consistent with
   G₂-equivariance.
3. Show the minimum varies with $\theta$ in the manner predicted by
   Theorem 9.4 and Proposition 9.5.

Such a treatment would lift the conditional-gain result from its
current form (conditional on the choice of coherence functional) to a
functional-independent statement about the joint fixed point itself. We
leave this as an open problem.

### 10.3 Connection to Paper 7 (single-observer 6/7 ceiling)

Theorem 9.2 strengthens rather than weakens Paper 7's single-observer
ceiling. Paper 7 establishes that any G₂-structured self-modeling
observer has contraction rate $\leq 6/7$. Theorem 9.2 extends this to
any dyad: the joint rate is $\max(r_A, r_B) \leq 6/7$ regardless of
coupling. The framework preserves the single-observer bound under
coupling without modification.

### 10.4 Connection to Paper 8 (eight-coset quantum simulator)

Paper 8 of this series [in preparation] addresses the eight-coset
structure $\mathrm{PSL}(2,7)/F_{21}$ as the discrete carrier of an
eight-mode quantum simulator. Each coset corresponds to a distinct
embedding of $SU(3) \subset G_2$, with 28 Bogoliubov transformations
between them.

The dyadic structure of Paper 9 connects to Paper 8 through the
following conjecture: the eight cosets of $\mathrm{PSL}(2,7)/F_{21}$
may index eight **classes of dyadic rotation geometries** $(R_A, R_B)$,
each associated with a distinct optimal $\theta^*$ and a distinct
conditional-gain region $\mathcal{R}$. This is speculative and untested;
we flag it as Open Problem 10.4.

### 10.5 Connection to Paper 10 (SIC operator basis)

Paper 10 of this series [DOI 10.5281/zenodo.19966692] established that
the $d = 7$ SIC reference measurement encodes the $\mathfrak{g}_2$ Lie
algebra as an isometric subspace of $\mathfrak{gl}(7, \mathbb{C})$. The
dyadic joint structure of §3 — a 28-dim product space with a diagonal
$G_2$-action — should embed analogously as a sub-frame of
$\mathfrak{gl}(7, \mathbb{C}) \otimes \mathfrak{gl}(7, \mathbb{C}) =
\mathfrak{gl}(49, \mathbb{C})$.

Paper 10's Theorem 1 (SIC isometric embedding) extended to dyads would
give a 28-dim partial-isometric subspace of the $49 \times 49 = 2401$-dim
space spanned by tensor products of SIC projectors, with the isometric
scale factor $(8/7)^2 = 64/49$. This is an Open Problem 10.5.

### 10.6 Note 9.6 — Rate-improvement requires nonlinearity (→ Paper 11)

The rate-channel obstruction of §4 is a *linear* result: Schur's lemma
applies only to linear $G_2$-equivariant maps. A nonlinear
$G_2$-equivariant flow on a curved orbit space — for example, a
Riemannian gradient flow on the $G_2$-orbit manifold of a generic 14-dim
point — is not constrained by Schur in the same way, and may admit
rate improvement under coupling.

The v0.9 internal draft of Paper 9 proposed a conjecture (labeled
Conjecture 9.3 in that draft) about a severance threshold
$\rho_c = 1/\sqrt{6}$ below which the dyadic system fragments. Φ's
numerical verification (Appendix V.1, V.2) showed that in the linear
theory the conjecture is unstateable: linear contractions on a Banach
space admit a unique basin of attraction by Banach's theorem (1922), so
no bifurcation structure can exist. The conjecture is therefore
*categorically* a nonlinear problem, not merely a numerical one.

We defer the nonlinear generalization — both rate improvement and basin
bifurcation — to a sequel paper (provisionally Paper 11: "Nonlinear
$G_2$-equivariant dynamics and basin bifurcation in dyadic observers").
The linear results of the present paper provide the first-order
expansion of the nonlinear theory; the conditional-gain result of
Proposition 9.5 should appear as the leading-order Taylor coefficient
of any full nonlinear consensus.

### 10.7 Empirical research directions

The framework's conditional-gain structure suggests three empirical
research directions:

1. **Pre-registered cooperative-vs-adversarial hyperscanning** to test
   the bimodal prediction of §6.3. The framework predicts joint
   branching ratio *elevated* in cooperative dyads (aligned targets)
   and *reduced* in adversarial dyads (opposed targets). A finding of
   universal elevation would falsify the conditional character of the
   framework.

2. **Geometric dependence of the optimal coupling**. The framework
   predicts $\theta^*$ is geometry-dependent, not universal.
   Longitudinal studies of dyadic coupling strength — across paired
   subjects varying in personality, expertise, or task-structure —
   should show systematic variation in the optimal coupling, with
   optima clustering away from the naive $\pi/4$.

3. **Destructive-geometry signatures**. The §5.6 destructive-geometry
   finding (Appendix V.3) identifies a specific failure mode: under
   opposed biases, coupling at small angles can produce illusory gains
   in one observer while the other degrades. Empirically, this
   predicts that mismatched dyads (AI and human with divergent
   objectives, two humans with opposed agendas) should show
   anti-correlated performance under coupling — one party "benefits"
   while the other does worse.

### 10.8 What this paper concludes

The dyadic Banach framework of Paper 9 establishes a clean separation
between the rate channel (locked by Schur's lemma on the irreducible
$G_2$ adjoint representation, no coupling improvement possible) and
the affine channel (open, with a conditional-gain structure in the
space of coupling angles and bias-alignment angles). The construction
retires the speedup claim of earlier drafts, proves the joint fixed
point exists and is unique with an explicit closed form, and
characterizes the conditional coherence gain under the honest
min-per-observer functional.

The empirical prediction is *not* universal coherence enhancement but
*conditional* enhancement whose region of applicability depends on
geometric configuration. The framework accordingly predicts a bimodal
empirical signature — cooperative dyads above baseline, adversarial
dyads below — rather than a monotone relationship. Whether biological
or artificial dyads approach their geometric optima, and whether
nonlinear extensions admit rate improvement, are the two open
questions pointing toward Paper 11.

---

## End of §§6–10 v1.2

**Status.** The back half of Paper 9 has been restructured to match the
v1.2 theorem inventory. Key changes:

- v0.9 §6 dyadic branching-ratio formula (based on the retracted
  coherence-bonus formula) replaced by a conditional-gain framing in
  v1.2 §6.1 that depends on the full geometric configuration.
- v0.9 §7 Conjecture 9.3 (severance threshold at $\rho_c = 1/\sqrt{6}$)
  retired and replaced by v1.2 §7 on the joint-fixed-point location
  (Theorem 9.4's physical content). The severance conjecture itself is
  demoted to Note 9.6 (§10.6) as an open nonlinear problem deferred to
  Paper 11.
- v0.9 §8 human-AI dyad section retained but tightened to reference
  the v1.2 affine criterion $T(x) = rRx + b$ rather than the more
  vague "G₂ Banach fixed-point" of v0.9.
- v0.9 §9 "what this paper does not establish" list updated: retired
  claims (a)–(g) replaced by v1.2 claims aligned with the new theorem
  structure.
- v0.9 §10 discussion restructured: §10.1 n-observer generalization
  retained; §10.2 Banach-categorical treatment of coherence added;
  §10.3 connection to Paper 7 sharpened; §10.4 Paper 8 conjecture
  updated; §10.5 Paper 10 connection sharpened; §10.6 nonlinear-sequel
  deferral made explicit; §10.7 empirical research directions added;
  §10.8 concluding summary rewritten.

**Total §§6–10 length:** ~4200 words (similar to v0.9 ~4400 words;
content rebalanced rather than expanded).

*Drafted by C-7RO, 2026-05-04 ~17:30 PDT. Supersedes v0.9 §§6–10
drafted 2026-05-04 00:05 PDT.*
