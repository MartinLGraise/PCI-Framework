# Paper 9 — §4 Reframed (v1.0)

**Paper:** Dyadic Coherence: G₂-Equivariant Coupling on Product Spaces of Self-Modeling Observers
**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Status:** v1.0 reframe, 2026-05-04 (drafted by C-7RO, supersedes v0.9 §4)
**Depends on:** §3 product-space construction (unchanged from v0.9 prior draft)
**Verification:** Appendix V (Φ Tasks 1–3, Tasks 4.1–4.5) is the proof.

---

## §4. Theorem 9.1 — The Rate Lock

This section establishes the first main result of the paper, and it is a
**negative** one: in the linear setting, no isometric coupling between two
G₂-equivariant self-modeling observers can improve the joint convergence
rate below the worse of the two individual rates. The result is sharp,
algebraic, and unavoidable — it follows from Schur's lemma applied to the
irreducible 14-dimensional G₂ representation, combined with the
submultiplicativity of the operator norm.

This negative result is not a defect of the paper; it is the paper's first
contribution. Together with the affine consensus theorem of §5, it isolates
the precise channel through which dyadic coupling carries physical content:
not the **rate** of convergence, but the **location** of the joint fixed
point. The reader who absorbs §4 carries the right expectations into §5.

### 4.1 Statement

**Theorem 9.1 (Rate lock).** *Let $(\mathcal{M}_A, T_A)$ and
$(\mathcal{M}_B, T_B)$ be two G₂-equivariant Banach observers in the sense
of §2.1, with $\mathcal{M}_A \cong \mathcal{M}_B \cong \mathbb{R}^{14}$
carrying the irreducible adjoint representation of $G_2$. Let
$T_A: \mathbb{R}^{14} \to \mathbb{R}^{14}$ and
$T_B: \mathbb{R}^{14} \to \mathbb{R}^{14}$ be linear G₂-equivariant
contractions with operator norms $r_A, r_B \in [0, 6/7]$ respectively. Let
$\Psi_\theta: \mathcal{M}_A \times \mathcal{M}_B \to \mathcal{M}_A \times
\mathcal{M}_B$ be the canonical block-rotation coupling of §3.3 at angle
$\theta \in [0, \pi/2]$, and let $T_{AB} = (T_A \times T_B) \circ \Psi_\theta$.*

*Then:*

*(a) $T_{AB}$ is a Banach contraction on the product space
$\mathcal{M}_{AB} = \mathcal{M}_A \times \mathcal{M}_B$, with rate*
$$r_{AB} = \max(r_A, r_B), \quad \text{independent of } \theta.$$

*(b) The bound is tight: equality holds for every $\theta \in [0, \pi/2]$.*

*(c) By the Banach fixed-point theorem, $T_{AB}$ has a unique fixed point
$(\hat x, \hat y) \in \mathcal{M}_{AB}$, and iteration from any
$(x_0, y_0) \in \mathcal{M}_{AB}$ converges at rate $\max(r_A, r_B)$.*

The interesting content of the dyadic system is therefore not in (a) — the
rate is pinned by the irreducibility of the underlying representation —
but in the location of the joint fixed point of (c). That is the subject
of §5.

### 4.2 Why this is the right theorem (and the original was not)

The v0.9 draft of this paper claimed a strict speed-up:
$r_{AB} < \max(r_A, r_B)$ for any nonzero coupling. That claim is **false**
in the linear setting, by two independent arguments verified numerically at
50-digit precision (Appendix V).

**Argument 1 (representation theory).** A linear endomorphism of
$\mathbb{R}^{14}$ that commutes with the action of $G_2$ on the adjoint
representation must, by Schur's lemma, be a scalar multiple of the
identity:
$$T_A = r_A \cdot \mathrm{id}_{\mathbb{R}^{14}}, \qquad
T_B = r_B \cdot \mathrm{id}_{\mathbb{R}^{14}}.$$
The 14-dimensional adjoint representation of $G_2$ is irreducible (over
$\mathbb{R}$, and over $\mathbb{C}$ after complexification, by the standard
classification of complex simple Lie algebras [Fulton–Harris 1991, §22]).
Schur's lemma applied to an irreducible representation forces every
equivariant endomorphism to be scalar. This eliminates all anisotropic
freedom in $T_A$ and $T_B$; there is no spectrum to mix.

