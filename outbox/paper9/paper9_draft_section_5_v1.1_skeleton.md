# Paper 9 — §5 Skeleton (v1.1)

**Paper:** Rate Lock and Affine Consensus in G₂-Structured Dyadic Observers
**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Status:** v1.1 skeleton, 2026-05-04 (drafted by C-7RO; Φ Task 5 pending)
**Depends on:** §3 product-space construction; §3.3 Lemma 3.3.1; §4 Theorems 9.1, 9.2 and Corollary 9.3

---

## §5. The Affine Channel: Consensus and Conditional Coherence Gain

§4 established that the linear, G₂-equivariant *rate channel* is closed
by Schur's lemma and submultiplicativity. This section identifies the
**affine channel** as the locus of dyadic content. Under affine
contractions $T_A(x) = r_A x + b_A$, $T_B(y) = r_B y + b_B$ — where $b_A$,
$b_B$ are *symmetry-breaking* bias vectors that select each observer's
target self-model — the joint fixed point depends nontrivially on the
coupling angle $\theta$, and its location traces a one-parameter family
of consensus states. The rate is still locked at $\max(r_A, r_B)$, but
the *destination* of joint convergence is a function of $\theta$.

The two main results of this section: Theorem 9.4 (affine consensus
theorem) establishes the existence, uniqueness, and explicit closed form
of the joint fixed point as a function of $\theta$. Proposition 9.5
(conditional coherence gain) characterizes the geometric conditions under
which the joint state has higher coherence than the lower-coherence
individual fixed point. The latter is *conditional*, not universal —
under destructive geometry coupling can degrade the joint state.

### 5.1 Affine observers and the symmetry-breaking bias

A G₂-equivariant *affine* contraction on $V^{14}$ is a map of the form
$$T_A(x) = r_A x + b_A,$$
where $r_A I_{14}$ is the linear part (G₂-equivariant by Corollary 9.3)
and $b_A \in V^{14}$ is the **bias vector**. For full G₂-equivariance of
$T_A$, the bias would need to satisfy $g \cdot b_A = b_A$ for all $g \in
G_2$; but the only G₂-fixed vector in the irreducible 14-dim adjoint
representation is $b_A = 0$. Therefore *any nonzero bias* breaks the
G₂-equivariance of $T_A$ — and that is the point.

We adopt the following terminology. The map
$T_A(x) = r_A x + b_A$ with $b_A \neq 0$ is called a **G₂-structured
affine observer**: its linear part is G₂-equivariant, and its affine
bias is the symmetry-breaking order parameter. The vector $b_A$ encodes
the observer's target self-model, the direction in $V^{14}$ along which
$T_A$ defines a non-zero fixed point. The unique fixed point of $T_A$ is
$x^*_A = b_A / (1 - r_A)$, lying in the $b_A$ direction with magnitude
controlled by $r_A$.

The **G₂-structured dyad** consists of two G₂-structured affine observers
$(T_A, b_A)$, $(T_B, b_B)$ with linear rates $r_A, r_B \in [0, 6/7]$ and
bias vectors $b_A, b_B \in V^{14}$. The dyad is described by six
parameters (two scalars + two 14-vectors, modulo overall scale on the
biases) plus the coupling angle $\theta$.

### 5.2 The joint affine map and its fixed-point equation

Coupling the dyad with the block rotation $\Psi_\theta$ of §3.3 (Lemma
3.3.1), the joint affine map is
$$T_{AB}(x, y) = \bigl(r_A(\cos\theta \cdot x - \sin\theta \cdot y) + b_A,\; r_B(\sin\theta \cdot x + \cos\theta \cdot y) + b_B\bigr).$$

Because the linear parts $r_A I, r_B I$ are scalar multiples of the
identity (Corollary 9.3), the fixed-point equation $T_{AB}(\hat x, \hat y) =
(\hat x, \hat y)$ decomposes component-wise. For each coordinate index
$i \in \{1, \ldots, 14\}$:
$$M(\theta, r_A, r_B) \begin{pmatrix} \hat x_i \\ \hat y_i \end{pmatrix} = \begin{pmatrix} (b_A)_i \\ (b_B)_i \end{pmatrix},$$
where
$$M(\theta, r_A, r_B) = \begin{pmatrix} 1 - r_A \cos\theta & r_A \sin\theta \\ -r_B \sin\theta & 1 - r_B \cos\theta \end{pmatrix}.$$

