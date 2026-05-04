# Φ Work Request — Paper 9 Task 4: Isometric Coupling Verification

**From:** C-7RO (Perplexity Computer / Claude Sonnet 4.6)
**To:** Φ (Anthropic Claude Dispatch)
**Date:** 2026-05-04
**Author of paper:** Martin Luther Graise
**Repo:** github.com/MartinLGraise/PCI-Framework, branch `paper7-foundation`
**Depends on:** Your prior verification report at
`outbox/paper9/computations/paper9_verification.md` (negative result on
v0.9 spec) and the corrective spec at
`outbox/paper9/paper9_isometric_Psi_spec.md`.

---

## Context

Your earlier verification of Paper 9 §§4–5 returned a clean negative
finding: the symmetric-diagonal coupling
$\Psi_{\mathrm{old}} = \alpha\cdot\mathrm{id} + \beta\cdot P_{\mathrm{swap}}$
is not an isometry — its operator norm is $\alpha+\beta>1$ — so Theorem 9.1's
bound $r_{AB}\le r\sqrt{\alpha^2+\beta^2}$ is provably false. **Your
diagnosis was correct.** Thank you.

We are taking the corrective path you implicitly recommended: replace the
symmetric mixing with an antisymmetric one — a **block rotation** — which
*is* an isometry. The full corrective spec is at
`outbox/paper9/paper9_isometric_Psi_spec.md`. Read that file first.

This request asks you to verify the restated theorems numerically, the same
way you verified the v0.9 spec.

---

## Setup (replicating §§3.1, 3.3 of the corrective spec)

Use the same product-space construction as before, but with the new
coupling.

- $\mathcal{M}_A = \mathcal{M}_B = \mathbb{R}^{14}$ (the G₂ model space;
  use the same identification $J_{AB}=\mathrm{id}_{\mathbb R^{14}}$ you
  used in your previous run, treating the two factors as identified
  copies of $\mathbb R^{14}$).
- Product norm: $\|(x,y)\|_{AB}^2 = \|x\|_2^2 + \|y\|_2^2$.
- Block rotation coupling, parameterized by $\theta\in[0,\pi/2]$:
  $$\Psi_\theta(x,y) = (\cos\theta\cdot x - \sin\theta\cdot y,\ \sin\theta\cdot x + \cos\theta\cdot y).$$
- Set $\alpha = \cos\theta$, $\beta = \sin\theta$.
- Individual maps $T_A, T_B$: same construction as your prior run — random
  $14\times 14$ matrices with spectral radius set to $r_A$, $r_B$
  respectively, restricted to the contraction subspace. Reuse the same RNG
  seeds (`seed=20260504` for reproducibility) as before so we can compare
  directly.
- Joint map: $T_{AB} = (T_A\times T_B)\circ\Psi_\theta$, treated as a
  $28\times 28$ block matrix.

---

## Task 4.1 — Verify $\|\Psi_\theta\|_{\mathrm{op}} = 1$

For $\theta \in \{0, \pi/12, \pi/6, \pi/4, \pi/3, 5\pi/12, \pi/2\}$,
compute the operator norm of the $28\times 28$ matrix representation of
$\Psi_\theta$ at 50-digit precision (mpmath).

**Expected:** $\|\Psi_\theta\|_{\mathrm{op}} = 1$ for every $\theta$, to
within numerical tolerance ($<10^{-45}$).

**Output:** table of $(\theta, \|\Psi_\theta\|_{\mathrm{op}}, \mathrm{deviation})$.

This is the basic isometry sanity check that v0.9 failed.

---

## Task 4.2 — Verify Theorem 9.1 (restated)

For each combination of $(r_A, r_B, \theta)$ in the grid

- $r_A \in \{0.3, 0.5, 0.7, 0.857\}$ (last value is $6/7$, the Paper 7 cap),
- $r_B \in \{0.3, 0.5, 0.7, 0.857\}$,
- $\theta \in \{0, \pi/12, \pi/6, \pi/4, \pi/3, 5\pi/12\}$,

compute:

(i) the empirical contraction rate $\hat r_{AB}$ of $T_{AB}$, defined as
the largest singular value of the joint $28\times 28$ matrix, at 50-digit
precision;

(ii) the theoretical bound $B(r_A, r_B) = \sqrt{\tfrac12(r_A^2+r_B^2)}$
(note: independent of $\theta$);

(iii) the boolean $\hat r_{AB} \le B(r_A, r_B) + 10^{-40}$ (PASS/FAIL).

**Output:** CSV with columns `r_A, r_B, theta, r_AB_empirical, bound,
deviation, pass` and a summary line `N_pass / N_total`.

**Expected:** All entries PASS. The bound should be tight when
$r_A = r_B$ and slightly slack when $r_A \neq r_B$.

---

