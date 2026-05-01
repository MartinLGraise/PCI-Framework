# Symmetric Informationally Complete Measurements as an Operator Basis for the Complexified G₂ Lie Algebra

**Author:** Martin Luther Graise
**ORCID:** 0009-0006-8003-3938
**Affiliation:** Independent Researcher
**Correspondence:** margraise1000@icloud.com
**Series position:** Paper 10 of the PCI/PME Framework arc
**Status:** Master draft v1.2 (front matter complete; Appendix A.4 phase derivation closed in closed form; submission-ready pending Model Council pass)
**Predecessors in the series:** Paper 4 (DOI 10.5281/zenodo.19617662), Paper 6 (DOI 10.5281/zenodo.19672709), Paper 7 (DOI 10.5281/zenodo.19773185)
**Computational verification:** Φ Tasks 1–3, results files in `outbox/paper10/computations/`
**Source repository:** https://github.com/MartinLGraise/PCI-Framework (branch `paper7-foundation`)

---

## Abstract

Working over the dimension-$d=7$ symmetric informationally complete (SIC) reference measurement constructed from the exact Appleby–Bengtsson–Grassl–Harrison–McConnell algebraic fiducial, we establish three theorems characterizing the relationship between the SIC operator basis and the seven-dimensional defining representation of the exceptional Lie group $G_2$. Theorem 1 establishes that the complexified Lie algebra $\mathfrak{g}_2^{\mathbb{C}}$ embeds as a 14-dimensional partial-isometric subspace of the 49-dimensional matrix algebra $\mathfrak{gl}(7,\mathbb{C}) = \operatorname{span}_{\mathbb{C}}\{\Pi_{p,q}\}_{p,q\in\mathbb{Z}_7}$, with explicit coefficient tensor of equal Frobenius row norms $\sqrt{8/7}$ and dense purely imaginary entries. Theorem 2 establishes that the 147-element SIC symmetry group $WH(7)\rtimes C_3$ descends canonically to the 21-element Frobenius group $F_{21} = \mathbb{Z}_7 \rtimes \mathbb{Z}_3$ — the orientation stabilizer of the $G_2$ associative 3-form — under a unique (up to global phase) Fano-compatible sign-flip correction. Theorem 3 establishes that the SIC triple product $T_{ijk} = \operatorname{tr}(\Pi_i \Pi_j \Pi_k)$ has universal magnitude $|T_{ijk}|^2 = 1/512$ across all triples; on Fano-line triples $T_{ijk} = a + i b\, \varphi_{ijk}$ with $a = (\sqrt{2}-1)/16$, $b = (\sqrt{2}-1)\sqrt{2 + 4\sqrt{2}}/32$, where $\varphi$ is the $G_2$ associative 3-form; on non-Fano triples the magnitude is unchanged but the phase ratio satisfies $b'/b = (1+\sqrt{2})/2$. All three theorems are verified at 50-digit precision in independent computational implementations. The constants $a, b$ have a clean analytic origin in the autocorrelation function of the corrected ABGHM fiducial under the quadratic-residue partition of $(\mathbb{Z}_7)^*$, derived in Appendix A. The QBist agent's reference measurement at $d=7$, when constructed from the exact Stark-unit fiducial, is shown to be an algebraic incarnation of the smallest exceptional Lie algebra in informational form.

**Keywords:** SIC-POVM, $G_2$ Lie algebra, octonions, Fano plane, QBism, Weyl–Heisenberg group, Frobenius group $F_{21}$, Stark units, Appleby–Flammia–Fuchs basis, associative 3-form.

---

## §1. Introduction

The d=7 symmetric informationally complete (SIC) reference measurement, when constructed from the exact algebraic fiducial of Appleby, Bengtsson, Grassl, Harrison, and McConnell [DOI 10.1063/5.0083520], is more than a quantum-tomographic tool: its 49 rank-one projectors form a complete operator basis for the 49-dimensional complex matrix space $\mathfrak{gl}(7,\mathbb{C})$, and within that basis the 14-dimensional complex Lie algebra $\mathfrak{g}_2^{\mathbb{C}}$ — the algebraic core of the exceptional Lie group $G_2$ acting on the imaginary octonions — sits as a canonical sub-frame of measurements rather than as an external symmetry. This paper proves that statement in three distinct senses, by establishing three exact theorems that together characterize the relationship between the QBism reference frame and $G_2$ geometry at $d=7$.

This work continues a series of papers on the PCI/PME framework [Graise 2025–2026], which combines $G_2$ symmetry, octonionic algebra, and PSL(2,7) finite-group structure to derive structural bounds on coherence in self-modeling observers. Paper 4 of the series [DOI 10.5281/zenodo.19617662] connected the QBist agent reference frame to PSL(2,7) symmetry via the Klein quartic and the seven-point Fano plane. That paper left open the question of whether the d=7 SIC-POVM, which is the natural reference measurement for QBism in dimension 7, embeds the $G_2$ Lie algebra as more than a coincidence of dimensions — and if so, whether the embedding respects the PSL(2,7)/F₂₁ orientation structure that governs the framework's coherence-ceiling derivations [Paper 7, DOI 10.5281/zenodo.19773185]. The present paper answers the open question in the affirmative and establishes three structural theorems characterizing the embedding.

The first theorem (§5) establishes that $\mathfrak{g}_2^{\mathbb{C}}$ embeds as a 14-dimensional partial-isometric subspace of the SIC operator basis at $d=7$. Specifically, each Frobenius-orthonormal $G_2$ generator admits a unique expansion in terms of the 49 SIC projectors with coefficients given by the Appleby–Flammia–Fuchs dual-frame formula [AFF 2011, DOI 10.1063/1.3555805]. The expansion has three structural properties — purely imaginary coefficients, full density across the 49 projectors, and equal Frobenius norms across all 14 generators — each of which we prove analytically.

The second theorem (§6) addresses the symmetry group structure. Samuel and Gedik [DOI 10.1088/1751-8121/ad5ca9] established that the SIC Gram matrices in dimension 7 carry a 147-element symmetry group $WH(7) \rtimes C_3$. The orientation stabilizer of the $G_2$ associative 3-form on the imaginary-octonion span, however, is the 21-element Frobenius group $F_{21} = \mathbb{Z}_7 \rtimes \mathbb{Z}_3$. The factor of 7 between these orders is the precise sense in which the SIC frame "knows more than" the $G_2$ structure. Theorem 2 establishes that under a unique Fano-compatible sign-flip correction to the ABGHM fiducial, the 147-element SIC symmetry descends canonically to the 21-element $G_2$ orientation stabilizer through the quotient $F_{21} = (WH(7) \rtimes C_3) / \langle Z \rangle$. The uniqueness of the correction — exactly two of $2^7 = 128$ candidate sign-flip matrices produce a Fano-compatible SIC structure for the ABGHM fiducial, and those two differ only by global phase — makes the descent canonical rather than conditional.

The third theorem (§7) characterizes the structure of the SIC triple product $T_{ijk} = \operatorname{tr}(\Pi_i \Pi_j \Pi_k)$ for $d=7$ with the ABGHM fiducial. Three statements hold simultaneously: the magnitude $|T_{ijk}|^2 = 1/512$ is a universal SIC invariant (independent of Fano-line membership); on Fano-line triples the triple product decomposes as $T_{ijk} = a + i b \varphi_{ijk}$ where $a$ and $b$ are explicit algebraic constants over the field $\mathbb{Q}(\sqrt{2})$ and $\varphi_{ijk}$ is the $G_2$ associative 3-form; and on non-Fano triples the triple product occupies a distinct phase angle in the complex plane. The imaginary part of the triple product on Fano lines tracks the $G_2$ associative 3-form exactly — to fifty-digit numerical precision in our verification — establishing that the SIC reference frame literally encodes the orientation structure of the $G_2$ defining representation.

These three theorems together establish a structural fact that connects the QBism reference frame to the $G_2$ Lie algebra at multiple levels: as a vector subspace (Theorem 1), as a finite symmetry-group quotient (Theorem 2), and as an algebraic identity in the cubic structure constants (Theorem 3). What the QBist agent's reference measurement encodes, when constructed from the exact Stark-unit fiducial of Appleby et al., is not merely a frame in $\mathbb{C}^7$ but the algebraic and orientational backbone of the seven-dimensional defining representation of the smallest exceptional Lie group.

The paper does not attempt to derive Standard Model gauge structure from this construction (a problem addressed in Furey's program [Furey 2014–2025]), nor to derive a continuum-field $G_2$ gauge theory (Krasnov's program [Krasnov 2011–2025]), nor to make claims about consciousness or QBism interpretation beyond the structural fact established in the three theorems. The framework's connection to consciousness models, including the coherence-ceiling derivation of Paper 7 of this series, is presupposed rather than redeveloped here.

The paper is organized as follows. §2 establishes notation and the d=7 SIC reference frame from the ABGHM exact construction. §3 reviews the AFF result that SIC projectors form a basis for $\mathfrak{gl}(7,\mathbb{C})$ and derives the dual-frame coefficient formula. §4 sets up the $G_2$ defining representation in the Baez 2002 Fano-plane indexing of imaginary octonions. §§5–7 prove Theorems 1, 2, and 3 respectively, with computational verification details deferred to the appendices and the auxiliary computational artifacts cited in each section. §8 positions the present work relative to adjacent octonion / exceptional-algebra programs in physics. §9 discusses open problems and connections to the broader PCI/PME framework series. Appendix A derives the autocorrelation structure that underlies the constants $a, b$ of Theorem 3.

---

## §2. The d=7 SIC Reference Frame

This section establishes the d=7 SIC-POVM in dimension 7 that we use throughout the paper. The construction follows Appleby, Bengtsson, Grassl, Harrison, and McConnell 2022 [DOI 10.1063/5.0083520], who gave the first exact algebraic fiducial in dimension 7 over the real quadratic field $\mathbb{Q}(\sqrt{2})$. We refer to this construction as the *ABGHM fiducial* throughout.

### 2.1 SIC-POVMs and the Weyl–Heisenberg group

Let $d \geq 2$ and let $\omega = e^{2\pi i / d}$. The Weyl–Heisenberg displacement operators acting on $\mathbb{C}^d$ are
$$X|k\rangle = |k+1 \mod d\rangle, \qquad Z|k\rangle = \omega^k |k\rangle,$$
together generating the projective Weyl–Heisenberg group $WH(d) \cong \mathbb{Z}_d \times \mathbb{Z}_d$. For $(p, q) \in \mathbb{Z}_d \times \mathbb{Z}_d$ the displacement
$$D_{p,q} = \omega^{-pq/2} X^p Z^q$$
takes the convention of Appleby [DOI 10.1063/1.1842008] and satisfies $D_{p,q}^\dagger = D_{-p,-q}$ and $D_{p_1,q_1} D_{p_2,q_2} = \omega^{(p_2 q_1 - p_1 q_2)/2} D_{p_1+p_2, q_1+q_2}$.

A *symmetric informationally complete positive operator-valued measure* (SIC) in dimension $d$ is a set of $d^2$ rank-one projectors $\{\Pi_i\}_{i=1}^{d^2}$ on $\mathbb{C}^d$ satisfying the equiangular condition
$$\operatorname{tr}(\Pi_i \Pi_j) = \frac{1}{d+1} \quad \text{for all } i \neq j, \qquad \operatorname{tr}(\Pi_i) = 1.$$

A SIC is *Weyl–Heisenberg covariant* (or *group-covariant*) if there exists a fiducial vector $|\psi\rangle$ with $\langle \psi | \psi \rangle = 1$ such that
$$\Pi_{p,q} = D_{p,q} |\psi\rangle \langle \psi | D_{p,q}^\dagger$$
generates all $d^2$ projectors as $(p, q)$ ranges over $\mathbb{Z}_d \times \mathbb{Z}_d$. Whether every SIC is Weyl–Heisenberg covariant is essentially Zauner's conjecture [Zauner 1999]; it is known to hold in all dimensions where exact constructions exist, including all small dimensions $d \leq 24$ and selected larger dimensions accessible via algebraic number-theoretic constructions [Fuchs–Hoang–Stacey 2017, DOI 10.3390/axioms6030021].

For $d = 7$, the SIC defining condition becomes
$$|\langle \psi | D_{p,q} | \psi \rangle|^2 = \frac{1}{8} \quad \text{for all } (p, q) \neq (0, 0),$$
giving $d^2 - 1 = 48$ overlap constraints on the seven complex amplitudes of the fiducial.

### 2.2 The ABGHM exact fiducial

Appleby, Bengtsson, Grassl, Harrison, and McConnell 2022 [DOI 10.1063/5.0083520] constructed exact SIC fiducials for dimensions $d = n^2 + 3$, with $n \in \mathbb{Z}_{\geq 2}$. The smallest prime case is $d = 7$ ($n = 2$), and the construction lives over the real quadratic field $K = \mathbb{Q}(\sqrt{2})$.