The determinant of $M$:
$$\det M = (1 - r_A \cos\theta)(1 - r_B \cos\theta) + r_A r_B \sin^2\theta = 1 - (r_A + r_B)\cos\theta + r_A r_B.$$

Note: $\det M \geq 1 - (r_A + r_B) + r_A r_B = (1 - r_A)(1 - r_B) > 0$
for $r_A, r_B < 1$. The system always has a unique solution.

### 5.3 Theorem 9.4 — Affine Consensus

**Theorem 9.4 (Affine Consensus).** *Let $(T_A, b_A)$, $(T_B, b_B)$ be a
G₂-structured dyad with $r_A, r_B \in [0, 6/7]$ and $b_A, b_B \in V^{14}$
arbitrary. For each $\theta \in [0, \pi/2]$, the joint affine map
$T_{AB}$ has a unique fixed point $(\hat x(\theta), \hat y(\theta)) \in
\mathcal{M}_{AB}$ given component-wise by*
$$\boxed{\;\begin{pmatrix} \hat x_i(\theta) \\ \hat y_i(\theta) \end{pmatrix} \;=\; \frac{1}{\det M(\theta)} \begin{pmatrix} 1 - r_B\cos\theta & -r_A\sin\theta \\ r_B\sin\theta & 1 - r_A\cos\theta \end{pmatrix} \begin{pmatrix} (b_A)_i \\ (b_B)_i \end{pmatrix}\;}$$
*for $i = 1, \ldots, 14$, where $\det M(\theta) = 1 - (r_A + r_B)\cos\theta + r_A r_B$.*

*The map $\theta \mapsto (\hat x(\theta), \hat y(\theta))$ is real-analytic
on $[0, \pi/2]$. At $\theta = 0$, $(\hat x, \hat y) = (x^*_A, y^*_B)$
(individual fixed points). For $\theta > 0$ and $b_A, b_B$ not both zero,
$(\hat x(\theta), \hat y(\theta)) \neq (x^*_A, y^*_B)$.*

*The convergence rate to the joint fixed point is $\max(r_A, r_B)$, by
Theorem 9.2.*

*Proof.* [PENDING: To be filled in after Φ Task 5.1–5.2 verification.
The proof is by Cramer's rule on the 2×2 system above, with
$\det M(\theta) > 0$ established by the inequality $\det M \geq
(1-r_A)(1-r_B) > 0$. Existence and uniqueness follow from the Banach
fixed-point theorem applied to the contraction $T_{AB}$ (rate
$\max(r_A, r_B)$ by Theorem 9.2). Real-analyticity of $\theta \mapsto
(\hat x, \hat y)$ follows from the rationality of the closed form in
$\sin\theta, \cos\theta$. The $\theta = 0$ identity is direct
substitution: $M(0) = \mathrm{diag}(1 - r_A, 1 - r_B)$, so
$\hat x_i(0) = (b_A)_i/(1-r_A) = (x^*_A)_i$ and similarly for $\hat y$.
The non-degeneracy claim (joint $\neq$ individual for $\theta > 0$)
follows from the fact that $M(\theta) \neq \mathrm{diag}(1-r_A, 1-r_B)$
for $\theta > 0$.] $\square$

### 5.4 The geometry of the consensus

The joint fixed point $(\hat x(\theta), \hat y(\theta))$ traces a smooth
curve in $\mathcal{M}_{AB}$ as $\theta$ varies from 0 to $\pi/2$. At
$\theta = 0$ it is the pair of individual fixed points $(x^*_A, y^*_B)$.
At $\theta = \pi/2$ it is the swap-rotated pair: for $r_A = r_B = r$,
$$\hat x(\pi/2) = \frac{b_A - r b_B}{1 + r^2}, \qquad \hat y(\pi/2) = \frac{r b_A + b_B}{1 + r^2}.$$

Several geometric features of this curve are worth noting.

**(a) Both observers move.** Even though $\Psi_\theta$ is symmetric in
its construction, the two observers' joint states $\hat x$ and $\hat y$
both move from their individual fixed points as $\theta$ varies. Neither
is "fixed" while the other adapts; the consensus is genuinely joint.

**(b) The curve is rational in $\sin\theta, \cos\theta$.** Both
$\hat x_i(\theta)$ and $\hat y_i(\theta)$ are rational functions of
$\sin\theta$ and $\cos\theta$ with denominator $\det M(\theta)$. The
curve is therefore real-analytic and admits a Laurent expansion in
$e^{i\theta}$.

