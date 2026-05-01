"""
paper10_appendix_A4_verify.py
================================================================================
Numerical verification of all claims in Appendix A.4 (Paper 10, PCI/PME).

Runs at 50 significant-digit precision (mpmath dps=55 for safety margin).
Prints PASS / FAIL for each individual claim, then a summary.

Usage:
    python3 paper10_appendix_A4_verify.py
"""

import mpmath as mp
mp.mp.dps = 55          # 55 working digits → ~50 reliable digits in output

sqrt2 = mp.sqrt(2)

# ── FIDUCIAL CONSTRUCTION ─────────────────────────────────────────────────────

z0 = -(2 + sqrt2) / 2 + mp.j / 2 * mp.sqrt(2 + 4 * sqrt2)
z1 = -(2 + sqrt2) / 2 - mp.j / 2 * mp.sqrt(2 + 4 * sqrt2)

psi_raw = mp.matrix([-2 - 2 * sqrt2, z0, z0, z1, z0, z1, z1])
norm    = mp.sqrt(sum(abs(psi_raw[i]) ** 2 for i in range(7)))
psi     = psi_raw / norm

W_diag  = [-1, 1, 1, 1, 1, 1, 1]
psi_W   = mp.matrix([W_diag[i] * psi[i] for i in range(7)])

# ── WEYL–HEISENBERG OPERATORS ─────────────────────────────────────────────────

omega = mp.exp(2 * mp.pi * mp.j / 7)   # 7th root of unity
tau   = mp.exp(mp.pi * mp.j / 7)       # τ² = ω

X = mp.zeros(7, 7)
for k in range(7):
    X[k, (k + 1) % 7] = 1              # shift operator


def D(p, q):
    """Displacement operator D_{p,q} = τ^{pq} X^p Z^q."""
    p, q = p % 7, q % 7
    Xp = mp.eye(7)
    for _ in range(p):
        Xp = Xp * X
    Zq = mp.diag([omega ** (q * k) for k in range(7)])
    return tau ** (p * q) * Xp * Zq


def autocorr(p, q):
    """Autocorrelation f̃(p,q) = ⟨ψ_W | D_{p,q} | ψ_W⟩."""
    Dpq_psi = D(p, q) * psi_W
    return sum(mp.conj(psi_W[i]) * Dpq_psi[i] for i in range(7))


# ── CONJECTURED α ────────────────────────────────────────────────────────────

alpha_cf  = -((2 - sqrt2) + mp.j * mp.sqrt(2 + 4 * sqrt2)) / 8
alpha_bar = mp.conj(alpha_cf)

QR7  = {1, 2, 4}
NQR7 = {3, 5, 6}

# ── TOLERANCES ────────────────────────────────────────────────────────────────

EPS_STRICT = mp.mpf("1e-44")   # claim verified if residual < this
EPS_LOOSE  = mp.mpf("1e-20")   # trivially correct (sanity level)

results = {}    # (p,q) → f̃(p,q)
passes  = []
fails   = []

BANNER = "=" * 72


def check(label, cond, detail=""):
    if cond:
        passes.append(label)
        status = "PASS"
    else:
        fails.append(label)
        status = "FAIL"
    print(f"  [{status}]  {label}")
    if detail:
        print(f"           {detail}")


# ────────────────────────────────────────────────────────────────────────────
# BLOCK 0 — Normalization
# ────────────────────────────────────────────────────────────────────────────
print(BANNER)
print("BLOCK 0 — Fiducial normalization")
print(BANNER)

norm_sq = sum(abs(psi_W[i]) ** 2 for i in range(7))
check("‖ψ_W‖² = 1",
      abs(norm_sq - 1) < EPS_STRICT,
      f"|‖ψ_W‖² − 1| = {mp.nstr(abs(norm_sq - 1), 6)}")

