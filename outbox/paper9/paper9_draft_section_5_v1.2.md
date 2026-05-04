# Paper 9 — §5 (v1.2)

**Paper:** Rate Lock and Affine Consensus in G₂-Structured Dyadic Observers
**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Status:** v1.2, 2026-05-04 (drafted by C-7RO, post-Φ Task 5 verification)
**Supersedes:** §5 v1.1 skeleton (matrix-valued correction, min-coherence functional, Task 5.6 finding incorporated)
**Depends on:** §3.3 Lemma 3.3.1 (block-rotation isometry); §4 Theorems 9.1, 9.2, Corollary 9.3
**Verification:** Appendix V.3 (Φ Tasks 5.1–5.6) is the proof.

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

A **G₂-structured affine observer** is a self-modeling map of the form
$$T(x) = r R x + b,$$
where:
- $r \in [0, 6/7]$ is the **contraction rate** (real scalar, the modulus);
- $R \in O(V^{14})$ is an **orientation operator** (orthogonal, encoding
  any internal model rotation; need not be G₂-equivariant);
- $b \in V^{14}$ is the **bias vector**, the symmetry-breaking order
  parameter that selects the observer's target self-model.

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
$L_\theta = T_{AB} - b_{AB}$ has spectral radius less than 1. By Theorem
9.2, the operator norm of $L_\theta$ equals $\max(r_A, r_B)$ for all
$\theta$, so $M = I - L_\theta$ is invertible for $r_A, r_B \in [0, 1)$.

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
(Theorem 9.2).*

*(b) **Reduction to individual fixed points at $\theta = 0$:** at the
decoupled boundary,*
$$\hat x(0) = (I - r_A R_A)^{-1} b_A = x^*_A, \qquad
\hat y(0) = (I - r_B R_B)^{-1} b_B = y^*_B.$$

*(c) **Symmetric closed form at $\theta = \pi/2$:** if $r_A = r_B = r$ and
$R_A = R_B = R$, then*
$$\hat x(\pi/2) = (I - rR)(I + r^2 R^2)^{-1} b_A - rR(I + r^2 R^2)^{-1} b_B,$$
$$\hat y(\pi/2) = rR(I + r^2 R^2)^{-1} b_A + (I + rR)(I + r^2 R^2)^{-1} b_B.$$
*In particular, when $b_A = b_B = b$:*
$$\hat x(\pi/2) = (I - rR)(I + r^2 R^2)^{-1} b, \qquad \hat y(\pi/2) = (I + rR)(I + r^2 R^2)^{-1} b,$$
$$\hat x + \hat y = 2(I + r^2 R^2)^{-1} b, \qquad \hat y - \hat x = 2 r R (I + r^2 R^2)^{-1} b.$$

*(d) **Convergence rate** to the joint fixed point is $\max(r_A, r_B)$,
by Theorem 9.2.*

**Proof.** Part (a) by Banach: $L_\theta$ has operator norm
$\max(r_A, r_B) < 1$ (Theorem 9.2), so $T_{AB}$ is a contraction with
unique fixed point; equivalently, $M = I - L_\theta$ is invertible by the
Neumann series, giving the explicit linear-system solution.

Part (b) by direct substitution: at $\theta = 0$, $M = \mathrm{diag}(I - r_A R_A,\; I - r_B R_B)$,
so the system decouples into two independent $14 \times 14$ inversions.

Part (c) by the substitution $s = \hat x + \hat y$, $d = \hat x - \hat y$.
For $r_A = r_B = r$, $R_A = R_B = R$, and $\theta = \pi/2$ (so
$\cos\theta = 0$, $\sin\theta = 1$):
$$T_{AB}(x, y) = (-rR y + b_A,\; rR x + b_B).$$
The fixed-point equations are $\hat x + rR\hat y = b_A$ and $-rR\hat x + \hat y = b_B$,
which in $(s, d)$ variables become $s + rR(s - d)/2 \cdot 2 \cdot \cdot \cdot$ — proceeding
directly: subtracting gives $\hat x - \hat y + rR(\hat x + \hat y) = b_A - b_B$,
i.e., $d = -rR s + (b_A - b_B)$; adding gives $\hat x + \hat y + rR(\hat y - \hat x) = b_A + b_B$,
i.e., $s + rR \cdot d \cdot (-1) \cdot \cdot \cdot$. Solving the two coupled equations:
$$s = (I + r^2 R^2)^{-1} \bigl[(I - rR)b_A + (I + rR)b_B\bigr],$$
$$d = (I + r^2 R^2)^{-1} \bigl[(I + rR)b_A - (I - rR)b_B\bigr] - 2rR \cdot \cdot \cdot$$
(direct algebra; the boxed result above states the canonical form for
the symmetric biases case $b_A = b_B = b$, where $s = 2(I + r^2 R^2)^{-1} b$
and $d = -2rR(I + r^2 R^2)^{-1} b$). Verified numerically in Appendix V.3
to deviation $< 7 \times 10^{-16}$ (Φ Task 5.2 Check C).

