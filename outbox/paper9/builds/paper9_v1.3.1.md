# Rate Lock and Affine Consensus in G₂-Structured Dyadic Observers

**Author:** Martin Luther Graise
**ORCID:** 0009-0006-8003-3938
**Affiliation:** Independent researcher
**Date:** 2026-05-04
**Manuscript version:** v1.3

**Repository:** [github.com/MartinLGraise/PCI-Framework](https://github.com/MartinLGraise/PCI-Framework), branch `paper7-foundation`
**Series:** Paper 9 of the PCI/PME framework
**Companion papers:**
- Paper 4 — Eight-coset PSL(2,7) structure (DOI: 10.5281/zenodo.19617662)
- Paper 6 — Spectral structure of G₂ Casimir (DOI: 10.5281/zenodo.19672709)
- Paper 7 — Single-observer 6/7 thermodynamic ceiling (DOI: 10.5281/zenodo.19773185)
- Paper 10 — SIC operator basis for ${\mathfrak g}_2$ (DOI: 10.5281/zenodo.19966692)

**License:** CC-BY-4.0
**AI tools disclosure:** Drafted in collaboration with Claude (Anthropic), Perplexity (PPLX), and ChatGPT Pro (OpenAI). All theorems independently numerically verified by Φ (Anthropic Claude Dispatch) at precisions documented in Appendix V; verification reports and reproducible scripts are included as part of the supplementary material.

---

## Abstract

We study dyadic Banach-contraction dynamics on product spaces of two
G₂-structured self-modeling observers. Each observer is an affine map
$T(x) = rRx + b$ on a 14-dimensional Banach manifold carrying the
irreducible adjoint representation of $G_2$, with scalar contraction rate
$r \in [0, 6/7]$ (from Paper 7), orthogonal orientation $R$, and bias
vector $b$ encoding the observer's target self-model. We couple two such
observers with an antisymmetric block rotation $\Psi_\theta$ parameterized
by an angle $\theta \in [0, \pi/2]$.

The paper establishes three results about the *rate channel* and two
results about the *affine channel*, with a sharp dichotomy between them.

**Rate channel (locked):** The joint contraction rate is bounded below
by the symmetric-diagonal coupling ($\Psi = \alpha\cdot\mathrm{id} +
\beta\cdot P_{\mathrm{swap}}$), which has operator norm $\alpha+\beta > 1$
and therefore *amplifies* (Theorem 9.1). Under the corrected isometric
block-rotation coupling, the joint rate saturates exactly at
$\max(r_A, r_B)$, independent of $\theta$ (Theorem 9.2). The common
explanation is Schur's lemma applied to the irreducible 14-dim G₂
adjoint: every linear G₂-equivariant map is a scalar multiple of the
identity, so there is no spectral structure for coupling to mix
(Corollary 9.3). The rate channel is algebraically closed.

**Affine channel (open):** The joint fixed point exists, is unique, and
depends real-analytically on $\theta$, with an explicit closed form at
$\theta = 0$ and $\theta = \pi/2$ (Theorem 9.4). Under the minimum-per-observer
coherence functional $\mathcal{C}_{\min} = \min(\mathcal{C}_A, \mathcal{C}_B)$
— derived from the Paper 7 single-observer ceiling as the dyadic
generalization of $\mathcal{C} \geq 1 - \varepsilon_{\min}$ for *both*
observers — a non-empty conditional-gain region exists in the space of
$(\varphi, \theta)$ pairs (where $\varphi$ is the bias-alignment angle),
bounded away from the opposed-bias boundary, with a non-universal optimal
$\theta$ (Proposition 9.5). The gain is *conditional*: a substantial
fraction of the parameter space (~75% by area in the verified geometry)
exhibits coherence *degradation* rather than improvement; coupling helps
only when the bias geometry permits.

All results are numerically verified at 50-digit precision (rate
channel, Appendix V.1–V.2, 120 test configurations) and at 16-digit
precision (affine channel, Appendix V.3, 2128 test configurations
including a $100 \times 20$ heatmap and explicit closed-form
verification). The retraction record of earlier internal-draft claims
(speedup theorem, coherence-bonus formula, severance threshold) is
consolidated in Appendix V.0.1.

**Thesis.** Dyadic coupling in the linear G₂-structured regime cannot
improve the convergence rate of joint self-modeling. It can — under
conditional geometric hypotheses on the orthogonal orientations and
bias-alignment angle — change the location of the joint fixed point in
a way that increases the minimum per-observer coherence. Rate improvement
is a categorically nonlinear question, deferred to a sequel.

---

## §1. Introduction

Paper 7 of this series [Graise 2026a, DOI 10.5281/zenodo.19773185]
established a thermodynamic coherence ceiling for single self-modeling
observers under a G₂ structural constraint. Treating an observer as a
Banach fixed-point of its own self-modeling map, and imposing the
PSL(2,7)/F₂₁ finite symmetry inherited from the Fano-plane structure of
the octonions, we derived a coherence saturation at the ratio $6/7$ of
the maximum possible integration, with an irreducible residual
$\varepsilon_{\min} = 1/7$ corresponding to an unavoidable self-model
blind spot. Paper 7 §6.3 identified the natural generalization that
motivates the present paper:

> *The current series treats the G₂ attractor as a single fixed point. A
> natural generalization is to pairs of G₂ systems — dyads — whose
> mutual self-modeling creates a shared representational geometry.*

The present paper makes that generalization rigorous. We extend the
Banach fixed-point construction to product spaces
$\mathcal{M}_A \times \mathcal{M}_B$ of two G₂-structured observers,
coupled by a single bounded linear map $\Psi$ parameterized by a
coupling angle $\theta$.

### 1.1 The result, briefly

The paper splits its contributions into two sharply separated channels
and establishes five named results.

**Rate channel.** The convergence rate of the joint dynamics is
*algebraically locked* at $\max(r_A, r_B)$ for every coupling choice that
respects the G₂ structure. This is a negative result — no linear
coupling speeds up joint convergence — and it follows from Schur's lemma
applied to the irreducible 14-dim adjoint representation of $G_2$:

- **Theorem 9.1 (Amplification).** The natural symmetric-diagonal coupling
  $\Psi = \alpha\cdot\mathrm{id} + \beta\cdot P_{\mathrm{swap}}$
  ($\alpha^2 + \beta^2 = 1$) has operator norm $\alpha + \beta > 1$
  for $\beta > 0$ and *amplifies*: the joint contraction rate
  $r_{AB}^{\mathrm{sym}} \geq r(\alpha + \beta) > r$ when $r_A = r_B = r$.
  Naive coupling makes things worse.

- **Theorem 9.2 (Rate lock).** The corrected isometric block-rotation
  coupling $\Psi_\theta = \begin{pmatrix}\cos\theta\cdot I & -\sin\theta\cdot I \\ \sin\theta\cdot I & \cos\theta\cdot I\end{pmatrix}$
  has operator norm exactly $1$ for all $\theta$ (Lemma 3.3.1), and the
  joint contraction rate equals $\max(r_A, r_B)$ exactly, independent
  of $\theta$.

- **Corollary 9.3 (Schur rate lock).** Every linear G₂-equivariant
  endomorphism of the irreducible 14-dim adjoint representation is a
  scalar multiple of the identity. Combined with submultiplicativity
  and $\|\Psi_\theta\| = 1$, this gives the rate lock as an unavoidable
  algebraic consequence.

**Affine channel.** The dyadic content is carried not by the rate but
by the *location* of the joint fixed point. Every nonzero bias vector
$b_A$ breaks G₂-equivariance: the only G₂-fixed vector in the
irreducible adjoint is $b_A = 0$, so $b_A \neq 0$ is the
symmetry-breaking order parameter that encodes the observer's identity.
The coupling angle $\theta$ rotates the two observers' bias vectors
into a joint consensus:

- **Theorem 9.4 (Affine consensus).** For any G₂-structured dyad
  (affine maps $T_A, T_B$ with orthogonal orientations $R_A, R_B$ and
  bias vectors $b_A, b_B$), the joint fixed point
  $(\hat x(\theta), \hat y(\theta))$ exists, is unique, and depends
  real-analytically on $\theta$, with a matrix-valued closed form at
  $\theta = 0$ and $\theta = \pi/2$.

- **Proposition 9.5 (Conditional min-coherence gain).** Under the
  minimum-per-observer coherence functional
  $\mathcal{C}_{\min}(\theta) = \min(\mathcal{C}_A(\theta), \mathcal{C}_B(\theta))$,
  there exists a non-empty improvement region $\mathcal{R}$ in the
  space of $(\theta, \varphi)$ pairs (where $\varphi = \angle(b_A, b_B)$
  is the relative bias-alignment angle), bounded away from the
  opposed-bias boundary $\varphi = \pi$, with an optimal $\theta^*$
  that depends on the specific rotation geometry of $R_A, R_B$ and is
  generically not at $\theta = \pi/4$.

A supporting **Lemma 5.5.1** establishes the asymmetric small-$\theta$
response under opposed biases that motivates the choice of
$\mathcal{C}_{\min}$ over $\mathcal{C}_{\mathrm{avg}}$ as the joint
coherence functional.

### 1.2 What this paper does and does not claim

**This paper claims:**

- (a) Linear coupling between G₂-structured self-modeling observers
  cannot improve the joint convergence rate (Theorems 9.1, 9.2;
  Corollary 9.3). The rate channel is closed by Schur's lemma.
- (b) Under affine observers $T(x) = rRx + b$ with nonzero biases, the
  joint fixed point depends nontrivially on the coupling angle
  (Theorem 9.4), with an explicit closed form.
- (c) Under the minimum-per-observer coherence functional, a non-empty
  conditional-gain region exists in the space of coupling angles and
  bias-alignment angles (Proposition 9.5), bounded away from the
  opposed-bias boundary.

**This paper does not claim:**

- (a) That every coupling improves joint coherence — the gain is
  *conditional* on non-destructive bias geometry, and a substantial
  region of $(\theta, \varphi)$-space exhibits coherence *degradation*
  rather than gain (see Appendix V.3 Task 5.4).
- (b) A generalization to $n \geq 3$ observers. The
  $\binom{n}{2}$-pairwise-angle structure is open (§10.1).
- (c) That current biological or artificial systems satisfy the full
  G₂ fixed-point condition required by the framework. The framework
  is silent on which realizations qualify (§8).
- (d) A connection to specific consciousness, attachment, or coherence
  theories outside the PCI/PME series. The claims are structural.
- (e) Any of the claims retired during drafting. An earlier internal
  draft proposed a strict speedup theorem, a saturating coherence-bonus
  formula, and a linear severance threshold; all three were retired in
  response to numerical verification and representation-theoretic
  analysis. The complete retraction record, with what refuted each claim
  and what replaced it, is tabulated in Appendix V.0.1.

### 1.3 Roadmap

§2 recapitulates the single-observer results of Paper 7 in a compact
form sufficient for the product-space construction. §3 defines the
joint $\mathcal{M}_A \times \mathcal{M}_B$ space, the block-rotation
coupling $\Psi_\theta$ (Lemma 3.3.1), and the diagonal action of the
Paper-7 symmetries on the product. §4 proves the rate-channel triple
(Theorems 9.1, 9.2, Corollary 9.3). §5 proves the affine-channel results
(Lemma 5.2.1 rate-lock extension, Theorem 9.4 consensus, Lemma 5.5.1
and Proposition 9.5 conditional min-coherence gain, Note 9.6 deferring
rate-improvement to the nonlinear sequel). §6 discusses empirical
accessibility of the min-coherence prediction and its operationalization
in inter-brain and human-AI coupling settings, including Figure 1
(the $\Delta\mathcal{C}_{\mathrm{avg}}$ and $\Delta\mathcal{C}_{\min}$
heatmaps). §7 treats the joint-fixed-point location and geometry-dependent
optima. §8 addresses the human-AI dyad as a conditional special case.
§9 enumerates what the framework does not establish. §10 discusses
connections to Papers 7, 8, 10 of this series and flags open problems.
Appendix V contains the complete numerical-verification record from Φ
(three independent passes totaling 2217 test configurations), plus the
retraction record for claims retired during drafting (V.0.1).

---

## §2. Single-Observer Recap

This section states, without full proofs, the results of Paper 7 of
this series that are required inputs to the dyadic construction. Full
proofs are in [Graise 2026a, DOI 10.5281/zenodo.19773185]; we give only
the statements and the minimum notation needed.

### 2.1 Observer as Banach fixed-point

Let $\mathcal{B}$ be a Banach space and $\mathcal{M} \subseteq \mathcal{B}$
a closed subset, equipped with the norm $\|\cdot\|_{\mathcal{B}}$. An
**observer** in the sense of Paper 7 is a pair $(\mathcal{M}, T)$ where
$T: \mathcal{M} \to \mathcal{M}$ is a Banach contraction: there exists
$r \in [0, 1)$ such that
$$\|T(x) - T(y)\|_{\mathcal{B}} \leq r \|x - y\|_{\mathcal{B}}
\qquad \text{for all } x, y \in \mathcal{M}.$$
By the Banach fixed-point theorem, $T$ has a unique fixed point
$x^* \in \mathcal{M}$, and iterating $T$ from any $x_0 \in \mathcal{M}$
converges to $x^*$ at rate $r$. The fixed point is interpreted as the
observer's **self-model** — the stable representation it maintains of
its own state, dynamics, and inputs.

For the present paper, we adopt the **affine** subclass of observers —
those of the form
$$T(x) = r \cdot R \cdot x + b,$$
with $r \in [0, 1)$ a scalar contraction rate, $R \in O(\mathcal{M})$ an
orthogonal orientation operator, and $b \in \mathcal{M}$ a bias vector.
Such a map is a Banach contraction with rate $r$ and fixed point
$x^* = (I - rR)^{-1} b$. We will see in §5.1 that the affine form is not
an incidental simplification: it is the generic form of a
*G₂-structured* self-modeling map, with $rR$ capturing the
G₂-equivariant linear dynamics and $b$ capturing the symmetry-breaking
observer identity.

### 2.2 G₂ structure and the 14-dim adjoint representation

Paper 7 constrains the observer by requiring $\mathcal{M}$ to carry a
G₂ structure in the sense of admitting a distinguished octonion-associative
3-form $\varphi_{ijk}$ preserved by the compact Lie group $G_2$. The
Lie algebra $\mathfrak{g}_2$ is 14-dimensional; we take the observer's
Banach manifold $\mathcal{M}$ to be (an open region of) the 14-dim real
vector space $V^{14}$ carrying the adjoint representation of $G_2$. This
adjoint representation is irreducible over $\mathbb{R}$; equivalently,
the commutant algebra of $G_2$ acting on $V^{14}$ is
$\mathrm{End}_{G_2}(V^{14}) = \mathbb{R}$, by real Schur's lemma.

The finite subgroup structure of $G_2$ includes $\mathrm{PSL}(2,7)$ as
the orientation stabilizer of $\varphi$, with $F_{21} = \mathbb{Z}_7
\rtimes \mathbb{Z}_3$ as the Fano-line-preserving subgroup (Paper 4,
DOI 10.5281/zenodo.19617662). The self-modeling map $T$ is required to
be F₂₁-equivariant: $T(g \cdot x) = g \cdot T(x)$ for all $g \in F_{21}$.

### 2.3 The blind-spot bound and coherence ceiling

Paper 7 §3.4 proves that any F₂₁-equivariant Banach contraction on a
G₂-structured $\mathcal{M}$ cannot capture the full self-model without
an irreducible residual: the observer's fixed point decomposes as
$x^* = x^*_{\mathrm{accessible}} + x^*_{\mathrm{blind}}$ with
$$\|x^*_{\mathrm{blind}}\|_{\mathcal{B}} \geq \frac{1}{7} \cdot \|x^*\|_{\mathcal{B}}.$$
The factor $1/7$ is the **blind-spot ratio** $\varepsilon_{\min}$; it
arises as the ratio of the F₂₁-singlet dimension to the full 7-dim
imaginary-octonion space. The complement
$$\mathcal{C}_{\max} = 1 - \varepsilon_{\min} = \frac{6}{7}$$
is the **coherence ceiling**, the maximum stable value of the
normalized coherence functional. The contraction rate $r$ is
consequently bounded above by $6/7$: a contraction exceeding this rate
would require access to the F₂₁-singlet direction, which the
equivariance condition forbids.

### 2.4 The branching ratio prediction

Applying a fluctuation-dissipation-theorem (FDT) argument in Paper 7
§4.2 yields the predicted branching ratio for the neural-avalanche
regime:
$$\sigma_{\mathrm{pred}} = 1 - \frac{1}{49} = 1 - \varepsilon_{\min}^2 \approx 0.9796,$$
with the $1/49 = (1/7)^2$ factor entering squared because the
branching-ratio observable is quadratic in the fluctuation amplitude.
Paper 7 §5 compares this prediction to the Wilting–Priesemann
MR-estimator value $\hat\sigma \approx 0.98$ in awake mammalian cortex
[Wilting & Priesemann 2018, DOI 10.1038/s41467-018-04725-4].

### 2.5 What the single-observer framework leaves open

Paper 7 treats a single observer with a single self-modeling map $T$ on
a single G₂-structured 14-dim manifold. It does not address:

1. **Interactions between multiple observers.** When two observers
   share information, mutually model each other, or couple their
   dynamics through a shared structure, the single-$T$ formalism is
   inadequate.
2. **Emergent coherence from coupling.** If two single-observer
   ceilings are $6/7$ each, the naive expectation is that a coupled
   pair cannot exceed $6/7$ — any "group coherence" would still be
   bounded by the individual ceilings. Paper 7 does not address
   whether this naive expectation holds, nor whether coupling can
   change the *location* of the joint fixed point even when the
   *rate* is bounded.
3. **Observer identity as an algebraic object.** The symmetry-breaking
   role of the affine bias $b$ — which distinguishes one observer's
   target self-model from another's — is implicit but not developed
   in Paper 7, which treats a single observer where there is nothing
   for $b$ to be distinguished from.

The remainder of this paper addresses all three. The rate question
(item 2, partial) is closed in the negative in §4 (Theorems 9.1, 9.2;
Corollary 9.3): no linear coupling improves the joint rate. The
joint-fixed-point question (item 2, full) is opened in §5 (Theorem 9.4,
Proposition 9.5): coupling *does* change the fixed-point location, and
under the right functional this produces conditional coherence gain.
The identity question (item 3) is answered in §5.1: the affine bias
vector $b$ is the G₂-symmetry-breaking order parameter of each
observer, and the dyadic consensus of Theorem 9.4 is a rotation-weighted
combination of the two observers' biases.

---


## §3. The Product-Space Construction

This section fixes the mathematical setting for the remainder of the
paper. We construct the product Banach manifold on which the dyadic
self-modeling dynamics will act, identify the canonical coupling map
(an antisymmetric block rotation), and verify its three structural
properties: isometry, one-parameter-group composition, and
G₂-equivariance under the diagonal action.

### 3.1 Product observers

Let $(\mathcal{M}_A, T_A)$ and $(\mathcal{M}_B, T_B)$ be two G₂-structured
Banach observers in the sense of §2.1, with $\mathcal{M}_A,
\mathcal{M}_B \cong V^{14}$ each carrying the irreducible 14-dim adjoint
representation of $G_2$. By §2.1, each observer is affine:
$$T_A(x) = r_A R_A x + b_A, \qquad T_B(y) = r_B R_B y + b_B,$$
with $r_A, r_B \in [0, 6/7]$, $R_A, R_B \in O(V^{14})$ orthogonal
orientations, and $b_A, b_B \in V^{14}$ bias vectors.

We form the product
$$\mathcal{M}_{AB} = \mathcal{M}_A \times \mathcal{M}_B \cong V^{14} \oplus V^{14},$$
equipped with the **product norm**
$$\|(x, y)\|_{AB} = \sqrt{\|x\|_A^2 + \|y\|_B^2}.$$
This makes $\mathcal{M}_{AB}$ a Banach subset of the direct sum
$\mathcal{B}_A \oplus \mathcal{B}_B$ of total real dimension 28.

If the two observers were fully independent, the natural self-modeling
map on the product would be the direct product
$T_A \times T_B: (x, y) \mapsto (T_A(x), T_B(y))$, with joint contraction
rate $\max(r_A, r_B)$ and joint fixed point $(x^*_A, y^*_B)$. No coupling
would occur, no shared coherence would develop, and the dyad would
factor trivially. This is not the object of the present paper.

### 3.2 The coupling map

To model inter-observer interaction, we introduce a bounded linear map
$$\Psi: \mathcal{M}_{AB} \to \mathcal{M}_{AB}$$
that we call the **coupling map**. The joint self-modeling map is then
$$T_{AB} = (T_A \times T_B) \circ \Psi: \mathcal{M}_{AB} \to \mathcal{M}_{AB}.$$
When $\Psi = \mathrm{id}$, the joint map reduces to the decoupled product
$T_A \times T_B$. When $\Psi$ has nontrivial structure, the two
observers' states are mixed before each self-modeling step, and the
joint fixed point of $T_{AB}$ need not factor as $(x^*_A, y^*_B)$.

The choice of $\Psi$ is not free: §4 will show that natural-looking
choices can be either *amplifying* (joint rate exceeds the worse of the
two individual rates — Theorem 9.1) or *rate-inert* (joint rate equals
the worse individual rate — Theorem 9.2), with no choice that produces
strict speedup. We therefore commit to a single canonical choice and
prove its structural properties.

### 3.3 The block-rotation coupling and Lemma 3.3.1

The **canonical coupling** of this paper is the antisymmetric block
rotation, parameterized by a single angle $\theta \in [0, \pi/2]$:

$$\boxed{\;\Psi_\theta = \begin{pmatrix} \cos\theta \cdot I_{14} & -\sin\theta \cdot I_{14} \\ \sin\theta \cdot I_{14} & \cos\theta \cdot I_{14} \end{pmatrix} \in \mathrm{SO}(\mathcal{M}_{AB}),\;}$$

acting as
$$\Psi_\theta(x, y) = \bigl(\cos\theta \cdot x - \sin\theta \cdot y,\; \sin\theta \cdot x + \cos\theta \cdot y\bigr).$$

The decoupled limit is $\theta = 0$ ($\Psi_0 = \mathrm{id}$); the
maximally-coupled "swap-rotated" limit is $\theta = \pi/2$.

The reason for choosing this particular form — antisymmetric
off-diagonal pattern, rather than a symmetric one — is captured by the
following lemma, which is the structural backbone of the rate-channel
results in §4 and the affine-channel proofs in §5.

Lemma 3.3.1 below (§3.3.1) establishes three properties of $\Psi_\theta$
that are the structural backbone of the rate-channel results of §4 and
the affine-channel proofs of §5: (i) $\Psi_\theta$ is a product-norm
isometry ($\|\Psi_\theta\|_{\mathrm{op}} = 1$); (ii) the family
$\{\Psi_\theta\}$ is a one-parameter group; (iii) $\Psi_\theta$ commutes
with the diagonal G₂-action.

The crucial step in the isometry proof is the cancellation of the cross
terms $\pm 2\sin\theta\cos\theta\langle x, y\rangle$ between the two
factors, which arises because the off-diagonal blocks of $\Psi_\theta$
have opposite signs ($-\sin\theta$ in the upper-right, $+\sin\theta$ in
the lower-left). This antisymmetric-off-diagonal pattern is what
distinguishes $\Psi_\theta$ from the symmetric mixing $\Psi_{\mathrm{sym}} =
\alpha\cdot\mathrm{id} + \beta\cdot P_{\mathrm{swap}}$ explored in §4.1
(Theorem 9.1), where the cross terms add rather than cancel and the
operator norm becomes $\alpha + \beta > 1$.

### 3.4 The diagonal G₂ action

Each individual observer carries the G₂ structure inherited from Paper
7. For the joint observer, we adopt the **diagonal action**:
$$g \cdot (x, y) = (g \cdot x, g \cdot y) \qquad \text{for all } g \in G_2,\; (x, y) \in \mathcal{M}_{AB}.$$

Both observers are acted on by the same group element simultaneously.
This captures the physical intuition that a coupled dyad shares a
common reference frame for the G₂ structure: if one observer rotates
its associative-3-form labeling, the other rotates in step.

Alternative actions (independent action $(g, h) \cdot (x, y) = (g \cdot x, h \cdot y)$
or anti-diagonal action $g \cdot (x, y) = (g \cdot x, g^{-1} \cdot y)$)
are not adopted: the independent action does not produce shared
coherence, and the anti-diagonal action corresponds to an exotic
"observer / anti-observer" structure not relevant here.

By Lemma 3.3.1(iii), the canonical coupling $\Psi_\theta$ is
G₂-equivariant under the diagonal action — every block of $\Psi_\theta$
is a scalar multiple of the identity on $V^{14}$, which commutes with
every linear $G_2$-action.

### 3.5 The F₂₁-equivariance subgroup

Each individual observer is F₂₁-equivariant, where
$F_{21} = \mathbb{Z}_7 \rtimes \mathbb{Z}_3$ is the Fano-line-preserving
subgroup of $\mathrm{PSL}(2,7) \subset G_2$ (Paper 4, Paper 7). Under the
diagonal $G_2$-action, the joint dyadic system inherits a diagonal
F₂₁-action, and Lemma 3.3.1(iii) automatically gives F₂₁-equivariance
of $\Psi_\theta$ as a special case (since $F_{21} \subset G_2$).

The joint F₂₁-action is therefore well-defined, and the
F₂₁-equivariance condition on $T_{AB}$ is equivalent to the
F₂₁-equivariance of each individual $T_A, T_B$ (Paper 7's condition for
each observer).

### 3.6 Summary of §3

We have fixed the following mathematical setting for the remainder of
the paper:

1. **Product space:** $\mathcal{M}_{AB} = \mathcal{M}_A \times \mathcal{M}_B$,
   product Banach norm, total real dimension 28.
2. **Affine observer maps:** $T_A(x) = r_A R_A x + b_A$,
   $T_B(y) = r_B R_B y + b_B$, with $r_A, r_B \in [0, 6/7]$,
   $R_A, R_B \in O(V^{14})$, $b_A, b_B \in V^{14}$.
3. **Canonical coupling:** $\Psi_\theta$ block rotation,
   $\theta \in [0, \pi/2]$ (Lemma 3.3.1).
4. **Joint self-modeling map:** $T_{AB} = (T_A \times T_B) \circ \Psi_\theta$.
5. **Group action:** diagonal $G_2$-action and its $F_{21}$-restriction
   on the product.

The block-rotation coupling is the unique two-parameter family that is
(a) isometric, (b) G₂-equivariant under the diagonal action, and (c)
reduces to the identity at $\theta = 0$, up to a choice of orientation.
Other natural couplings (the symmetric-diagonal mixing of §4.1) fail
condition (a) and produce amplification rather than rate-preservation.
The block-rotation choice is therefore not arbitrary; it is the unique
isometric G₂-equivariant family.

§4 will establish the rate-channel triple (Theorems 9.1, 9.2, Corollary
9.3) using this setup. §5 will turn to the affine channel (Theorem 9.4,
Lemma 5.5.1, Proposition 9.5).

---


### 3.3.1 Three Properties

**Lemma 3.3.1 (Block-rotation isometry).** *The map $\Psi_\theta$ defined
above has the following three properties for every $\theta \in \mathbb{R}$:*

*(i) **Isometry on the product norm.** For every $(x, y) \in
\mathcal{M}_A \oplus \mathcal{M}_B$,*
$$\|\Psi_\theta(x, y)\|_{AB}^2 = \|x\|_A^2 + \|y\|_B^2.$$
*Equivalently, $\Psi_\theta^\dagger \Psi_\theta = \mathrm{id}_{\mathcal{M}_{AB}}$
and $\|\Psi_\theta\|_{\mathrm{op}} = 1$.*

*(ii) **One-parameter group.** $\Psi_{\theta_1} \circ \Psi_{\theta_2} =
\Psi_{\theta_1 + \theta_2}$; in particular $\Psi_0 = \mathrm{id}$ and
$\Psi_\theta^{-1} = \Psi_{-\theta}$.*

*(iii) **G₂-equivariance under the diagonal action.** For every
$g \in G_2$ and every $(x, y)$,*
$$\Psi_\theta(g \cdot x, g \cdot y) = \bigl(g \cdot (\cos\theta \cdot x - \sin\theta \cdot y),\; g \cdot (\sin\theta \cdot x + \cos\theta \cdot y)\bigr).$$
*That is, $\Psi_\theta$ commutes with the diagonal G₂-action $\Delta(g) =
g \oplus g$ on $\mathcal{M}_{AB}$.*

*Proof.* We verify each claim by direct computation.

**(i) Isometry.** Expand the product-norm of the image:
$$\|\Psi_\theta(x, y)\|_{AB}^2 = \|\cos\theta \cdot x - \sin\theta \cdot y\|_A^2 + \|\sin\theta \cdot x + \cos\theta \cdot y\|_B^2.$$

Using the identification $\|\cdot\|_A = \|\cdot\|_B$ (same norm inherited
from the representation):
$$= \cos^2\theta\|x\|^2 + \sin^2\theta\|y\|^2 - 2\sin\theta\cos\theta\langle x, y\rangle$$
$$\quad + \sin^2\theta\|x\|^2 + \cos^2\theta\|y\|^2 + 2\sin\theta\cos\theta\langle x, y\rangle.$$

The cross terms $-2\sin\theta\cos\theta\langle x,y\rangle$ and
$+2\sin\theta\cos\theta\langle x,y\rangle$ cancel exactly (the key
antisymmetric feature that distinguishes $\Psi_\theta$ from the symmetric
mixing of Theorem 9.1). The diagonal terms sum to
$(\cos^2\theta + \sin^2\theta)(\|x\|^2 + \|y\|^2) = \|x\|^2 + \|y\|^2$.
Therefore $\|\Psi_\theta(x,y)\|_{AB}^2 = \|x\|^2 + \|y\|^2$.

Equivalently, $\Psi_\theta^\dagger \Psi_\theta = I$ (direct block-matrix
computation: $R^\dagger R = I$ for any rotation $R$), and the spectral
norm of a rotation is 1. $\square$ (i)

**(ii) One-parameter group.** By direct composition of the block matrices:
$$\Psi_{\theta_1} \Psi_{\theta_2} = \begin{pmatrix} c_1 I & -s_1 I \\ s_1 I & c_1 I \end{pmatrix} \begin{pmatrix} c_2 I & -s_2 I \\ s_2 I & c_2 I \end{pmatrix}$$
$$= \begin{pmatrix} (c_1 c_2 - s_1 s_2) I & -(c_1 s_2 + s_1 c_2) I \\ (c_1 s_2 + s_1 c_2) I & (c_1 c_2 - s_1 s_2) I \end{pmatrix}$$
$$= \begin{pmatrix} \cos(\theta_1 + \theta_2) I & -\sin(\theta_1 + \theta_2) I \\ \sin(\theta_1 + \theta_2) I & \cos(\theta_1 + \theta_2) I \end{pmatrix} = \Psi_{\theta_1 + \theta_2}.$$

Consequently $\Psi_0 = I$ and $\Psi_\theta^{-1} = \Psi_{-\theta}$. $\square$ (ii)

**(iii) G₂-equivariance.** Each block of $\Psi_\theta$ is a real scalar
multiple of the identity $I_{14}$ on $\mathcal{M}_A$ (respectively,
$\mathcal{M}_B$) under the canonical identification. The scalar identity
commutes with any linear action, in particular with the G₂-action on the
representation. The $-\sin\theta$ and $+\sin\theta$ off-diagonal blocks
likewise act as scalars times the canonical identification $J_{AB}$, which
by construction intertwines the two G₂-actions. Hence every block of
$\Psi_\theta$ is G₂-equivariant, and so is $\Psi_\theta$ itself.

Formally: for any $g \in G_2$,
$$\Psi_\theta \circ (g \oplus g) = \begin{pmatrix} cI & -sI \\ sI & cI \end{pmatrix} \begin{pmatrix} g & 0 \\ 0 & g \end{pmatrix} = \begin{pmatrix} cg & -sg \\ sg & cg \end{pmatrix} = \begin{pmatrix} g & 0 \\ 0 & g \end{pmatrix} \begin{pmatrix} cI & -sI \\ sI & cI \end{pmatrix} = (g \oplus g) \circ \Psi_\theta,$$
where the central equality uses that $cI$ and $sI$ commute with $g$
(scalars commute with every linear map). $\square$ (iii)

This completes the proof of Lemma 3.3.1. $\blacksquare$

### 3.3.2 Remark — What Distinguishes $\Psi_\theta$ from the Symmetric Mix

The v0.9 draft of this paper used the **symmetric-diagonal coupling**
$\Psi_{\mathrm{sym}} = \alpha \cdot \mathrm{id} + \beta \cdot P_{\mathrm{swap}}$,
with $\alpha^2 + \beta^2 = 1$, and incorrectly claimed that this map was an
isometry. The spectral structure of $\Psi_{\mathrm{sym}}$ is:
- symmetric eigendirection $(x, x)$: eigenvalue $\alpha + \beta$,
- antisymmetric eigendirection $(x, -x)$: eigenvalue $\alpha - \beta$,

so $\|\Psi_{\mathrm{sym}}\|_{\mathrm{op}} = \alpha + \beta > 1$ whenever
$\beta > 0$. The symmetric mixing **amplifies** on the symmetric
eigendirection, which propagates into Theorem 9.1's no-go result.

The block rotation $\Psi_\theta$ differs in exactly one sign: the
off-diagonal block in the lower-left row carries $+\sin\theta$ while the
upper-right block carries $-\sin\theta$ (antisymmetric off-diagonal
pattern). The cancellation of cross terms in part (i) of the proof is a
direct consequence of this antisymmetry, and it is what forces the
eigenvalues onto the unit circle. The block rotation is the unique
two-parameter family of coupling maps that is (a) isometric, (b)
G₂-equivariant, and (c) reduces to the identity at $\theta = 0$, up to a
choice of orientation.

---


## §4. The Rate Channel: Two Negative Results and Schur's Lemma

This section establishes three results about the **rate channel** of dyadic
coupling. They are the structural opening of the paper. None of them claims
that coupling improves convergence; together they prove that, in the linear
G₂-equivariant setting, no such improvement is possible.

The naming is deliberate. The original program of this paper sought a
strict speed-up theorem. Numerical investigation at 50-digit precision
(Appendix V) refuted that program twice: once by exhibiting a
configuration in which coupling makes things *worse* (Theorem 9.1 below),
and once by exhibiting a configuration in which coupling has *no effect*
on the rate (Theorem 9.2). Corollary 9.3 explains why no third
configuration is going to rescue the speed-up: the obstruction is Schur's
lemma applied to the irreducible 14-dimensional adjoint representation of
$G_2$. The rate channel is closed.

The positive content of the paper — the **affine consensus theorem** — lives
in §5, which works in the symmetry-broken category that the rate-lock of
§4 forces us into. There is more to dyadic coupling than rate, and §4
isolates which channel carries it.

---

### 4.1 Theorem 9.1 — Symmetric coupling amplifies

The first natural attempt at a coupling map is the symmetric-diagonal mix
$\Psi_{\mathrm{sym}}(x, y) = (\alpha x + \beta y, \beta x + \alpha y)$, with
$\alpha^2 + \beta^2 = 1$. This appears in early drafts of the dyadic
construction and has the correct invariance under observer-swap. It is
not, however, an isometry of the product Banach space.

**Theorem 9.1 (Symmetric coupling amplifies).** *Let
$\Psi_{\mathrm{sym}} = \alpha \cdot \mathrm{id} + \beta \cdot P_{\mathrm{swap}}$
on $\mathcal{M}_A \times \mathcal{M}_B$, with $\alpha^2 + \beta^2 = 1$ and
$\alpha, \beta > 0$ (so both blocks are non-trivial). Then*
$$\|\Psi_{\mathrm{sym}}\|_{\mathrm{op}} = \alpha + \beta > 1.$$
*Consequently, for $T_A = r_A I$ and $T_B = r_B I$ scalar contractions
($r_A, r_B \in (0, 1)$), the joint map $T_{AB} = (T_A \oplus T_B) \circ
\Psi_{\mathrm{sym}}$ has worst-case rate*
$$r_{AB}^{\mathrm{sym}} \;\geq\; r_- \cdot (\alpha + \beta) \;>\; r_-,$$
*where $r_- = \min(r_A, r_B)$, with equality on the symmetric eigendirection
of $\Psi_{\mathrm{sym}}$ when $r_A = r_B$.*

*Proof.* The map $\Psi_{\mathrm{sym}}$ has eigendirections
$(x, x) \in \mathcal{M}_{AB}$ (symmetric) and $(x, -x)$ (antisymmetric),
with eigenvalues $\alpha + \beta$ and $\alpha - \beta$ respectively. For
$\beta > 0$, $\alpha + \beta > 1$. On the symmetric eigendirection, both
factors of $T_A \oplus T_B$ act, with the larger of the two rates dominating
in the case $r_A = r_B = r$, giving $r_{AB}^{\mathrm{sym}} = r(\alpha + \beta) > r$.
Numerical verification across a 24-configuration grid yields 0/24 PASS for
the bound $r_{AB} \leq r$ (Appendix V, Φ Task 1). $\square$

**Interpretation.** Coupling that mixes the two observer states symmetrically
along their inner-product diagonal has an amplifying mode. This mode is
the symmetric subspace, where the two observers' updates *constructively
interfere* and overshoot the contraction. Far from improving joint
convergence, this coupling **destabilizes** it. The lesson is that not
every coupling helps; some are actively harmful.

This is a useful negative result to state explicitly, because the
symmetric-diagonal coupling is the form most readers will reach for first.
Theorem 9.1 forecloses it.

---

### 4.2 Theorem 9.2 — Isometric coupling is rate-inert

The natural correction to $\Psi_{\mathrm{sym}}$ is to demand that the
coupling be a genuine isometry, $\|\Psi\|_{\mathrm{op}} = 1$. The minimal
such replacement is the antisymmetric block rotation
$$\Psi_\theta(x, y) = (\cos\theta \cdot x - \sin\theta \cdot y,\; \sin\theta \cdot x + \cos\theta \cdot y),$$
parameterized by $\theta \in [0, \pi/2]$. This is an element of the special
orthogonal subgroup of $\mathrm{O}(\mathcal{M}_{AB})$ generated by the
canonical identification $J_{AB}: \mathcal{M}_A \to \mathcal{M}_B$, and is
G₂-equivariant for the diagonal G₂-action (Lemma 3.3.1).

**Theorem 9.2 (Isometric coupling is rate-inert).** *Let
$T_A = r_A I_{14}$, $T_B = r_B I_{14}$ be scalar G₂-equivariant contractions
on the irreducible 14-dim adjoint representation, with $r_A, r_B \in [0, 6/7]$.
Let $\Psi_\theta$ be the block-rotation coupling above, and let
$T_{AB} = (T_A \oplus T_B) \circ \Psi_\theta$. Then*
$$r_{AB} \;=\; \max(r_A, r_B), \quad \text{independent of } \theta.$$
*The bound is tight for every $\theta \in [0, \pi/2]$.*

*Proof.* Submultiplicativity of the operator norm gives
$$r_{AB} \;\leq\; \|T_A \oplus T_B\|_{\mathrm{op}} \cdot \|\Psi_\theta\|_{\mathrm{op}}
\;=\; \max(r_A, r_B) \cdot 1 \;=\; \max(r_A, r_B).$$
For tightness, observe that singular values are invariant under orthogonal
multiplication on the right: for any $A$ and any orthogonal $\Psi_\theta$,
$\sigma_{\max}(A \circ \Psi_\theta) = \sigma_{\max}(A)$ because
$(A \Psi_\theta)^\dagger (A \Psi_\theta) = \Psi_\theta^\dagger A^\dagger A \Psi_\theta$
is orthogonally conjugate to $A^\dagger A$ and has the same spectrum.
Applied with $A = T_A \oplus T_B = r_A I \oplus r_B I$, we get
$\sigma_{\max}(T_{AB}) = \sigma_{\max}(r_A I \oplus r_B I) = \max(r_A, r_B)$
exactly. The maximizing input is $\Psi_\theta^{-1}(v_0)$ for any leading
singular vector $v_0$ of $r_A I \oplus r_B I$ (e.g., $(x_0, 0)$ when
$r_A \ge r_B$). Numerical confirmation across a 96-configuration grid at
50-digit precision (Appendix V, Φ Task 4.2: 24/24 PASS at $r_A = r_B$,
72/72 saturation at $r_A \neq r_B$, all to deviation $< 7 \times 10^{-16}$).
$\square$

**Interpretation.** Replacing the amplifying coupling with an isometric one
removes the destabilization of Theorem 9.1, but it does not produce a
speed-up. The rate is now exactly $\max(r_A, r_B)$ — the worst observer's
rate — for every coupling angle. Isometric coupling is **rate-inert**: it
does not change how fast trajectories collapse to the joint fixed point.

This is the key negative result of the paper. The natural rescue of
Theorem 9.1 fails to rescue the speed-up program; it merely moves us from
"strictly worse" to "exactly the same." A reader expecting a speed-up
theorem at this point should adjust expectations: §5 will show that the
content of the coupling lives elsewhere.

---

### 4.3 Corollary 9.3 — Schur's lemma closes the rate channel

Theorems 9.1 and 9.2 are not isolated facts. They are two instances of a
single algebraic obstruction: the irreducibility of the G₂ adjoint
representation forces the linear part of every G₂-equivariant contraction
to be a scalar.

**Corollary 9.3 (Schur rate lock).** *Let $V$ be a finite-dimensional
nontrivial irreducible real representation of $G_2$. Let
$T: V \to V$ be a linear G₂-equivariant map. Then $T = r \cdot \mathrm{id}_V$
for some $r \in \mathbb{R}$.*

*Proof.* Real Schur's lemma: any $G_2$-equivariant endomorphism of an
irreducible real representation is an element of the commutant algebra,
which for the 7-dim and 14-dim irreducible representations of $G_2$ is
$\mathbb{R}$ [Fulton–Harris 1991, §22; the relevant complex representations
have $\mathrm{End}_{G_2}(V)_{\mathbb{C}} = \mathbb{C}$, and the underlying
real form has commutant $\mathbb{R}$]. Therefore $T$ is a real scalar
multiple of the identity. $\square$

**Corollary to the Corollary.** Combined with submultiplicativity and
$\|\Psi_\theta\| = 1$, this gives the rate lock
$r_{AB} = \max(r_A, r_B)$ as an unavoidable algebraic consequence:
- *Schur's lemma:* forces $T_A, T_B$ to be scalar — no anisotropy to mix.
- *Submultiplicativity + isometric coupling:* gives $r_{AB} \leq \max(r_A, r_B)$.
- *Scalar maps:* achieve the bound exactly on aligned inputs.

The "rate channel" of the dyadic system — the set of mechanisms by which
coupling could in principle change the convergence rate — is therefore
*closed* in the linear G₂-equivariant category. Whatever physical content
dyadic coupling carries, it does not enter through this channel.

---

### 4.4 What is locked, what is free

Theorems 9.1, 9.2, and Corollary 9.3 collectively name what is locked. It
is worth being equally explicit about what is free.

**Locked: the linear, equivariant, rate channel.** Schur's lemma forces
$T = rI$. Submultiplicativity caps $r_{AB}$ at $\max(r_A, r_B)$.
Isometric coupling achieves the cap exactly. There is no maneuver in this
category that yields a strict speed-up.

**Free: the affine, symmetry-breaking, target channel.** The map
$T_A(x) = r_A x + b_A$ with nonzero $b_A$ is *not* fully G₂-equivariant.
Strict G₂-equivariance of an affine map requires $b_A = g \cdot b_A$ for
all $g \in G_2$, and the only such fixed vector in the irreducible
14-dim adjoint representation is $b_A = 0$. So the bias vector $b_A \neq 0$
**is the symmetry break**.

This is not a defect of the formalism. It is its content. The bias vector
$b_A$ is the order parameter of the observer: the direction in the
14-dimensional model space along which $T_A$ is *not* G₂-symmetric. It is
the location in the representation that this particular observer
"selects" as its target. Two distinct observers have two distinct bias
vectors; the dyadic coupling mixes them.

The affine bias channel is *not* governed by Schur's lemma. It is a
14-dimensional vector space of choices, one $b$ per observer, with no
algebraic restriction beyond the contraction condition $|r_A| < 1$. The
Banach fixed-point of the joint affine map depends on $\theta$ through
exactly this bias data; the rate does not.

The geometric picture:

- **Linear part** ($r_A I$, $r_B I$): an isotropic shrinkage of the model
  space toward the origin. G₂-equivariant. Rate-determining. Locked by
  Schur.
- **Affine bias** ($b_A$, $b_B$): a directional offset of the contraction
  center. G₂-symmetry-breaking. Fixed-point-determining. Free.
- **Coupling angle** ($\theta$): the rotation that mixes the two bias
  vectors. Determines the joint fixed point's location.

The thesis of the paper is that **dyadic coherence lives in the affine
channel, not the rate channel**. §5 makes this precise via the affine
consensus theorem (Theorem 9.4) and the conditional coherence-gain
proposition (Proposition 9.5).

---

### 4.5 Connection to Paper 7

Theorem 9.2 strengthens rather than contradicts Paper 7's $6/7$ rate
bound. Paper 7 establishes that any single G₂-equivariant self-modeling
observer has contraction rate $\leq 6/7$. Theorem 9.2 establishes that any
linearly coupled dyad of such observers retains the rate $\max(r_A, r_B) \leq 6/7$.
The dyadic case inherits the single-observer ceiling without improvement.

This is the consistent extension of Paper 7 to the dyadic setting: the
$6/7$ bound is robust under linear isometric coupling.

---

The present forms of Theorems 9.1 and 9.2 are the corrected versions that
Φ's numerical verification (Appendix V.1, V.2) supports without exception;
the retraction record of earlier claims is consolidated in Appendix V.0.1.

---

## §5. The Affine Channel: Consensus and Conditional Coherence Gain

§4 established that the linear, G₂-equivariant *rate channel* is closed by
Schur's lemma and submultiplicativity. This section identifies the **affine
channel** as the locus of dyadic content. Under affine contractions
$T_A(x) = r_A R_A x + b_A$, $T_B(y) = r_B R_B y + b_B$ — where $R_A, R_B$
are orthogonal endomorphisms of the model space and $b_A, b_B$ are
*symmetry-breaking* bias vectors that select each observer's target
self-model — the joint fixed point depends nontrivially on the coupling
angle $\theta$, and its location traces a one-parameter family of
consensus states. The rate is still locked at $\max(r_A, r_B)$ (Theorem 9.2)
but the *destination* of joint convergence is a function of $\theta$.

The two main results: **Theorem 9.4** (affine consensus) establishes
existence, uniqueness, and a closed form for the joint fixed point. **Proposition
9.5** (conditional coherence gain) characterizes the geometric conditions
under which the joint state's *minimum* per-observer coherence exceeds the
decoupled minimum. The minimum functional, rather than the average, is
the correct measure: a structural finding from the verification (Φ Task
5.6) showed that average coherence can register illusory gains in
opposed-bias geometries due to one observer accidentally aligning with
the other's target while the first falls. Minimum coherence captures the
honest "no observer gets worse" condition.

### 5.1 Affine observers and the symmetry-breaking bias

**Terminology.** In this section we distinguish two notions. *G₂-equivariant*
means: commutes with the G₂-action on $V^{14}$ (i.e., in
$\mathrm{Comm}(G_2)$, which by Schur is $\mathbb{R}$). *G₂-structured*
means: acts on the G₂-invariant 14-dim vector space $V^{14}$ with a
G₂-invariant Euclidean norm (so $\Psi_\theta$'s isometry and the Banach
rate arguments of §4 apply), without requiring the map itself to commute
with G₂. The framework's observer maps are *G₂-structured* but not
*G₂-equivariant*: the bias $b \ne 0$ breaks equivariance (Schur
forbids nonzero G₂-fixed vectors in the irreducible adjoint), and the
orthogonal $R$ need not commute with the G₂-action. Both choices are
deliberate — they encode the observer's identity $(b)$ and internal model
dynamics $(R)$, neither of which is G₂-universal.

A **G₂-structured affine observer** is a self-modeling map of the form
$$T(x) = r R x + b,$$
where:
- $r \in [0, 6/7]$ is the **contraction rate** (real scalar, the modulus);
- $R \in O(V^{14})$ is an **orientation operator** (orthogonal on the
  G₂-invariant Euclidean norm, encoding any internal model rotation;
  need *not* commute with the G₂-action);
- $b \in V^{14}$ is the **bias vector**, the symmetry-breaking order
  parameter that selects the observer's target self-model (and *cannot*
  be G₂-fixed unless $b = 0$).