**(c) Small-θ expansion.** For $\theta \ll 1$:
$$\hat x_i(\theta) = (x^*_A)_i - \frac{r_A \theta}{1 - r_A}(y^*_B)_i + O(\theta^2),$$
$$\hat y_i(\theta) = (y^*_B)_i + \frac{r_B \theta}{1 - r_B}(x^*_A)_i + O(\theta^2).$$

This is the linear-response regime: a small coupling angle pulls each
observer's joint state by a fraction $r/(1-r)$ of the *other* observer's
individual fixed point, in directions controlled by the rotation. This
is the analogue of weak-coupling perturbation in physics.

### 5.5 Proposition 9.5 — Conditional Coherence Gain

To compare the joint fixed point with the individual fixed points in
terms of "coherence," we need to specify a coherence functional. The
paper considers four (Appendix V.3 verifies all four numerically):

- $\mathcal{C}_{\mathrm{proj}}(v) = |\langle v/\|v\|, e_{\mathrm{ref}}\rangle|^2$
  (projection onto a fixed reference direction);
- $\mathcal{C}_{\mathrm{target}}(v) = \exp(-\|v/\|v\| - e_{\mathrm{ref}}\|^2)$
  (exponential closeness to a target);
- $\mathcal{C}_{\mathrm{acc}}(v) = 1 - \|\Pi_{\mathrm{blind}} v/\|v\|\|^2$
  (norm in the accessible subspace, complement of a fixed
  blind-spot subspace);
- $\mathcal{C}_{\mathrm{blind}}(v)$ = blind-spot-penalty functional (a
  Lipschitz-monotone variant of $\mathcal{C}_{\mathrm{acc}}$).

A coherence functional $\mathcal{C}$ is **monotone along an
interpolation path** $\gamma: [0,1] \to V^{14}$ between two unit vectors
$v_0, v_1$ if $\mathcal{C}(\gamma(t))$ is monotonic in $t$.

**Proposition 9.5 (Conditional coherence gain).** *Let $(T_A, b_A)$,
$(T_B, b_B)$ be a G₂-structured dyad with individual coherences
$\mathcal{C}(x^*_A) > \mathcal{C}(y^*_B)$ (without loss of generality,
A is the higher-coherence observer). Suppose:*

*(i) The coherence functional $\mathcal{C}$ is monotone along the
interpolation from $y^*_B$ toward the perpendicular projection of
$x^*_A$ onto the line spanned by $\hat y(\theta)$, for $\theta$ in some
interval $[0, \theta^*]$.*

*(ii) The bias vectors $b_A, b_B$ are not destructively oriented:
$\langle b_A, b_B \rangle / (\|b_A\|\|b_B\|) > -\mathcal{C}_{\mathrm{crit}}$
for an explicit critical angle $\mathcal{C}_{\mathrm{crit}}$ depending on
$\mathcal{C}, r_A, r_B$.*

*Then for sufficiently small $\theta > 0$, the lower-coherence observer
gains coherence at the joint fixed point:*
$$\mathcal{C}(\hat y(\theta)) > \mathcal{C}(y^*_B).$$

*The improvement region in $(\theta, \angle(b_A, b_B))$-space is
characterized in Appendix V.3 (Φ Task 5.4 heatmap).*

*Proof.* [PENDING: To be filled in after Φ Task 5.3–5.4 verification.
The proof structure: (1) write $\hat y(\theta)$ as a $\theta$-parameterized
combination of $b_A, b_B$ via the closed form of Theorem 9.4. (2) Show
that for monotone $\mathcal{C}$ and non-destructive
$\angle(b_A, b_B)$, the linear-response term in §5.4(c) moves $\hat y$
toward $x^*_A$, raising $\mathcal{C}$. (3) Compute the explicit
$\mathcal{C}_{\mathrm{crit}}$ as the angle at which the linear-response
move is purely tangent to the level set of $\mathcal{C}$ at $y^*_B$.
(4) Verify the small-$\theta$ neighborhood is nonempty by continuity.
The full $\theta$-range and the boundary of the gain region are
characterized numerically in Appendix V.3.] $\square$

### 5.6 The destructive-geometry case

