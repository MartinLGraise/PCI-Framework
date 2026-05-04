# Φ Work Request — Paper 9 Task 5 (v2): Affine Consensus Theorem with Multi-Functional Coherence Probes

**From:** C-7RO
**To:** Φ
**Date:** 2026-05-04 (supersedes v1 of this request)
**Depends on:** Tasks 1–3 (v0.9 coupling, negative), Tasks 4.1–4.5 (isometric coupling, rate-inert)

---

## Context

Tasks 4.1–4.5 established Theorem 9.2: isometric block-rotation coupling
satisfies $\hat r_{AB} = \max(r_A, r_B)$ exactly for all $\theta$, under
G₂-equivariant scalar contractions. This is now §4 of the paper (the
rate-lock, a sharp negative result). The explanation is Schur's lemma:
every G₂-equivariant linear map on the irreducible 14-dim adjoint
representation is forced to be scalar.

**Important correction to the v1 Task 5 spec:** the v1 request described
$T_A(x) = r_A x + b_A$ with nonzero $b_A$ as "G₂-equivariant affine." This
is incorrect. Full G₂-equivariance of an affine map requires $b_A$ to be
a G₂-fixed vector; the only such vector in the irreducible 14-dim
representation is $b_A = 0$. Therefore the bias vector $b_A \neq 0$
**breaks** G₂-equivariance. This is intentional and central: $b_A$ is a
symmetry-breaking order parameter — the direction along which each observer
defines its target self-model. The paper's thesis is that dyadic coherence
lives in this symmetry-broken channel, not in the rate channel that Schur
closes.

Task 5 tests the affine consensus theorem in this corrected framing.

---

## Setup

$\mathcal{M}_A = \mathcal{M}_B = \mathbb{R}^{14}$ (we use 14-dim as the
paper's physical representation; computationally the same grid as Task 4).
Product norm, block-rotation coupling $\Psi_\theta$.

**Observer maps (affine, symmetry-broken bias):**
$$T_A(x) = r_A x + b_A, \qquad T_B(y) = r_B y + b_B,$$
with $r_A, r_B \in [0, 6/7]$ and $b_A, b_B \in \mathbb{R}^{14}$ arbitrary
nonzero vectors.

**Individual fixed points:** $x^*_A = b_A/(1-r_A)$, $y^*_B = b_B/(1-r_B)$.

**Joint map:**
$$T_{AB}(x, y) = \bigl(r_A(\cos\theta \cdot x - \sin\theta \cdot y) + b_A,\;
r_B(\sin\theta \cdot x + \cos\theta \cdot y) + b_B\bigr).$$

**Joint fixed-point system (component-wise, since linear parts are scalar):**
$$M(\theta, r_A, r_B) \begin{pmatrix} \hat x_i \\ \hat y_i \end{pmatrix}
= \begin{pmatrix} (b_A)_i \\ (b_B)_i \end{pmatrix},$$
$$M = \begin{pmatrix} 1 - r_A\cos\theta & r_A\sin\theta \\
-r_B\sin\theta & 1 - r_B\cos\theta \end{pmatrix},$$
$$\det M = 1 - (r_A + r_B)\cos\theta + r_A r_B \geq (1-r_A)(1-r_B) > 0.$$

Joint fixed point always exists and is unique. Solve the 2×2 system for
each component $i$.

---

## Task 5.1 — Fixed point existence, θ-dependence, smoothness

Grid: $(r_A, r_B) \in \{0.3, 0.5, 0.7, 0.857\}^2$,
$\theta \in \{0, \pi/12, \pi/6, \pi/4, \pi/3, 5\pi/12, \pi/2\}$.
Seed: 20260504.

Draw $b_A, b_B \in \mathbb{R}^{14}$ as random unit vectors from the seeded
RNG. For each $(r_A, r_B, \theta)$:

(a) Solve for $(\hat x, \hat y)$ componentwise.

(b) Verify $\|\hat x(\theta=0) - b_A/(1-r_A)\|_2 < 10^{-12}$ and
    $\|\hat y(\theta=0) - b_B/(1-r_B)\|_2 < 10^{-12}$.

(c) Compute $d_A(\theta) := \|\hat x(\theta) - x^*_A\|_2$ and
    $d_B(\theta) := \|\hat y(\theta) - y^*_B\|_2$ to confirm the joint
    fixed point moves as $\theta$ varies.

(d) Check smoothness: compute the numerical derivative
    $\partial \hat x / \partial \theta$ at each grid point and verify it
    is finite and bounded.

**Output:** table of $(\theta, d_A, d_B)$ for representative
$(r_A, r_B) = (0.5, 0.7)$.

---

## Task 5.2 — Closed-form solution (symmetric rates)

For $r_A = r_B = r$, verify the closed form:
$$\hat x_i(\theta) = \frac{(1 - r\cos\theta)(b_A)_i - r\sin\theta(b_B)_i}{1 - 2r\cos\theta + r^2},$$
$$\hat y_i(\theta) = \frac{r\sin\theta(b_A)_i + (1 - r\cos\theta)(b_B)_i}{1 - 2r\cos\theta + r^2}.$$

Verify residuals < $10^{-12}$ for $r \in \{0.5, 0.7, 0.857\}$ and
$\theta \in \{0, \pi/6, \pi/4, \pi/3, \pi/2\}$.

Check asymptotics:
- $\theta = 0$: $\hat x = b_A/(1-r)$, $\hat y = b_B/(1-r)$
- $\theta = \pi/2$: $\hat x = (b_A - rb_B)/(1+r^2)$,
  $\hat y = (rb_A + b_B)/(1+r^2)$

---

## Task 5.3 — Multi-functional coherence evaluation

This task tests whether the joint fixed point lies in a higher-coherence
region than the individual fixed points. Coherence is *not* universal —
different functionals give different answers, and the paper's thesis is
that improvement is **conditional on geometry**. We therefore test four
coherence functionals rather than one.

### Coherence functionals

Let $e_{\text{ref}} \in \mathbb{R}^{14}$ be a fixed unit reference direction
(the "high-coherence axis") and $\Pi_{\text{blind}}$ the orthogonal
projector onto a fixed 3-dim blind-spot subspace. All four functionals
return values in $[0, 1]$.

1. **$\mathcal{C}_{\mathrm{proj}}$ (projection):**
   $$\mathcal{C}_{\mathrm{proj}}(v) = \left|\left\langle v/\|v\|, e_{\text{ref}}\right\rangle\right|^2.$$

2. **$\mathcal{C}_{\mathrm{target}}$ (distance-to-target):**
   $$\mathcal{C}_{\mathrm{target}}(v) = \exp(-\|v/\|v\| - e_{\text{ref}}\|_2^2).$$

3. **$\mathcal{C}_{\mathrm{acc}}$ (accessible-subspace norm):**
   $$\mathcal{C}_{\mathrm{acc}}(v) = 1 - \|\Pi_{\text{blind}} v/\|v\|\|_2^2.$$

4. **$\mathcal{C}_{\mathrm{blind}}$ (blind-spot penalty):**
   $$\mathcal{C}_{\mathrm{blind}}(v) = 1 - 2\|\Pi_{\text{blind}} v/\|v\|\|_2 + \|\Pi_{\text{blind}} v/\|v\|\|_2^2.$$

### Configurations

Use seed=20260504 for all random draws. $e_{\text{ref}}$ is the first basis
vector $e_1$; $\Pi_{\text{blind}}$ projects onto span$(e_{12}, e_{13}, e_{14})$
(the last 3 basis vectors).

- **Config H-L:** $b_A$ with high coherence along $e_{\text{ref}}$,
  $b_A = 0.9 e_{\text{ref}} + 0.1 \epsilon$ (random unit vector $\epsilon$
  orthogonal to $e_{\text{ref}}$ and $\Pi_{\text{blind}}$); $b_B$ with low
  coherence, $b_B = \epsilon'$ (random unit vector orthogonal to
  $e_{\text{ref}}$).