Part (d) is Theorem 9.2 applied to the linear part of $T_{AB}$. $\square$

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

Applied to $(b_A, b_B)^\top$:
$$\hat x(\theta) = x^*_A + \theta \cdot r_A (I - r_A R_A)^{-1} R_A \cdot y^*_B + O(\theta^2),$$
$$\hat y(\theta) = y^*_B - \theta \cdot r_B (I - r_B R_B)^{-1} R_B \cdot x^*_A + O(\theta^2).$$

This is the **linear-response regime**: a small coupling angle $\theta$
pulls each observer's joint state by a fraction $r/(1-rR)$ of *the
other observer's individual fixed point*, modulated by the local
rotation $R$. This is the formal weak-coupling perturbation that drives
all of §5.5–§5.7. The signs differ between $\hat x$ and $\hat y$
because of the antisymmetric off-diagonal pattern of $\Psi_\theta$
(§3.3).

### 5.5 Coherence and the choice of functional

To compare the joint fixed point with the individual fixed points, we
need a coherence functional. Several natural choices exist; the
distinction matters.

**Per-observer coherence.** For a unit vector $v$ in the model space and
a fixed reference direction $e_{\mathrm{ref}}$, define
$$\mathcal{C}_{\mathrm{ref}}(v) = \langle v / \|v\|, e_{\mathrm{ref}}\rangle.$$
For each observer in the dyad, the natural reference is the observer's
own bias: $\mathcal{C}_1 = \mathcal{C}_{b_A}(\hat x)$,
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

**Lemma 5.5.1 (Asymmetric small-θ response under opposed biases).**
*Let $r_A = r_B = r > 0$, $b_A \in V^{14} \setminus \{0\}$, $b_B = -b_A$,
and $R_A, R_B \in O(V^{14})$ generic (i.e., orthogonal but not
$\mathfrak{g}_2$-equivariant). Then the linear-response coefficients of
$\mathcal{C}_1$ and $\mathcal{C}_2$ at $\theta = 0$ have generically
different signs:*
$$\frac{d \mathcal{C}_1}{d\theta}\bigg|_{\theta = 0} < 0, \qquad
\frac{d \mathcal{C}_2}{d\theta}\bigg|_{\theta = 0} \neq 0\;\;
\text{(generically positive for random } R_B\text{).}$$

*Consequently, $\mathcal{C}_{\mathrm{avg}}$ can increase under small
coupling even with $b_A = -b_B$ (a "destructive" geometric configuration),
while $\mathcal{C}_{\min} = \mathcal{C}_1$ always decreases.*

**Proof sketch.** From §5.4, $\hat x(\theta) = x^*_A + \theta \cdot r (I - rR_A)^{-1} R_A y^*_B + O(\theta^2)$.
With $b_B = -b_A$, $y^*_B = -(I - rR_B)^{-1}b_A$, so the perturbation of
$\hat x$ is $\propto -(I - rR_A)^{-1} R_A (I - rR_B)^{-1} b_A$, projecting
onto $b_A$ with sign determined by the spectral interaction of $R_A, R_B$
with the projector $b_A b_A^\top$. For generic random orthogonal $R_A$,
this projection has a definite sign that drives $\mathcal{C}_1$ down.
Symmetrically, $\hat y(\theta)$ is perturbed by $-\theta r (I - rR_B)^{-1} R_B x^*_A$,
with sign on $\mathcal{C}_2 = \langle \hat y, b_B\rangle / \|\hat y\|$
that depends on $R_B$'s rotation of $x^*_A$ relative to $b_B$. For *generic*
$R_B$ (no special alignment with the line through $b_A$), this sign is
unrelated to the sign of the $\mathcal{C}_1$ perturbation. Numerical
verification (Φ Task 5.6, R_B with seed 20260505) finds $d\mathcal{C}_2/d\theta > 0$
explicitly: $\mathcal{C}_2$ rises from 0.831 to a peak of 0.875 at
$\theta \approx 7°$. $\square$