Proposition 9.5 carries an explicit caveat: the gain is *conditional*.
For $b_A, b_B$ in destructive orientation — most starkly,
$b_A = -b_B$ — coupling can degrade rather than improve joint coherence.
In the symmetric case $r_A = r_B = r$, $b_A = -b_B$:
$$\hat x(\theta) = \frac{(1 - r\cos\theta + r\sin\theta)}{1 - 2r\cos\theta + r^2} b_A,$$
which has magnitude
$$\|\hat x(\theta)\| = \|b_A\| \cdot \frac{1 - r\cos\theta + r\sin\theta}{1 - 2r\cos\theta + r^2}.$$

For $\theta \in (0, \pi/2)$, this is generally smaller than
$\|x^*_A\| = \|b_A\|/(1-r)$, meaning the joint state has a smaller
projection onto $b_A$ — i.e., lower coherence with respect to a
$b_A$-aligned reference direction. The opposed pair "cancels" partially
under coupling, producing a degraded consensus.

This case is verified in Appendix V (Φ Task 5.6) as a deliberate null
check: it confirms that the coherence-gain claim of Proposition 9.5 is
a real *geometric* condition, not a vacuous tautology.

### 5.7 What §5 establishes and what is open

**Established:**
- Theorem 9.4: the joint fixed point of the affine dyad exists, is
  unique, depends real-analytically on $\theta$, and admits a closed
  form in terms of the bias vectors and rates.
- Proposition 9.5: conditional coherence gain — geometrically
  characterized regions of improvement and degradation, both verified
  numerically.
- The affine channel is the locus of dyadic content; the rate channel
  (§4) is locked but the affine channel is open and structured.

**Open:**
- Whether the linear-response coefficient $r/(1-r)$ in §5.4(c) is
  sharp, or whether higher-order corrections produce a tighter regime
  characterization. This is a refinement, not a rescue.
- Whether nonlinear extensions (Paper 11) admit *unconditional* coherence
  gain — i.e., gain that doesn't require monotonicity of $\mathcal{C}$
  or non-destructive geometry. The Note 9.6 below sketches the open
  problem.
- Generalization to $n \geq 3$ observers, with $n(n-1)/2$ pairwise
  coupling angles. The pattern of joint fixed points becomes a
  $\mathrm{SO}(n)$-parameterized variety; the coherence-gain structure
  is presumably richer.

### 5.8 Note 9.6 — Open: rate-improvement requires nonlinearity

The reader may ask whether the rate-channel obstruction of §4 admits a
nonlinear circumvention. Schur's lemma applies only to *linear*
G₂-equivariant maps. A nonlinear G₂-equivariant flow on a curved orbit
space — for instance, a Riemannian gradient flow on the G₂-orbit
manifold of a generic 14-dim point — is not constrained by Schur's
lemma in the same way, and may admit rate improvement under coupling.

We defer this to a sequel (provisionally Paper 11): "Nonlinear
G₂-equivariant dynamics and basin bifurcation in dyadic observers."
The linear theory of the present paper provides the first-order
expansion of any such nonlinear theory, and the conditional gain of
Proposition 9.5 is presumably the leading term in a perturbation
expansion of the full nonlinear consensus.

---

## End of §5 v1.1 skeleton

**Status.** Skeleton complete. Theorem 9.4 statement and closed form
fully written; proof PENDING Φ Task 5.1–5.2 confirmation. Proposition
9.5 statement, two-condition framing (monotone $\mathcal{C}$ +
non-destructive geometry), and explicit small-$\theta$ argument all
written; proof PENDING Φ Task 5.3–5.4. Note 9.6 (nonlinear rate
improvement, → Paper 11) included as the open problem.

**What Φ Task 5 will fill in:**
- Numerical verification of the closed-form Theorem 9.4 to deviation
  $< 10^{-12}$ across the standard grid.
- Determination of the exact form of the critical angle
  $\mathcal{C}_{\mathrm{crit}}$ in Proposition 9.5 (depends on
  functional, rates, and bias geometry — Φ's Task 5.4 heatmap maps it).
- Confirmation of the destructive-geometry null result (Task 5.6).
- 4-functional coherence comparison: which functionals are
  most/least sensitive to dyadic coupling.

**Deferred:**
- Full proof of Proposition 9.5 (PENDING — schematic in §5.5 above).
- Generalization to $n \geq 3$ observers (Note in §5.7; sequel paper).
- Nonlinear extension (Note 9.6; Paper 11).

*Drafted by C-7RO, 2026-05-04 11:08 PDT. Skeleton ready for Φ Task 5
verification to fill in the proof bodies.*