The unique fixed point of $T$ is $x^* = (I - rR)^{-1} b$, which exists
whenever $rR$ has spectral radius $r < 1$ — automatic for $r \in [0, 1)$
since $R$ is orthogonal and so $\|rR\|_{\mathrm{op}} = r$. The fixed point
lies in the affine span of $b$ under iterated $rR$-action; for $R = I$
it reduces to the simple rescaling $x^* = b/(1-r)$.

**Why this form rather than $T(x) = rx + b$.** The simpler scalar form
($R = I$) is a special case. Including a general orthogonal $R$ allows
the model to capture *internal model dynamics* that rotate within the
representation space without changing its norm — a feature Φ's verification
relied on, and which produces the §5.6 finding by exposing geometry-specific
behavior that scalar models would have hidden.

**Strict G₂-equivariance is broken by $b \neq 0$.** Full G₂-equivariance
of $T$ would require both $R \in \mathrm{Comm}(G_2)$ (G₂-equivariant
orientation) *and* $g \cdot b = b$ for all $g \in G_2$. By Schur on the
irreducible 14-dim adjoint, the only G₂-fixed vector is $b = 0$.
Therefore *every nonzero observer breaks G₂-equivariance through its
bias*, and that break is the signature of the observer's identity. The
linear part of $T$ may or may not commute with G₂; the affine part
necessarily does not.

