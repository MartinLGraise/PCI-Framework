# Paper 9 — §3.3 Lemma 3.3.1 (Block-Rotation Isometry)

**Paper:** Rate Lock and Affine Consensus in G₂-Structured Dyadic Observers
**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Status:** §3.3 addendum, 2026-05-04 (drafted by C-7RO)
**Purpose:** Supplies the lemma cited by §4 Theorem 9.2; replaces the v0.9 §3.3 unitarity claim (which was incorrect and was retracted in the §4 v1.1 reframe).

---

## §3.3 — The Coupling Map

We introduce the canonical coupling map $\Psi_\theta$ between two
G₂-equivariant self-modeling observers $(\mathcal{M}_A, T_A)$ and
$(\mathcal{M}_B, T_B)$. With $\mathcal{M}_A \cong \mathcal{M}_B \cong V^{14}$
denoting the 14-dim irreducible adjoint representation of $G_2$, and
$J_{AB}: \mathcal{M}_A \to \mathcal{M}_B$ the canonical G₂-equivariant
identification (both factors are isomorphic copies of the same
representation), define the **block-rotation coupling at angle $\theta$**:

$$\boxed{\;\Psi_\theta(x, y) \;=\; \bigl(\cos\theta \cdot x - \sin\theta \cdot J_{BA} y,\;\; \sin\theta \cdot J_{AB} x + \cos\theta \cdot y\bigr), \quad \theta \in [0, \pi/2].\;}$$

In block-matrix form on $\mathcal{M}_A \oplus \mathcal{M}_B$ (with the
identification $J_{AB} = \mathrm{id}$ so the two factors share a common basis):

$$\Psi_\theta \;=\; \begin{pmatrix} \cos\theta \cdot I_{14} & -\sin\theta \cdot I_{14} \\ \sin\theta \cdot I_{14} & \cos\theta \cdot I_{14} \end{pmatrix} \in \mathrm{SO}(\mathcal{M}_{AB}).$$

The one-parameter family $\{\Psi_\theta\}_{\theta \in \mathbb{R}}$ is the
standard orthogonal rotation in the two-block decomposition of the
28-dimensional product space, with generator
$\dot\Psi_0 = \begin{pmatrix}0 & -I_{14}\\ I_{14} & 0\end{pmatrix} \in
\mathfrak{so}(\mathcal{M}_{AB})$.

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

## End of §3.3 addendum

**Status.** Lemma 3.3.1 proved. All three properties — isometry,
one-parameter group, G₂-equivariance — are established by direct block-matrix
calculation. The isometry property is the one cited by §4 Theorem 9.2
(rate-inert) and referenced in the proof of the rate lock.

**Cross-references.**
- Theorem 9.1 (§4.1) — uses $\Psi_{\mathrm{sym}}$ as contrast.
- Theorem 9.2 (§4.2) — uses Lemma 3.3.1 (i) in the submultiplicativity
  argument.
- Theorem 9.4 (§5, pending Φ Task 5) — uses $\Psi_\theta$ in the affine
  consensus construction.

*Drafted by C-7RO, 2026-05-04 10:42 PDT.*