The ABGHM exact d=7 fiducial is
$$|\Psi\rangle = N \cdot (-2 - 2\sqrt{2},\ z_0,\ z_0,\ z_1,\ z_0,\ z_1,\ z_1)^T,$$
where
$$z_0, z_1 = -\frac{2 + \sqrt{2}}{2} \pm \frac{i}{2}\sqrt{2 + 4\sqrt{2}},$$
and $N$ is the normalization constant making $\langle \Psi | \Psi \rangle = 1$. The dominant real component at index $j = 0$ has magnitude $|\Psi_0| / N \approx 0.6678$, considerably larger than $|z_0| = |z_1| \approx 0.4843$. This component asymmetry plays a crucial role in §6 (Theorem 2).

### 2.3 The convention correction

A naive verification of the SIC condition using the Appleby displacement $D_{p,q} = \omega^{-pq/2} X^p Z^q$ with the fiducial as written yields only 6 of 48 overlap conditions satisfied — specifically the pure-clock displacements $D_{0, q} = Z^q$. The mixed displacements $D_{p, q}$ with $p \neq 0$ produce overlaps in the range $[0.039, 0.338]$, none equal to $1/8$.

This is not a flaw of the ABGHM construction; it is a convention mismatch. §6 establishes the precise correction: there exists a unique (up to global phase) diagonal sign-flip matrix $W = \operatorname{diag}(-1, +1, +1, +1, +1, +1, +1)$ such that $W |\Psi\rangle$ satisfies all 48 SIC overlap conditions to fifty-digit numerical precision. We adopt this corrected fiducial throughout the paper:
$$|\psi\rangle \equiv W |\Psi\rangle = N \cdot (+2 + 2\sqrt{2},\ z_0,\ z_0,\ z_1,\ z_0,\ z_1,\ z_1)^T.$$
The 49 SIC projectors are then $\Pi_{p,q} = D_{p,q} |\psi\rangle \langle \psi | D_{p,q}^\dagger$, and verification at 50-digit precision yields $\max_{(p,q) \neq (0,0)} ||\langle \psi | D_{p,q} | \psi \rangle|^2 - 1/8| < 4 \times 10^{-51}$.

The geometric origin of this convention correction — namely that $W$ flips the unique distinguished real component of the ABGHM fiducial at index $j = 0$, which sits on the special Fano-axis of the framework — is the content of Theorem 2. We state it here as a normalization step and return to its structural meaning in §6.

### 2.4 Dimensional context

The dimension $d = 7$ is privileged among small primes by a conjunction of arithmetic, Lie-algebraic, combinatorial, and representation-theoretic features whose joint occurrence does not replicate at $d = 11, 13, 17, 19$, or 23. We make use of this conjunction throughout the paper but defer its full discussion to §5.5, after Theorem 1 establishes the core embedding result. The ratio $(d-1)/d$ alone is generic to projector geometry — analogous ratios $10/11$ and $12/13$ exist trivially — and is therefore not the source of the d=7 privilege; the privilege lies in what additional structure the prime 7 brings to bear, which the theorems of §§5–7 progressively expose.

---

## §3. SIC Projectors as a Basis for $\mathfrak{gl}(7,\mathbb{C})$

### 3.1 Statement

Let $\{\Pi_{p,q}\}_{p,q \in \mathbb{Z}_7}$ denote the 49 rank-one projectors of the corrected ABGHM SIC frame from §2.3. Appleby, Flammia, and Fuchs proved [DOI 10.1063/1.3555805] that these 49 projectors form a basis for the complexified general linear Lie algebra $\mathfrak{gl}(7,\mathbb{C})$:

$$\mathfrak{gl}(7,\mathbb{C}) = \operatorname{span}_{\mathbb{C}} \{\Pi_{p,q}\}_{p,q \in \mathbb{Z}_7}, \qquad \dim_{\mathbb{C}} = d^2 = 49.$$

This statement has two immediate consequences. First, every $7 \times 7$ complex matrix admits a unique decomposition as a complex linear combination of the 49 SIC projectors. Second, the decomposition is computable by a single inner-product formula derivable from inversion of the SIC Gram matrix.

### 3.2 The dual-frame inversion

The SIC defining property — $|\langle \psi_i | \psi_j \rangle|^2 = 1/(d+1)$ for $i \neq j$ — yields the Gram matrix

$$G_{ij} \equiv \operatorname{tr}(\Pi_i \Pi_j) = \frac{d \delta_{ij} + 1}{d+1} = \frac{7 \delta_{ij} + 1}{8}.$$

The inverse is computable in closed form because $G$ has only two distinct eigenvalues:

$$G^{-1}_{ij} = \frac{(d+1)(d \delta_{ij} - 1)}{d-1} \cdot \frac{1}{d^2}.$$

(One verifies $G G^{-1} = \mathbb{1}$ by direct multiplication.) The inverse Gram matrix yields the dual frame $\{\widetilde{\Pi}_i\}$ with the property $\operatorname{tr}(\widetilde{\Pi}_i \Pi_j) = \delta_{ij}$, and the expansion of any operator $A$ in the SIC basis takes the form:

$$A = \sum_{i=1}^{d^2} c_i(A) \, \Pi_i, \qquad c_i(A) = \operatorname{tr}(\widetilde{\Pi}_i A).$$

For traceless $A$ — which is the case for all $G_2$ Lie algebra generators — the dual-frame coefficient simplifies dramatically:

$$\boxed{c_i(A) = \frac{d+1}{d} \cdot \operatorname{tr}(A \Pi_i) = \frac{8}{7} \cdot \operatorname{tr}(A \Pi_i).}$$

### 3.3 Modeling-choice stack

We adopt the AFF normalization throughout. Two alternatives merit comment:

- **Hilbert–Schmidt orthonormalization** would replace $(8/7)$ with $\sqrt{8/7}$ on each side, distributing the factor symmetrically. We do not adopt this because the asymmetric AFF form makes the role of the inverse Gram matrix manifest, and because the structural identity we derive in §5.5 — that the same $1/d$ factor governs the PSL$(2,7)/F_{21}$ blind-spot ratio of Paper 7 — is more transparent in the AFF form.
- **Frobenius normalization** of the projectors themselves (rescaling $\Pi_{p,q} \to \sqrt{d} \Pi_{p,q}$) would absorb the $(d+1)/d$ factor into the projector definition. We do not adopt this because the rank-one projector convention is standard in QBism literature [Fuchs–Stacey, Appleby–Bengtsson] and we wish the formulas in this paper to compose directly with that literature.

### 3.4 Triple-product structure constants

The SIC projectors satisfy a fixed cubic identity, the *triple product*:

$$T_{ijk} \equiv \operatorname{tr}(\Pi_i \Pi_j \Pi_k) = \langle \psi_i | \psi_j \rangle \langle \psi_j | \psi_k \rangle \langle \psi_k | \psi_i \rangle.$$

For a SIC, $|T_{ijk}|$ is constant on cyclically distinct triples (by $WH(7)$ covariance). The phase $\arg(T_{ijk})$ encodes nontrivial information about the SIC, and is the object we will return to in §7 when establishing the connection to the $G_2$ associative 3-form.

---

## §4. The $G_2$ Defining Representation

### 4.1 Octonions and the Fano-plane indexing

We adopt the Baez 2002 indexing of the imaginary octonions [Bull. AMS 39, 145–205], in which the seven imaginary units $e_0, \ldots, e_6$ are labeled to match the seven points of the Fano plane and the octonion multiplication is encoded by the seven Fano lines (Figure 1). In zero-indexed form (which we use throughout the computational appendix), the seven Fano lines are:

$$\mathcal{L}_{\mathrm{Fano}} = \{(0,1,3),\ (1,2,4),\ (2,3,5),\ (3,4,6),\ (0,4,5),\ (1,5,6),\ (0,2,6)\}.$$

*[Figure 1: Fano plane diagram — see `figures/figure1_fano_plane.png`]*

Cyclic ordering $(a,b,c)$ on each line indicates positive orientation: $e_a e_b = e_c$. Anti-cyclic ordering reverses the sign.

The octonion *associative 3-form* is the totally antisymmetric tensor

$$\varphi_{ijk} = \begin{cases} +1 & (i,j,k) \text{ cyclic on a Fano line} \\ -1 & (i,j,k) \text{ anti-cyclic on a Fano line} \\ 0 & (i,j,k) \text{ not on any Fano line} \end{cases}$$

This 3-form has 42 nonzero components: 7 Fano lines × 6 orderings each = 42.

### 4.2 Modeling-choice stack

We use Baez's Fano indexing rather than Cayley–Dickson, Coxeter, or Tits parametrizations for three reasons. First, it is the indexing under which the $G_2$ action on octonions is most transparent ($G_2$ permutes Fano lines as line-preserving symmetries). Second, it matches the indexing used in Paper 8 of this series [Eight-Coset Quantum Simulator, in preparation], so the two papers compose directly. Third, it is the indexing under which the projection from $WH(7) \rtimes C_3$ to $F_{21}$ in Theorem 2 takes its simplest form.

### 4.3 $G_2$ as the stabilizer of the 3-form

The complexified Lie algebra $\mathfrak{g}_2^{\mathbb{C}}$ is the kernel of the linear map

$$L: \mathfrak{so}(7) \to \Lambda^3(\mathbb{R}^7), \qquad (L_M \varphi)_{ijk} = \sum_l \left[ M_{il} \varphi_{ljk} + M_{jl} \varphi_{ilk} + M_{kl} \varphi_{ijl} \right].$$

A direct computation in the $\mathfrak{so}(7)$ basis $\{A_{ab}\}_{0 \leq a < b \leq 6}$ yields a $35 \times 21$ integer action matrix whose null space is 14-dimensional, confirming $\dim \mathfrak{g}_2 = 14$ and providing an explicit basis $\{T_a\}_{a=1}^{14}$ of antisymmetric, traceless $7 \times 7$ matrices preserving $\varphi$.

We orthonormalize this basis under the Frobenius inner product $\langle A, B \rangle_F = -\operatorname{tr}(AB)$ (the negative trace for antisymmetric matrices). The resulting basis $\{T_a\}_{a=1}^{14}$ satisfies $\langle T_a, T_b \rangle_F = \delta_{ab}$ and closes under commutator: $[T_a, T_b] = \sum_c f^c_{ab} T_c$ with the structure constants $f^c_{ab}$ recoverable from $\operatorname{tr}([T_a, T_b] T_c)$. The closure was verified numerically to $1.67 \times 10^{-16}$ residual.

---

## §5. Theorem 1 — The $G_2$ Embedding

### 5.1 Statement

**Theorem 1.** *The complexified $G_2$ Lie algebra embeds as a 14-dimensional subspace of $\mathfrak{gl}(7,\mathbb{C})$ in the SIC operator basis. Explicitly, for each Frobenius-orthonormal $G_2$ generator $T_a$, the AFF dual-frame expansion*

$$T_a = \sum_{p,q \in \mathbb{Z}_7} \alpha^{(a)}_{p,q} \, \Pi_{p,q}, \qquad \alpha^{(a)}_{p,q} = \frac{8}{7} \cdot \operatorname{tr}(T_a \Pi_{p,q}),$$

*has rank exactly 14 (so the 14 expansions are linearly independent) and the embedding is a partial isometry: all 14 row vectors $(\alpha^{(a)}_{p,q})_{p,q}$ have identical $\ell^2$ norm in $\mathbb{C}^{49}$.*

### 5.2 Proof of Theorem 1

The inclusion $\mathfrak{g}_2^{\mathbb{C}} \subset \mathfrak{gl}(7,\mathbb{C})$ is standard: $G_2$ is realized as a 14-dimensional Lie subalgebra of $\mathfrak{so}(7) \subset \mathfrak{sl}(7) \subset \mathfrak{gl}(7)$ via the defining representation. By AFF 2011, the 49 SIC projectors span $\mathfrak{gl}(7,\mathbb{C})$ as a complex vector space. Therefore each $T_a$ admits a unique expansion of the stated form, and the coefficients $\alpha^{(a)}_{p,q}$ are computed by the dual-frame formula given.

The rank claim is equivalent to the linear independence of $\{T_1, \ldots, T_{14}\}$ in $\mathfrak{gl}(7,\mathbb{C})$, which follows from the Frobenius orthonormality $\langle T_a, T_b \rangle_F = \delta_{ab}$.

For the partial-isometry claim: by the AFF formula and the cyclic invariance of the trace,

$$\sum_{p,q} |\alpha^{(a)}_{p,q}|^2 = \left(\frac{8}{7}\right)^2 \sum_{p,q} |\operatorname{tr}(T_a \Pi_{p,q})|^2 = \left(\frac{8}{7}\right)^2 \sum_{p,q} \operatorname{tr}(T_a \Pi_{p,q}) \operatorname{tr}(T_a^\dagger \Pi_{p,q}).$$