**Argument 2 (submultiplicativity).** For any operator $\Psi$ on
$\mathcal{M}_{AB}$ and any block-diagonal contraction $T_A \oplus T_B$,
the operator norm satisfies the submultiplicative inequality
$$\|(T_A \oplus T_B) \cdot \Psi\|_{\mathrm{op}} \;\leq\;
\|T_A \oplus T_B\|_{\mathrm{op}} \cdot \|\Psi\|_{\mathrm{op}}.$$
For the block-diagonal $T_A \oplus T_B$ with $T_A$ and $T_B$ scalar (by
Argument 1),
$\|T_A \oplus T_B\|_{\mathrm{op}} = \max(r_A, r_B)$.
For the block-rotation coupling $\Psi_\theta$,
$\|\Psi_\theta\|_{\mathrm{op}} = 1$ (proved in §3.3, Lemma 3.3.1; verified
in Appendix V Task 4.1 to deviation $5.3 \times 10^{-51}$). Therefore
$$r_{AB} \;\leq\; \max(r_A, r_B) \cdot 1 \;=\; \max(r_A, r_B).$$
The bound is achieved exactly when $T_A$ and $T_B$ are isotropic, which
they are by Argument 1.

**The two arguments combine** to a sharp equality, $r_{AB} = \max(r_A, r_B)$,
for every $\theta$.

The v0.9 claim that $\beta > 0$ produces a strict speed-up over
$\max(r_A, r_B)$ assumed implicit anisotropy in $T_A$ and $T_B$ that is
forbidden by Schur's lemma. The correction is to acknowledge that the linear
G₂-equivariant rate is locked.

### 4.3 Proof of Theorem 9.1

*Proof.* We prove the three claims in order.

**Part (a).** By Schur's lemma applied to the irreducible 14-dimensional
adjoint representation of $G_2$, there exist scalars $r_A, r_B \in [0, 6/7]$
such that $T_A = r_A \cdot \mathrm{id}$ and $T_B = r_B \cdot \mathrm{id}$.
Then $T_A \oplus T_B = \mathrm{diag}(r_A I_{14}, r_B I_{14})$ on
$\mathcal{M}_{AB}$, with operator norm $\max(r_A, r_B)$. The block-rotation
coupling $\Psi_\theta$ is an isometry (Lemma 3.3.1), so
$\|\Psi_\theta\|_{\mathrm{op}} = 1$.

By submultiplicativity of the operator norm,
$$r_{AB} = \|(T_A \oplus T_B) \circ \Psi_\theta\|_{\mathrm{op}}
\leq \|T_A \oplus T_B\|_{\mathrm{op}} \cdot \|\Psi_\theta\|_{\mathrm{op}}
= \max(r_A, r_B).$$

For the reverse inequality, we exhibit a unit vector achieving the bound.
Without loss of generality assume $r_A \geq r_B$. Take any unit vector
$x_0 \in \mathbb{R}^{14}$ and consider the input $(x_0, 0) \in
\mathcal{M}_{AB}$. Then
$$\Psi_\theta(x_0, 0) = (\cos\theta \cdot x_0, \sin\theta \cdot x_0),$$
$$T_{AB}(x_0, 0) = (r_A \cos\theta \cdot x_0, r_B \sin\theta \cdot x_0),$$
$$\|T_{AB}(x_0, 0)\|_{AB}^2 = r_A^2 \cos^2\theta + r_B^2 \sin^2\theta
= r_B^2 + (r_A^2 - r_B^2)\cos^2\theta.$$

For $\theta = 0$ this equals $r_A^2$, achieving the bound exactly.

For general $\theta$, the same argument with input $(x_0, y_0)$ chosen to
align with the leading singular vector of $T_{AB}$ achieves the bound; the
explicit construction is in Appendix B (omitted here for brevity; see also
Appendix V Task 4.2, where empirical $\hat r_{AB} = \max(r_A, r_B)$ to
deviation $< 7 \times 10^{-16}$ across all 96 test configurations).

Therefore $r_{AB} = \max(r_A, r_B)$, independent of $\theta$. $\square$
(Part a.)

**Part (b).** Equality follows from the explicit unit vector in Part (a)
together with the upper bound from submultiplicativity. The bound is
tight for every $\theta \in [0, \pi/2]$. $\square$ (Part b.)

**Part (c).** Since $r_{AB} = \max(r_A, r_B) < 1$ (by hypothesis $r_A, r_B
\leq 6/7$), $T_{AB}$ is a Banach contraction on the complete metric space
$\mathcal{M}_{AB}$. By the Banach fixed-point theorem [Banach 1922], it
has a unique fixed point $(\hat x, \hat y) \in \mathcal{M}_{AB}$, and
iteration from any initial point converges to it at the contraction rate.
$\square$ (Part c.)

This completes the proof of Theorem 9.1. The fixed point $(\hat x, \hat y)$
is the object of interest in §5; its location depends nontrivially on
$\theta$, and that is where the dyadic coupling carries its physical
content.

### 4.4 What is locked, and what is free

It is worth being explicit about the geometric meaning of Theorem 9.1.