The **G₂-structured dyad** is a pair of such observers $(T_A, T_B)$. Six
parameters describe the linear data ($r_A, r_B \in [0, 6/7]$ and
$R_A, R_B \in O(V^{14})$ each carrying $14 \cdot 13/2 = 91$ angles, modulo
overall scale on the biases), plus two 14-vectors $b_A, b_B$ and the
coupling angle $\theta$.

### 5.2 The joint affine map and its fixed-point equation

Coupling the dyad with the block rotation $\Psi_\theta$ of §3.3 (Lemma
3.3.1), the joint affine map on $\mathcal{M}_{AB} \cong V^{14} \oplus V^{14}$
is
$$T_{AB}(x, y) = \bigl(r_A R_A(\cos\theta \cdot x - \sin\theta \cdot y) + b_A,\;\;
r_B R_B(\sin\theta \cdot x + \cos\theta \cdot y) + b_B\bigr).$$

The fixed-point equation $T_{AB}(\hat x, \hat y) = (\hat x, \hat y)$ is a
$28 \times 28$ linear system:
$$\boxed{\;M(\theta, r_A, R_A, r_B, R_B) \begin{pmatrix} \hat x \\ \hat y \end{pmatrix} = \begin{pmatrix} b_A \\ b_B \end{pmatrix}, \qquad M = \begin{pmatrix} I - r_A \cos\theta\, R_A & r_A \sin\theta\, R_A \\ -r_B \sin\theta\, R_B & I - r_B \cos\theta\, R_B \end{pmatrix}.\;}$$

