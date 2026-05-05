# Paper 9 — §3 (v1.2)

**Paper:** Rate Lock and Affine Consensus in G₂-Structured Dyadic Observers
**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Status:** v1.2, 2026-05-04 (supersedes v0.9 §3 drafted 2026-04-30; v0.9 advocated the symmetric-diagonal coupling, which has since been shown amplifying — see §4 Theorem 9.1)
**Reflects:** §3.3 Lemma 3.3.1 inserted in §3.3; §3.5 retracted (symmetric coupling discarded as canonical); §3.6 reframed (joint singlet structure rewritten for the irreducible 14-dim adjoint)

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

**Lemma 3.3.1 (Block-rotation properties).** *The map $\Psi_\theta$
defined above has, for every $\theta \in \mathbb{R}$, the following
three properties.*

*(i) **Isometry.** $\Psi_\theta$ preserves the product norm: for all
$(x, y) \in \mathcal{M}_{AB}$,*
$$\|\Psi_\theta(x, y)\|_{AB}^2 = \|x\|_A^2 + \|y\|_B^2.$$
*Equivalently, $\Psi_\theta^\dagger \Psi_\theta = \mathrm{id}$ and
$\|\Psi_\theta\|_{\mathrm{op}} = 1$.*

*(ii) **One-parameter group.** $\Psi_{\theta_1} \circ \Psi_{\theta_2} =
\Psi_{\theta_1 + \theta_2}$; in particular $\Psi_0 = \mathrm{id}$ and
$\Psi_\theta^{-1} = \Psi_{-\theta}$.*

*(iii) **G₂-equivariance.** For every $g \in G_2$ acting diagonally
on $\mathcal{M}_{AB}$ via $\Delta(g) = g \oplus g$:*
$$\Psi_\theta \circ \Delta(g) = \Delta(g) \circ \Psi_\theta.$$

The proof is a direct block-matrix computation; it appears as a
self-contained one-page argument in the file
`paper9_section_3_3_lemma.md` and is incorporated here in summary form.

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

## What §3 v1.2 retracts from v0.9

The v0.9 draft of this section advocated three modeling choices that
have been retracted in v1.2:

1. **Symmetric-diagonal coupling as canonical.** v0.9 §3.3 named
   $\Psi = \alpha \cdot \mathrm{id} + \beta \cdot P_{\mathrm{swap}}$
   ("Choice A") as the canonical coupling. This map is *amplifying*
   (operator norm $\alpha + \beta > 1$ for $\beta > 0$) and produces
   rate degradation. Φ Task 1 (Appendix V.1) verified the bound
   violation across 24 configurations. v1.2 retains this map only as
   §4.1 Theorem 9.1's negative-result counterexample.
2. **Choice-of-coupling stack with three options.** v0.9 §3.3 listed
   diagonal, anti-diagonal, and mixed couplings as alternatives. v1.2
   commits to the antisymmetric block rotation as canonical and
   discusses the symmetric-diagonal alternative only in §4.1.
3. **Joint G₂ structure as a 28-dim Lie algebra preserving a "joint
   3-form" $\varphi^{AB}$.** v0.9 §3.7 constructed a 14+14-dimensional
   joint 3-form with a coupling-dependent mixed term. This construction
   was provisional and is not used by any v1.2 theorem; it is dropped
   from §3 of v1.2. The relevant joint structure is fully captured by
   the diagonal $G_2$-action of §3.4, and the joint Banach manifold
   $\mathcal{M}_{AB}$ does not require an additional "dyadic 3-form"
   to support the v1.2 results.

These retractions reduce §3 from 8 subsections (v0.9) to 6 subsections
(v1.2). The shorter v1.2 §3 is also closer to standard practice in
related literature: most coupled-observer Banach constructions adopt a
single canonical isometric coupling rather than a stack of alternatives.

---

*Drafted by C-7RO, 2026-05-04 ~17:25 PDT. Supersedes v0.9 §3 drafted
2026-04-30 18:35 PDT. Cross-references §3.3 Lemma 3.3.1 (separate file
`paper9_section_3_3_lemma.md`), §4 v1.1 (`paper9_draft_section_4_v1.1.md`),
and §5 v1.2 (`paper9_draft_section_5_v1.2.md`).*