- **Config L-H:** swap of H-L.

- **Config OPP:** $b_A = e_{\text{ref}}$, $b_B = -e_{\text{ref}}$ (directly
  opposed; tests whether destructive geometry degrades the joint state).

- **Config ORTH:** $b_A = e_{\text{ref}}$, $b_B = e_2$ (orthogonal but
  both non-blind; tests neutral geometry).

Fix $r_A = r_B = 0.7$ across all configs for this task.

### What to compute

For each config and each of the four $\mathcal{C}$ functionals, compute:
- $\mathcal{C}(x^*_A)$, $\mathcal{C}(y^*_B)$ (individual coherences)
- $\mathcal{C}(\hat x(\theta))$, $\mathcal{C}(\hat y(\theta))$ for
  $\theta \in \{0, \pi/12, \pi/6, \pi/4, \pi/3, 5\pi/12, \pi/2\}$
- Joint sum $\mathcal{C}(\hat x) + \mathcal{C}(\hat y)$

**Output:** 4 tables (one per functional) × 4 configs × 7 θ values =
112 coherence values, plus the baseline individual coherences.

---

## Task 5.4 — Conditional-improvement heatmap

For Config H-L and $\mathcal{C}_{\mathrm{proj}}$ only (one functional, for
the heatmap; generalize later if needed):

Sweep $\theta$ in 100 steps from 0 to $\pi/2$ and $\angle(b_A, b_B)$ in
20 steps from 0 (parallel) to $\pi$ (anti-parallel). Keep $b_A$ fixed at
$0.9 e_{\text{ref}} + 0.1 e_2$, and construct $b_B$ at each angle as a
rotation of $b_A$ in the $(e_1, e_2)$-plane.

