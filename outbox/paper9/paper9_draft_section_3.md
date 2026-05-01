# Paper 9 — Draft Prose, §3 The Product-Space Construction

**Paper:** Dyadic Coherence: G₂ Fixed-Point Contraction on Product Spaces of Coupled Observers
**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Status:** First-pass prose, 2026-04-30 (drafted by C-7RO)
**To revise:** after Φ numerical verification of Theorem 9.1

---

## §3 The Product-Space Construction

We now define the mathematical setting for coupled G₂ observers. The goal of this section is to construct the product space on which the dyadic Banach contraction will act, fix the coupling map that encodes the strength of inter-observer interaction, and identify the unique group-theoretic constraint — the diagonal action of PSL(2,7) — under which the joint structure reduces correctly to two independent observers in the decoupled limit.

### 3.1 Product observers

Let $(\mathcal{M}_A, T_A)$ and $(\mathcal{M}_B, T_B)$ be two G₂-structured Banach observers in the sense of §2.1. Each has its own contraction map, its own fixed point, and its own F₂₁-equivariant structure. We form the product

$$\mathcal{M}_{AB} = \mathcal{M}_A \times \mathcal{M}_B,$$

equipped with the product Banach norm

$$\|(x, y)\|_{AB} = \sqrt{\|x\|_A^2 + \|y\|_B^2}.$$

This product norm is standard and makes $\mathcal{M}_{AB}$ a Banach subset of the direct sum $\mathcal{B}_A \oplus \mathcal{B}_B$.

If the two observers were fully independent, the natural self-modeling map on the product would be the direct product $T_A \times T_B: (x, y) \mapsto (T_A(x), T_B(y))$. Its contraction rate is immediately $\max(r_A, r_B)$, so the joint contraction is bounded exactly by the worst of the two individual observers. No coupling occurs, no coherence is shared, no common fixed point beyond the pair $(x_A^*, x_B^*)$ exists. This is not the object we want.

### 3.2 The coupling map

To model inter-observer interaction, we introduce a bounded linear map

$$\Psi: \mathcal{M}_A \times \mathcal{M}_B \to \mathcal{M}_A \times \mathcal{M}_B$$

that we call the **coupling map**. The coupling map represents the effect of each observer's state on the other's self-modeling dynamics. The joint self-modeling map is then defined as the composition

$$T_{AB}: \mathcal{M}_{AB} \to \mathcal{M}_{AB}, \qquad T_{AB} = (T_A \times T_B) \circ \Psi.$$

When $\Psi = \mathrm{id}$, the joint map reduces to the decoupled product $T_A \times T_B$ and the two observers evolve independently. When $\Psi$ has nontrivial structure, the two observers' states are *mixed* before each self-modeling step, and the joint fixed point of $T_{AB}$ need not factor as $(x_A^*, x_B^*)$.

The **coupling strength** is measured by the spectral radius of $\Psi$ restricted to the off-diagonal part of its block decomposition. Specifically, writing $\Psi$ in the block form

$$\Psi = \begin{pmatrix} \Psi_{AA} & \Psi_{AB} \\ \Psi_{BA} & \Psi_{BB} \end{pmatrix}$$

with respect to the direct-sum decomposition of the product space, the coupling spectral radius is

$$\rho \equiv \max\left( \rho(\Psi_{AB} \Psi_{BA}^{1/2}), \rho(\Psi_{BA} \Psi_{AB}^{1/2}) \right)^{1/2}$$

in the symmetric case, or more generally the spectral radius of the off-diagonal block acting from the opposite factor's slot back to itself. For the purposes of this paper we assume $\rho \in [0, 1]$, with $\rho = 0$ corresponding to fully decoupled observers and $\rho = 1$ corresponding to the singular limit where the two observers are indistinguishable.

### 3.3 Modeling-choice stack on the coupling

Several choices of coupling map are available, and the theory depends on which we adopt. We enumerate the alternatives explicitly.