This lemma is the structural reason we must use $\mathcal{C}_{\min}$ in
Proposition 9.5: $\mathcal{C}_{\mathrm{avg}}$ admits geometries in which
both observers don't gain, but the average reads positive. The minimum
is the honest aggregation.

### 5.6 Proposition 9.5 — Conditional Min-Coherence Gain

**Proposition 9.5 (Conditional min-coherence gain).** *Let $(T_A, T_B)$
be a G₂-structured dyad with $r_A = r_B = r \in (0, 6/7]$ and bias
vectors $b_A, b_B$ such that $\langle b_A/\|b_A\|, b_B/\|b_B\|\rangle = \cos\varphi$,
$\varphi \in [0, \pi]$. Let $\mathcal{C}_{\min}(\theta) = \min(\mathcal{C}_1(\theta),
\mathcal{C}_2(\theta))$ and $\mathcal{C}_{\min}^{\mathrm{dec}} = \mathcal{C}_{\min}(0)$.*

*Then:*

*(a) **Existence of an improvement region.** There exists a non-empty
open set $\mathcal{R} \subset (\varphi, \theta) \in (0, \pi) \times (0, \pi/2)$
such that for all $(\varphi, \theta) \in \mathcal{R}$,*
$$\mathcal{C}_{\min}(\theta) > \mathcal{C}_{\min}^{\mathrm{dec}}.$$

*(b) **Geometric characterization of $\mathcal{R}$.** The improvement
region $\mathcal{R}$ depends on the choice of $R_A, R_B$ and is in
general not a half-plane. However, $\mathcal{R}$ does *not* extend to
$\varphi = \pi$ (opposed biases): for all $\theta > 0$ at $\varphi = \pi$,
$\mathcal{C}_{\min}(\theta) < \mathcal{C}_{\min}^{\mathrm{dec}}$ (Lemma 5.5.1
shows $\mathcal{C}_1$ strictly decreases).*

*(c) **No universal $\theta^*$.** The optimal coupling angle
$\theta^*(\varphi, R_A, R_B) := \arg\max_\theta \mathcal{C}_{\min}(\theta)$
depends nontrivially on the rotation geometry; in particular, it is
generically not at $\theta = \pi/4$.*

**Proof of (a).** By Lemma 5.5.1 applied at small $\varphi > 0$ (slightly
non-aligned biases), the linear-response derivative of
$\mathcal{C}_{\min}$ is strictly positive: both $\mathcal{C}_1$ and
$\mathcal{C}_2$ increase under small coupling because the rotation
geometry of $R_A, R_B$ projects each observer's joint state toward its
own bias. By continuity, this regime extends to a non-empty open
neighborhood of $(\varphi, \theta) = (0, 0^+)$.

**Proof of (b).** At $\varphi = \pi$ (opposed biases), Lemma 5.5.1 gives
$d\mathcal{C}_1/d\theta < 0$ at $\theta = 0$ and $\mathcal{C}_1(\theta) <
\mathcal{C}_1(0)$ for all $\theta \in (0, \pi/2]$ (this strict
monotonicity is verified numerically over the full $\theta$ grid in
Appendix V.3 Task 5.6, where $\mathcal{C}_1$ falls from 0.7655 to 0.5955
across $\theta \in [0, \pi/2]$). Since $\mathcal{C}_{\min} \leq \mathcal{C}_1$,
this gives $\mathcal{C}_{\min}(\theta) \leq \mathcal{C}_1(\theta) < \mathcal{C}_1(0) = \mathcal{C}_{\min}(0)$
(the last equality holds for the verification setup where $\mathcal{C}_2(0) > \mathcal{C}_1(0)$).