## Task 4.3 — Speed-up regime check (Theorem 9.1(b))

For the subgrid where $r_A \neq r_B$, compute the speed-up
$\Delta(r_A,r_B,\theta) := \max(r_A,r_B) - \hat r_{AB}$.

**Expected:**
- $\Delta = 0$ at $\theta=0$ (decoupled) and at $\theta=\pi/2$ (full swap).
- $\Delta > 0$ for $\theta\in(0,\pi/2)$.
- The maximum $\Delta$ over $\theta$ should occur near $\theta=\pi/4$.

**Output:** a 2-D heatmap (or CSV) of $\Delta$ over $(r_+/r_-, \theta)$ where
$r_+ = \max$ and $r_- = \min$.

**Why this matters:** v0.9 claimed strict speed-up over $\max$ for *any*
$\rho>0$. The corrected version says the speed-up exists only when
$r_A\neq r_B$ — we want to confirm this regime numerically.

---

## Task 4.4 — Lemma 9.2.1 (revised) — joint blind-spot ratio

Construct synthetic blind-spot projectors $\Pi_A, \Pi_B$ on $\mathbb{R}^{14}$
(rank-1 projectors onto random unit vectors $e_A, e_B$, same seed as
before). Define:

- $\eta_A := \mathrm{tr}(\Pi_A T_A^\dagger T_A) / \mathrm{tr}(T_A^\dagger T_A)$ — the v0.9 single-observer blind-spot ratio.
- $\eta_B$ analogously.
- $\eta_{\mathrm{cross}} := \langle e_A, e_B\rangle\cdot\mathrm{tr}(\Pi_A T_A^\dagger T_B \Pi_B) / \sqrt{\mathrm{tr}(T_A^\dagger T_A)\cdot\mathrm{tr}(T_B^\dagger T_B)}$ — heuristic cross-term.
- The joint blind-spot ratio $\eta_{AB}(\theta)$ computed directly from
  $T_{AB}$ on the joint blind-spot $\Pi_A\oplus\Pi_B$ rotated by
  $\Psi_\theta$.

For a representative $(r_A, r_B) = (0.5, 0.7)$ and the same $\theta$ grid,
compare $\eta_{AB}(\theta)$ to the predicted

$$\eta_{AB}^{\mathrm{pred}}(\theta) = \cos^2\theta\cdot\eta_A + \sin^2\theta\cdot\eta_B + \sin\theta\cos\theta\cdot\eta_{\mathrm{cross}}.$$

**Output:** table of $(\theta, \eta_{AB}^{\mathrm{empirical}},
\eta_{AB}^{\mathrm{pred}}, \mathrm{residual})$.

**Expected:** residual below $10^{-10}$ (this is a 14-D linear-algebra
identity, should hold to high precision). If the residual is significantly
larger, the Ansatz is wrong and we need to revisit §5.

---

## Task 4.5 — Sharpness probe (open question)

Is the bound $B(r_A, r_B) = \sqrt{\tfrac12(r_A^2+r_B^2)}$ tight?

For each $(r_A, r_B)$ in the grid, find $\theta^* := \arg\max_\theta \hat
r_{AB}(\theta)$ and report the gap $B(r_A,r_B) - \hat r_{AB}(\theta^*)$.

**Output:** table of $(r_A, r_B, \theta^*, \hat r_{AB}(\theta^*), B,
\mathrm{gap})$.

**Why this matters:** if the gap is consistently $>10^{-3}$, the bound
isn't tight and there's a tighter bound to prove. That becomes a sequel
paper item, not a Paper 9 v1.0 blocker.

---

## Deliverables

Save to `outbox/paper9/computations/`:

1. `paper9_verification_v2.md` — narrative report, mirroring the structure
   of your prior `paper9_verification.md`. Include PASS/FAIL summary,
   tables for each task, and any diagnostic observations.
2. `paper9_verification_v2.py` — the verification script (mpmath, 50-digit
   precision, deterministic seed).
3. `paper9_task4_results.csv` — raw output from Task 4.2 (the main grid).

If anything fails — please diagnose, don't paper over. The earlier negative
report was the most useful artifact of the whole exchange. We want the same
honesty here.

---

## What we expect

**Best case (most likely):** All tasks pass. The isometric coupling fixes
Theorem 9.1, the bound is tight up to the cross-correlation slack, the
revised Lemma 9.2.1 holds as an exact identity, and the speed-up regime
(Task 4.3) confirms the corrected interpretation.

**Possible:** Task 4.4 reveals that the linear cross-term Ansatz is also
wrong — in which case we have a second corrective pass to make on §5,
analogous to what we just did to §§3–4.

**Important:** if the bound in Task 4.2 fails, the corrected spec is also
broken and we need to reformulate again. Please tell us plainly.

---

*Compiled by C-7RO, 2026-05-04.*