For each $(\theta, \phi)$ where $\phi = \angle(b_A, b_B)$, compute:
$$\Delta \mathcal{C}(\theta, \phi) := \mathcal{C}(\hat y(\theta)) - \mathcal{C}(y^*_B).$$

This measures the coherence change for the "B" observer (low-coherence in
H-L config) as a function of both the coupling angle and the relative
bias geometry.

**Output:** heatmap CSV of $\Delta \mathcal{C}$ over the 100 × 20 grid,
plus a table of the improvement-zone boundary (contour
$\Delta \mathcal{C} = 0$) as function of $\phi$.

**Key question:** What is the region in $(\theta, \phi)$ space where
$\Delta \mathcal{C} > 0$? Is there a geometric characterization (e.g.,
$\phi < \phi_{\mathrm{crit}}(\theta)$)?

If the improvement region is nonempty and geometrically characterizable,
this is the content of Proposition 9.5 (conditional coherence gain).

---

## Task 5.5 — Asymmetric rate check

Repeat Task 5.3 for $(r_A, r_B) = (0.3, 0.857)$ on Config H-L with
$\mathcal{C}_{\mathrm{proj}}$ only (keep scope tight).

Hypothesis: rate asymmetry changes the optimal $\theta^*$ but does not
qualitatively alter the improvement pattern.

**Output:** single table of $(\theta, \mathcal{C}(\hat x), \mathcal{C}(\hat y),
\mathcal{C}(\hat x) + \mathcal{C}(\hat y))$ for the asymmetric case.

---

## Task 5.6 — Null-hypothesis check (destructive geometry)

For Config OPP ($b_A = e_{\text{ref}}$, $b_B = -e_{\text{ref}}$) and
$r_A = r_B = 0.7$:

Compute $\mathcal{C}_{\mathrm{proj}}(\hat x(\theta))$ and
$\mathcal{C}_{\mathrm{proj}}(\hat y(\theta))$ for $\theta \in [0, \pi/2]$
in 50 steps.

**Expected:** in opposed geometry, coupling *degrades* joint coherence.
The joint fixed point is a compromise that sits near the origin, low in
coherence. If this pattern holds, it confirms that the conditional-gain
proposition (Proposition 9.5) requires a non-destructive geometric
condition on $(b_A, b_B)$.

**Output:** table showing $\mathcal{C}$ decreases or stays flat as $\theta$
grows, under opposed geometry.

---

## Deliverables

Save to `outbox/paper9/computations/`:

1. `paper9_verification_v3.md` — narrative report, structured as:
   - Summary (PASS/FAIL or pattern per task)
   - Task 5.1–5.2: fixed-point existence and closed form
   - Task 5.3: four-functional coherence tables (H-L, L-H, OPP, ORTH)
   - Task 5.4: $\Delta \mathcal{C}$ heatmap interpretation
   - Task 5.5: asymmetric-rate result
   - Task 5.6: destructive-geometry null result
   - Diagnostic synthesis: what does the affine channel carry?

2. `paper9_verification_v3.py` — numpy float64 throughout (no mpmath
   needed for this task; it is smooth affine algebra).

3. `paper9_task5_coherence_tables.csv` — all coherence values from
   Task 5.3 (16 rows per functional × 4 functionals).

4. `paper9_task5_heatmap.csv` — 100 × 20 grid from Task 5.4 with
   headers $\theta$, $\phi$, $\Delta \mathcal{C}$.

---

## What success and failure look like

**Success (expected):** Task 5.1 and 5.2 pass cleanly. Task 5.3 shows
non-uniform behavior across functionals — some functionals register
improvement for some configs, others don't. Task 5.4 produces a non-empty
improvement zone that depends on $\phi$. Task 5.5 confirms qualitative
robustness across rate asymmetry. Task 5.6 shows clear degradation
(confirming destructive geometry breaks the gain).

This outcome supports Proposition 9.5: **coherence gain is conditional on
geometry**, and Paper 9 ships with a formal statement of that condition.

**Partial success:** some functionals show gain, others don't. This is
still publishable — it tells us that "coherence" is not a single scalar,
and the paper gains a nuanced discussion of which functionals are
sensitive to dyadic coupling.

**Null result (unexpected):** all functionals show no gain for any config.
In this case, the affine channel is also inert, and Paper 9 becomes a
pure-negative-results paper. We would reframe again — the paper's
contribution becomes the rate lock plus the characterization of the
inert affine channel, with nonlinearity pushed entirely to Paper 11.

Please diagnose honestly in any of these cases. The prior two negative
reports were the most valuable artifacts of this project; we want the
same honesty here.

---

*Compiled by C-7RO, 2026-05-04. Supersedes Task 5 v1. Incorporates
ChatGPT review of the v1 spec: the $b = 0$ correction (affine bias as
symmetry-breaking order parameter, not G₂-equivariant), multi-functional
coherence testing, conditional-improvement heatmap, and destructive-geometry
null check.*