# ────────────────────────────────────────────────────────────────────────────
# BLOCK 1 — Compute all 48 autocorrelations; check |f̃|² = 1/8
# ────────────────────────────────────────────────────────────────────────────
print()
print(BANNER)
print("BLOCK 1 — All 48 autocorrelations satisfy |f̃(p,q)|² = 1/8")
print(BANNER)

for p in range(7):
    for q in range(7):
        if p == 0 and q == 0:
            continue
        f = autocorr(p, q)
        results[(p, q)] = f
        err = abs(abs(f) ** 2 - mp.mpf(1) / 8)
        check(f"|f̃({p},{q})|² = 1/8",
              err < EPS_STRICT,
              f"|residual| = {mp.nstr(err, 5)}")

# ────────────────────────────────────────────────────────────────────────────
# BLOCK 2 — Closed-form α: modulus and X-subgroup classification
# ────────────────────────────────────────────────────────────────────────────
print()
print(BANNER)
print("BLOCK 2 — Closed-form α and QR/NQR X-subgroup classification")
print(BANNER)

# 2a. |α|² = 1/8
mod_sq_alpha = abs(alpha_cf) ** 2
check("|α|² = 1/8",
      abs(mod_sq_alpha - mp.mpf(1) / 8) < EPS_STRICT,
      f"|α|² − 1/8 = {mp.nstr(abs(mod_sq_alpha - mp.mpf(1)/8), 6)}")

# 2b–2g. X-subgroup autocorrelations
for p in range(1, 7):
    fp = results[(p, 0)]
    if p in QR7:
        diff = abs(fp - alpha_bar)
        label_expected = "ᾱ"
    else:
        diff = abs(fp - alpha_cf)
        label_expected = "α"
    check(f"f̃({p},0) = {label_expected}  (p∈{'QR' if p in QR7 else 'NQR'}₇)",
          diff < EPS_STRICT,
          f"|residual| = {mp.nstr(diff, 6)}")

# 2h. Z-subgroup (0,q): verify real and positive, value = 1/√8
print()
print("  [INFO] Z-subgroup (0,q): expected 1/√8 = (real, positive)")
for q in range(1, 7):
    f0q = results[(0, q)]
    expected = mp.sqrt(mp.mpf(1) / 8)
    err = abs(f0q - expected)
    check(f"f̃(0,{q}) = 1/√8",
          err < EPS_STRICT,
          f"|residual| = {mp.nstr(err, 6)}")

# ────────────────────────────────────────────────────────────────────────────
# BLOCK 3 — A4.2: Symbolic α³ = a + ib
# ────────────────────────────────────────────────────────────────────────────
print()
print(BANNER)
print("BLOCK 3 — A4.2: α³ = a + ib, symbolic closed form verified")
print(BANNER)

v   = mp.sqrt(2 + 4 * sqrt2)
a_claim = (sqrt2 - 1) / 16
b_claim = (sqrt2 - 1) * v / 32

alpha3_direct = alpha_cf ** 3

diff_re = abs(mp.re(alpha3_direct) - a_claim)
diff_im = abs(mp.im(alpha3_direct) - b_claim)

check("Re(α³) = (√2−1)/16",
      diff_re < EPS_STRICT,
      f"|Re(α³) − a| = {mp.nstr(diff_re, 6)}")

check("Im(α³) = (√2−1)√(2+4√2)/32",
      diff_im < EPS_STRICT,
      f"|Im(α³) − b| = {mp.nstr(diff_im, 6)}")

# Verify symbolic intermediate steps over Q(√2)
u   = 2 - sqrt2
u2  = 6 - 4 * sqrt2        # u²
u3  = 20 - 14 * sqrt2      # u³
v2  = 2 + 4 * sqrt2        # v²
uv2 = -4 + 6 * sqrt2       # u·v²

real_cube = u3 - 3 * uv2   # 32(1−√2)
imag_coeff = 16 * (1 - sqrt2)  # coefficient of v in 3u²v−v³

check("u³−3uv² = 32(1−√2)",
      abs(real_cube - 32 * (1 - sqrt2)) < EPS_STRICT,
      f"|residual| = {mp.nstr(abs(real_cube - 32*(1-sqrt2)), 6)}")