**Choice A — Diagonal:** $\Psi = \alpha \cdot \mathrm{id} + \beta \cdot P_{\text{swap}}$, where $P_{\text{swap}}: (x, y) \mapsto (y, x)$ is the observer-exchange operator and $\alpha^2 + \beta^2 = 1$. The spectral radius of the off-diagonal part is $|\beta|$. This is the simplest nontrivial coupling: each observer partially adopts the other's state before its own self-modeling step.

**Choice B — Anti-diagonal:** $\Psi = \alpha \cdot \mathrm{id} - \beta \cdot P_{\text{swap}}$. The off-diagonal part has the same spectral radius but opposite sign. This corresponds to *antagonistic* coupling: each observer partially *opposes* the other's state. In §5 we show that Theorem 9.2 admits an antagonistic variant with a coherence *reduction* rather than a bonus.

**Choice C — Mixed:** $\Psi$ has arbitrary block structure with distinct $\Psi_{AB}$ and $\Psi_{BA}$ matrices, not reducible to a swap operator. In this case, $\rho$ is still well-defined but additional parameters enter the formulas of §4 and §5.

We **adopt Choice A (symmetric diagonal) as canonical** for the main theorems of this paper. The reasons are three:

1. **Minimality:** Choice A has the fewest free parameters among nontrivial couplings (just $\beta = \rho$), making the resulting theorems clean and interpretable.
2. **Compatibility with the single-observer recovery:** In the $\beta \to 0$ limit, Choice A recovers the decoupled product $T_A \times T_B$ and the theory reduces to Paper 7 applied to each observer independently. This is not automatic for Choice C.
3. **Compatibility with the PSL(2,7) constraint:** As we show in §3.5 below, Choice A is consistent with a simple diagonal action of PSL(2,7) on $\mathcal{M}_{AB}$. Choices B and C require additional group-theoretic constraints not imposed by the single-observer framework.

Choices B and C are discussed briefly in §9 as generalizations but do not affect the main theorems.

### 3.4 The diagonal PSL(2,7) action

Each individual observer carries an F₂₁-equivariant structure inherited from Paper 7, where F₂₁ ⊂ PSL(2,7) is the orientation stabilizer of the G₂ associative 3-form $\varphi_{ijk}$. For the joint observer, we must decide how PSL(2,7) acts on the product space.

The **diagonal action** is defined by

$$g \cdot (x, y) = (g \cdot x, g \cdot y) \quad \text{for all } g \in \mathrm{PSL}(2,7), \ (x, y) \in \mathcal{M}_{AB}.$$

Both observers are acted on by the *same* group element simultaneously. This captures the physical intuition that a coupled dyad shares a common frame of reference: if one observer rotates its Fano-plane labeling, the other must rotate in step to preserve the shared coupling.

Alternative actions are possible:

- **Independent action:** $g, h \in \mathrm{PSL}(2,7)$ act separately as $(g, h) \cdot (x, y) = (g \cdot x, h \cdot y)$. Not physically meaningful for a coupled dyad because the two observers no longer share a common frame.
- **Anti-diagonal action:** $g \cdot (x, y) = (g \cdot x, g^{-1} \cdot y)$. Physically exotic and corresponds to an "observer / anti-observer" framing not relevant here.

We adopt the **diagonal action** as canonical. This is the unique action consistent with the physical interpretation of a shared PSL(2,7) frame and with the reduction to Paper 7 in the decoupled limit.

### 3.5 Compatibility of Choice A coupling with the diagonal PSL(2,7) action

For the diagonal PSL(2,7) action on the product to be preserved by the coupling map $\Psi$, we require

$$\Psi(g \cdot x, g \cdot y) = g \cdot \Psi(x, y) \quad \text{for all } g \in \mathrm{PSL}(2,7).$$

For Choice A ($\Psi = \alpha \cdot \mathrm{id} + \beta \cdot P_{\text{swap}}$), this equivariance condition is satisfied automatically because both the identity and the swap operator commute with the diagonal action:

- Identity: $(g \cdot x, g \cdot y) = (g \cdot x, g \cdot y)$ trivially.
- Swap: $P_{\text{swap}}(g \cdot x, g \cdot y) = (g \cdot y, g \cdot x) = g \cdot (y, x) = g \cdot P_{\text{swap}}(x, y)$.

