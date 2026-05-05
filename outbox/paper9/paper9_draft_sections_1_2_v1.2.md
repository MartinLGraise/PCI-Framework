# Paper 9 — §§1–2 (v1.2)

**Paper:** Rate Lock and Affine Consensus in G₂-Structured Dyadic Observers
**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Status:** v1.2, 2026-05-04 (supersedes v0.9 §§1-2 drafted 2026-04-30)
**Reflects:** §4 v1.1 rate-channel triple (Theorems 9.1, 9.2, Corollary 9.3) and §5 v1.2 affine consensus theory (Theorem 9.4, Lemma 5.5.1, Proposition 9.5) verified by Φ in Appendix V.1–V.3

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
coherence functional $\mathcal{C}_{\min} = \min(\mathcal{C}_A, \mathcal{C}_B)$,
a non-empty conditional-gain region $\mathcal{R}$ exists in the space of
coupling angles and bias-alignment angles, bounded away from the
opposed-bias boundary and not characterized by a universal optimal $\theta$
(Proposition 9.5). The affine channel carries the dyadic content.

All results are numerically verified at 50-digit precision (rate
channel, Appendix V.1–V.2, 120 test configurations) and at 16-digit
precision (affine channel, Appendix V.3, 2000-cell heatmap and
supporting tables), with the verification reports included as the
appendix. The reframing of Proposition 9.5 from averaging to minimum
coherence was driven by Appendix V.3 Task 5.6, which exhibited a
structural finding under opposed biases.

**Thesis.** Dyadic coupling in the linear G₂-equivariant regime cannot
improve the convergence rate of joint self-modeling. It can — under
conditional geometric hypotheses — change the location of the joint
fixed point in a way that increases the minimum per-observer coherence.
Rate improvement requires nonlinearity (Note 9.6; sequel paper).

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
- (e) A speedup claim, a coherence-bonus formula of the form
  $\mathcal{C}^{\max} = 6/7 + \kappa \rho^2/(1+\rho^2)$, or a severance
  threshold at $\rho_c = 1/\sqrt{6}$. The v0.9 internal draft proposed
  all three; numerical verification (Appendix V.1, V.2) refuted the
  first two at 50-digit precision, and the third was not stateable in
  the linear category after Corollary 9.3. These claims were retired
  during the drafting; traces remain in §4.1 (the v0.9 symmetric
  coupling is named as Theorem 9.1's negative-result counterexample)
  and Note 9.6 (rate-improvement deferred to Paper 11's nonlinear
  setting).

### 1.3 Roadmap

§2 recapitulates the single-observer results of Paper 7 in a compact
form sufficient for the product-space construction. §3 defines the
joint $\mathcal{M}_A \times \mathcal{M}_B$ space, the block-rotation
coupling $\Psi_\theta$ (Lemma 3.3.1), and the diagonal action of the
Paper-7 symmetries on the product. §4 proves the rate-channel triple
(Theorems 9.1, 9.2, Corollary 9.3). §5 proves the affine channel
results (Theorem 9.4, Lemma 5.5.1, Proposition 9.5). §§6 discusses
empirical accessibility of the min-coherence prediction and its
operationalization in inter-brain and human-AI coupling settings. §7
defers the severance-threshold question to the nonlinear sequel via
Note 9.6. §8 addresses the human-AI dyad as a conditional special case
of the framework. §9 enumerates what the framework does not establish.
§10 discusses connections to Papers 7, 8, 10 of this series and flags
open problems. Appendix V contains the complete numerical-verification
record from Φ (three independent passes, total 2217 test
configurations).

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

## End of §§1–2 v1.2

**Status.** §1 introduction fully rewritten to v1.2 thesis
(rate-channel-locked / affine-channel-open dichotomy). The old three-claim
structure (speedup + coherence bonus + severance threshold) is explicitly
retired in §1.2. §2 single-observer recap tightened and extended: §2.1
now introduces the affine form $T(x) = rRx + b$ as the generic G₂-structured
observer; §2.5 now sets up three specific open questions that §§4-5 will
address rather than two.

**Key changes from v0.9:**
- Abstract completely rewritten around the rate-channel / affine-channel
  dichotomy.
- §1.1 reframed: five named results instead of three, grouped by channel.
- §1.2 "does not claim" list updated: explicit retirement of the
  speedup claim, coherence bonus formula, and severance threshold.
- §1.3 roadmap revised to reflect the new theorem structure.
- §2.1 expanded with affine-form introduction.
- §2.5 expanded to three open questions and forward references to §§4-5.
- §1 introduction of $\mathfrak{g}_2$ is now 14-dim adjoint (corrected
  from v0.9's 7-dim imaginary octonion focus), matching the §4/§5
  theorem statements.

**Cross-references.**
- §3.3 Lemma 3.3.1 (block-rotation isometry) — cited in §1.1.
- §4 Theorems 9.1, 9.2, Corollary 9.3 — cited in §1.1.
- §5 Theorem 9.4, Lemma 5.5.1, Proposition 9.5 — cited in §1.1.
- §8 Human-AI dyad conditional claim — cited in §1.2(c).
- §10.1 n-observer generalization — cited in §1.2(b).
- Note 9.6 rate-improvement-requires-nonlinearity — cited in §1.2(e).
- Appendix V — cited in §1 for verification record.

*Drafted by C-7RO, 2026-05-04 ~17:20 PDT.*