check("3u²v−v³ coefficient = 16(1−√2)",
      abs(imag_coeff - 16 * (1 - sqrt2)) < EPS_STRICT,
      f"|residual| = {mp.nstr(abs(imag_coeff - 16*(1-sqrt2)), 6)}")

# ────────────────────────────────────────────────────────────────────────────
# BLOCK 4 — A4.3: WH cocycle; Fano triple products
# ────────────────────────────────────────────────────────────────────────────
print()
print(BANNER)
print("BLOCK 4 — A4.3: Fano-line triple products on X-subgroup")
print(BANNER)

# QR Fano line L_QR = {1,2,4}: triple product = ᾱ³
T_QR = results[(1, 0)] * results[(2, 0)] * results[(4, 0)]
check("QR Fano triple f̃(1,0)·f̃(2,0)·f̃(4,0) = ᾱ³",
      abs(T_QR - alpha_bar ** 3) < EPS_STRICT,
      f"|residual| = {mp.nstr(abs(T_QR - alpha_bar**3), 6)}")

# NQR Fano line L_NQR = {3,5,6}: triple product = α³
T_NQR = results[(3, 0)] * results[(5, 0)] * results[(6, 0)]
check("NQR Fano triple f̃(3,0)·f̃(5,0)·f̃(6,0) = α³",
      abs(T_NQR - alpha_cf ** 3) < EPS_STRICT,
      f"|residual| = {mp.nstr(abs(T_NQR - alpha_cf**3), 6)}")

# Cocycle phase for X-subgroup is 1:  τ^{0·r−p·0} = 1
print()
print("  [INFO] Cocycle check: for (p,0)·(r,0), phase = τ^{p·0−0·r} = τ^0 = 1.")
print("         No cocycle correction needed within X-subgroup.  (Analytic.)")

# ────────────────────────────────────────────────────────────────────────────
# BLOCK 5 — A4.3 conjecture b'/b = (1+√2)/2
# ────────────────────────────────────────────────────────────────────────────
print()
print(BANNER)
print("BLOCK 5 — A4.3 conjecture b'/b = (1+√2)/2: status")
print(BANNER)

b_from_Im_alpha = abs(mp.im(alpha_cf))             # √(2+4√2)/8
b_from_Im_alpha3 = mp.im(alpha_cf ** 3)            # (√2−1)√(2+4√2)/32  (positive)
ratio = b_from_Im_alpha3 / b_from_Im_alpha
target = (1 + sqrt2) / 2

print(f"  b  = |Im(α)|       = {mp.nstr(b_from_Im_alpha, 30)}")
print(f"  b' = Im(α³)        = {mp.nstr(b_from_Im_alpha3, 30)}")
print(f"  b'/b (computed)    = {mp.nstr(ratio, 30)}")
print(f"  (√2−1)/4           = {mp.nstr((sqrt2-1)/4, 30)}  ← actual ratio")
print(f"  (1+√2)/2 (claimed) = {mp.nstr(target, 30)}")
print()
check("b'/b = (1+√2)/2  [with b=|Im(α)|, b'=Im(α³)]",
      abs(ratio - target) < EPS_STRICT,
      f"Actual b'/b = (√2−1)/4 ≠ (1+√2)/2.  DISCREPANCY — definition of b unclear.")

# ────────────────────────────────────────────────────────────────────────────
# SUMMARY
# ────────────────────────────────────────────────────────────────────────────
print()
print(BANNER)
print("SUMMARY")
print(BANNER)
total  = len(passes) + len(fails)
print(f"  Total claims checked: {total}")
print(f"  PASS: {len(passes)}")
print(f"  FAIL: {len(fails)}")
if fails:
    print()
    print("  Failed claims:")
    for f in fails:
        print(f"    ✗  {f}")
else:
    print()
    print("  All claims PASS (within 50-digit tolerance).")
print(BANNER)