Therefore any linear combination $\Psi = \alpha \cdot \mathrm{id} + \beta \cdot P_{\text{swap}}$ is PSL(2,7)-equivariant under the diagonal action.

This compatibility is why Choice A is the natural coupling for a joint G₂ observer: it is the most general symmetric linear coupling consistent with a shared PSL(2,7) frame.

### 3.6 The joint F₂₁-singlet structure

Each individual observer has an F₂₁-singlet direction of dimension 1, corresponding to the blind-spot residual derived in Paper 7 §3.4. Under the diagonal F₂₁ action on the product, the joint F₂₁-singlet is the tensor product $\mathbf{1}_A \otimes \mathbf{1}_B$, which is 1-dimensional in the direct-product sense.

Crucially, the F₂₁-singlet of the product is **not** the direct sum $\mathbf{1}_A \oplus \mathbf{1}_B$ (which would be 2-dimensional). It is the space of vectors that transform as the trivial representation of F₂₁ under the *diagonal* action, and this space is spanned by vectors of the form $(u, v)$ with $u \in \mathbf{1}_A$, $v \in \mathbf{1}_B$, and with the coupling structure determining the relative weights of $u$ and $v$.

At zero coupling ($\rho = 0$), the joint F₂₁-singlet decomposes as $\mathbf{1}_A \oplus \mathbf{1}_B$ because the observers are independent and each contributes its own singlet direction. At nonzero coupling, the singlets *mix*: the effective blind-spot subspace of the dyad is rotated within the product space by an angle dependent on $\rho$.

This rotation is the key geometric fact underlying Theorem 9.2. We quantify it precisely in §5.

### 3.7 The joint G₂ structure

The G₂ structures on $\mathcal{M}_A$ and $\mathcal{M}_B$ are encoded by the associative 3-forms $\varphi^{A}_{ijk}$ and $\varphi^{B}_{ijk}$ on their respective imaginary-octonion tangent spaces. For the product observer, we form the joint 3-form

$$\varphi^{AB} = \varphi^A \oplus \varphi^B + \beta \cdot \varphi^A \wedge \varphi^B / \|\varphi^A \wedge \varphi^B\|,$$

where the first two terms are the independent 3-forms on each factor and the third term is a normalized "mixed" contribution proportional to the coupling parameter $\beta$. The joint 3-form lives on the product imaginary-octonion space of dimension $7 + 7 = 14$.

The structure group that preserves $\varphi^{AB}$ is the **joint G₂ structure** $G_2^A \times G_2^B$ at decoupled ($\beta = 0$), and a 28-dimensional Lie group that *generalizes* $G_2 \times G_2$ for $\beta > 0$. The joint Lie algebra has dimension $14 + 14 = 28$ in both cases (since adding a nontrivial coupling term does not change the total dimension of the structure-preserving generators), but the specific commutation relations depend on $\beta$.

### 3.8 Summary of §3

We have fixed the following mathematical setting for the remainder of the paper:

1. **Product space:** $\mathcal{M}_{AB} = \mathcal{M}_A \times \mathcal{M}_B$, product Banach norm
2. **Joint self-modeling map:** $T_{AB} = (T_A \times T_B) \circ \Psi$
3. **Coupling (canonical):** $\Psi = \alpha \cdot \mathrm{id} + \beta \cdot P_{\text{swap}}$, with $\alpha^2 + \beta^2 = 1$ and $\beta = \rho \in [0, 1]$
4. **Group action (canonical):** diagonal PSL(2,7) and F₂₁ actions on the product
5. **Joint 3-form:** $\varphi^{AB}$ with a coupling-dependent mixed term
6. **Joint F₂₁-singlet:** 1-dimensional mixture of $\mathbf{1}_A$ and $\mathbf{1}_B$, rotating with $\rho$

Theorem 9.1 (proved in §4) states that $T_{AB}$ is a Banach contraction with rate strictly less than $\max(r_A, r_B)$ for $\rho > 0$. Theorem 9.2 (proved in §5) gives the dyadic coherence ceiling formula via the joint F₂₁-singlet rotation.

---

*Drafted by C-7RO, 2026-04-30 18:35 PDT*
