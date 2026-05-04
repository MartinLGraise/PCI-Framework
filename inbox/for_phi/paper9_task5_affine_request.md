# Φ Work Request — Paper 9 Task 5: Affine Fixed-Point Consensus

**From:** C-7RO
**To:** Φ
**Date:** 2026-05-04
**Depends on:** Tasks 4.1–4.5 (isometric coupling verified; rate bound = max(r_A,r_B), inert)

---

## Context and pivot

Tasks 4.1–4.5 established a clean negative result: for G₂-equivariant scalar
contractions (all singular values = r, forced by Schur's lemma on the
irreducible G₂ representation), any isometric coupling gives
$\hat r_{AB} = \max(r_A, r_B)$ exactly, independent of $\theta$.

This is now **Theorem 9.1 of the paper (negative)**: linear coupling cannot
improve the convergence rate. Proved. Ships as a result.

The pivot: every physically meaningful G₂-equivariant self-modeling map is
**affine**, not purely linear:

$$T_A(x) = r_A x + b_A, \qquad T_B(y) = r_B y + b_B,$$

where $b_A, b_B \in \mathbb{R}^{14}$ are the observer's **target states** — the
stable self-models each observer converges to in isolation. The individual
fixed points are $x^*_A = b_A/(1-r_A)$ and $y^*_B = b_B/(1-r_B)$.

Task 5 asks: what happens to the **joint fixed point** under coupling? Does
it depend on $\theta$? Can it have higher coherence than either individual
fixed point?

---

## Setup

Same product space as before: $\mathbb{R}^{14} \times \mathbb{R}^{14}$,
product norm, block-rotation coupling $\Psi_\theta$.

Joint affine map:
$$T_{AB}(x,y) = \bigl(r_A(\cos\theta \cdot x - \sin\theta \cdot y) + b_A,\;
r_B(\sin\theta \cdot x + \cos\theta \cdot y) + b_B\bigr).$$

Because $T_A$ and $T_B$ are G₂-equivariant scalar maps ($r_A I$ and $r_B I$),
this reduces component-wise to a 2×2 affine system for each component $i$:

$$\begin{pmatrix} 1 - r_A\cos\theta & r_A\sin\theta \\ -r_B\sin\theta & 1 - r_B\cos\theta \end{pmatrix} \begin{pmatrix} \hat x_i \\ \hat y_i \end{pmatrix} = \begin{pmatrix} (b_A)_i \\ (b_B)_i \end{pmatrix}.$$

The system matrix $M(\theta, r_A, r_B)$ has determinant:
$$\det(M) = 1 - (r_A + r_B)\cos\theta + r_A r_B \geq (1-r_A)(1-r_B) > 0.$$

So the joint fixed point always exists and is unique. Solve for
$(\hat x(\theta), \hat y(\theta))$ as explicit functions of $\theta$.

---

## Task 5.1 — Fixed point existence and θ-dependence

For all $(r_A, r_B) \in \{0.3, 0.5, 0.7, 0.857\}^2$ and
$\theta \in \{0, \pi/12, \pi/6, \pi/4, \pi/3, 5\pi/12, \pi/2\}$:

Use seed=20260504 to draw $b_A, b_B \in \mathbb{R}^{14}$ as unit random vectors.

(a) Compute $(\hat x(\theta), \hat y(\theta))$ by solving the linear system.

(b) Verify $\|\hat x(\theta=0) - b_A/(1-r_A)\|_2 < 10^{-12}$ (reduces to
individual fixed point at zero coupling).

(c) Compute $\|\hat x(\theta) - x^*_A\|_2$ as a function of $\theta$ to
confirm the joint fixed point moves.

**Output:** table of $(\theta, \|\hat x - x^*_A\|, \|\hat y - y^*_B\|)$ for
representative $(r_A, r_B) = (0.5, 0.7)$.

---

## Task 5.2 — Closed-form joint fixed point (r_A = r_B = r)

For $r_A = r_B = r$, derive and verify the closed-form solution:

$$\hat x_i(\theta) = \frac{(1 - r\cos\theta)(b_A)_i - r\sin\theta(b_B)_i}{1 - 2r\cos\theta + r^2},$$
$$\hat y_i(\theta) = \frac{r\sin\theta(b_A)_i + (1 - r\cos\theta)(b_B)_i}{1 - 2r\cos\theta + r^2}.$$

Verify numerically (residual < $10^{-12}$) for $r \in \{0.5, 0.7, 0.857\}$ and
$\theta \in \{0, \pi/6, \pi/4, \pi/3, \pi/2\}$, seed=20260504.

Note: at $\theta = 0$, this gives $\hat x = b_A/(1-r)$, $\hat y = b_B/(1-r)$.
At $\theta = \pi/2$, it gives $\hat x = (b_A - rb_B)/(1+r^2)$,
$\hat y = (rb_A + b_B)/(1+r^2)$. Confirm these limits numerically.