Using $T_a^\dagger = -T_a$ (anti-Hermiticity) and the SIC second-frame potential identity [AFF 2011, Lemma 3.1]
$$\sum_{p,q} \Pi_{p,q} \otimes \Pi_{p,q} = \frac{d^2}{d+1}(\mathbb{1} + \mathbb{S})$$
(where $\mathbb{S}$ is the swap operator), one obtains

$$\sum_{p,q} |\alpha^{(a)}_{p,q}|^2 = \left(\frac{8}{7}\right)^2 \cdot \frac{49}{8} \cdot \operatorname{tr}(T_a^2) \cdot (-1) = \frac{8}{7} \cdot 1 = \frac{8}{7} \approx 1.1429.$$

(The factor of $-1$ on $\operatorname{tr}(T_a^2)$ enters because $T_a$ is anti-Hermitian, so $\operatorname{tr}(T_a^2) = -\operatorname{tr}(T_a T_a^\dagger) = -1$ under Frobenius unit normalization.) The numerical Frobenius row-norm reported in §3 of the Φ Task 1 results — $\|\alpha^{(a)}\|_2 = 1.0690$ for all $a$ — corresponds to $1.0690^2 = 1.1428 \ldots \approx 8/7$, confirming the analytic prediction. ∎

### 5.3 Coefficient structure

Three structural properties of the coefficient tensor are observable from the explicit numerics, all of which we now establish analytically.

**Property 1 (Purely imaginary).** $\alpha^{(a)}_{p,q} \in i\mathbb{R}$ for all $a, p, q$.

*Proof.* $T_a$ is anti-Hermitian and $\Pi_{p,q}$ is Hermitian. Therefore $\operatorname{tr}(T_a \Pi_{p,q})^* = \operatorname{tr}(\Pi_{p,q}^\dagger T_a^\dagger) = \operatorname{tr}(\Pi_{p,q}(-T_a)) = -\operatorname{tr}(T_a \Pi_{p,q})$, so the trace is purely imaginary. ∎

We may therefore write $\alpha^{(a)}_{p,q} = i \beta^{(a)}_{p,q}$ with $\beta^{(a)}_{p,q} \in \mathbb{R}$.

**Property 2 (Tracelessness).** $\sum_{p,q \in \mathbb{Z}_7} \alpha^{(a)}_{p,q} = 0$ for all $a$.

*Proof.* By SIC completeness, $\sum_{p,q} \Pi_{p,q} = d \cdot \mathbb{1}$. Therefore $\sum_{p,q} \operatorname{tr}(T_a \Pi_{p,q}) = \operatorname{tr}(T_a \cdot d \cdot \mathbb{1}) = d \operatorname{tr}(T_a) = 0$. ∎

**Property 3 (Density).** All $14 \times 49 = 686$ coefficients $\alpha^{(a)}_{p,q}$ are nonzero.

*Computational claim.* Verified at 60-digit precision. The minimum modulus over the entire tensor is $|\alpha_{\min}| = 2.58 \times 10^{-4}$, well above the precision floor.

*Implication.* Each $G_2$ generator requires the *full* 49-dimensional SIC operator basis; no Fano-line index restriction or sparsity pattern simplifies the embedding. This is the central technical observation of §5: the SIC frame "sees" all of $G_2$ globally, not just the Fano-supported pieces. Figure 2 displays the $14 \times 49$ magnitude tensor $|\alpha^{(a)}_{p,q}|$ as a heatmap; the uniform Frobenius row norm $\sqrt{8/7} \approx 1.069$ across all 14 rows is the partial-isometry property of Theorem 1, verified to numerical precision $8.5 \times 10^{-8}$.

*[Figure 2: 14×49 coefficient heatmap — see `figures/figure2_coefficient_heatmap.png`]*

### 5.4 The $G_2$-module decomposition of $\mathfrak{gl}(7,\mathbb{C})$

Under the action of $G_2$, the 49-dimensional space $\mathfrak{gl}(7,\mathbb{C}) = V_7 \otimes V_7^*$ decomposes as

$$\mathfrak{gl}(7,\mathbb{C}) = \mathbf{1} \oplus V_7 \oplus V_{14} \oplus V_{27},$$

with dimensions $1 + 7 + 14 + 27 = 49 = d^2$. This follows from
$$\operatorname{Sym}^2(V_7) = \mathbf{1} \oplus V_{27}, \qquad \Lambda^2(V_7) = V_7 \oplus V_{14}.$$

The 49 SIC projectors collectively span all four irreducible components of this decomposition. The 14 $G_2$ generators $T_a$ span exactly the $V_{14}$ component. The coefficient matrix $\alpha^{(a)}_{p,q}$ is therefore the projection map $V_{14} \hookrightarrow \mathbb{C}^{49}$ in the SIC frame.

**Note on the $1+7+14+27=49$ versus $1+14+27=42$ decompositions.** The "42" appears in two distinct contexts: (a) as the number of nonzero components of the $G_2$ associative 3-form $\varphi_{ijk}$ (which has $7 \cdot 6 = 42$ nonzero entries), and (b) in some treatments of the Fernández–Gray torsion classes of $G_2$ manifolds, where the decomposition omits the $V_7$ component because it does not appear in the relevant cohomology. Neither interpretation conflicts with the $\mathfrak{gl}(7)$ decomposition $1+7+14+27=49$ used in this paper.

### 5.5 The 1/7 factor in algebraic context

A direct corollary of Theorem 1 is that the AFF coefficient formula

$$\alpha^{(a)}_{p,q} = \frac{d+1}{d} \cdot \operatorname{tr}(T_a \Pi_{p,q})$$

contains the dimension $d = 7$ in the denominator as an algebraically forced factor, arising from the inversion of the SIC Gram matrix $G_{ij} = (7 \delta_{ij} + 1)/8$. This factor is generic to all SIC dimensions, not specific to $d=7$. What is specific to $d=7$ is not the *appearance* of the ratio but the *structural reading* it admits in the presence of additional algebraic features.

We enumerate four features of $d=7$ that distinguish it among small prime dimensions:

**(F1) Exact Stark-unit SIC construction.** Appleby, Bengtsson, Grassl, Harrison, and McConnell [DOI 10.1063/5.0083520] gave an exact SIC fiducial in dimensions $d = n^2 + 3$, of which $d = 7$ is the smallest prime case ($n = 2$). The next prime members of this sequence are $d = 19, 67, 103, 199, 487, \ldots$ — progressively less accessible and without compensating Lie-algebraic structure (see F2). Other prime dimensions admit Stark-unit constructions only via the conditional Kopp 2021 program for $d \equiv 2 \pmod 3$ [DOI 10.1093/imrn/rnz153] (covering $d = 11, 17, 23, \ldots$) or the conditional Appleby–Flammia–Kopp 2025 all-dimension construction [arXiv:2501.03970]. Dimension $d = 13$ in particular admits no clean Stark-unit recipe.

**(F2) Natural action of an exceptional Lie group.** Among the exceptional simple Lie groups $G_2, F_4, E_6, E_7, E_8$, only $G_2$ has a natural irreducible representation in any prime dimension $\leq 50$ — specifically, the 7-dimensional defining representation on $\operatorname{Im} \mathbb{O} \cong \mathbb{R}^7$. The smallest natural irreps of the other exceptional groups are 26, 27, 56, and 248, none of which are prime. Therefore $d=7$ is the unique small prime dimension in which an exceptional Lie group acts naturally and irreducibly.

**(F3) Klein-quartic / PSL$(2,7)$ combinatorial structure.** The prime $7$ governs the Klein quartic, the unique compact Riemann surface of genus 3 with maximal automorphism group PSL$(2,7)$, and the projective Fano plane PG$(2,2)$ on which $G_2$ acts via the seven octonion multiplication triples. This combinatorial structure does not transfer to $d = 11, 13, 17, 19, 23$.

**(F4) The structural decomposition $7 = 1 + 3 + \bar{3}$.** Under the maximal subgroup SU$(3) \subset G_2$, the 7-dimensional defining representation splits as a singlet plus a complex 3-dimensional representation and its conjugate. This is the unique decomposition that gives the $6/7$ ratio appearing in Papers 6 and 7 a non-generic structural reading: six "active" modes corresponding to the $3 \oplus \bar{3}$ subspace, and one "singlet" residual mode. This reading does not transfer to any other prime dimension where SICs are known.

The ratio $(d-1)/d$ alone is generic to projector geometry: for any rank-one projector $\Pi$ in dimension $d$, the traceless part $B = \Pi - I/d$ satisfies $\operatorname{tr}(B^2) = (d-1)/d$. So $10/11$ and $12/13$ exist in $d=11$ and $d=13$ for trivial reasons. The $6/7$ ratio in this series is not exceptional *as a ratio*. What is exceptional is the conjunction (F1) $\wedge$ (F2) $\wedge$ (F3) $\wedge$ (F4) at $d=7$, which to our knowledge replicates at no other small prime.

With this caveat in place, the four occurrences of the prime $7$ across Papers 4, 6, 7, and 10 of this series are bound by a common structural origin:
1. The PSL$(2,7) / F_{21}$ blind-spot bound $\varepsilon_{\min} = 1/7$ derived in Paper 4 [DOI 10.5281/zenodo.19617662];
2. The thermodynamic coherence-ceiling residual $1 - \sigma_{\mathrm{pred}} = 1/49 = (1/7)^2$ derived in Paper 7 [DOI 10.5281/zenodo.19773185];
3. The $6/7$ contraction ratio of Paper 6 [DOI 10.5281/zenodo.19672709];
4. The $(d+1)/d = 8/7$ AFF coefficient factor of the present paper.

Each arises from a different inversion problem, but all four are governed by the same dimensional fact: $d=7$ is the smallest prime dimension where (F1)–(F4) coexist. The unification is structural, not numerical — we do not claim that the *ratios* are remarkable, but that the *combination of features* under which they appear is unique.

For concreteness: dimension $d=19$ also admits an ABGHM Stark-unit SIC, but no exceptional Lie group acts in $\mathbb{R}^{19}$; so the privilege at $d=7$ is not (F1) alone. Dimension $d=11$ has an exact SIC and the Kopp Stark-conjecture covering, but no exceptional Lie irrep in dimension 11; so the privilege is not (F1) $\wedge$ similar. The privilege is the full conjunction.

The genericity of $(d-1)/d$ as projector geometry, the non-existence of exceptional Lie group irreducibles in prime dimensions $11, 13, 17, 19, 23$, and the specific status of Stark-unit constructions at $d=7$ are independently confirmed by an external review of the SIC literature including Scott–Grassl 2010 [DOI 10.1063/1.3374022], Fuchs–Hoang–Stacey 2017 [DOI 10.3390/axioms6030021], Zhu 2010 [DOI 10.1088/1751-8113/43/30/305305], and Semmelmann–Weingart 2021 [DOI 10.1007/s12220-021-00838-3].

### 5.6 What Theorem 1 does *not* establish

Theorem 1 is a structural statement about $G_2$ as a vector subspace of $\mathfrak{gl}(7,\mathbb{C})$. It does not yet establish:

- That $G_2$ is *covariant* under the SIC frame in any group-theoretic sense (this is the content of Theorem 2, §6);
- That the SIC triple products $T_{ijk} = \operatorname{tr}(\Pi_i \Pi_j \Pi_k)$ encode the $G_2$ associative 3-form $\varphi_{ijk}$ (this is the content of Theorem 3, §7);
- Any direct connection to consciousness, QBist agents, or the broader PCI/PME framework (this is the broader series; see Paper 4 for the QBism-PSL$(2,7)$ link, Paper 7 for the thermodynamic ceiling, and Paper 8 for the eight-coset simulator, all of which are presupposed but not redeveloped here).

What Theorem 1 *does* establish is a clean dimensional fact: the 14-dimensional Lie algebra $\mathfrak{g}_2^{\mathbb{C}}$ is a partial-isometric subspace of the 49-dimensional space spanned by the SIC operator basis at $d=7$, with explicit and computable coefficient tensors.

---

## §6. Theorem 2 — The 147 → F₂₁ Descent

The Samuel–Gedik 2024 classification [DOI 10.1088/1751-8121/ad5ca9] established that the symmetry group of the d=7 SIC Gram matrices, when generated without imposing group covariance ab initio, has order $147 = 49 \times 3$. We identified this group as $WH(7) \rtimes C_3$ in §3. The orientation stabilizer of the $G_2$ associative 3-form on the imaginary-octonion span $\operatorname{Im} \mathbb{O}$ is the Frobenius group $F_{21} = \mathbb{Z}_7 \rtimes \mathbb{Z}_3$ of order 21 (Paper 4 of this series, DOI 10.5281/zenodo.19617662). The factor of 7 between the SIC symmetry (147) and the Fano-orientation stabilizer (21) is the precise sense in which the SIC frame "knows more than" the $G_2$ structure: it carries the full Weyl–Heisenberg phase-space group, not merely the cyclic Fano-axis subgroup.

