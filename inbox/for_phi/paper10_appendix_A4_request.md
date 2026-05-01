# Φ Work Request — Paper 10 Appendix A.4 Phase-Angle Derivation

**From:** Martin (via C-7RO)
**Date drafted:** 2026-05-01
**Priority:** Polish — does not block submission, tightens Appendix A
**Estimated effort:** 2–4 hours of computation + LaTeX prose
**Output destination:** `outbox/paper10/computations/paper10_appendix_A4_derivation.md`

---

## Context

Paper 10 master draft is at `outbox/paper10/paper10_master_draft.md` (commit `ec3fc8d` and later on branch `paper7-foundation`). Appendix A derives the constants $a, b$ of Theorem 3 part (b) from the autocorrelation structure of the corrected ABGHM fiducial.

The current §A.4 derivation has one weak step: it writes
$$\alpha^3 = a + ib$$
via $\alpha = r e^{i\phi}$ but reverse-engineers $r, \phi$ from the known target rather than computing them from first principles. The result is correct (verified by your Task 3 at 50-digit precision) but the prose currently reads "we know the answer, here's the consistency check."

This request asks for the missing step: a clean *forward* derivation of $\alpha$ from the corrected ABGHM fiducial, computing $\alpha^3$ in closed form, and showing that the result equals $(\sqrt{2}-1)/16 + i (\sqrt{2}-1)\sqrt{2 + 4\sqrt{2}}/32$.

---

## Inputs available

All in `outbox/paper10/computations/`:

- `paper10_task3_compute.py` — your existing 50-digit verification computation (mpmath). The autocorrelation function $\tilde{f}(p, q)$ for $WH(7)$-displacements is computed there.
- `paper10_task3_triple_products.json` — verified triple-product values, including `exact_values.f1_exact = "f(1) = -[(2-sqrt(2)) + i*sqrt(2+4*sqrt(2))] / 8"`.
- `paper10_task3_results.md` §6 — the autocorrelation organization you found.
- `paper10_master_draft.md` Appendix A — the current prose.

Note that `f(1)` here refers to the *full* fiducial autocorrelation $\tilde{f}(1, ?)$, not the pure-$Z$ branch $f(k) = \langle\psi|Z^k|\psi\rangle$ which is real. The question is which $(p, q)$ pair this corresponds to.

---

## Three concrete tasks

### Task A4.1 — Identify $\alpha$

Compute $\tilde{f}(p, q) = \langle \psi | D_{p, q} | \psi \rangle$ for the corrected ABGHM fiducial $|\psi\rangle = W |\Psi\rangle$ at all 48 nontrivial displacements.

Identify which $(p, q)$ correspond to "QR-cyclic-axis" displacements such that $\tilde{f}$ takes the constant value $\alpha$, and which correspond to NQR with value $\bar{\alpha}$. Confirm:
- $|\alpha|^2 = 1/8$ (SIC condition)
- $\alpha^3 = a + ib$ (the Fano-line cyclic triple product)

Report $\alpha$ in closed form over $\mathbb{Q}(\sqrt{2}, i)$. The conjecture from `exact_values.f1_exact` is
$$\alpha = -\frac{(2-\sqrt{2}) + i\sqrt{2 + 4\sqrt{2}}}{8},$$
which should give $|\alpha|^2 = ((2-\sqrt{2})^2 + (2 + 4\sqrt{2}))/64 = (6 - 4\sqrt{2} + 2 + 4\sqrt{2})/64 = 8/64 = 1/8$. ✓

Verify this $\alpha$ formula against your numerical $\tilde{f}(p, q)$ values and confirm which $(p, q)$ pairs realize it.

### Task A4.2 — Closed-form cube

Compute $\alpha^3$ symbolically (SymPy or mpmath with high precision + algebraic recognition):

$$\alpha = -\frac{(2-\sqrt{2}) + i\sqrt{2 + 4\sqrt{2}}}{8}$$

Show that
$$\alpha^3 = \frac{\sqrt{2}-1}{16} + i \cdot \frac{(\sqrt{2}-1)\sqrt{2 + 4\sqrt{2}}}{32} = a + ib.$$

This should be a direct algebraic computation. The minus sign of $\alpha$ enters as $(-1)^3 = -1$, so the verification is

$$\left(\frac{(2-\sqrt{2}) + i\sqrt{2 + 4\sqrt{2}}}{8}\right)^3 \stackrel{?}{=} -\left(\frac{\sqrt{2}-1}{16} + i \cdot \frac{(\sqrt{2}-1)\sqrt{2 + 4\sqrt{2}}}{32}\right).$$

Expand and simplify. The relevant algebraic identity is $(2-\sqrt{2})^2 - (2 + 4\sqrt{2}) = 6 - 4\sqrt{2} - 2 - 4\sqrt{2} = 4 - 8\sqrt{2}$ for the real-part-of-$\alpha^2$ piece, and $2(2-\sqrt{2})\sqrt{2 + 4\sqrt{2}}$ for the cross term. The full expansion of $\alpha^3 = \alpha \cdot \alpha^2$ should land cleanly.

Provide the full step-by-step algebraic derivation, suitable for inclusion in Appendix A.4 verbatim.

### Task A4.3 — Cocycle phase tracking

The Weyl–Heisenberg cocycle phase $\omega^\Phi$ for a triple of displacements $D_{p_1, q_1}, D_{p_2, q_2}, D_{p_3, q_3}$ is determined by the symplectic form on $\mathbb{Z}_7^2$. Verify that for a cyclic Fano-line triple of displacements (all with the same QR class on the Fano axis), the cocycle phase is real (so $T_{\mathrm{Fano, cyclic}} = \alpha^3$ without phase correction).

For non-Fano triples (mixed-residue-class), compute the cocycle phase and identify the constants $a', b'$ in closed form. The conjecture from §7.3 is that $b'/b = (1 + \sqrt{2})/2$ exactly. Verify this analytically — not just numerically.

If the closed-form derivation of $a'$ is too combinatorially heavy, partial progress is fine: identify the cocycle phase formula, show $b'/b = (1+\sqrt{2})/2$ exactly, and leave $a'$ closed form as an open problem within Appendix A (already flagged in §9.4).

---

## Deliverable format

A markdown file `outbox/paper10/computations/paper10_appendix_A4_derivation.md` containing:

1. **Setup** — definitions of $\alpha$, $\tilde{f}(p,q)$, the QR-cyclic-axis correspondence
2. **Task A4.1 result** — explicit $\alpha$ formula + numerical verification table
3. **Task A4.2 result** — full algebraic expansion of $\alpha^3 = a + ib$
4. **Task A4.3 result** — cocycle phase computation, $b'/b$ proof, $a'$ status
5. **Suggested replacement prose for Appendix A.4** — clean LaTeX-ready paragraphs that C-7RO can drop into the master draft

The replacement prose should be self-contained: a reader should follow the derivation without consulting the computation file.

---

## Why this matters

Appendix A is the only place in Paper 10 where we admit the derivation is incomplete. Closing this gap converts Theorem 3 part (b) from "verified at 50-digit precision plus a consistency-check sketch" to "fully derived in closed form over $\mathbb{Q}(\sqrt{2}, i)$." For a *Foundations of Physics* or *J. Math. Phys.* submission, that's the difference between "this looks right" and "this is the result."

---

*Drafted by C-7RO, 2026-05-01 10:35 PDT.*