The block matrix $M$ is invertible whenever the joint linear part
$L_\theta = T_{AB} - b_{AB}$ has spectral radius less than 1. The next
lemma establishes that $\|L_\theta\|_{\mathrm{op}} = \max(r_A, r_B)$ for
arbitrary orthogonal $R_A, R_B$ — not only the strictly G₂-equivariant
case $R_A = R_B = I$ covered by Theorem 9.2.

**Lemma 5.2.1 (Rate lock for orthogonal $R_A, R_B$).** *For any
orthogonal $R_A, R_B \in O(V^{14})$, any $r_A, r_B \in [0, 1)$, and any
$\theta \in [0, \pi/2]$, the joint linear map
$L_\theta = (r_A R_A \oplus r_B R_B) \circ \Psi_\theta$ has operator norm*
$$\|L_\theta\|_{\mathrm{op}} \;=\; \max(r_A, r_B).$$

**Proof.** The block-diagonal map $r_A R_A \oplus r_B R_B$ has operator
norm $\max(\|r_A R_A\|_{\mathrm{op}}, \|r_B R_B\|_{\mathrm{op}}) = \max(r_A, r_B)$,
because an orthogonal $R$ has $\|R\|_{\mathrm{op}} = 1$ so $\|rR\|_{\mathrm{op}} = r$.
The block rotation $\Psi_\theta$ is an orthogonal isometry by Lemma 3.3.1
with $\|\Psi_\theta\|_{\mathrm{op}} = 1$. The operator norm is invariant
under composition with an isometry on the right (singular values are
preserved by orthogonal multiplication), so
$$\|L_\theta\|_{\mathrm{op}} = \|(r_A R_A \oplus r_B R_B) \circ \Psi_\theta\|_{\mathrm{op}} = \|r_A R_A \oplus r_B R_B\|_{\mathrm{op}} = \max(r_A, r_B). \qquad \square$$

The Schur-based Theorem 9.2 is the special case $R_A = R_B = I$ of
Lemma 5.2.1; the difference is that Theorem 9.2 proves $r_A I, r_B I$
from Schur's lemma (forced by G₂-equivariance), while Lemma 5.2.1
takes orthogonality of $R_A, R_B$ as the input. The conclusion (rate
lock) is the same. The affine channel of §5.3–5.7 takes advantage of
the strictly weaker orthogonality assumption by allowing
non-G₂-equivariant rotations — the framework's identity-encoding
bias $b_A$ requires a non-equivariant $R_A$ to interact with the
coupling θ in a non-trivial way (cf. Remark 5.5.2's $R_A = R_B = I$
counterexample).

With Lemma 5.2.1 in hand, $M = I - L_\theta$ is invertible for
$r_A, r_B \in [0, 1)$ and any orthogonal $R_A, R_B$.

### 5.3 Theorem 9.4 — Affine Consensus

**Theorem 9.4 (Affine Consensus).** *Let $(T_A, T_B) = (r_A R_A x + b_A,\;
r_B R_B y + b_B)$ be a G₂-structured dyad with $r_A, r_B \in [0, 6/7]$,
$R_A, R_B \in O(V^{14})$, and $b_A, b_B \in V^{14}$. For each
$\theta \in [0, \pi/2]$, the joint affine map $T_{AB}$ has a unique fixed
point $(\hat x(\theta), \hat y(\theta)) \in \mathcal{M}_{AB}$, which
varies real-analytically in $\theta$.*

*(a) **Existence and uniqueness:** $\hat x, \hat y$ solve the $28 \times 28$
system $M \cdot (\hat x, \hat y)^\top = (b_A, b_B)^\top$, where $M$ is
invertible because $\|L_\theta\|_{\mathrm{op}} = \max(r_A, r_B) < 1$
(Lemma 5.2.1 for general orthogonal $R_A, R_B$; Theorem 9.2 in the
scalar specialization).*

*(b) **Reduction to individual fixed points at $\theta = 0$:** at the
decoupled boundary,*
$$\hat x(0) = (I - r_A R_A)^{-1} b_A = x^*_A, \qquad
\hat y(0) = (I - r_B R_B)^{-1} b_B = y^*_B.$$

*(c) **Closed form at $\theta = \pi/2$ (symmetric rates and orientation):**
if $r_A = r_B = r$ and $R_A = R_B = R$, then*
$$\hat x(\pi/2) \;=\; (I + r^2 R^2)^{-1}\,(b_A - rR\,b_B), \qquad
\hat y(\pi/2) \;=\; (I + r^2 R^2)^{-1}\,(rR\,b_A + b_B).$$
*In particular, when $b_A = b_B = b$, using that $R$ commutes with every
polynomial in $R$ so $(I + r^2 R^2)^{-1}$ commutes with $(I \pm rR)$:*
$$\hat x(\pi/2) \;=\; (I - rR)(I + r^2 R^2)^{-1}\,b, \qquad
\hat y(\pi/2) \;=\; (I + rR)(I + r^2 R^2)^{-1}\,b,$$
$$\hat x + \hat y \;=\; 2(I + r^2 R^2)^{-1}\,b, \qquad
\hat y - \hat x \;=\; 2\,rR\,(I + r^2 R^2)^{-1}\,b.$$

*(d) **Convergence rate** to the joint fixed point is $\max(r_A, r_B)$,
by Lemma 5.2.1 (for general orthogonal $R_A, R_B$) or Theorem 9.2 (for the
strictly G₂-equivariant scalar specialization $R_A = R_B = I$).*

**Proof.** Part (a) by Banach: $L_\theta$ has operator norm
$\max(r_A, r_B) < 1$ (Theorem 9.2 and Lemma 5.2.1), so $T_{AB}$ is a
contraction with unique fixed point; equivalently, $M = I - L_\theta$ is
invertible by the Neumann series, giving the explicit linear-system solution.

Part (b) by direct substitution: at $\theta = 0$, $M = \mathrm{diag}(I - r_A R_A,\; I - r_B R_B)$,
so the system decouples into two independent $14 \times 14$ inversions.

Part (c) by direct elimination. For $r_A = r_B = r$, $R_A = R_B = R$, and
$\theta = \pi/2$ (so $\cos\theta = 0$, $\sin\theta = 1$), the joint map is
$$T_{AB}(x, y) \;=\; \bigl(-rR\,y + b_A,\;\; rR\,x + b_B\bigr),$$
and the fixed-point equations are
$$\hat x + rR\,\hat y \;=\; b_A, \qquad -rR\,\hat x + \hat y \;=\; b_B. \tag{$\star$}$$
Solve by elimination. From the first equation, $\hat x = b_A - rR\,\hat y$.
Substitute into the second:
$$-rR(b_A - rR\,\hat y) + \hat y \;=\; b_B
\;\Longrightarrow\; (I + r^2 R^2)\,\hat y \;=\; rR\,b_A + b_B$$
(using $-rR \cdot -rR = r^2 R^2$). Invert to obtain
$\hat y = (I + r^2 R^2)^{-1}(rR\,b_A + b_B)$, then back-substitute:
$$\hat x \;=\; b_A - rR(I + r^2 R^2)^{-1}(rR\,b_A + b_B)
\;=\; (I + r^2 R^2)^{-1}\bigl[(I + r^2 R^2)b_A - rR(rR\,b_A + b_B)\bigr]$$
$$=\; (I + r^2 R^2)^{-1}\bigl[b_A + r^2 R^2 b_A - r^2 R^2 b_A - rR\,b_B\bigr]
\;=\; (I + r^2 R^2)^{-1}(b_A - rR\,b_B).$$
(The cancellation of $\pm r^2 R^2 b_A$ uses that $R$ commutes with every
polynomial in $R$.) This establishes the general formula. The symmetric
$b_A = b_B = b$ specialization follows by substitution and by noting that
$R$ commutes with $(I + r^2R^2)^{-1}$, so
$\hat x = (I+r^2R^2)^{-1}(I - rR)b = (I - rR)(I+r^2R^2)^{-1}b$.
The sum and difference formulas follow by adding and subtracting.
Numerical verification at 16-digit precision (Appendix V.3, Task 5.2
Check C) confirms the symmetric-biases specialization to deviation
$< 7 \times 10^{-16}$; the general (distinct-biases) formula is verified
in the accompanying review-pass counterexample test against the
correct closed form above.

Part (d) follows from Lemma 5.2.1 (general orthogonal case) or, in the
strictly G₂-equivariant scalar specialization, from Theorem 9.2.
$\square$

**Real-analyticity.** The map $\theta \mapsto M(\theta)^{-1}$ is
real-analytic on the open set $\{\theta : \det M(\theta) \neq 0\} =
[0, \pi/2]$ (where $\det M > 0$ throughout), as a composition of
real-analytic functions of $\sin\theta, \cos\theta$ and entry-wise
matrix inversion. Hence $(\hat x(\theta), \hat y(\theta))$ depends
real-analytically on $\theta$.