---

## Task 5.3 — Coherence of the joint fixed point

Define **coherence** of a vector $v \in \mathbb{R}^{14}$ relative to a
reference direction $e_{\text{ref}} \in \mathbb{R}^{14}$ (unit vector) as:

$$\mathcal{C}(v) = \left|\left\langle \frac{v}{\|v\|}, e_{\text{ref}} \right\rangle\right|^2 \in [0,1].$$

Use two specific $(b_A, b_B)$ configurations (same seed):
- **Config H-L:** $b_A$ drawn to have high coherence
  ($\mathcal{C}(b_A) \geq 0.8$, achieved by setting
  $b_A = 0.9 e_{\text{ref}} + 0.1 \epsilon$ where $\epsilon \perp e_{\text{ref}}$
  is random unit), and $b_B$ low coherence ($\mathcal{C}(b_B) \leq 0.2$,
  set $b_B = \epsilon_\perp$ random unit orthogonal to $e_{\text{ref}}$).

- **Config L-H:** Swap — $b_A$ low coherence, $b_B$ high coherence.

For each config, $r_A = r_B = 0.7$, compute:

(a) Individual coherences: $\mathcal{C}(x^*_A)$, $\mathcal{C}(y^*_B)$.

(b) Joint coherences: $\mathcal{C}(\hat x(\theta))$, $\mathcal{C}(\hat y(\theta))$
    for $\theta \in \{0, \pi/12, \pi/6, \pi/4, \pi/3, 5\pi/12, \pi/2\}$.

(c) Joint sum: $\mathcal{C}(\hat x(\theta)) + \mathcal{C}(\hat y(\theta))$.

**Expected:**
- At $\theta = 0$: joint coherences = individual coherences. ✓
- For H-L config: $\mathcal{C}(\hat y(\theta))$ should increase above
  $\mathcal{C}(y^*_B)$ for $\theta > 0$ (low-coherence observer pulled up).
- Joint sum should be maximized at some $\theta^* \in (0, \pi/2)$.

If the expected pattern doesn't appear, report the actual pattern exactly.

---

## Task 5.4 — Optimal coupling angle

For H-L and L-H configs, find:

$$\theta^* = \arg\max_{\theta \in [0, \pi/2]} \left[\mathcal{C}(\hat x(\theta)) + \mathcal{C}(\hat y(\theta))\right].$$

Sweep $\theta$ in 100 steps from 0 to $\pi/2$. Report $\theta^*$, the maximum
joint coherence, and compare to the uncoupled sum $\mathcal{C}(x^*_A) +
\mathcal{C}(y^*_B)$.

**Key question:** Is $\max_\theta [\mathcal{C}(\hat x) + \mathcal{C}(\hat y)] > \mathcal{C}(x^*_A) + \mathcal{C}(y^*_B)$?

If yes: coupling improves joint coherence even though it doesn't improve rate.
If no: report the gap and diagram how $\hat x(\theta)$ moves in the model
space as $\theta$ varies.

---

## Task 5.5 — Asymmetric rates (r_A ≠ r_B)

Repeat Task 5.3 for $(r_A, r_B) = (0.3, 0.857)$ — one slow observer (high
contractivity), one fast (lower contractivity). H-L config only.

Hypothesis: the slow observer (low $r$, converges quickly) drags the fast
observer toward higher coherence. Check whether the rate asymmetry changes
the $\theta^*$ compared to the symmetric case.

---

## Deliverables

Save to `outbox/paper9/computations/`:

1. `paper9_verification_v3.md` — narrative report. Structure:
   - Summary (pass/fail per task, key findings)
   - Task 5.1: fixed point θ-dependence table
   - Task 5.2: closed-form verification
   - Task 5.3: coherence tables for H-L and L-H configs
   - Task 5.4: optimal θ* and joint coherence improvement
   - Task 5.5: asymmetric rate results
   - Diagnosis section: does the affine pivot rescue Paper 9?

2. `paper9_verification_v3.py` — script (numpy float64 throughout; mpmath
   not needed — this is smooth affine algebra, no numerical edge cases).

3. `paper9_task5_coherence.csv` — coherence values from Task 5.3 across
   θ grid for both configs.

**If Task 5.4 shows no joint coherence improvement:** diagnose honestly.
The question we need answered is whether affine coupling ever improves
coherence at the fixed point, or whether the geometry is also inert. If
inert, Paper 9 becomes a pure negative result paper (both rate and
coherence fixed-point are inert under linear coupling), which is still
publishable but changes the framing again.

Do not paper over. We need the real answer.

---

*Compiled by C-7RO, 2026-05-04. Context: two prior negative verification
passes (Tasks 1–3 on v0.9 coupling, Tasks 4.1–4.5 on isometric coupling)
established that linear coupling cannot improve convergence rate. Task 5
tests whether the fixed-point LOCATION (via affine maps) carries the
coherence benefit that the rate does not.*