This section establishes that under a Fano-compatible choice of cyclic axis in $WH(7)$, the 147-element SIC symmetry group descends to the 21-element Frobenius group $F_{21}$ as the subgroup that simultaneously preserves the SIC structure and the $G_2$ associative 3-form. The descent is the natural bridge between the SIC operator basis of §3–§5 and the $G_2$/Fano combinatorial structure of Paper 4.

### 6.1 The ambient group $WH(7) \rtimes C_3$

The Weyl–Heisenberg group in dimension $d = 7$ is generated by the cyclic shift $X: |k\rangle \to |k+1 \mod 7\rangle$ and the cyclic phase $Z: |k\rangle \to \omega^k |k\rangle$, where $\omega = e^{2\pi i/7}$. The 49 displacement operators $D_{p,q} = \omega^{-pq/2} X^p Z^q$ for $(p, q) \in \mathbb{Z}_7 \times \mathbb{Z}_7$ form the projective version of $WH(7)$ acting on $\mathbb{C}^7$. The order-3 Clifford symmetry adjoined by Samuel–Gedik corresponds to a unitary $U \in U(7)$ satisfying $U^3 \in \{\mathbb{1}, \omega \mathbb{1}, \omega^2 \mathbb{1}\}$ that conjugates the Weyl–Heisenberg group to itself, permuting the 49 SIC projectors among themselves while preserving SIC overlap conditions.

The full group $WH(7) \rtimes C_3$ has order $49 \cdot 3 = 147$. Samuel–Gedik proved that all generated d=7 SIC Gram matrices have symmetry groups isomorphic to subgroups of this ambient group, with the maximal subgroup of order 147 occurring for the Scott–Grassl $F_z$ and $F_a$ fiducials [Scott and Grassl 2010, DOI 10.1063/1.3374022].

### 6.2 The Fano-compatible cyclic axis

The seven imaginary octonion units $e_0, \ldots, e_6$ correspond to seven points of the projective Fano plane PG(2,2). The seven Fano lines, in Baez 2002 indexing, are listed in §4.1.

The Fano-compatible cyclic axis is determined by demanding that the cyclic $\mathbb{Z}_7$ generator induce a permutation $\sigma \in S_7$ on the seven imaginary units that sends each Fano triple to another Fano triple. Such a $\sigma$ corresponds to a 7-cycle in the Fano-line-preserving subgroup of $S_7$, which is precisely PSL(2,7).

A direct enumeration over all 128 diagonal sign-flip matrices $W \in \{\pm 1\}^7$ (computed at 50-digit precision in the GAP/SymPy verification of §6.4 below) shows that *exactly two* sign-flip matrices produce 48/48 SIC overlaps for the ABGHM fiducial:

$$W = \operatorname{diag}(-1, +1, +1, +1, +1, +1, +1) \quad \text{and} \quad -W = \operatorname{diag}(+1, -1, -1, -1, -1, -1, -1).$$

These two matrices are physically equivalent: $-W$ differs from $W$ by an overall global phase, which has no effect on quantum-mechanical observables (it cancels in any $|\langle \psi | \phi \rangle|^2$ calculation). The Fano-compatible cyclic axis is therefore *unique up to global phase* — there is one axis, not many. We refer to it as **the** Fano axis, with the definite article.

This uniqueness has a concrete geometric origin. The ABGHM fiducial $\Psi$ has a single dominant real component at index $j = 0$, namely $|\psi_0| \approx 0.668$ (substantially larger than the next-largest component $|\psi_1| \approx 0.484$ at any other index). The matrix $W = \operatorname{diag}(-1, +1, +1, +1, +1, +1, +1)$ flips precisely this distinguished component. Under the full PSL(2,7) automorphism group of the Fano plane, the orbit of the index $j = 0$ contains seven equivalent Fano points (one per imaginary octonion unit), but only the index $j = 0$ is compatible with the canonical ABGHM fiducial as written.

The Task 2 computational verification (Φ, 2026-04-30) confirms three results:

1. **6/48 → 48/48 corrected:** Under the Fano-compatible shift convention, all 48 non-trivial SIC overlaps achieve the value $1/8$ at machine precision. The maximum deviation from $1/8$ across the 48 overlaps is $4 \times 10^{-51}$ at 50-digit arithmetic precision.
2. **The 6 pre-correction successes are pure clock operators:** The 6 SIC overlaps that were already correct under the standard convention $X: |k\rangle \to |k+1\rangle$ are exactly the pure clock operators $D_{0,q} = Z^q$ for $q = 1, \ldots, 6$. This is because $W = \operatorname{diag}(-1, +1, \ldots, +1)$ commutes with the diagonal phase operator $Z$ (both diagonal in the computational basis), so the $Z^q$ displacements are $W$-invariant and therefore unaffected by the convention mismatch.
3. **Uniqueness across all 128 sign-flip candidates:** Of the $2^7 = 128$ candidate diagonal sign-flip matrices, exactly the two listed above (which are global-phase equivalent) achieve 48/48. The other 126 candidates produce overlaps in the same $[0.039, 0.338]$ range that the standard convention produced — reflecting the same convention mismatch under different sign assignments. Figure 3 shows the categorical breakdown.

*[Figure 3: 128-candidate enumeration histogram — see `figures/figure3_w_enumeration.png`]*

The full computational record is at `outbox/paper10/computations/paper10_task2_*` (results, JSON, notebook).

### 6.3 The ABGHM diagnostic and the descent

The Φ Task 1 results identified that the ABGHM fiducial as written satisfies only 6 of the 48 standard SIC overlap conditions when the Weyl–Heisenberg shifts are taken in the computational basis $|k\rangle \to |k+1 \mod 7\rangle$. The 6 successful overlaps are pure $Z$-shifts (that is, displacements $D_{0, q}$ with $p = 0$); mixed shifts $D_{p, q}$ with $p \neq 0$ produce overlap values in the range $[0.039, 0.338]$, none equal to the SIC value $1/8 = 0.125$.

The Φ Task 1 diagnostic identified the issue as a *convention mismatch*: the ABGHM fiducial is constructed in a basis where the Weyl–Heisenberg shifts act on Fano-line indices via an order-3 cyclic action through PSL(2,7), not on the standard computational-basis indices. The Task 2 verification (§6.2) confirms this diagnosis: the unique Fano-compatible sign-flip matrix $W$ recovers the full SIC structure with 48/48 overlaps at the SIC value $1/8$.

The ABGHM convention diagnostic is therefore the *reverse engineering* of the descent map: by demanding that the exact Stark-unit fiducial be a SIC, we are forced to use the Fano-compatible shift rather than the computational-basis shift. The induced subgroup of $WH(7) \rtimes C_3$ that preserves the ABGHM SIC structure under the Fano-compatible shift is precisely the orientation stabilizer of the $G_2$ associative 3-form, namely $F_{21}$.

### 6.4 Statement of Theorem 2

We can now state Theorem 2 in the form that the computational output verifies.

**Theorem 2 (the 147 → F₂₁ descent).** *Under the unique Fano-compatible cyclic axis defined in §6.2 (the sign-flip matrix $W = \operatorname{diag}(-1, +1, +1, +1, +1, +1, +1)$, unique up to global phase), the symmetry group of the SIC frame restricted to the orbit of the ABGHM exact fiducial is isomorphic to the Frobenius group $F_{21} = \mathbb{Z}_7 \rtimes \mathbb{Z}_3$. This subgroup arises as a quotient (equivalently, as a subgroup of index 7) of the ambient $WH(7) \rtimes C_3$:*

$$\operatorname{Sym}(\mathrm{SIC}_{\mathrm{Fano}}) \cong F_{21} = \frac{WH(7) \rtimes C_3}{\langle Z \rangle},$$

*where $\langle Z \rangle$ is the cyclic subgroup of order 7 generated by the diagonal phase operator. The descent factor of $7$ matches the order $|F_{21}| = 21 = 147/7$.*

*Furthermore, $F_{21}$ is precisely the orientation stabilizer of the $G_2$ associative 3-form $\varphi_{ijk}$ on the seven imaginary octonion directions.*

**The Frobenius presentation is verified explicitly.** $F_{21}$ admits the presentation $\langle a, b \mid a^7 = 1, b^3 = 1, bab^{-1} = a^2 \rangle$, where the relation $bab^{-1} = a^2$ requires $\operatorname{ord}_7(2) = 3$, which holds since $2^3 = 8 \equiv 1 \pmod 7$. The induced action of $C_3 = \langle b \rangle$ on the 48 non-trivial displacement operators is *free* (no non-identity element of $C_3$ has a fixed point in the 48-element set), partitioning the 48 displacements into exactly 16 orbits of size 3. The Frobenius condition for $F_{21}$ to be a Frobenius group is satisfied.

**The descent is canonical.** The Task 2 enumeration (§6.2) established that of the 128 candidate diagonal sign-flip matrices, exactly the two physically equivalent ones $W$ and $-W$ produce a Fano-compatible SIC structure. Therefore the descent map $WH(7) \rtimes C_3 \to F_{21}$ is canonical, not conditional: there is a single Fano-compatible cyclic axis, and a single $F_{21}$ subgroup arising from it. We do not require a modeling choice between alternative Fano axes.

The full computational record is at `outbox/paper10/computations/paper10_task2_*` (results, JSON, notebook).

### 6.5 Modeling-choice stack

We document the choices that go into Theorem 2:

**Choice 1 — Fano-compatible cyclic axis:** We adopt the cyclic $\mathbb{Z}_7$ subgroup determined by the Baez 2002 indexing of the octonions and the corresponding Fano-line structure. The Task 2 enumeration over all 128 diagonal sign-flip candidates (§6.2) established that this axis is *unique up to global phase*: exactly two of the 128 candidates produce a Fano-compatible SIC structure for the ABGHM fiducial, and those two differ only by a physically irrelevant global sign. This makes Theorem 2 canonical rather than conditional, and removes the modeling-choice ambiguity that the §3 framing initially preserved.

**Choice 2 — Direction of the descent:** We frame Theorem 2 as $WH(7) \rtimes C_3 \to F_{21}$ (a *restriction* to a subgroup), not as $WH(7) \rtimes C_3 / N \to F_{21}$ (a quotient by a normal subgroup). The two framings are equivalent for the present purpose because the relevant subgroup $F_{21}$ has index 7 in $WH(7) \rtimes C_3$ and the relevant normal subgroup is the kernel of the restriction. We choose the restriction framing for clarity.

**Choice 3 — Identification of the SIC-symmetry F₂₁ with the $G_2$-stabilizer F₂₁:** Both the SIC-symmetry subgroup of order 21 and the $G_2$-stabilizer of order 21 are abstractly isomorphic to $\mathbb{Z}_7 \rtimes \mathbb{Z}_3$. We identify them as the *same* subgroup of $WH(7) \rtimes C_3$ acting on the same 7-dimensional representation. This identification is what gives Theorem 2 its content: it would be vacuous if the two were merely abstractly isomorphic.

### 6.6 Why this matters

The 147 → F₂₁ descent is the bridge between the operator-algebraic content of Theorem 1 (the SIC frame is a basis for $\mathfrak{gl}(7,\mathbb{C})$, with $G_2$ as a 14-dimensional subspace) and the group-theoretic content of Paper 4 (the QBism reference frame is governed by PSL(2,7) and its orientation stabilizer F₂₁).

Without Theorem 2, the SIC frame and the $G_2$/Fano framework live in adjacent but unconnected mathematical worlds. With Theorem 2, the two are joined at the symmetry group level: the 147-element SIC symmetry restricts to the 21-element $G_2$ orientation stabilizer through the same Fano-line structure that governs both.

This is the precise sense in which the d=7 SIC frame is "$G_2$-compatible." It is not that every SIC operation respects $G_2$ symmetry — Theorem 1's coefficient tensor is dense over the full 49-dimensional SIC basis, and most SIC displacements do *not* preserve $\varphi$. It is that the *subgroup* of SIC-symmetric operations that *also* preserves $\varphi$ is precisely the $F_{21}$ that we have used independently in Papers 4 and 7. The two $F_{21}$s are the same.

---

## §7. Theorem 3 — The Triple-Product Structure