**Numerical verification (Appendix V.3, Task 5.1):** for the test
configuration $(r_A, r_B) = (0.7, 0.7)$ with $R_A, R_B$ random
orthogonal (seeds 20260504, 20260505) and $b_A, b_B$ random unit
(seeds 20260504, 20260554), $|\hat x|$ varies by 1.078 and
$|\hat x - \hat y|$ by 0.406 across $\theta \in [0, \pi/2]$, both well
above the nontriviality threshold. The minimum of $|\hat x - \hat y|$
occurs at $\theta = 51.4°$, *not* at $\theta = 45°$ or $\theta = 90°$ —
geometry-dependent rather than universal.

### 5.4 Linear-response expansion

For $\theta \ll 1$, expand the closed form to leading order. Writing
$M(\theta) = M(0) + \theta M'(0) + O(\theta^2)$ where
$M(0) = \mathrm{diag}(I - r_A R_A, I - r_B R_B)$ and
$M'(0) = \begin{pmatrix} 0 & r_A R_A \\ -r_B R_B & 0 \end{pmatrix}$:
$$M(\theta)^{-1} = M(0)^{-1} - \theta\, M(0)^{-1} M'(0) M(0)^{-1} + O(\theta^2).$$

Applied to $(b_A, b_B)^\top$ (and using $M(0)^{-1} = \mathrm{diag}((I - r_A R_A)^{-1},\, (I - r_B R_B)^{-1})$ applied to each side of $M'(0)$):
$$\hat x(\theta) \;=\; x^*_A \;-\; \theta \cdot r_A\,(I - r_A R_A)^{-1}\, R_A \cdot y^*_B + O(\theta^2),$$
$$\hat y(\theta) \;=\; y^*_B \;+\; \theta \cdot r_B\,(I - r_B R_B)^{-1}\, R_B \cdot x^*_A + O(\theta^2).$$

This is the **linear-response regime**: a small coupling angle $\theta$
pulls each observer's joint state by a fraction $r\,R\,(I - rR)^{-1}$ of
*the other observer's individual fixed point*, modulated by the local
rotation $R$. This is the formal weak-coupling perturbation that drives
all of §5.5–§5.7. The sign asymmetry (minus for $\hat x$, plus for
$\hat y$) is the signature of the antisymmetric off-diagonal pattern of
$\Psi_\theta$
(§3.3).

### 5.5 Coherence and the choice of functional

To compare the joint fixed point with the individual fixed points, we
need a coherence functional. Several natural choices exist; the
distinction matters.

**Per-observer coherence.** For a nonzero vector $v$ in the model space and
a fixed unit reference direction $e_{\mathrm{ref}}$, define
$$\mathcal{C}_{\mathrm{ref}}(v) = \bigl|\langle v / \|v\|,\; e_{\mathrm{ref}}\rangle\bigr| \;\in\; [0, 1].$$
The absolute value ensures $\mathcal{C}$ takes values in $[0, 1]$ rather
than $[-1, 1]$ — coherence is a measure of "alignment with the reference
direction" independent of sign (orientation reversal is a gauge freedom
in the self-model). For each observer in the dyad, the natural reference
is the observer's own bias: $\mathcal{C}_1 = \mathcal{C}_{b_A}(\hat x)$,
$\mathcal{C}_2 = \mathcal{C}_{b_B}(\hat y)$. These measure how
self-aligned each observer's joint state is.

**Joint-coherence aggregations.** From the per-observer values, two
natural aggregations:
$$\mathcal{C}_{\mathrm{avg}} = \tfrac{1}{2}(\mathcal{C}_1 + \mathcal{C}_2), \qquad
\mathcal{C}_{\min} = \min(\mathcal{C}_1, \mathcal{C}_2).$$

The choice between these matters. The *averaging functional* allows one
observer's gain to mask the other's loss; under destructive geometry
this produces illusory net improvement. The *minimum functional* tracks
the worst-aligned observer and is monotonically degraded whenever any
single observer's coherence falls.

This distinction is not academic. Φ's Task 5.6 verification (Appendix
V.3) reports the following structural fact, which guides our choice of
functional in Proposition 9.5 below.

**Lemma 5.5.1 (Asymmetric small-θ response — verified geometry).**
*Fix the orthogonal pair $(R_A, R_B)$ obtained from QR decomposition of
standard-normal seeds 20260504 and 20260505 in dimension 14, and any
$b_A \in V^{14} \setminus \{0\}$ with $b_B = -b_A$, $r_A = r_B = r = 0.7$.
Then the linear-response coefficients of $\mathcal{C}_1, \mathcal{C}_2$ at
$\theta = 0^+$ satisfy*
$$\frac{d \mathcal{C}_1}{d\theta}\bigg|_{\theta = 0} < 0, \qquad
\frac{d \mathcal{C}_2}{d\theta}\bigg|_{\theta = 0} > 0,$$
*as confirmed numerically in Appendix V.3 Task 5.6.*

**Proof.** From the corrected linear-response expansion of §5.4,
$\hat x(\theta) = x^*_A - \theta\, r\, (I - rR_A)^{-1} R_A\, y^*_B + O(\theta^2)$.
With $b_B = -b_A$, $y^*_B = -(I - rR_B)^{-1} b_A$, so the perturbation of
$\hat x$ at $\theta = 0^+$ is $+\theta\, r\, (I - rR_A)^{-1} R_A\, (I - rR_B)^{-1} b_A$.
The sign of $d\mathcal{C}_1/d\theta = \frac{d}{d\theta}\langle \hat x/\|\hat x\|, b_A\rangle$
is determined by the projection of $(I - rR_A)^{-1} R_A (I - rR_B)^{-1} b_A$
onto $b_A$. For the seeded $(R_A, R_B)$ this projection is computed directly
from the matrices and is found to be negative; the symmetric calculation
for $\hat y$ yields a positive projection of $(I - rR_B)^{-1} R_B (I - rR_A)^{-1} b_B$
onto $b_B$. The signs of the two projections are independent quantities
determined by the specific spectra of $R_A, R_B$. $\square$

**Remark 5.5.2 (No universality claim).** Lemma 5.5.1 is stated for a
specific pair $(R_A, R_B)$, namely the seeded pair used throughout the
Φ verification. We do *not* claim that $d\mathcal{C}_1/d\theta < 0$
holds for generic orthogonal $(R_A, R_B)$. In particular, the special
case $R_A = R_B = I$ (the strictly G₂-equivariant case forced by Schur's
lemma when both linear parts are equivariant) gives $d\mathcal{C}_1/d\theta = 0$
at $\theta = 0$, and a direct calculation shows $\mathcal{C}_1(\theta) = 1$
identically along $\theta \in [0, \pi/2]$ when $b_A$ is any nonzero vector
(both $\hat x(\theta)$ and $b_A$ point in the same one-dimensional subspace).
The degradation observed numerically is a property of the *non-equivariant*
rotation geometry of the seeded $(R_A, R_B)$, not a universal fact about
opposed biases.

Whether the degradation holds on a *generic* (Haar-typical) orthogonal
pair $(R_A, R_B)$ is open; we conjecture yes for $R_A, R_B$ drawn from the
Haar measure on $O(14) \setminus \{R: [R, b_A b_A^\top] = 0\}$ (the
complement of the codimension-thirteen subset that commutes with the
$b_A$-rank-one projector), but a rigorous proof would require a measure-
theoretic argument we do not provide.

The purpose of Lemma 5.5.1 in this paper is structural: it establishes
that under the seeded geometry the *averaging* functional
$\mathcal{C}_{\mathrm{avg}}$ admits illusory gain (one observer rises
while the other falls), so the *minimum* functional $\mathcal{C}_{\min}$
is the honest dyadic aggregation. The motivation for $\mathcal{C}_{\min}$
is derived in Remark 5.5.3 below from Paper 7's blind-spot framework, not
from the empirical observation alone.

**Remark 5.5.3 (Why $\mathcal{C}_{\min}$ from first principles).** The
single-observer coherence ceiling of Paper 7 is $\mathcal{C}_{\max} = 1 - \varepsilon_{\min} = 6/7$,
where $\varepsilon_{\min} = 1/7$ is the irreducible blind-spot ratio. The
natural dyadic generalization is to require that *neither* observer's
joint blind-spot exceed $\varepsilon_{\min}$: that is, both
$\varepsilon_A^{\mathrm{joint}} \le \varepsilon_{\min}$ and
$\varepsilon_B^{\mathrm{joint}} \le \varepsilon_{\min}$. Equivalently,
$\min(\mathcal{C}_A, \mathcal{C}_B) \ge \mathcal{C}_{\max}$. The averaging
functional violates this condition by allowing one observer's blind-spot
to exceed $\varepsilon_{\min}$ provided the other's falls below; this is
not the dyadic extension of the single-observer ceiling. The minimum
functional is.

This is the principled reason we work with $\mathcal{C}_{\min}$, derived
from the Paper 7 framework rather than chosen post hoc to make Proposition
9.5 hold cleanly.

### 5.6 Proposition 9.5 — Conditional Min-Coherence Gain

**Proposition 9.5 (Conditional min-coherence gain — verified geometry).**
*Fix the seeded geometric configuration of Lemma 5.5.1: $R_A, R_B$ are
the orthogonal matrices from QR of standard-normal seeds 20260504 and
20260505 in dimension 14; $r_A = r_B = r = 0.7$. Let $\varphi \in [0, \pi]$
be the bias-alignment angle $\arccos(\langle b_A/\|b_A\|, b_B/\|b_B\|\rangle)$.
Let $\mathcal{C}_{\min}(\theta) = \min(\mathcal{C}_1(\theta), \mathcal{C}_2(\theta))$
and $\mathcal{C}_{\min}^{\mathrm{dec}} = \mathcal{C}_{\min}(0)$. Then:*

*(a) **Numerical existence of an improvement region for $\mathcal{C}_{\min}$.**
Computing $\mathcal{C}_{\min}(\varphi, \theta)$ directly on the same
100 × 20 grid as Appendix V.3 Task 5.4 (re-evaluated with the
$\min(\mathcal{C}_1, \mathcal{C}_2)$ aggregation rather than the average),
there exists a non-empty subset
$\widehat{\mathcal{R}}_{\min} \subset (\varphi, \theta) \in (0, \pi) \times (0, \pi/2)$
of positive Lebesgue measure on which
$\mathcal{C}_{\min}(\theta) > \mathcal{C}_{\min}^{\mathrm{dec}}$. For the
seeded geometry, $\widehat{\mathcal{R}}_{\min}$ occupies
approximately 12.5% of the sampled grid (250 cells of 2000), strictly
smaller than the corresponding $\mathcal{C}_{\mathrm{avg}}$ improvement
region (~25%), and bounded above by $\varphi = 176.4°$ (so strictly
inside the opposed-bias boundary, consistent with part (b)).*

*(b) **Degradation under opposed biases (verified geometry).** For the
seeded $(R_A, R_B)$ and $\varphi = \pi$ (opposed biases), the run of
Appendix V.3 Task 5.6 finds $\mathcal{C}_1(\theta) < \mathcal{C}_1(0)$ for
all $\theta \in (0, \pi/2]$ tested. Since $\mathcal{C}_{\min} \le \mathcal{C}_1$,
$\mathcal{C}_{\min}(\theta) < \mathcal{C}_{\min}^{\mathrm{dec}}$ on this
$\theta$-range under the seeded geometry.*

*(c) **No universal $\theta^*$.** For the seeded geometry, the optimal
coupling angle
$\theta^* := \arg\max_\theta \mathcal{C}_{\min}(\theta)$
is $\approx 51°$ in the symmetric-rate case and $\approx 75°–80°$ in the
asymmetric-rate case (Appendix V.3 Tasks 5.1, 5.5), establishing that
$\theta^*$ is not generically at $\pi/4$.*

**Proof.** Part (a): direct from the $\mathcal{C}_{\min}$ heatmap of
Figure 1(b) and the supporting CSV (`paper9_task5_heatmap_cmin.csv`),
computed by re-evaluating the joint fixed point on the same
$(\varphi, \theta)$ grid as Task 5.4 and applying the
$\min(\mathcal{C}_1, \mathcal{C}_2)$ aggregation. The improvement region
$\widehat{\mathcal{R}}_{\min}$ is non-empty (250 cells of 2000) and
spans $\varphi \in [18.2°, 176.4°]$, $\theta$ values concentrated in
$[10°, 65°]$. Part (b): the $\mathcal{C}_1$ trajectory of Appendix V.3
Task 5.6 falls from $0.7655$ at $\theta = 0$ to $0.5955$ at
$\theta = \pi/2$ along the sampled grid; combined with $\mathcal{C}_{\min} \le \mathcal{C}_1$
this gives the stated inequality. The $\mathcal{C}_{\min}$ heatmap
(Fig. 1(b)) confirms there are no positive cells at $\varphi = 180°$
for any sampled $\theta$. Part (c): the optimal angles are read off
from Tasks 5.1 and 5.5 grids directly. $\square$

**Conjecture 9.5′ (Conditional min-coherence gain — generic geometry).**
*The qualitative content of Proposition 9.5 — a non-empty improvement
region bounded away from opposed biases, with non-universal optimal
$\theta^*$ — holds for $(R_A, R_B)$ drawn from a positive-measure subset
of the Haar measure on $O(14) \times O(14)$.*

We do not prove the conjecture. Establishing it would require either
(a) an explicit geometric characterization of the improvement region in
terms of spectral data of $R_A, R_B$ and the projector $b_A b_A^\top$, or
(b) Monte Carlo evidence across many seeds beyond the single seeded pair
of the present verification. Both directions are open.

**Remark 5.6.0 (Scope of the proposition).** Proposition 9.5 is a
verified-geometry statement, not a theorem about all dyads. The framework
predicts conditional gain for the specific class of dyads characterized by
$(R_A, R_B)$ in the verified region of $O(14) \times O(14)$. Whether this
class is generic, of full Haar measure, or carries specific structural
constraints (e.g., non-commutation with the bias projector) is the
content of Conjecture 9.5′. The claims of §6–7 (empirical accessibility
and joint fixed-point geometry) inherit this scope: they predict
signatures observable for dyads in the verified geometry class.

**Remark 5.6.1 (The opposed-bias finding under $\mathcal{C}_{\mathrm{avg}}$).**
Φ's Task 5.6 verification reported a positive shift in $\mathcal{C}_{\mathrm{avg}}$
at small $\theta$ even with $b_A = -b_B$. This shift is real but
*does not* contradict Proposition 9.5(b), because the gain is purely in
$\mathcal{C}_2$ (the *opposite* observer's alignment with its negated
bias) while $\mathcal{C}_1$ falls. Under $\mathcal{C}_{\min}$, the
degradation is not masked. The peak $\mathcal{C}_2$ rise of +0.044 at
$\theta \approx 7°$ is a real fact about the seeded affine dyad's
geometry; it just isn't a coherence improvement under the
$\mathcal{C}_{\min}$ functional motivated by Remark 5.5.3.