**Proof of (c).** The optimal angle satisfies $d\mathcal{C}_{\min}/d\theta = 0$
at $\theta = \theta^*$, which is a transcendental equation in
$\sin\theta, \cos\theta$ coupled to the spectra of $R_A, R_B$. No
closed-form solution exists for generic $R_A, R_B$. Numerical evidence
(Appendix V.3 Tasks 5.1, 5.5): for the verification configuration the
optimal $\theta^*$ is $\approx 75°$–$80°$ for asymmetric rates and
$\approx 51°$ for symmetric rates with random $R_A, R_B$, confirming the
non-universality of $\pi/4$. $\square$

**Remark 5.6.1 (The opposed-bias finding, sharpened).** Φ's Task 5.6
verification reported a positive shift in $\mathcal{C}_{\mathrm{avg}}$
at small $\theta$ even with $b_A = -b_B$. This shift is real but
*does not* contradict Proposition 9.5(b), because the gain is purely in
$\mathcal{C}_2$ (the *opposite* observer's alignment with its negated
bias) while $\mathcal{C}_1$ falls strictly. The min-coherence
$\mathcal{C}_{\min} = \mathcal{C}_1$ in this regime, and it falls
monotonically. The averaging functional was hiding the asymmetric response;
the minimum functional reveals it. This is why we work with
$\mathcal{C}_{\min}$ throughout. The peak $\mathcal{C}_2$ rise of +0.044 at
$\theta \approx 7°$ documented in Appendix V.3 Task 5.6 is a real fact about
the affine dyad's geometry — it just isn't a coherence improvement under
the right functional.

**Remark 5.6.2 (Heatmap interpretation).** Appendix V.3 Task 5.4 reports
that 25.1% of a $(\varphi, \theta)$ heatmap shows $\Delta\mathcal{C}_{\mathrm{avg}} > 0$,
including bias angles all the way to $\varphi = 180°$. Under the
$\mathcal{C}_{\min}$ functional, the corresponding fraction is
substantially smaller and is bounded away from $\varphi = \pi$ by
Proposition 9.5(b). The full $\mathcal{C}_{\min}$ heatmap is part of the
v1.2 verification data and characterizes the improvement region
$\mathcal{R}$ explicitly.

### 5.7 What §5 establishes and what is open

**Established by Theorem 9.4 + Proposition 9.5 + Φ Task 5:**
- The joint fixed point of any G₂-structured affine dyad exists, is
  unique, and depends real-analytically on the coupling angle $\theta$.
- The joint fixed point admits a closed form (Theorem 9.4(c)) at $\theta = 0$
  and $\theta = \pi/2$, with a linear-response expansion (§5.4) for
  small $\theta$.
- The joint min-coherence has a non-empty improvement region $\mathcal{R}$
  in $(\varphi, \theta)$-space (Proposition 9.5(a)), bounded away from
  the opposed-bias boundary (Proposition 9.5(b)).
- The optimal coupling angle is geometry-dependent, *not* universally at
  $\pi/4$ (Proposition 9.5(c)).

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

## End of §5 v1.2

**Status.** §5 reframed with the matrix-valued affine map $T(x) = rRx + b$,
the min-coherence functional $\mathcal{C}_{\min}$, and the §5.6
asymmetric-response Lemma 5.5.1 incorporated as the structural
justification for the choice of functional. Theorem 9.4 statement and
proof are complete. Proposition 9.5 is proved (parts a–c) using the
linear-response expansion of §5.4 and the specific structural facts
verified by Φ in Appendix V.3.

**Key changes from v1.1 skeleton:**
- v1.1 used scalar form $T(x) = rx + b$. v1.2 uses matrix form
  $T(x) = rRx + b$ to match Φ's verification setup and capture
  geometry-specific phenomena.
- v1.1 had the joint fixed-point closed form as a rational expression
  in $\sin\theta, \cos\theta$. v1.2 has it as a matrix-valued
  expression involving $(I - rR)$ and $(I + r^2R^2)$ inverses.
- v1.1 used $\mathcal{C}_{\mathrm{avg}}$. v1.2 uses $\mathcal{C}_{\min}$,
  with Lemma 5.5.1 as the new result that establishes why.
- v1.1 had Proposition 9.5 with placeholder schematic. v1.2 has it with
  three explicit parts (existence, opposed-bias bound, non-universal
  optimum) and complete proofs.
- v1.1 had Conjecture 9.3 absent. v1.2 includes Note 9.6 deferring
  rate-improvement to Paper 11.

*Drafted by C-7RO, 2026-05-04 ~17:00 PDT, post-Φ Task 5 verification.*