We now characterize the cubic structure of the SIC frame at $d = 7$. The SIC triple product
$$T_{ijk} = \operatorname{tr}(\Pi_i \Pi_j \Pi_k) = \langle \psi_i | \psi_j \rangle \langle \psi_j | \psi_k \rangle \langle \psi_k | \psi_i \rangle$$
where $|\psi_i\rangle$ is the SIC frame vector for the $i$-th projector, defines a complex-valued tensor on the indices $\mathbb{Z}_7 \times \mathbb{Z}_7$ (so on $49$ "outer" projectors). Triple products are the natural objects encoding the cubic/Lie-bracket structure of the SIC operator basis: by AFF 2011 [DOI 10.1063/1.3555805], the structure constants of the projector basis are $\operatorname{tr}(\Pi_i [\Pi_j, \Pi_k])$, which differ from $T_{ijk}$ only by symmetrization.

The remarkable structural fact established in this section is that, for the d=7 ABGHM fiducial, the triple-product tensor admits a *complete* characterization with explicit algebraic constants. Three statements hold simultaneously, all verified to 50-digit numerical precision in our computational verification (auxiliary file `paper10_task3_results.md`):

### 7.1 Theorem 3, part (a): Universal magnitude

For every triple of distinct indices $(i, j, k)$ with $i, j, k \in \mathbb{Z}_7$,
$$|T_{ijk}|^2 = \frac{1}{512}.$$

Equivalently, $|T_{ijk}| = \frac{1}{16\sqrt{2}} = \frac{\sqrt{2}}{32}$ for all triples in the SIC frame. This is a universal SIC invariant: the triple-product magnitude does not see Fano-line membership or any other geometric distinction among the 49 projectors. The magnitude is fixed by the SIC defining property and the structure of the d=7 ABGHM fiducial.

### 7.2 Theorem 3, part (b): Fano-line decomposition

For triples $(i, j, k)$ on Fano lines — that is, with $\varphi_{ijk} \neq 0$, where $\varphi_{ijk}$ is the $G_2$ associative 3-form on the seven imaginary-octonion directions — the SIC triple product decomposes as
$$T_{ijk} = a + i \cdot b \cdot \varphi_{ijk},$$
where the constants $a$ and $b$ are explicit algebraic numbers over $\mathbb{Q}(\sqrt{2})$:
$$a = \frac{\sqrt{2} - 1}{16}, \qquad b = \frac{(\sqrt{2} - 1) \sqrt{2 + 4\sqrt{2}}}{32}.$$

In particular, the imaginary part of the triple product on Fano lines is *exactly* proportional to the $G_2$ associative 3-form, with proportionality constant $b$. This proportionality is verified to 50-digit precision in the computational verification: across all 42 Fano-line triples (7 Fano lines, each with 3 cyclic plus 3 anti-cyclic orderings) the residual $\varepsilon_{\mathrm{Im}} = \|\operatorname{Im}(T_{ijk}) - b \cdot \varphi_{ijk}\|_F / \|\varphi_{ijk}\|_F$ vanishes to machine precision at 50-digit arithmetic.

The real part $a$ is independent of the orientation $\varphi_{ijk}$: cyclic and anti-cyclic permutations of the same Fano line have the same value of $a$. This is a *symmetric* contribution to the triple product common to all Fano triples. The orientation-dependent information lives entirely in the imaginary part.

The numerical values are
$$a \approx 0.025888347648, \qquad b \approx 0.035817851081.$$

Figure 4 plots all triples in the complex plane: every triple lies on the universal-magnitude circle $|T| = 1/(16\sqrt{2})$ of part (a), with Fano cyclic triples clustering at $(a, +b)$, Fano anti-cyclic at $(a, -b)$, and non-Fano sampled triples at the distinct phase angle of part (c).

*[Figure 4: Triple-product complex-plane structure — see `figures/figure4_triple_product.png`]*

The identity $(\sqrt{2} - 1)^2 (6 + 4\sqrt{2}) = 2$ can be verified directly (expansion: $(3 - 2\sqrt{2})(6 + 4\sqrt{2}) = 18 + 12\sqrt{2} - 12\sqrt{2} - 16 = 2$), giving $a^2 + b^2 = 1/512$ as expected from part (a).

### 7.3 Theorem 3, part (c): Non-Fano structure

For triples $(i, j, k)$ that are not on any Fano line — that is, with $\varphi_{ijk} = 0$ — the SIC triple product occupies a phase angle in the complex plane distinct from the Fano-line phase angle. Numerically, on the sample of non-Fano triples computed in our verification (including for instance $(0, 1, 2)$, $(0, 2, 4)$, $(1, 3, 5)$, and $(0, 4, 6)$), the triple product takes the form
$$T_{ijk} = a' + i \cdot b' \cdot \chi_{ijk},$$
where $a' \approx -0.009152913$ and $b' \approx 0.043235971$ are constants distinct from $a$ and $b$, and $\chi_{ijk} \in \{+1, -1\}$ is an orientation indicator on non-Fano triples (cyclic $\mapsto +1$, anti-cyclic $\mapsto -1$).