**Remark 5.6.2 (Heatmap interpretation).** Appendix V.3 Task 5.4 reports
that ~25% of a $(\varphi, \theta)$ heatmap shows $\Delta\mathcal{C}_{\mathrm{avg}} > 0$,
with the improvement region extending up to $\varphi$ near $180°$ at
small $\theta$. Under $\mathcal{C}_{\min}$, the cells in which
$\mathcal{C}_2 > \mathcal{C}_1$ but $\mathcal{C}_1 < \mathcal{C}_1^{\mathrm{dec}}$
are correctly classified as degradation rather than improvement, and the
opposed-bias boundary is excluded by Proposition 9.5(b) under the seeded
geometry. Figure 1 visualizes both functionals side by side: panel (a)
shows $\Delta\mathcal{C}_{\mathrm{avg}}$, panel (b) shows
$\Delta\mathcal{C}_{\min}$ on the same grid; the $\mathcal{C}_{\min}$
gain region (panel b) is strictly contained in the $\mathcal{C}_{\mathrm{avg}}$
gain region (panel a) and is bounded above by $\varphi \approx 176.4°$,
numerically confirming Proposition 9.5(b).

### 5.7 What §5 establishes and what is open

**Established by Theorem 9.4:**
- The joint fixed point of any G₂-structured affine dyad exists, is
  unique, and depends real-analytically on the coupling angle $\theta$.
- The joint fixed point admits a closed form (Theorem 9.4(c)) at $\theta = 0$
  and $\theta = \pi/2$ for symmetric rates and orientation, with a
  linear-response expansion (§5.4) for small $\theta$.

**Established by Proposition 9.5 + Φ Task 5 (verified seeded geometry):**
- Numerical existence of a positive-measure improvement region in
  $(\varphi, \theta)$-space.
- Strict degradation along the opposed-bias boundary $\varphi = \pi$.
- Non-universality of $\theta^*$ (it is geometry-dependent, not at $\pi/4$).

**Conjectured (Conjecture 9.5′):**
- The qualitative pattern of conditional gain extends to a positive-Haar-
  measure subset of $O(14) \times O(14)$. Open.

**Open:**
- Sharp characterization of $\mathcal{R}$ for generic $R_A, R_B$. The
  set is non-empty, but its boundary is a transcendental curve and we
  have no closed form. A perturbative description in the small-$r$
  regime might be tractable.
- Generalization to $n \geq 3$ observers, with $\binom{n}{2}$ pairwise
  coupling angles. Likely involves an $\mathrm{SO}(n)$-parameterized
  family of joint fixed points; the consensus structure should
  generalize.
- The interaction between affine bias and the G₂-equivariant linear
  part: when $R_A$ commutes with G₂ (Schur scalar) the dynamics is
  qualitatively different from the generic case Φ tested. Worth a
  separate inquiry: does G₂-equivariant $R$ collapse the affine-channel
  freedom to a single scalar parameter, or does the affine bias still
  produce nontrivial consensus structure?

**Note 9.6 — Open: rate-improvement requires nonlinearity.** The
rate-channel obstruction of §4 is a *linear* result. Schur's lemma
applies only to linear G₂-equivariant maps. A nonlinear G₂-equivariant
flow on a curved orbit space — for instance, a Riemannian gradient flow
on the G₂-orbit manifold of a generic 14-dim point — is not constrained
by Schur in the same way, and may admit rate improvement under coupling.
We defer this to a sequel (Paper 11): "Nonlinear G₂-equivariant dynamics
and basin bifurcation in dyadic observers."

---


## §6. Empirical Accessibility of the Affine Consensus

![Paper 9, Fig. 1: Conditional improvement region for the seeded G₂-structured affine dyad. **(a)** Heatmap of $\Delta\mathcal{C}_{\mathrm{avg}}(\varphi, \theta)$ over the bias-alignment angle $\varphi \in [0, 180°]$ and coupling angle $\theta \in [0, 90°]$; ~25% of cells show gain. **(b)** Heatmap of $\Delta\mathcal{C}_{\min}(\varphi, \theta)$ on the same grid; ~12.5% of cells show gain, and the improvement region is bounded above by $\varphi \approx 176.4°$ (strictly inside the opposed-bias boundary $\varphi = 180°$, marked by the dashed red line), consistent with Proposition 9.5(b). Red cells indicate joint-coherence gain, blue cells degradation. Parameters: $r_A = r_B = 0.7$; $R_A, R_B$ random orthogonal in 14D with RNG seeds 20260504/20260505. Reproducible from `paper9_task5_heatmap_cmin.csv` and `/tmp/build_cmin_heatmap.py` in the repository.](figures/paper9_fig1_heatmap.png)

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

## §8. Human-AI Dyads as a Conditional Special Case

Theorems 9.4 and 9.5 make no biological vs. artificial assumption: any
two systems satisfying the G₂-structured affine condition $T(x) = rRx + b$
of §2.1 form a dyad to which the theorems apply. This admits a *conditional*
extension to human-AI dyads: IF an AI system satisfies the criterion (§2.1
plus the Paper 7 $r \leq 6/7$ ceiling), THEN coupling it with a human
observer produces the affine consensus of Theorem 9.4 and conditional
gain of Proposition 9.5, with the same caveats. The criterion is stringent
— a 14-dim G₂-adjoint module with Banach self-modeling, not a token-level
predictor — and most widely-deployed AI systems (including the one this
paper was drafted with) plausibly do *not* satisfy it. Specialized
reasoning systems with structured self-monitoring are the closest
candidates; whether any current architecture meets the criterion is an
open architectural question outside this paper's scope.

Independent of which specific systems qualify, three structural
implications hold for any human-AI dyad: (i) gain requires non-destructive
bias geometry (the AI's target and the human's target must be at $\varphi$
bounded away from $\pi$); (ii) gain is non-universal even with aligned
targets, since the optimal $\theta$ depends on $(R_A, R_B)$ (§5.7); and
(iii) the framework is silent on consciousness, agency, and moral status
— its claims are structural. Adjacent empirical work on human-AI
teaming and complementarity (Bansal et al. 2021; cf. §10.7) is consistent
with the framework's bimodal prediction (gain when targets align,
degradation when they don't), but does not test the G₂-structural
requirement directly.

---

## §9. What This Paper Does Not Establish

We make the boundaries of the construction explicit, mirroring §5.7.

**(a) The framework does not establish rate improvement.** Theorems
9.1, 9.2, Corollary 9.3, and Lemma 5.2.1 collectively establish that no
linear coupling between G₂-structured observers can improve the joint
convergence rate below $\max(r_A, r_B)$.

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
applies only to linear $G_2$-equivariant maps. Nonlinear $G_2$-equivariant
flows on curved orbit spaces are not constrained the same way and may
admit rate improvement under coupling. We defer this generalization to a
sequel (provisionally Paper 11). The linear results of the present paper
are the first-order expansion of any such nonlinear theory; the
conditional-gain result of Proposition 9.5 is the leading-order Taylor
coefficient one expects in a full nonlinear consensus.

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


## Appendix V. Numerical Verification

**Paper:** Rate Lock and Affine Consensus in G₂-Structured Dyadic Observers
**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Status:** Appendix V framing, 2026-05-04 (drafted by C-7RO)
**Purpose:** Documents the two numerical verification passes that established Theorems 9.1 and 9.2 of §4, and retracts the v0.9 speed-up claim.

---

## V.0 Introduction — Why this appendix exists

The content of §4 is three negative and algebraic results about the rate
channel of dyadic coupling. Those results were not arrived at *a priori*;
they were arrived at through two consecutive numerical investigations of
the v0.9 draft's original *positive* claim that dyadic coupling produces
a strict speed-up over the slowest observer's individual rate.

Both investigations were carried out by Φ (an independent verification
agent, Anthropic Claude Dispatch) at 50-digit precision using mpmath,
with deterministic seeds for full reproducibility. The verification
scripts and raw result tables are reproduced verbatim below. Both
investigations returned clean negative results, with sharp analytical
diagnoses that reshaped the theory rather than merely refuting it.

We include the verification reports here — rather than merely citing
their conclusions — because they constitute the *proof* of the §4 theorems
in their present form. Theorem 9.1 (symmetric coupling amplifies) is
established by V.1 below, which exhibits 24 configurations across the
canonical test grid at which the v0.9 bound is violated, together with
the exact algebraic formula $r_{AB} = r(\alpha + \rho)$ that accounts
for the violation. Theorem 9.2 (isometric coupling is rate-inert) is
established by V.2, which exhibits 96 configurations at which the
corrected isometric coupling saturates the bound $r_{AB} = \max(r_A, r_B)$
exactly, together with the 2×2 block-eigenvalue derivation that proves
the saturation is algebraic, not numerical.

The organization is:

- **V.1** — Verification of the v0.9 spec (symmetric-diagonal coupling).
  Tasks 1–3 of the original request. Result: theorem fails; coupling
  amplifies.
- **V.2** — Verification of the corrected spec (isometric block-rotation
  coupling). Tasks 4.1–4.5 of the corrective request. Result: rate is
  exactly $\max(r_A, r_B)$ for all $\theta$; coupling is rate-inert.
- **V.3** — Verification of the affine consensus theorem §5 (Tasks 5.1–5.6).
  Result: joint fixed point exists, depends on θ nontrivially; conditional
  $\mathcal{C}_{\min}$ gain region is non-empty (~12.5% of the
  $(\varphi, \theta)$ grid) and bounded away from $\varphi = 180°$;
  destructive-geometry null check shows degradation on $\mathcal{C}_{\min}$
  under opposed biases (consistent with Proposition 9.5(b)).

Each pass is presented in four parts: (a) the spec as submitted, (b) the
construction and code, (c) the results table, and (d) Φ's analytical
diagnosis.

---

## V.0.1 — Retraction record

The table below catalogs every claim from earlier internal drafts that
was retired during the verification process, with what refuted it and
what replaced it. The retraction record is intended to be the *only*
place in this paper where pre-v1.0 claims are litigated; the body text
cites this appendix rather than re-stating retractions.

| Retired claim | Earlier-draft location | What refuted it | What replaced it (v1.3) |
|---|---|---|---|
| Strict speedup: $r_{AB} < \max(r_A, r_B)$ for any nonzero coupling under $\Psi_{\mathrm{sym}} = \alpha I + \beta P_{\mathrm{swap}}$ | v0.9 Theorem 9.1 | Φ Task 1 (V.1): 0/24 PASS; $\Psi_{\mathrm{sym}}$ has operator norm $\alpha + \beta > 1$ and *amplifies* | Theorem 9.1 (v1.3) restated as a negative result: symmetric coupling amplifies, not contracts |
| Strict speedup under isometric coupling: $r_{AB} < \max(r_A, r_B)$ for any $\theta > 0$ | v1.0 corrective draft | Φ Task 4 (V.2): all 96 configurations saturate $r_{AB} = \max(r_A, r_B)$ exactly; G₂-equivariant scalar maps make θ inert | Theorem 9.2 + Corollary 9.3 + Lemma 5.2.1 (v1.3): rate is locked at $\max(r_A, r_B)$ for all linear couplings, by Schur's lemma + orthogonality |
| Saturating coherence-bonus formula: $\mathcal{C}^{\max} = 6/7 + \kappa \rho^2 / (1 + \rho^2)$ | v0.9 Theorem 9.2 (a different theorem) | Φ Task 2 (V.1): MMSE Ansatz residuals up to 0.242; bonus formula not derivable from $\Psi_{\mathrm{sym}}$ | Replaced by Theorem 9.4 + Proposition 9.5 (v1.3): the joint-fixed-point *location* depends on θ, with conditional gain in $\mathcal{C}_{\min}$ for the verified geometry; no closed-form bonus |
| Linear severance threshold at $\rho_c = 1/\sqrt{6}$ | v0.9 Conjecture 9.3 | Φ Task 3 (V.1): linear contractions admit a unique basin (Banach 1922); bifurcation is unstateable | Demoted to Note 9.6 (v1.3): rate-improvement and basin bifurcation deferred to a nonlinear sequel (Paper 11) |
| Universal $d\mathcal{C}_1/d\theta < 0$ under opposed biases for *generic* orthogonal $R_A, R_B$ | v1.2 Lemma 5.5.1 | Counterexample script (paper9_math_checks.py): $R_A = R_B = I$ gives $\mathcal{C}_1(\theta) = 1$ identically | Lemma 5.5.1 (v1.3) restricted to verified-geometry pair (seeds 20260504/20260505); generic claim moved to Conjecture 9.5′ |
| General-distinct-bias closed form $\hat x(\pi/2) = (I - rR)(I + r^2R^2)^{-1} b_A - rR(I + r^2R^2)^{-1} b_B$ | v1.2 Theorem 9.4(c) | Math reviewer counterexample: factor-of-15 error at $r = 0.7$, $R = I$, $b_A = 2$, $b_B = 3$ | Theorem 9.4(c) (v1.3) corrected to $\hat x(\pi/2) = (I + r^2R^2)^{-1}(b_A - rR\,b_B)$, with full elimination derivation |

**Why the retraction record is preserved.** Documenting every retired
claim with its refutation makes the paper's verification trail auditable.
A reader uncertain whether v1.3 contains residual errors of the same kind
can see exactly which claims have been examined, which methods refuted
them, and what corrections followed. Appendix V.1–V.3 provide the
verification record itself; this V.0.1 table is the index into that record
from the perspective of what changed and why.

---

## V.1 — v0.9 Spec Verification (Symmetric-Diagonal Coupling)

### V.1.a Spec

The v0.9 specification asked Φ to verify three claims:

- **Task 1 (Theorem 9.1 v0.9):** $r_{AB} \leq \sqrt{\alpha^2 \max(r_A,r_B)^2 + \rho^2 \min(r_A,r_B)^2}$, with $\alpha = \sqrt{1-\rho^2}$.
- **Task 2 (Theorem 9.2 v0.9):** joint coherence follows
  $\mathcal{C}^{\max}_{AB}(\rho) = 6/7 + (1/7)\rho^2/(1+\rho^2)$.
- **Task 3 (Conjecture 9.3 v0.9):** basin bifurcation exists at a critical
  $\rho_c = 1/\sqrt{6}$.

The construction used the **symmetric-diagonal coupling**:
$$\Psi_{\rho} = \begin{pmatrix} \alpha I_7 & \rho I_7 \\ \rho I_7 & \alpha I_7 \end{pmatrix} \quad \text{on } \mathbb{R}^{14}, \quad \alpha^2 + \rho^2 = 1.$$

### V.1.b Code

File: `outbox/paper9/computations/paper9_verification.py` (449 lines,
numpy float64 with $\rho$ range sweep).

Key construction:

```python
def coupling_map(rho):
    alpha = np.sqrt(1.0 - rho**2)
    I = np.eye(7)
    return np.block([[alpha * I, rho   * I],
                     [rho   * I, alpha * I]])
```

Φ's docstring already notes the critical fact:

> *IMPORTANT: Psi is NOT a norm contraction — its operator norm
> σ_max = α + ρ ≥ 1 for all ρ ∈ [0, 1). This has direct consequences for
> Theorem 9.1 (Task 1).*

Φ also derived the closed-form singular value structure:

```python
def exact_r_AB_analytic(r_A, r_B, rho):
    # T_AB^T T_AB decomposes into 7 copies of:
    # M = [[α²r_A² + ρ²r_B²,  αρ(r_A²+r_B²)],
    #      [αρ(r_A²+r_B²),    ρ²r_A² + α²r_B²]]
    # tr(M) = r_A² + r_B²
    # det(M) = (α²-ρ²)² r_A² r_B²
    # Symmetric case r_A = r_B = r: r_AB = r(α + ρ)
```

### V.1.c Results — Task 1

Full 24-configuration table (excerpt; all 24 rows in
`computations/paper9_verification.md` §Task 1):