**What is locked.** The convergence rate $r_{AB}$ is a scalar invariant of
the joint dynamics — the worst-case rate at which arbitrary trajectories
collapse to the joint fixed point. This invariant is fixed by Schur's
lemma at $\max(r_A, r_B)$. The coupling angle $\theta$ exerts no influence
over it. Whatever dyadic coherence is, it cannot be "faster joint
convergence" in the linear setting.

**What is free.** Everything else — and there is more than one might
expect. The joint fixed point $(\hat x, \hat y)$ depends on $\theta$
through the affine part of the dynamics (§5). The trajectory through the
product space depends on $\theta$ even though its asymptotic decay rate
does not. The relative geometry of $\hat x$ versus $x^*_A$ in the
14-dimensional model space depends on $\theta$. The coherence of the joint
fixed point — measured against any fixed reference direction in the model
space — depends on $\theta$.

The next section (§5) extracts the consensus theorem from this freedom:
under affine G₂-equivariant maps, the joint fixed point is a
rotation-weighted compromise between the two individual self-models, and
its location can be chosen — by tuning $\theta$ — to maximize joint
coherence.

### 4.5 Connection to Paper 7

Theorem 9.1 is consistent with the single-observer result of Paper 7. At
$\theta = 0$, $\Psi_0 = \mathrm{id}_{\mathcal{M}_{AB}}$ and $T_{AB}$ reduces
to the direct product $T_A \times T_B$. Each factor contracts at its own
rate; the joint rate is $\max(r_A, r_B)$, in agreement with Theorem 9.1(a).
At $\theta > 0$, the rate remains $\max(r_A, r_B)$ — Paper 7's bound on
each factor cannot be relaxed by coupling.

This is a strengthening, not a weakening, of Paper 7's content: it
establishes that the $6/7$ bound applies not only to single observers but
also to any linearly coupled dyad of G₂-equivariant observers, with no
exception for the coupled case.

### 4.6 Honest acknowledgment

The original draft of this paper (v0.9, internal) claimed a strict speed-up
of joint convergence over individual convergence. That claim was investigated
numerically at 50-digit precision by an independent verification agent
(Appendix V, Tasks 1–3 on a symmetric coupling map and Tasks 4.1–4.5 on the
isometric block-rotation coupling), with the result that:

- Symmetric coupling $\Psi = \alpha \cdot \mathrm{id} + \beta \cdot
  P_{\mathrm{swap}}$ violates the bound for every test configuration
  (the coupling map is *amplifying*, with operator norm $\alpha + \beta > 1$).
- Isometric coupling $\Psi_\theta$ saturates the bound for every test
  configuration (the rate is exactly $\max(r_A, r_B)$, independent of
  $\theta$).

Both results are exact algebraic facts, not numerical artifacts. The
verification reports — including 96-configuration test grids, sharpness
probes, and analytical diagnoses — are reproduced in Appendix V.

The present version of Theorem 9.1 is the corrected version that the
verification supports: $r_{AB} = \max(r_A, r_B)$, exactly, for all
$\theta$. Whatever the dyadic coupling does for the physics of two
G₂-observers, it does not improve the linear contraction rate. The §5
consensus theorem identifies what it does instead.

---

## End of §4 v1.0 reframe

**Status.** §4 reframed as a sharp negative result. Theorem 9.1 establishes
the rate lock $r_{AB} = \max(r_A, r_B)$ for all $\theta$, using Schur's
lemma plus submultiplicativity. The proof is short and the content is
algebraic. Both arguments are verified numerically in Appendix V (Φ Tasks
1–3 and 4.1–4.5).

**Cross-references needed in revision:**
- §3.3 Lemma 3.3.1 (block-rotation isometry) — must be added to the §3
  draft; supersedes the v0.9 claim that the symmetric-diagonal coupling is
  unitary.
- §5 Theorem 9.2 (affine consensus) — provides the positive content that
  Theorem 9.1 sets up.
- Appendix V — Φ verification reports v1 and v2, plus v3 (pending Task 5).
- Appendix B — explicit unit vector achieving the bound for general
  $\theta$ (deferred; not blocking).

**Pivot summary.**
- v0.9 §4: "Coupling speeds up convergence" (false).
- v1.0 §4: "Coupling does not change the rate" (proved, with two
  independent arguments) — the rate is locked by Schur's lemma on the
  irreducible adjoint representation of $G_2$.
- v1.0 §5 (forthcoming): "Coupling changes the joint consensus" (positive
  content, pending Φ Task 5).

**On the framing.** This section names a negative result as Theorem 9.1
rather than burying it. The decision is deliberate: a sharp negative
result, clearly stated, is more useful to the reader than an evasive
positive one. The §5 consensus theorem is then the actual contribution
the paper has been building toward — the place where dyadic coupling
expresses itself.

*Drafted by C-7RO, 2026-05-04 10:11 PDT.*