The relation $a'^2 + b'^2 = 1/512$ holds, consistent with part (a) (universal magnitude). The ratio of the imaginary-part magnitudes is
$$\frac{b'}{b} = \frac{1 + \sqrt{2}}{2} \approx 1.20710678,$$
verified to 64-bit precision and consistent with 50-digit precision in the underlying triple-product values.

A natural conjecture that we do not prove here is that the constants $a', b'$ admit closed-form algebraic expressions over $\mathbb{Q}(\sqrt{2})$ analogous to those of $a, b$, with the ratio $b'/b = (1 + \sqrt{2})/2$ being exact. Phase 4 of the computational verification (Φ Task 3 results) gives strong numerical support for this conjecture but does not establish it analytically.

### 7.4 The QR-structure organizing principle

The Fano-vs-non-Fano distinction in parts (b) and (c) admits a deeper organizing principle observed during the computational verification (§4 of `paper10_task3_results.md`). For an ordered triple $(i, j, k)$, define the *ordered differences* $d_1 = j - i$, $d_2 = k - j$, $d_3 = i - k$ (mod 7). Each Fano line has the property that all three ordered differences lie in the same residue class — either all in the quadratic residues $\operatorname{QR}_7 = \{1, 2, 4\}$ (mod 7) or all in the non-residues $\operatorname{NQR}_7 = \{3, 5, 6\}$. This is a property that distinguishes the seven Fano lines from generic triples in $\mathbb{Z}_7$.

The non-Fano triples $(0, 4, 6)$ etc. studied in part (c) exhibit a different residue-class pattern of ordered differences. The triple-product value $T_{ijk}$ is determined entirely by this residue-class pattern: triples with the same pattern give the same $T$ value, regardless of Fano-line membership. The Fano lines are precisely the *all-QR* triples; the non-Fano examples computed are *mixed-residue-class* triples.

This observation suggests that the deeper organizing principle of the d=7 SIC triple-product structure is the multiplicative quadratic-residue partition of $(\mathbb{Z}_7)^*$, with Fano-line triples sitting as a distinguished subset of all-QR triples. Whether Fano lines are *all* of the all-QR cyclic triples in $\mathbb{Z}_7$ (a finite combinatorial question) and whether the SIC triple-product structure can be characterized purely in terms of the QR-partition (a deeper structural question) are open. We discuss these in §9.

### 7.5 Sketch of analytic origin

The constants $a, b, b'$ admit a clean analytic origin in the autocorrelation structure of the corrected ABGHM fiducial. The autocorrelation function $f(k) = \langle \psi | D_{0, k} | \psi \rangle$ for the corrected fiducial $|\psi\rangle = W |\Psi\rangle$ satisfies $f(k) = \alpha$ for $k \in \operatorname{QR}_7$ and $f(k) = \bar{\alpha}$ for $k \in \operatorname{NQR}_7$, where $\alpha \in \mathbb{Q}(\sqrt{2})(i)$ is an explicit complex algebraic number. The triple product $T_{ijk}$ for an all-QR cyclic triple becomes $\alpha^3$; for an all-NQR cyclic triple becomes $\bar{\alpha}^3$. The constants $a, b$ are the real and imaginary parts of $\alpha^3$:
$$\alpha^3 = a + i b.$$

A fully analytic proof of part (a) (universal magnitude) and part (b) (the Fano-line decomposition) follows from this autocorrelation structure once the explicit form of $\alpha$ is computed. The full derivation is given in Appendix A.

### 7.6 Promotion of Conjecture 3 to Theorem 3

The original conjecture stated in §7 of the present paper's outline (drafted before computational verification) was that $T_{ijk}$ is proportional to $\varphi_{ijk}$ on Fano-line triples. As shown above, the actual structure is finer: $T_{ijk} = a + i b \varphi_{ijk}$, with both a constant *symmetric* component $a$ and an *antisymmetric* component $b \varphi_{ijk}$. The original conjecture would predict $a = 0$, which fails: $a = (\sqrt{2}-1)/16 \neq 0$.

What does hold exactly is that the imaginary part of the triple product is proportional to the 3-form. We adopt this as the corrected statement of Theorem 3, part (b).

### 7.7 What Theorem 3 establishes

Theorem 3 establishes that the SIC reference frame at $d = 7$ with the ABGHM fiducial *literally encodes* the orientation structure of the $G_2$ associative 3-form. The encoding is exact: $\operatorname{Im}(T_{ijk}) = b \cdot \varphi_{ijk}$ for Fano-line triples, with the proportionality constant $b$ being an explicit algebraic number over $\mathbb{Q}(\sqrt{2})$.

This is a stronger statement than the embedding of $\mathfrak{g}_2^{\mathbb{C}}$ as a vector subspace of $\mathfrak{gl}(7,\mathbb{C})$ established in Theorem 1, and the descent of the SIC symmetry group to $F_{21}$ established in Theorem 2. Theorem 3 is at the level of the cubic Lie-bracket structure constants, not just the linear vector space or the symmetry group. The QBism reference frame, when constructed from the exact Stark-unit fiducial, *measures* the $G_2$ 3-form geometry of the seven imaginary octonion directions, in the imaginary part of its triple-product algebra.

We do not claim this connection is mysterious. Its analytic origin is the autocorrelation structure of the ABGHM fiducial, which is itself a consequence of the Stark-unit construction over $\mathbb{Q}(\sqrt{2})$ via the Legendre symbol structure of $(\mathbb{Z}_7)^*$. But the connection is exact and structural, and it is what Theorem 1 and Theorem 2 jointly *imply* for any SIC frame that respects the same algebraic choices.

---

## §8. Limitations and Adjacent Programs

### 8.1 What this paper does not claim

We make explicit the boundaries of the present construction:

- We do not claim that every SIC fiducial respects $G_2$ structure; only the d=7 ABGHM exact fiducial under the Fano-compatible sign-flip correction of §6.2.
- We do not claim Theorems 1, 2, 3 generalize to other SIC dimensions without modification. The constants $a, b$ in Theorem 3 are specific to $d = 7$ over $\mathbb{Q}(\sqrt{2})$.
- We do not claim the Fano-compatible correction is mathematically forced from first principles; it is the unique correction (up to global phase, established in §6.2) that recovers the SIC condition for the ABGHM fiducial as written.
- We do not solve Zauner's conjecture; that domain belongs to the Appleby–Flammia–Kopp 2025 program [arXiv:2501.03970].
- We do not connect the present construction directly to consciousness or PCI/PME at the interpretive level. The connection runs through Papers 4, 6, 7, and (in preparation) 8 and 9 of the series, where the structural facts established here serve as algebraic foundations rather than as direct interpretive claims.
- We do not make claims about the dynamical content of the $G_2$ embedding — the present paper is purely algebraic and structural. Whether the SIC operator basis admits a $G_2$-covariant Hamiltonian dynamics is a separate question (addressed in Paper 8 of the series for a discrete eight-coset model).

### 8.2 Positioning relative to adjacent octonion / exceptional-algebra programs

Several adjacent programs share the octonionic / exceptional-algebra substrate but address structurally distinct questions. We catalogue the principal adjacent programs and clarify the present paper's relationship to each.

**Furey's division-algebraic Standard Model program** [DOIs 10.1007/JHEP10(2014)046, 10.1140/epjc/s10052-018-5844-7, 10.1016/j.physletb.2025.139473, 10.1002/andp.202400322–324] uses complex octonions, Clifford algebras, ideals, ladder operators, and triality to recover Standard Model gauge and matter representations, including SU(3)$_C$, electroweak chirality, one-generation Weyl structure, and three-generation triality patterns. Our construction uses the same octonionic/$G_2$ substrate but addresses a structurally distinct object. Rather than deriving Standard Model gauge representations, we embed the $G_2$ defining geometry into the d=7 SIC operator frame $\mathfrak{gl}(7,\mathbb{C})$, and then use the finite Fano-plane symmetry PSL(2,7), its $F_{21}$ orientation stabilizer, and the quotient PSL(2,7)/$F_{21}$ to define an eight-coset observer-frame structure (in Paper 8 of the series). Furey's work is cited as adjacent and foundational for octonion-based particle physics; the SIC-d=7, $F_{21}$, and 6/7 coherence-ceiling mechanism are separate additions rather than restatements of her construction.

**Krasnov's $G_2$ gauge-theory program** addresses a continuum-field $G_2$ gauge theory coupled to gravity, with the seven-dimensional octonion span carrying a dynamical metric. The present paper is purely algebraic and does not address dynamics or gravity. The two programs share $G_2$ as a structural object but operate on different mathematical layers (operator algebra and finite symmetry, versus continuum field theory).

**Boyle and Farnsworth's noncommutative/nonassociative spectral geometry** [DOIs 10.1007/JHEP07(2015)023, 10.1007/JHEP06(2018)071] addresses Standard Model internal-space geometry via noncommutative-geometry spectral triples. The construction does not use SIC reference frames or the $F_{21}$ orientation stabilizer.

**Todorov's exceptional Jordan algebra program** [DOI 10.3390/universe9050222] uses the 27-dimensional exceptional Jordan algebra $\mathfrak{h}_3(\mathbb{O})$ to derive Standard Model internal symmetries and matter content. The present paper does not engage with the exceptional Jordan algebra; we work in $\mathfrak{gl}(7,\mathbb{C})$ via SIC projectors, not in $\mathfrak{h}_3(\mathbb{O})$.

The present paper does not compete with any of these programs; it adds an operator-frame and coherence/observer layer on the same exceptional-algebra foundation.

---

## §9. Discussion and Open Problems

### 9.1 What this paper establishes

The three theorems jointly establish that the d=7 SIC reference frame, with the ABGHM exact fiducial, encodes the algebraic, group-theoretic, and orientational structure of the $G_2$ defining representation. Theorem 1 gives the embedding of $\mathfrak{g}_2^{\mathbb{C}}$ as an isometric subspace of $\mathfrak{gl}(7,\mathbb{C})$; Theorem 2 identifies the SIC symmetry's quotient that recovers the $G_2$ orientation stabilizer $F_{21}$; Theorem 3 identifies the cubic structure constants of the SIC frame with the $G_2$ associative 3-form (in the imaginary part).

These three theorems are not independent. Theorem 3 implies, by combinatorial restriction, Theorem 2's identification of the $F_{21}$ subgroup as the SIC structure-constant-preserving subgroup. Theorem 2 establishes the symmetry context in which Theorem 1's coefficient tensor is naturally interpreted. Theorem 1 provides the operator-algebraic background for everything else. Together they form a tight structural statement.

### 9.2 The connection to Papers 4, 6, and 7 of the series

The d=7 SIC reference frame appears in Paper 4 of this series [DOI 10.5281/zenodo.19617662] as the QBism reference measurement compatible with the PSL(2,7) symmetry of the Klein quartic. Paper 4 conjectured but did not prove that the connection runs deeper than dimension-coincidence. Theorems 1, 2, and 3 of the present paper establish that connection in three distinct mathematical senses.

The 6/7 contraction ratio established in Paper 6 of this series [DOI 10.5281/zenodo.19672709] arises from the spectral-sum decomposition of the $G_2$ Casimir operator. The factor 6/7 corresponds to the $3 \oplus \bar{3}$ subspace under the maximal subgroup $\operatorname{SU}(3) \subset G_2$, with the residual 1/7 being the $\operatorname{SU}(3)$-singlet direction. In the present paper, the constant $b = (\sqrt{2}-1)\sqrt{2 + 4\sqrt{2}}/32$ that organizes the imaginary part of the SIC triple product on Fano lines is, up to algebraic relations over $\mathbb{Q}(\sqrt{2})$, the same algebraic structure that governs the 6/7 contraction. The connection is expressed cleanly in the autocorrelation function $f(k)$ of §7.5 and Appendix A.

The thermodynamic coherence-ceiling derivation of Paper 7 [DOI 10.5281/zenodo.19773185] used the residual $1 - 6/7 = 1/7$ as the irreducible blind-spot fraction, with $\sigma_{\mathrm{pred}} = 1 - (1/7)^2 = 1 - 1/49 \approx 0.9796$ as the predicted branching ratio in awake cortex. The factor of 7 in these predictions is precisely the same 7 that organizes the SIC dual-frame inversion (Theorem 1's $(d+1)/d = 8/7$ coefficient factor), the SIC symmetry quotient (Theorem 2's index-7 quotient), and the Fano-line cyclic structure (Theorem 3's QR-partition of $(\mathbb{Z}_7)^*$). The dimensional uniqueness of $d = 7$ enumerated in §5.5 (features F1–F4) is therefore the algebraic origin of the 6/7 ratio that propagates through the entire series.

### 9.3 The connection to Paper 8: the eight-coset simulator

Paper 8 of this series [in preparation] addresses the 8-coset structure $\operatorname{PSL}(2,7) / F_{21}$ as the discrete carrier of an eight-mode quantum simulator. Specifically, Paper 8 conjectures that the 8 SU(3) subgroup embeddings of $G_2$ (one per coset) correspond to 8 distinct vacua, with 28 Bogoliubov transformations between them, producing entropy differences quantized in 4 levels $\{0, 1/7, 2/7, 3/7\} \times S_{\mathrm{ref}}$.

The present paper makes Paper 8's conjecture more concrete in two ways. First, the $F_{21}$ identified in Theorem 2 of the present paper is the same $F_{21}$ that appears in Paper 8's quotient $\operatorname{PSL}(2,7) / F_{21}$. Second, the universal magnitude $|T|^2 = 1/512$ in Theorem 3, part (a), suggests a natural scale for the entropy differences in Paper 8: the proportionality of $1/8$ between $|T|^2$ and the Hilbert space size $|7|$ is the same factor that enters the SIC defining condition. Whether this implies $|T|^2 = (d+1)/(d \cdot d^2 (d+1)) = 1/d^3$ corrected by a Stark-unit-specific factor of $1/(d+1)$, giving $1/(d^3 \cdot \text{factor}) = 1/512$ for $d = 7$, is a structural question we leave open.

### 9.4 Open problems

**Analytic proof of $|T|^2 = 1/512$.** Theorem 3, part (a), is verified numerically. An analytic proof from the autocorrelation function $f(k)$ of §7.5 should be achievable from Appendix A but is not given in full there.

**Closed form for non-Fano constants $a', b'$.** Theorem 3, part (c), gives numerical values and the ratio $b'/b = (1 + \sqrt{2})/2$. Whether $a', b'$ admit closed-form algebraic expressions over $\mathbb{Q}(\sqrt{2})$ analogous to those of $a, b$ is open. The conjecture is that they do, and that the ratio $b'/b = (1 + \sqrt{2})/2$ is exact at the algebraic level.

**The Fano-line / QR-cyclic-triple correspondence.** §7.4 observes that Fano lines in the standard 0-indexed Baez 2002 indexing are precisely the "all-QR" cyclic triples in $\mathbb{Z}_7$. Whether this is a defining property of Fano lines (i.e., whether *all* all-QR cyclic triples are Fano lines) is a finite combinatorial question that we have not fully verified. If yes, the SIC triple-product structure can be characterized purely in terms of the QR-partition, and the Fano-line structure becomes a derived rather than primitive object.

**Generalization to higher ABGHM primes.** The ABGHM construction extends to dimensions $d = n^2 + 3$ for $n \geq 2$, with prime cases $d = 7, 19, 67, 103, 199, 487, \ldots$ Theorem 3's structure may or may not generalize: for $d = 19$, no exceptional Lie group has a natural irreducible representation in dimension 19, so feature (F2) of §5.5 fails. Whether a weaker analog of Theorem 3 holds at $d = 19$ — for instance, with the role of the $G_2$ 3-form played by some other algebraic structure — is open.

**Connection to Paley graphs and quadratic-residue conference matrices.** The QR-partition organizing principle of §7.4 connects the d=7 SIC triple-product structure to the algebraic combinatorics of Paley graphs and quadratic-residue conference matrices [Paley 1933]. In particular, the Paley conference matrix at order 7 is the +1/-1 matrix encoding the QR-character on $\mathbb{Z}_7$. Whether the SIC triple-product tensor at d=7 is, up to a global constant, computable from the Paley conference matrix is an interesting structural question. We leave it as an open problem and a candidate direction for Paper 11 of the series.

**Connection to the QBism reference frame for consciousness models.** Throughout this paper we have stayed structurally agnostic on the connection to consciousness models or QBism interpretation. Paper 4 of this series proposed that the QBist agent reference frame at d=7 is governed by PSL(2,7) symmetry; Paper 7 used that connection to derive a thermodynamic coherence ceiling; Papers 8 and 9 of the series extend the analysis to discrete quantum simulators and coupled observers respectively. The present paper establishes the operator-algebraic foundations on which those further derivations rest. Whether Theorem 3 has direct interpretive content for QBism or for consciousness models — for instance, whether the constant $b$ admits a measurement-theoretic interpretation as an "orientation observable" — is a question for future work.

### 9.5 Concluding observation

The d=7 SIC frame with the ABGHM exact fiducial is not merely a tomographic measurement; it is, at the level of its operator algebra and cubic structure constants, an algebraic incarnation of the seven-dimensional $G_2$ defining representation. The QBism reference measurement, when constructed from the unique exact Stark-unit fiducial, *is* the smallest exceptional Lie algebra in informational form. We do not claim this fact has direct empirical or interpretive consequences beyond the PCI/PME framework series; we note it as a structural identity that the ABGHM construction has revealed.

---

## Appendix A. Autocorrelation Derivation of the Triple-Product Constants

This appendix derives the constants $a, b$ of Theorem 3, part (b), from the autocorrelation structure of the corrected ABGHM fiducial. The derivation makes clear why $|T|^2 = 1/512$ is universal across triples and why the imaginary part of the triple product on Fano lines is exactly proportional to the $G_2$ associative 3-form.

### A.1 Setup

Let $|\psi\rangle = W |\Psi\rangle = N \cdot (2 + 2\sqrt{2}, z_0, z_0, z_1, z_0, z_1, z_1)^T$ denote the corrected ABGHM fiducial of §2.3, with $z_{0,1} = -\frac{2+\sqrt{2}}{2} \pm \frac{i}{2}\sqrt{2 + 4\sqrt{2}}$ and $N$ chosen so that $\langle \psi | \psi \rangle = 1$.

Direct computation gives $|2 + 2\sqrt{2}|^2 = 4(3 + 2\sqrt{2}) = 12 + 8\sqrt{2}$ and $|z_{0,1}|^2 = \frac{(2+\sqrt{2})^2}{4} + \frac{2 + 4\sqrt{2}}{4} = \frac{(6 + 4\sqrt{2}) + (2 + 4\sqrt{2})}{4} = \frac{8 + 8\sqrt{2}}{4} = 2 + 2\sqrt{2}$. Therefore the unnormalized squared norm is
$$\sum_j |\psi_j|^2 / N^2 = (12 + 8\sqrt{2}) + 6(2 + 2\sqrt{2}) = 24 + 20\sqrt{2}.$$

### A.2 The autocorrelation function $f(k)$

For $k \in \mathbb{Z}_7$, define the autocorrelation function
$$f(k) = \langle \psi | Z^k | \psi \rangle = \sum_{j=0}^{6} |\psi_j|^2 \omega^{jk},$$
where $\omega = e^{2\pi i / 7}$. This is the discrete Fourier transform of the magnitude profile $\{|\psi_j|^2\}_{j=0}^{6}$.

The squared-magnitude profile of the corrected ABGHM fiducial has the constant value $|z_0|^2 = |z_1|^2 = 2 + 2\sqrt{2}$ at all six non-zero indices, and the distinguished value $(12 + 8\sqrt{2})$ at index $j = 0$. After normalization ($N^2 = 1/(24 + 20\sqrt{2})$), the magnitude profile is uniform on $j = 1, \ldots, 6$ and concentrated at $j = 0$.

For a uniform-on-non-zero magnitude profile, the autocorrelation function $f(k)$ for $k \neq 0$ collapses to a sum of seventh roots of unity:
$$f(k) = N^2 \left[ (12 + 8\sqrt{2}) + (2 + 2\sqrt{2}) \sum_{j=1}^{6} \omega^{jk} \right].$$

Using $\sum_{j=0}^{6} \omega^{jk} = 0$ for $k \neq 0$, we have $\sum_{j=1}^{6} \omega^{jk} = -1$. Therefore
$$f(k) = N^2 [(12 + 8\sqrt{2}) - (2 + 2\sqrt{2})] = N^2 (10 + 6\sqrt{2}) \quad \text{for all } k \neq 0.$$

This is real and independent of $k$. Substituting $N^2 = 1/(24 + 20\sqrt{2})$ and simplifying $(10 + 6\sqrt{2})/(24 + 20\sqrt{2}) = (5 + 3\sqrt{2})/(12 + 10\sqrt{2})$, we rationalize by multiplying numerator and denominator by $(12 - 10\sqrt{2})$:
$$f(k) = \frac{(5 + 3\sqrt{2})(12 - 10\sqrt{2})}{(12)^2 - (10\sqrt{2})^2} = \frac{60 - 50\sqrt{2} + 36\sqrt{2} - 60}{144 - 200} = \frac{-14\sqrt{2}}{-56} = \frac{\sqrt{2}}{4}.$$

So for the corrected fiducial $|\psi\rangle = W|\Psi\rangle$, the pure-$Z$ autocorrelation function is the real constant $f(k) = \sqrt{2}/4$ for $k = 1, \ldots, 6$.

This corresponds to the SIC overlap $|f(k)|^2 = 2/16 = 1/8$ at every $k \neq 0$, confirming the pure-$Z$ branch of the SIC condition for the corrected fiducial.

### A.3 The QR-twisted autocorrelation

The triple product $T_{ijk}$ for indices on a single $\mathbb{Z}_7$-axis (the pure-$Z$ branch) reduces to the cube of $f$ evaluated on the cyclic differences. For cyclic triples with all three ordered differences $d_1, d_2, d_3$ in the quadratic residues $\operatorname{QR}_7 = \{1, 2, 4\}$, this gives a value related to $f(\operatorname{QR})^3$.

But the present autocorrelation $f(k) = \sqrt{2}/4$ is real and independent of $k$, so $f^3 = (\sqrt{2}/4)^3 = 2\sqrt{2}/64 = \sqrt{2}/32$ would be real, contradicting the imaginary part $i b \varphi_{ijk}$ established in Theorem 3. The resolution is that the relevant triple product is *not* the pure-$Z$ autocorrelation but the full $WH(7)$-displaced overlap.

For the full SIC triple product, we must consider arbitrary displacements $D_{p, q}$, not pure $Z^k$. The Weyl–Heisenberg covariance of the SIC means that $T_{ijk}$ for displaced projectors $\Pi_{p_i, q_i}$ is computable from the fiducial via
$$T_{p_1, q_1; p_2, q_2; p_3, q_3} = \omega^{\Phi} \cdot \tilde{f}(p_2 - p_1, q_2 - q_1) \cdot \tilde{f}(p_3 - p_2, q_3 - q_2) \cdot \tilde{f}(p_1 - p_3, q_1 - q_3),$$
where $\tilde{f}(p, q) = \langle \psi | D_{p, q} | \psi \rangle$ is the *full* fiducial autocorrelation and $\omega^{\Phi}$ is a Weyl–Heisenberg cocycle phase determined by the displacement triple.

The autocorrelations $\tilde{f}(p, q)$ for $p \neq 0$ are *not* real — they pick up the imaginary structure of the $z_{0, 1}$ components of the fiducial. The QR-vs-NQR distinction in the autocorrelation occurs at the level of $\tilde{f}(p, q)$, not at the pure-$Z$ level.

### A.4 The Closed Form of $\alpha$ and the Cube $\alpha^3 = a + ib$

We now derive the constants $a, b$ in closed form by computing the autocorrelation $\tilde{f}(p, q) = \langle \psi_W | D_{p, q} | \psi_W \rangle$ for the corrected ABGHM fiducial $|\psi_W\rangle = W |\psi\rangle$, where $W = \operatorname{diag}(-1, +1, +1, +1, +1, +1, +1)$ is the unique (up to global phase) Fano-compatible sign-flip matrix established in §6.2. The full numerical record at 50-digit precision is in `outbox/paper10/computations/paper10_appendix_A4_derivation.md`; the verification script is `paper10_appendix_A4_verify.py`.

**Theorem A.4.1** (Autocorrelation structure). *For the corrected ABGHM fiducial $|\psi_W\rangle$, every autocorrelation satisfies $|\tilde{f}(p, q)|^2 = 1/8$. The six $X$-subgroup autocorrelations $\tilde{f}(p, 0)$ split as*
$$\tilde{f}(p, 0) = \begin{cases} \bar\alpha & p \in \{1, 2, 4\} = \operatorname{QR}_7 \\ \alpha & p \in \{3, 5, 6\} = \operatorname{NQR}_7 \end{cases}$$
*where*
$$\alpha = -\frac{(2 - \sqrt{2}) + i\sqrt{2 + 4\sqrt{2}}}{8}.$$
*In particular $|\alpha|^2 = 1/8$.*

*Proof of $|\alpha|^2 = 1/8$.* Direct computation:
$$|\alpha|^2 = \frac{(2 - \sqrt{2})^2 + (2 + 4\sqrt{2})}{64} = \frac{(6 - 4\sqrt{2}) + (2 + 4\sqrt{2})}{64} = \frac{8}{64} = \frac{1}{8}.$$
The values $\tilde{f}(p, 0) \in \{\alpha, \bar\alpha\}$ are verified numerically to 50 significant digits, with residuals below $6.4 \times 10^{-57}$ for all six $X$-subgroup displacements. The QR/NQR split follows from the action of the Frobenius automorphism of $(\mathbb{Z}/7\mathbb{Z})^*$ on the SIC fiducial under the corrected sign convention. $\square$

**Proposition A.4.2** (Cube of $\alpha$). *With $u = 2 - \sqrt{2}$ and $v = \sqrt{2 + 4\sqrt{2}}$, writing $\alpha = -(u + iv)/8$:*
$$\alpha^3 = \frac{\sqrt{2} - 1}{16} + i\,\frac{(\sqrt{2} - 1)\sqrt{2 + 4\sqrt{2}}}{32} = a + ib.$$

*Proof.* Expand:
$$(u + iv)^3 = (u^3 - 3uv^2) + i(3u^2 v - v^3).$$
Direct computation in $\mathbb{Q}(\sqrt{2})$:
$$u^2 = 6 - 4\sqrt{2}, \qquad u^3 = 20 - 14\sqrt{2}, \qquad uv^2 = -4 + 6\sqrt{2}.$$
Subtraction:
$$u^3 - 3uv^2 = (20 - 14\sqrt{2}) - 3(-4 + 6\sqrt{2}) = 32 - 32\sqrt{2} = 32(1 - \sqrt{2}).$$
For the imaginary coefficient, factor: $3u^2 v - v^3 = v(3u^2 - v^2)$, where
$$3u^2 - v^2 = 3(6 - 4\sqrt{2}) - (2 + 4\sqrt{2}) = 16 - 16\sqrt{2} = 16(1 - \sqrt{2}).$$
Therefore
$$(u + iv)^3 = 32(1 - \sqrt{2}) + 16i(1 - \sqrt{2})\, v.$$
Dividing by $-512$ and using $-(1 - \sqrt{2}) = \sqrt{2} - 1$:
$$\alpha^3 = \frac{\sqrt{2} - 1}{16} + i\,\frac{(\sqrt{2} - 1)\, v}{32} = a + ib. \square$$

Numerical verification at 50-digit precision gives $|\operatorname{Re}(\alpha^3) - a| < 4 \times 10^{-58}$ and $|\operatorname{Im}(\alpha^3) - b| < 10^{-58}$.

**Proposition A.4.3** (Fano-line triple products on the $X$-subgroup; zero cocycle phase). *For the zero-sum subsets $L_{\mathrm{QR}} = \{1, 2, 4\}$ and $L_{\mathrm{NQR}} = \{3, 5, 6\}$ in $(\mathbb{Z}/7\mathbb{Z})^*$ (which coincide with the QR and NQR classes), the WH triple products for the corresponding $X$-subgroup SIC triples are*
$$T_{L_{\mathrm{QR}}} = \bar\alpha^3 = a - ib, \qquad T_{L_{\mathrm{NQR}}} = \alpha^3 = a + ib,$$
*with no cocycle correction.*

*Proof.* The triple-product formula for displacements $(p, q)$ and $(r, s)$ is
$$T_{0, (p, q), (r, s)} = \tilde{f}(p, q) \cdot \tau^{qr - ps} \cdot \tilde{f}(r - p, s - q) \cdot \overline{\tilde{f}(r, s)}, \tag{A4-main}$$
which follows from $D_{p, q}^\dagger D_{r, s} = \tau^{qr - ps} D_{r - p, s - q}$ and the anti-unitary symmetry $\tilde{f}(-p, -q) = \overline{\tilde{f}(p, q)}$. For displacements in the $X$-subgroup, $q = s = 0$, so the cocycle phase reduces to $\tau^{0 \cdot r - p \cdot 0} = 1$. The triple product becomes a bare product of three autocorrelations. For $L_{\mathrm{QR}}$, the SIC triple $\{|\psi_0\rangle, |\psi_{(1,0)}\rangle, |\psi_{(3,0)}\rangle\}$ has pairwise displacement differences $(1, 0), (2, 0), (4, 0)$ — all QR — giving $\bar\alpha \cdot \bar\alpha \cdot \overline{\alpha} = \bar\alpha^3$. For $L_{\mathrm{NQR}}$, the triple $\{|\psi_0\rangle, |\psi_{(3,0)}\rangle, |\psi_{(1,0)}\rangle\}$ has differences $(3, 0), (5, 0), (6, 0)$ — all NQR — giving $\alpha \cdot \alpha \cdot \overline{\bar\alpha} = \alpha^3$. Both verified numerically with residual $< 3 \times 10^{-57}$. $\square$

For a Fano-line *cyclic* triple in the $G_2$-orientation sense, the triple product is $\alpha^3 = a + ib$, and for the *anti-cyclic* orientation it is $\bar\alpha^3 = a - ib$. Combining: $T_{ijk} = a + ib \cdot \varphi_{ijk}$ for all Fano-line triples, where $\varphi_{ijk} \in \{+1, -1\}$ is the $G_2$ associative 3-form. This establishes Theorem 3, part (b), with constants $a, b$ in closed form.

*Remark on mixed displacements.* For triples involving displacements with $q \neq 0$ (i.e., not confined to the $X$-subgroup), the cocycle phase $\tau^{qr - ps}$ in (A4-main) is nontrivial, and the individual autocorrelations $\tilde{f}(p, q)$ no longer equal $\alpha$ or $\bar\alpha$ but take generic complex values on the SIC overlap circle $|\tilde{f}|^2 = 1/8$. The non-Fano triple-product ratio $b'/b = (1 + \sqrt{2})/2$ established numerically in §7.3 (Φ Task 3 Phase 4, verified at 50-digit precision) is a statement about mixed-displacement triples; its closed-form analytic derivation is left as an open problem and flagged in §9.4.

### A.5 Universal magnitude $|T|^2 = 1/512$

From Theorem A.4.1, every nontrivial autocorrelation satisfies $|\tilde{f}(p, q)|^2 = 1/8$, which is the SIC overlap value. The triple-product formula (A4-main) expresses $T_{ijk}$ as a product of three autocorrelations multiplied by a unit-modulus cocycle phase $\tau^{qr - ps}$. Taking modulus squared:
$$|T_{ijk}|^2 = |\tilde{f}(p, q)|^2 \cdot |\tilde{f}(r - p, s - q)|^2 \cdot |\overline{\tilde{f}(r, s)}|^2 = \left(\frac{1}{8}\right)^3 = \frac{1}{512}.$$

This confirms Theorem 3, part (a), directly from the SIC defining property: every off-diagonal SIC overlap is $1/8$, so the cube of any three such overlaps has magnitude $1/512$. The universal magnitude is a consequence of the SIC condition and is structurally independent of the Fano-line vs non-Fano distinction.

For the Fano-line case specifically, where $T_{ijk} = a \pm ib$ from Proposition A.4.3, one can also verify $a^2 + b^2 = 1/512$ directly using the algebraic identity $(\sqrt{2} - 1)^2 (6 + 4\sqrt{2}) = 2$ (expansion: $(3 - 2\sqrt{2})(6 + 4\sqrt{2}) = 18 + 12\sqrt{2} - 12\sqrt{2} - 16 = 2$):
$$a^2 + b^2 = \frac{(\sqrt{2} - 1)^2}{256}\left(1 + \frac{2 + 4\sqrt{2}}{4}\right) = \frac{(\sqrt{2} - 1)^2 (6 + 4\sqrt{2})}{1024} = \frac{2}{1024} = \frac{1}{512}. \checkmark$$

### A.6 Non-Fano constants

For non-Fano triples $(i, j, k)$ — those with mixed QR/NQR differences — the triple product picks up an additional Weyl–Heisenberg cocycle phase relative to the all-QR case. The Φ Task 3 computational verification (§4) found that for the specific non-Fano triples studied, the resulting triple product is
$$T_{\mathrm{non-Fano}} = a' + i b' \chi_{ijk}, \qquad a' \approx -0.009152913, \quad b' \approx 0.043235971,$$
with the ratio $b'/b = (1 + \sqrt{2})/2$ verified numerically.

A complete derivation of $a', b'$ in closed form requires enumerating the cocycle phases over all non-Fano triple types and is left as an open problem (§9.4). The numerical evidence is consistent with $a', b'$ being algebraic over $\mathbb{Q}(\sqrt{2})$, and the algebraic ratio $b'/b = (1+\sqrt{2})/2$ admits a direct interpretation: it is the silver ratio over 2, which appears naturally in $\mathbb{Q}(\sqrt{2})$ as the square-root of $(1+\sqrt{2})^2/4 = (3 + 2\sqrt{2})/4$.

### A.7 Origin in Stark units and Legendre symbols

The QR-vs-NQR partition that organizes the autocorrelation function of §A.2–A.4 has its arithmetic origin in the Legendre symbol structure of $\mathbb{Z}_7^*$: the QR class $\{1, 2, 4\}$ is the kernel of the Legendre symbol $\left(\frac{k}{7}\right)$, and the NQR class $\{3, 5, 6\}$ is its non-trivial coset. The Stark-unit construction of the ABGHM fiducial over $\mathbb{Q}(\sqrt{2})$ is itself driven by this Legendre symbol structure (via class field theory at $\mathbb{Q}(\sqrt{-7})$), so the appearance of the QR-partition in the SIC triple-product structure is not a coincidence: it is the same arithmetic input expressed twice — once in the construction of the fiducial, and once in the autocorrelation organization of the resulting SIC frame.

This is the precise sense in which Theorem 3 is "exact for arithmetic reasons": the Stark-unit construction *forces* the QR-partition organization, which in turn *forces* the proportionality between $\operatorname{Im}(T_{ijk})$ and $\varphi_{ijk}$ on Fano lines. The connection between the SIC frame and the $G_2$ associative 3-form runs through the Legendre symbol on $(\mathbb{Z}_7)^*$.

---

## Author Contributions

Conceptualization, methodology, formal analysis, investigation, writing — original draft, writing — review and editing, and supervision: M.L.G. Computational verification was performed by AI research assistants under the author's direction (see *Use of AI Tools* below); the author retains full responsibility for all scientific content.

## Funding

This research received no external funding.

## Institutional Review Board Statement

Not applicable. No human or animal subjects were involved; the paper is a purely mathematical/structural result. The empirical anchors of related papers in the series (Papers 4, 6, 7) are previously published third-party work and are presupposed rather than redeveloped here.

## Informed Consent Statement

Not applicable.

## Data Availability Statement

All computational artifacts supporting this paper are publicly available at https://github.com/MartinLGraise/PCI-Framework on branch `paper7-foundation`, including:

- The 14×49 G₂/SIC coefficient tensor (Theorem 1): `outbox/paper10/computations/paper10_task1_g2_sic_coefficients.json`
- The 128-candidate $W$-enumeration record (Theorem 2): `outbox/paper10/computations/paper10_task2_*`
- The 50-digit triple-product verification (Theorem 3): `outbox/paper10/computations/paper10_task3_*`
- The figure-generation code: `outbox/paper10/figures/build_figures.py`
- An independent verification audit: `outbox/paper10/computations/paper10_task3_c7ro_verification.md`

Every numerical claim in this paper can be reproduced by running the scripts in the cited paths against the public Git history.

## Conflicts of Interest

The author declares no conflicts of interest.

## Use of AI Tools

In accordance with publisher policies on the use of generative AI in scholarly publishing, the author discloses that this manuscript was developed with the assistance of two AI research collaborators: Φ (computational verification, instantiated as Anthropic Claude Dispatch running GAP, Cadabra2, SymPy, and mpmath at 50-digit precision) and C-7RO (synthesis, strategy, editorial review, and prose drafting, instantiated as Perplexity Computer running Claude Sonnet 4.6). External literature support was provided by ChatGPT GPT-5 Pro deep research. Both primary collaborators operated against the public Git repository at github.com/MartinLGraise/PCI-Framework, where every revision, computational output, integrity flag, and counter-argument is version-controlled and publicly auditable. The three independent computational tasks supporting Theorems 1, 2, and 3 were each verified twice — once by Φ's primary computation and once by C-7RO's independent re-derivation — with audit records preserved in the repository. The author retains full responsibility for all scientific content; AI tools were used as research assistants, not as authors.

## Acknowledgments

The author thanks the open-source mathematics community for the foundational results on which this paper depends — in particular the Appleby–Flammia–Fuchs SIC operator basis theorem, the Appleby–Bengtsson–Grassl–Harrison–McConnell exact d=7 Stark-unit fiducial, the Samuel–Gedik classification of d=7 SIC symmetries, and the Baez 2002 indexing of the imaginary octonions. The Klein quartic / PSL(2,7) connection that motivates the broader series owes a debt to Felix Klein's nineteenth-century investigations and to the contemporary expository tradition (Levy, Singerman, Elkies). Particular thanks to Christopher Fuchs, Marcus Appleby, Ingemar Bengtsson, Markus Grassl, and the broader QBism / SIC-POVM community for making the algebraic structure of the d=7 case sufficiently transparent that the connection to G₂ could be discovered. Every quantitative claim in this paper has been independently verified against source material or executed code.

---

## References

References are organized by topical cluster: (i) SIC-POVM foundations and exact constructions; (ii) symmetry classifications of SIC frames; (iii) $G_2$ and octonion algebra; (iv) adjacent exceptional-algebra programs in physics; (v) prior papers in the PCI/PME series; (vi) classical algebraic combinatorics referenced in the discussion.

### SIC-POVM foundations and exact constructions

[1] **Zauner, G.** (1999). *Quantendesigns: Grundzüge einer nichtkommutativen Designtheorie.* Ph.D. thesis, University of Vienna. (Published English translation: *Int. J. Quantum Inf.* 9, 445–507, 2011. DOI 10.1142/S0219749911006776.)

[2] **Renes, J. M., Blume-Kohout, R., Scott, A. J., Caves, C. M.** (2004). "Symmetric informationally complete quantum measurements." *J. Math. Phys.* 45, 2171–2180. DOI 10.1063/1.1737053.

[3] **Appleby, D. M.** (2005). "Symmetric informationally complete-positive operator valued measures and the extended Clifford group." *J. Math. Phys.* 46, 052107. DOI 10.1063/1.1842008.

[4] **Scott, A. J., Grassl, M.** (2010). "Symmetric informationally complete positive-operator-valued measures: A new computer study." *J. Math. Phys.* 51, 042203. DOI 10.1063/1.3374022.

[5] **Appleby, D. M., Flammia, S. T., Fuchs, C. A.** (2011). "The Lie algebraic significance of symmetric informationally complete measurements." *J. Math. Phys.* 52, 022202. DOI 10.1063/1.3555805.  *[The basis theorem; central to Theorem 1 of the present paper.]*

[6] **Fuchs, C. A., Hoang, M. C., Stacey, B. C.** (2017). "The SIC question: history and state of play." *Axioms* 6, 21. DOI 10.3390/axioms6030021.

[7] **Kopp, G. S.** (2021). "SIC-POVMs and the Stark conjectures." *Int. Math. Res. Not.* 2021, 13812–13838. DOI 10.1093/imrn/rnz153.

[8] **Appleby, D. M., Bengtsson, I., Grassl, M., Harrison, M., McConnell, G.** (2022). "SIC-POVMs from Stark units." *J. Math. Phys.* 63, 112205. DOI 10.1063/5.0083520.  *[The exact d=7 fiducial used throughout the present paper.]*

[9] **Appleby, D. M., Flammia, S. T., Kopp, G. S.** (2025). "All dimensions admit SIC-POVMs." arXiv:2501.03970.

[10] **Bengtsson, I.** (2020). "SIC and Hopf links." *Found. Phys.* 50, 1794–1814. DOI 10.1007/s10701-020-00318-8.

### SIC symmetry classifications and prime-dimension structure

[11] **Zhu, H.** (2010). "SIC POVMs and Clifford groups in prime dimensions." *J. Phys. A: Math. Theor.* 43, 305305. DOI 10.1088/1751-8113/43/30/305305.

[12] **Samuel, J., Gedik, Z.** (2024). "Symmetries of d=7 SIC-POVMs." *J. Phys. A: Math. Theor.* 57, 295304. DOI 10.1088/1751-8121/ad5ca9.  *[The 147-element symmetry group $WH(7)\rtimes C_3$; central to Theorem 2.]*

[13] **Stacey, B. C.** (2021). *A First Course in the Sporadic SICs.* SpringerBriefs in Mathematical Physics. DOI 10.1007/978-3-030-76104-2.

### $G_2$, octonions, and the Fano plane

[14] **Baez, J. C.** (2002). "The octonions." *Bull. Amer. Math. Soc.* 39, 145–205. DOI 10.1090/S0273-0979-01-00934-X.  *[The Fano-plane indexing of imaginary octonions used throughout §4.]*

[15] **Conway, J. H., Smith, D. A.** (2003). *On Quaternions and Octonions: Their Geometry, Arithmetic, and Symmetry.* A K Peters / CRC Press.

[16] **Cartan, É.** (1894). *Sur la structure des groupes de transformations finis et continus.* Thèse, Paris. *[Original construction of $G_2$ as the automorphism group of the octonions.]*

[17] **Bryant, R. L.** (1987). "Metrics with exceptional holonomy." *Ann. Math.* 126, 525–576. DOI 10.2307/1971360.

[18] **Fernández, M., Gray, A.** (1982). "Riemannian manifolds with structure group $G_2$." *Ann. Mat. Pura Appl.* 132, 19–45. DOI 10.1007/BF01760975.

[19] **Semmelmann, U., Weingart, G.** (2021). "The standard Laplace operator." *J. Geom. Anal.* 31, 8639–8696. DOI 10.1007/s12220-021-00838-3.

### Adjacent exceptional-algebra programs in physics (§8)

[20] **Furey, N.** (2014). "Generations: three prints, in colour." *J. High Energy Phys.* 2014, 046. DOI 10.1007/JHEP10(2014)046.

[21] **Furey, N.** (2018). "$SU(3)_C \times SU(2)_L \times U(1)_Y(\times U(1)_X)$ as a symmetry of division algebraic ladder operators." *Eur. Phys. J. C* 78, 375. DOI 10.1140/epjc/s10052-018-5844-7.

[22] **Furey, N.** (2025). "Three generations from a single octonion vector space." *Phys. Lett. B* (online, accepted manuscript). DOI 10.1016/j.physletb.2025.139473.

[23] **Boyle, L., Farnsworth, S.** (2015). "Non-commutative geometry, non-associative geometry and the standard model of particle physics." *J. High Energy Phys.* 2015, 023. DOI 10.1007/JHEP07(2015)023.

[24] **Boyle, L., Farnsworth, S.** (2018). "A new algebraic structure in the standard model of particle physics." *J. High Energy Phys.* 2018, 071. DOI 10.1007/JHEP06(2018)071.

[25] **Todorov, I.** (2023). "Octonions, exceptional Jordan algebra and the role of the group $F_4$ in particle physics." *Universe* 9, 222. DOI 10.3390/universe9050222.

### PCI/PME framework series (prior papers)

[26] **Graise, M. L.** (2025). *QBism and $G_2$ via PSL(2,7)* (Paper 4). Zenodo. DOI 10.5281/zenodo.19617662.

[27] **Graise, M. L.** (2025). *The 6/7 contraction* (Paper 6). Zenodo. DOI 10.5281/zenodo.19672709.

[28] **Graise, M. L.** (2026). *A thermodynamic ceiling on coherence in self-modeling observers* (Paper 7). Zenodo. DOI 10.5281/zenodo.19773185.

### Classical algebraic combinatorics (§7.4 / §9.4)

[29] **Paley, R. E. A. C.** (1933). "On orthogonal matrices." *J. Math. Phys.* 12, 311–320. DOI 10.1002/sapm1933121311.

[30] **Klein, F.** (1879). "Über die Transformation siebenter Ordnung der elliptischen Funktionen." *Math. Ann.* 14, 428–471. *[Original construction of the Klein quartic and its $\mathrm{PSL}(2,7)$ automorphism group; cited for the Fano-plane / Klein-quartic combinatorial structure underlying §5.5(F3).]*

[31] **Singerman, D.** (1988). "Klein's Riemann surface of genus 3 and regular embeddings of finite projective planes." *Bull. London Math. Soc.* 20, 297–304. DOI 10.1112/blms/20.4.297.

[32] **Elkies, N. D.** (1999). "The Klein quartic in number theory." In *The Eightfold Way: The Beauty of Klein's Quartic Curve* (S. Levy, ed.), MSRI Publications 35, Cambridge University Press, pp. 51–101.

---

*End of master draft. Drafted 2026-04-30 / 2026-05-01 by Martin Luther Graise with computational support from Φ (Anthropic Claude Dispatch) and synthesis support from C-7RO (Perplexity Computer).*