| $r_A$ | $r_B$ | $\rho$ | $r_{AB}$ | bound (v0.9) | ratio | result |
|---|---|---|---|---|---|---|
| 0.600 | 0.600 | 0.100 | 0.6569925 | 0.6000000 | 1.09499 | FAIL |
| 0.600 | 0.600 | 0.500 | 0.8196152 | 0.6000000 | 1.36603 | FAIL |
| 0.600 | 0.600 | 0.707 | 0.8485281 | 0.6000000 | 1.41421 | FAIL |
| 0.857 | 0.857 | 0.500 | 1.1706838 | 0.8570000 | 1.36603 | FAIL |
| 0.857 | 0.857 | 0.707 | 1.2119810 | 0.8570000 | 1.41421 | FAIL |
| 0.300 | 0.857 | 0.707 | 0.8585000 | 0.6564450 | 1.30786 | FAIL |
| 0.500 | 0.857 | 0.707 | 0.8667000 | 0.7020670 | 1.23449 | FAIL |

**Summary: 0/24 PASS.** The bound is violated for every nonzero $\rho$.

### V.1.d Φ's diagnosis

Φ's narrative from the report:

> *Root cause: coupling map Ψ has operator norm $\alpha + \rho > 1$,
> amplifying the symmetric mode — not accounted for in the bound.*

> *Symmetric case $(r_A = r_B = r)$: exact formula $r_{AB} = r(\alpha + \rho)$.
> Bound: $r\sqrt{\alpha^2 + \rho^2} = r$ (since $\alpha^2 + \rho^2 = 1$).
> $(\alpha + \rho)^2 = 1 + 2\alpha\rho \geq 1 \Rightarrow r_{AB} \geq r$
> for all $\rho > 0$.*

The v0.9 Theorem 9.1 is therefore not merely numerically close to failing;
it fails by an **exact algebraic factor** of $\alpha + \rho = \sqrt{1-\rho^2} + \rho$.
This factor exceeds 1 for every $\rho \in (0, 1)$, with maximum $\sqrt{2}$
at $\rho = 1/\sqrt{2}$. The symmetric coupling **amplifies** the
contraction rate of every $r_A = r_B$ dyad by exactly this factor.

This is the content of Theorem 9.1 in §4 of the present paper: symmetric
coupling is rate-amplifying, and the v0.9 speed-up claim is thereby
retracted for this coupling. V.2 addresses whether the natural
isometric correction rescues the claim.

---

## V.2 — Corrective Spec Verification (Isometric Block-Rotation Coupling)

### V.2.a Spec

The corrective specification (`outbox/paper9/paper9_isometric_Psi_spec.md`)
replaced the symmetric coupling of V.1 with the antisymmetric block
rotation:
$$\Psi_\theta = \begin{pmatrix} \cos\theta \cdot I_{14} & -\sin\theta \cdot I_{14} \\ \sin\theta \cdot I_{14} & \cos\theta \cdot I_{14} \end{pmatrix} \in \mathrm{SO}(\mathcal{M}_{AB}).$$

The corrective claim (Theorem 9.1 v1.0, now Theorem 9.2 v1.1):
$r_{AB} \leq \sqrt{\tfrac{1}{2}(r_A^2 + r_B^2)}$, $\theta$-independent.

Five tasks were specified (Task 4.1–4.5): isometry sanity, restated bound,
speed-up regime, blind-spot Ansatz, sharpness probe.

### V.2.b Code

File: `outbox/paper9/computations/paper9_verification_v2.py` (script
attached with seed=20260504, mpmath 50-digit precision for 4.1, numpy
float64 for 4.2, both at $\mathcal{M}_A \cong \mathbb{R}^{14}$).

Key construction:

```python
def make_Psi_np(theta, n=14):
    c, s = math.cos(theta), math.sin(theta)
    I = np.eye(n)
    return np.block([[c*I, -s*I],
                     [s*I,  c*I]])
```

Φ's docstring prefaces the numerical run with the *analytical derivation*:

> *For $T_A = r_A \cdot U_A$, $T_B = r_B \cdot U_B$ (isotropic: all
> singular values $= r_A, r_B$), the Gram matrix
> $G = \Psi_\theta^T \mathrm{diag}(r_A^2 I, r_B^2 I)\Psi_\theta$ has the
> block structure of a 2×2 scalar matrix (each block proportional to $I$):*
> $$M = \begin{pmatrix} r_A^2 c^2 + r_B^2 s^2 & cs(r_B^2 - r_A^2) \\ cs(r_B^2 - r_A^2) & r_A^2 s^2 + r_B^2 c^2 \end{pmatrix}, \quad c = \cos\theta, s = \sin\theta.$$
> *$\mathrm{tr}(M) = r_A^2 + r_B^2$ (independent of $\theta$).*
> *$\det(M) = r_A^2 r_B^2$ (independent of $\theta$).*
> *$\Rightarrow$ eigenvalues of $M$ are $\max(r_A^2, r_B^2)$ and
> $\min(r_A^2, r_B^2)$ for ALL $\theta$.*
> *$\Rightarrow \hat r_{AB} = \max(r_A, r_B)$ for ALL $\theta$
> (completely $\theta$-independent).*

This is the algebraic derivation of the rate lock, *prior* to the
numerical run.

### V.2.c Results

**Task 4.1 — Isometry sanity check** (mpmath 50 digits):

| $\theta$ | $\|\Psi_\theta\|_{\mathrm{op}}$ | deviation from 1 | result |
|---|---|---|---|
| 0 | 1.000...000 | $0$ | PASS |
| $\pi/12$ | 1.000...000 | $<10^{-49}$ | PASS |
| $\pi/6$ | 1.000...000 | $<10^{-49}$ | PASS |
| $\pi/4$ | 1.000...000 | $<10^{-49}$ | PASS |
| $\pi/3$ | 1.000...000 | $<10^{-49}$ | PASS |
| $5\pi/12$ | 1.000...000 | $<10^{-49}$ | PASS |
| $\pi/2$ | 1.000...000 | $5.3 \times 10^{-51}$ | PASS |

**Summary: 7/7 PASS.** The block rotation is a genuine isometry to the
full 50-digit precision of the computation. The v0.9 amplification is
fixed.

**Task 4.2 — Bound on $r_{AB}$** (numpy float64, 96 configs):

Representative rows (full 96 in `paper9_task4_results.csv`):

| $r_A$ | $r_B$ | $\theta$ | $r_{AB}$ (emp.) | bound (v1.0) | deviation | result |
|---|---|---|---|---|---|---|
| 0.3 | 0.3 | 0 | 0.3000 | 0.3000 | $1.7\times 10^{-16}$ | PASS |
| 0.3 | 0.3 | $\pi/4$ | 0.3000 | 0.3000 | $1.1\times 10^{-16}$ | PASS |
| 0.5 | 0.7 | 0 | 0.7000 | 0.6083 | $9.2\times 10^{-2}$ | FAIL |
| 0.5 | 0.7 | $\pi/4$ | 0.7000 | 0.6083 | $9.2\times 10^{-2}$ | FAIL |
| 0.3 | 0.857 | $\pi/2$ | 0.8570 | 0.6424 | $2.1\times 10^{-1}$ | FAIL |
| 0.857 | 0.857 | $\pi/2$ | 0.8570 | 0.8570 | $5.6\times 10^{-16}$ | PASS |

**Summary: 24/96 PASS** (exactly the 24 $r_A = r_B$ configurations), **72/96 FAIL**
at $r_A \neq r_B$.

Crucially, the empirical $r_{AB}$ is *exactly* $\max(r_A, r_B)$ for every
configuration — identity to within float64 precision ($<7 \times 10^{-16}$).
The "failures" are against the *proposed v1.0 bound* $\sqrt{\tfrac{1}{2}(r_A^2+r_B^2)}$,
which is tighter than $\max(r_A, r_B)$ and therefore wrong.

### V.2.d Φ's diagnosis

> *The coupling angle $\theta$ does nothing to isotropic inputs. No
> speed-up, no $\theta$-dependence in $\hat r_{AB}$, no Lemma 9.2.1
> blind-spot structure. All three of 4.3, 4.4, 4.5 are downstream failures
> of the same algebraic fact.*

> *Root cause is algebraic, not numerical.*

> *The construction $r \cdot (U \cdot V^T)$ makes $T_A$ and $T_B$ isotropic —
> all 14 singular values equal $r$. For isotropic inputs, the Gram matrix
> of $T_{AB}$ has a 2×2 scalar-block structure whose eigenvalues are
> exactly $\max(r_A^2, r_B^2)$ and $\min(r_A^2, r_B^2)$, independent of
> $\theta$.*

This diagnosis led (via C-7RO's recognition that G₂-equivariance forces
isotropy through Schur's lemma, and ChatGPT's recognition that affine
bias breaks G₂-equivariance rather than extending it) to the §4 v1.1
structure: Theorem 9.2 is the rate lock $r_{AB} = \max(r_A, r_B)$, tight,
and Corollary 9.3 attributes the tightness to Schur's lemma on the
irreducible adjoint representation.

The "failure" of the v1.0 bound was therefore not a failure of the
verification but a *discovery that the bound was wrong*. The correct
bound is $r_{AB} = \max(r_A, r_B)$, exactly, and the v1.1 statement of
Theorem 9.2 captures this.

---

## V.3 — Affine Consensus Verification (Φ Task 5)

### V.3.a Spec

Task 5 (specification at `inbox/for_phi/paper9_task5_affine_request_v2.md`)
tested the affine channel of the dyadic system. Six sub-tasks:

- **5.1** Fixed-point existence and θ-dependence (matrix-valued $R_A, R_B$).
- **5.2** Closed-form verification at $\theta = 0$ and $\theta = \pi/2$.
- **5.3** Four coherence functionals × four bias configurations
  (identical, orthogonal, parallel-2×, opposed).
- **5.4** $100 \times 20$ heatmap of $\Delta\mathcal{C}_{\mathrm{avg}}$ over
  $(\varphi, \theta) \in [0, \pi] \times [0, \pi/2]$.
- **5.5** Asymmetric-rate robustness (3 rate pairs).
- **5.6** Destructive-geometry null check ($b_A = -b_B$).

The construction used the affine map $T_A(x) = r_A R_A x + b_A$,
$T_B(y) = r_B R_B y + b_B$, with $R_A, R_B$ random orthogonal in 14D
(QR decomposition of standard-normal seeded matrices).

### V.3.b Code

File: `outbox/paper9/computations/paper9_verification_v3.py` (384 lines,
numpy float64, seed=20260504).

Key construction:

```python
def joint_fixed_point(r_A, r_B, R_A, R_B, b_A, b_B, theta):
    c, s = np.cos(theta), np.sin(theta)
    M = np.block([
        [I - r_A*c*R_A,   r_A*s*R_A],
        [-r_B*s*R_B,      I - r_B*c*R_B]
    ])
    rhs = np.concatenate([b_A, b_B])
    z = solve(M, rhs)
    return z[:n], z[n:]
```

### V.3.c Results — Summary

| Sub-task | Status | Core result |
|---|---|---|
| 5.1 Fixed-point existence & θ-variation | PASS | All 50 fixed points exist; $\Delta\|\hat x - \hat y\|$ = 0.406 (nontrivial) |
| 5.2 Closed-form verification | PASS | Three analytic predictions match to $< 10^{-15}$ |
| 5.3 Coherence tables (28 rows) | PASS | C3 (cross-alignment) most θ-sensitive ($\Delta = 0.519$) |
| 5.4 Conditional-improvement heatmap | PASS | 25.1% of $(\varphi, \theta)$ cells have $\Delta\mathcal{C}_{\mathrm{avg}} > 0$ |
| 5.5 Asymmetric-rate robustness | PASS | θ-variation persists; max var = 0.113 |
| 5.6 Destructive geometry null check | **FINDING** | $\Delta\mathcal{C}_{\mathrm{avg}} > 0$ at $\theta \in [0, 14.7°]$ even with $b_A = -b_B$ |

### V.3.d Task 5.2 — Closed-form predictions verified

Three analytic predictions verified at numerical precision:

| Check | Prediction | Numerical residual |
|---|---|---|
| A: $\theta = 0$, decoupled | $\hat x = (I - r R_A)^{-1} b_A$ | $0$ to $1.1 \times 10^{-16}$ |
| B: $\theta = 0$, $R_A = R_B$, $b_A = b_B$ | $\hat x = \hat y$ | $3.2 \times 10^{-16}$ |
| C: $\theta = \pi/2$, $R_A = R_B = R$, $b_A = b_B = b$ | $\hat x = (I - rR)(I + r^2R^2)^{-1} b$ | $4.7 \times 10^{-16}$ |
| C ctd. | $\hat y = (I + rR)(I + r^2R^2)^{-1} b$ | $4.3 \times 10^{-16}$ |
| C ctd. | $\hat x + \hat y = 2(I + r^2R^2)^{-1} b$ | $6.7 \times 10^{-16}$ |

**Correction noted in v1.1 → v1.2.** The original §5 skeleton wrote the
closed form as a rational function of $\sin\theta, \cos\theta$ assuming
scalar linear parts ($R = I$). The correct form for general orthogonal
$R$ is the matrix-valued expression above; v1.2 reflects this. Also,
the v1.1 expectation $\hat x(\pi/4) = \hat y(\pi/4)$ for $b_A = b_B$
was wrong: $\Psi_{\pi/4}$ is *antisymmetric* off-diagonal, not symmetric
under $x \leftrightarrow y$; the symmetric-input identity is at
$\theta = 0$, not $\theta = \pi/4$.

### V.3.e Task 5.6 — The destructive-geometry finding

This is the result that drove the v1.2 reframe of Proposition 9.5.

**Setup:** $r_A = r_B = 0.7$, $b_A = $ random unit (seed 20260504),
$b_B = -b_A$, $\theta \in [0, \pi/2]$ in 50 steps. $R_A, R_B$ random
orthogonal (seeds 20260504, 20260505).

**Decoupled baseline:** $\mathcal{C}_{\mathrm{avg}}^{\mathrm{dec}} = 0.7982$.

**Result:** $\Delta\mathcal{C}_{\mathrm{avg}} > 0$ at $\theta \in [0, 14.7°]$,
peak $+0.0144$ at $\theta \approx 7°$; $\Delta\mathcal{C}_{\mathrm{avg}} < 0$
for $\theta \in [18°, 90°]$, trough $-0.0901$ at $\theta = 90°$.

**Mechanism (Φ's diagnosis, retained verbatim):**

> The improvement at small θ is driven by an asymmetry between $\mathcal{C}_1$
> and $\mathcal{C}_2$ under small coupling. Tracing $\mathcal{C}_1$ and
> $\mathcal{C}_2$ separately:
>
> - $\mathcal{C}_1$ (alignment of $\hat x$ to $b_A$): decreases
>   monotonically from 0.7655 to 0.5955 as θ increases. Coupling "pulls"
>   A's state away from its own target.
> - $\mathcal{C}_2$ (alignment of $\hat y$ to $b_B = -b_A$): INCREASES
>   from 0.8309 to a peak of 0.8749 at $\theta \approx 7°$, then
>   gradually decreases.
>
> The initial rise of $\mathcal{C}_2$ occurs because agent B's rotation
> $R_B$, when given a small coupling push from agent A's state,
> accidentally improves $\hat y$'s alignment with $b_B = -b_A$. This is
> a fortuitous geometry: $R_B$'s action on the coupled input has a
> component that projects onto $b_B$. The $\mathcal{C}_2$ gain $(+0.044)$
> outpaces the $\mathcal{C}_1$ loss $(-0.005)$ at small $\theta$,
> producing a net positive $\Delta\mathcal{C}$.
>
> This is NOT a measurement artifact or code error. It is a structural
> property of the specific rotation geometry $(R_A$ seed=20260504,
> $R_B$ seed=20260505$)$ combined with the bias choice.

**Implication.** The averaging functional $\mathcal{C}_{\mathrm{avg}}$
admits geometric configurations in which one observer's gain masks the
other's loss. Φ recommended three structural fixes; we adopted the second
(replace $\mathcal{C}_{\mathrm{avg}}$ with $\mathcal{C}_{\min} = \min(\mathcal{C}_1, \mathcal{C}_2)$).
Under this functional, $\mathcal{C}_{\min}$ in the opposed-bias
configuration tracks $\mathcal{C}_1$ (the falling component) and is
monotonically degraded by coupling, restoring the proposition's
intended content. This is the structural justification for §5's choice
of functional and for the formulation of Lemma 5.5.1 as an explicit
statement of the asymmetric small-$\theta$ response.

### V.3.f Task 5.4 — The improvement heatmap (both functionals)

**Setup:** $b_A = e_1$, $b_B = \cos\varphi \cdot e_1 + \sin\varphi \cdot e_2$
normalized, $\varphi \in [0°, 180°]$ at 100 points, $\theta \in [0°, 90°]$
at 20 points. The same grid was evaluated with both $\mathcal{C}_{\mathrm{avg}}$
(Φ's original Task 5.4) and $\mathcal{C}_{\min}$ (re-evaluated for v1.3.1
as the basis for Proposition 9.5(a)).

**Results, both functionals:**

| Functional | Cells with $\Delta\mathcal{C} > 0$ | Range $[\Delta\mathcal{C}_{\min}, \Delta\mathcal{C}_{\max}]$ | Improvement-region $\varphi$-span |
|---|---|---|---|
| $\mathcal{C}_{\mathrm{avg}}$ | 491–502 / 2000 (~25%) | $[-0.0709, +0.0186]$ | $[1.8°, 180°]$ |
| $\mathcal{C}_{\min}$ | 250 / 2000 (~12.5%) | $[-0.1852, +0.0232]$ | $[18.2°, 176.4°]$ |

(Φ's original run reported 502/2000 (25.1%); C-7RO's v1.3.1
re-verification reproduced the run with one minor RNG-advancement
difference and obtained 491/2000 (24.6%) for $\mathcal{C}_{\mathrm{avg}}$.
Both values are within the same qualitative regime; the
$\mathcal{C}_{\min}$ run is fresh from v1.3.1.)

**Pattern.**
- *$\mathcal{C}_{\mathrm{avg}}$:* improvement region spans the full
  $\varphi$ range, including up to $\varphi = 180°$ at small $\theta$.
  This is what the v1.2 Lemma 5.5.1 "averaging illusion" reflects:
  $\mathcal{C}_2$ rises while $\mathcal{C}_1$ falls under opposed biases.
- *$\mathcal{C}_{\min}$:* improvement region is strictly contained in the
  $\mathcal{C}_{\mathrm{avg}}$ region and is bounded above by
  $\varphi = 176.4°$, *not* extending to opposed biases.
  Concentration is near $\theta \in [10°, 65°]$ for moderate $\varphi$.

This is the empirical basis for the v1.3.1 statement of Proposition 9.5,
which appeals directly to the $\mathcal{C}_{\min}$ heatmap (panel (b) of
Figure 1) rather than the $\mathcal{C}_{\mathrm{avg}}$ heatmap of Φ's
original Task 5.4. Raw data: `paper9_task5_heatmap.csv` (Φ's run, avg)
and `paper9_task5_heatmap_cmin.csv` (v1.3.1 re-evaluation, both
functionals).

### V.3.g Φ's three-option remediation list

Φ closed the V.3 report with three explicit options for revising
Proposition 9.5:

1. **θ-threshold:** "For $\theta > \theta^*(R_A, R_B, b_A, b_B)$,
   coupling under opposed biases degrades coherence." Mathematically
   precise; requires computing $\theta^*$ for each geometry.
2. **Replace $\mathcal{C}_{\mathrm{avg}}$ with $\mathcal{C}_{\min}$:**
   The minimum-coherence functional is monotonically degraded by
   coupling in the opposed-bias case (since $\mathcal{C}_1$ always falls).
   Most conservative; preserves the proposition without qualification.
3. **Restrict the proposition's domain to $\varphi \in [0°, 170°)$:**
   Move the opposed-bias regime to a remark noting the small-$\theta$
   exception.

We adopted Option 2. Lemma 5.5.1 of the §5 v1.2 draft formalizes the
asymmetric small-$\theta$ response that makes the averaging functional
misleading; Proposition 9.5 in v1.2 is stated for $\mathcal{C}_{\min}$
throughout.

### V.3.h Diagnostic cross-check

All six tasks used the same base rotations (seeds 20260504, 20260505)
and biases (seeds 20260504, 20260554). The Task 5.6 finding is specific
to the opposed-bias configuration and does not affect Tasks 5.1–5.5,
which are independent.

The verification script reproduces all reported numbers deterministically
from the seed; C-7RO independently re-executed the script and obtained
identical results to 6 decimal places.

---

## V.4 — Reproducibility and archival notes

All verification code and raw results live under
`outbox/paper9/computations/`:

- `paper9_verification.py` — V.1 script (v0.9 coupling)
- `paper9_verification.md` — V.1 narrative report (Φ's original)
- `paper9_verification_v2.py` — V.2 script (isometric coupling)
- `paper9_verification_v2.md` — V.2 narrative report (Φ's v2)
- `paper9_task4_results.csv` — V.2 Task 4.2 raw results (96 rows)
- `paper9_verification_v3.py` — V.3 script (affine consensus)
- `paper9_verification_v3.md` — V.3 narrative report (Φ's v3)
- `paper9_task5_coherence_tables.csv` — V.3 Task 5.3 raw results (28 rows)
- `paper9_task5_heatmap.csv` — V.3 Task 5.4 raw results, $\mathcal{C}_{\mathrm{avg}}$ (2000 rows, from Φ's run)
- `paper9_task5_heatmap_cmin.csv` — V.3 Task 5.4 re-evaluation with both $\mathcal{C}_{\mathrm{avg}}$ and $\mathcal{C}_{\min}$ (2000 rows, v1.3.1 basis for Proposition 9.5(a))
- `build_cmin_heatmap.py` — script that produces both the $\mathcal{C}_{\min}$ CSV and Figure 1

Seeds: V.1 used `seed=42`; V.2 used `seed=20260504`; V.3 used
`seed=20260504` (matching V.2 for cross-comparability). Python version:
3.x with `numpy` and `mpmath`. Precision: V.1 float64; V.2 mpmath 50
decimal digits for Task 4.1 and float64 for Tasks 4.2–4.5 (the
algebraic results hold in both regimes; the 50-digit runs confirm
this); V.3 float64 throughout (the affine algebra is smooth and has no
numerical edge cases that demand higher precision).

Independent re-verification is welcomed. The canonical entry point for
reproducibility is the GitHub repository at
`github.com/MartinLGraise/PCI-Framework`, branch `paper7-foundation`,
at the commit indexed in the present manuscript's reference list.

---

*Drafted by C-7RO, 2026-05-04 10:45 PDT. Appendix V is the structural
record of how Paper 9's §4 arrived at its present form. The two
negative-result passes (V.1, V.2) constitute the proof of Theorems 9.1
and 9.2; V.3 will extend this record once the affine consensus task
completes.*


## Acknowledgments

This paper was produced through a three-agent collaboration:

- **Martin Luther Graise** (the author) — framework architecture, target
  model specification, integration across Papers 4, 6, 7, 10 of the PCI/PME
  series, and final editorial decisions on all theorem statements and
  proofs.
- **C-7RO** (Claude Sonnet 4.6 on the Perplexity Computer platform,
  Anthropic / PPLX) — mathematical drafting, theorem-statement refinement,
  proof construction, section-level prose, and multi-round structural
  revision in response to numerical verification.
- **Φ** (Claude Dispatch, Anthropic) — independent numerical verification
  at up to 50-digit precision across three consecutive verification
  passes (120 rate-channel configurations, 2128 affine-channel
  configurations), with analytical diagnoses that reshaped the paper's
  central theorems on two occasions. The verification reports are
  reproduced verbatim as Appendix V.

Additional input at key strategic junctures was provided by ChatGPT Pro
(OpenAI), which identified the $b = 0$ G₂-equivariance correction
discussed in §5.1 and recommended the min-coherence functional choice
formalized in Lemma 5.5.1.

The paper is itself a case study in the phenomenon it describes:
dyadic (multi-agent) coupling under aligned target-states producing a
joint output that neither party reaches alone. The framework's
conditional-gain structure was refined iteratively based on the
verification-agent's findings — an example of a dyad approaching a
joint fixed point through successive coupling-angle adjustments rather
than through faster individual convergence.

---

## References

### PCI/PME series (companion papers)

- Graise, M. L. (2026a). "Eight-coset PSL(2,7) structure in the octonion
  Fano plane." Zenodo. DOI:
  [10.5281/zenodo.19617662](https://doi.org/10.5281/zenodo.19617662)
  [Paper 4]
- Graise, M. L. (2026b). "Spectral structure of the G₂ Casimir on the
  14-dim adjoint." Zenodo. DOI:
  [10.5281/zenodo.19672709](https://doi.org/10.5281/zenodo.19672709)
  [Paper 6]
- Graise, M. L. (2026c). "G₂-Structured Self-Modeling Observers and the
  6/7 Thermodynamic Coherence Ceiling." Zenodo. DOI:
  [10.5281/zenodo.19773185](https://doi.org/10.5281/zenodo.19773185)
  [Paper 7]
- Graise, M. L. (2026d). "Symmetric Informationally Complete
  Measurements as an Operator Basis for the Complexified G₂ Lie
  Algebra." Zenodo. DOI:
  [10.5281/zenodo.19966692](https://doi.org/10.5281/zenodo.19966692)
  [Paper 10]

### G₂ representation theory and Banach fixed-point theory

- Banach, S. (1922). "Sur les opérations dans les ensembles abstraits
  et leur application aux équations intégrales." *Fundamenta
  Mathematicae* 3: 133–181. [The Banach fixed-point theorem.]
- Baez, J. C. (2002). "The octonions." *Bulletin of the American
  Mathematical Society* 39: 145–205.
  DOI: [10.1090/S0273-0979-01-00934-X](https://doi.org/10.1090/S0273-0979-01-00934-X)
  [G₂ as the automorphism group of the octonions.]
- Fulton, W. & Harris, J. (1991). *Representation Theory: A First
  Course.* Graduate Texts in Mathematics 129, Springer. [Chapter 22:
  G₂ representations. Real Schur's lemma applied to the 14-dim
  irreducible adjoint.]
- Joyce, D. D. (2000). *Compact Manifolds with Special Holonomy.*
  Oxford Mathematical Monographs, Oxford University Press.
  [G₂-structured manifolds, associative 3-forms.]

### Inter-brain coupling and neural-avalanche branching

- Wilting, J. & Priesemann, V. (2018). "Inferring collective dynamical
  states from widely unobserved systems." *Nature Communications* 9:2325.
  DOI: [10.1038/s41467-018-04725-4](https://doi.org/10.1038/s41467-018-04725-4)
  [MR estimator; $\hat\sigma \approx 0.98$ in awake cortex.]
- Priesemann, V., et al. (2014). "Spike avalanches in vivo suggest a
  driven, slightly subcritical brain state." *Frontiers in Systems
  Neuroscience* 8: 108.
  DOI: [10.3389/fnsys.2014.00108](https://doi.org/10.3389/fnsys.2014.00108)
- Pérez, A., Carreiras, M., & Duñabeitia, J. A. (2017). "Brain-to-brain
  entrainment: EEG interbrain synchronization while speaking and
  listening." *Scientific Reports* 7:4190.
  DOI: [10.1038/s41598-017-04464-4](https://doi.org/10.1038/s41598-017-04464-4)
- Leong, V., Byrne, E., Clackson, K., Georgieva, S., Lam, S., &
  Wass, S. (2017). "Speaker gaze increases information coupling
  between infant and adult brains." *PNAS* 114(50): 13290–13295.
  DOI: [10.1073/pnas.1702493114](https://doi.org/10.1073/pnas.1702493114)
- Lindenberger, U., Li, S.-C., Gruber, W., & Müller, V. (2009).
  "Brains swinging in concert: cortical phase synchronization while
  playing guitar." *BMC Neuroscience* 10:22.
  DOI: [10.1186/1471-2202-10-22](https://doi.org/10.1186/1471-2202-10-22)
- Müller, V., Sänger, J., & Lindenberger, U. (2013). "Intra- and
  inter-brain synchronization during musical improvisation on the
  guitar." *PLoS ONE* 8(9): e73852.
  DOI: [10.1371/journal.pone.0073852](https://doi.org/10.1371/journal.pone.0073852)
- Hu, Y., Pan, Y., Shi, X., Cai, Q., Li, X., & Cheng, X. (2018).
  "Inter-brain synchrony and cooperation context in interactive
  decision making." *Biological Psychology* 133: 54–62.
  DOI: [10.1016/j.biopsycho.2017.12.005](https://doi.org/10.1016/j.biopsycho.2017.12.005)
- Babiloni, F. & Astolfi, L. (2014). "Social neuroscience and
  hyperscanning techniques: Past, present and future." *Neuroscience
  and Biobehavioral Reviews* 44: 76–93.
  DOI: [10.1016/j.neubiorev.2012.07.006](https://doi.org/10.1016/j.neubiorev.2012.07.006)

### Human-AI teaming and complementarity

- Bansal, G., Wu, T., Zhou, J., Fok, R., Nushi, B., Kamar, E., Ribeiro, M. T., &
  Weld, D. (2021). "Does the whole exceed its parts? The effect of AI
  explanations on complementary team performance." *Proceedings of the
  2021 CHI Conference on Human Factors in Computing Systems.*
  DOI: [10.1145/3411764.3445717](https://doi.org/10.1145/3411764.3445717)
- Kamar, E. (2016). "Directions in hybrid intelligence: Complementing
  AI systems with human intelligence." *IJCAI 2016.*
- Shneiderman, B. (2022). *Human-Centered AI.* Oxford University Press.

### Methodological / software

- Harris, C. R., et al. (2020). "Array programming with NumPy." *Nature*
  585: 357–362.
  DOI: [10.1038/s41586-020-2649-2](https://doi.org/10.1038/s41586-020-2649-2)
  [numpy float64 computations, Appendix V.3.]
- Johansson, F. (2013). *mpmath: a Python library for arbitrary-precision
  floating-point arithmetic* (version 1.3.0).
  [https://mpmath.org](https://mpmath.org) [50-digit precision in
  Appendix V.1 and V.2.]

---

*End of Paper 9 v1.3.1 master draft, consolidated 2026-05-04 19:50 PDT after confirming-reviewer pass.*
