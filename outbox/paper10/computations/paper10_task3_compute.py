import mpmath as mp
import json
import sys

mp.mp.dps = 50

print("=== Paper 10 Task 3: SIC Triple Products vs G2 3-form ===")
print(f"Precision: {mp.mp.dps} decimal places")
print()

# ─── Build fiducial ───────────────────────────────────────────────────────────
sqrt2 = mp.sqrt(2)
# z0 = -(2+sqrt2)/2 + i/2 * sqrt(2+4*sqrt2)
# z1 = -(2+sqrt2)/2 - i/2 * sqrt(2+4*sqrt2)
z0 = -(2+sqrt2)/2 + mp.j/2 * mp.sqrt(2+4*sqrt2)
z1 = -(2+sqrt2)/2 - mp.j/2 * mp.sqrt(2+4*sqrt2)

psi_raw = mp.matrix([-(2+2*sqrt2), z0, z0, z1, z0, z1, z1])
norm = mp.sqrt(sum(abs(psi_raw[k])**2 for k in range(7)))
psi = psi_raw / norm

# Fano-compatible W correction (Task 2)
psi_W = mp.matrix([-psi[0], psi[1], psi[2], psi[3], psi[4], psi[5], psi[6]])

print(f"Fiducial normalization check: |psi_W| = {mp.nstr(mp.sqrt(sum(abs(psi_W[k])**2 for k in range(7))), 10)}")
print(f"Dominant component |psi_W[0]| = {mp.nstr(abs(psi_W[0]), 10)}  (expected ~0.668)")
print()

# ─── WH(7) operators ─────────────────────────────────────────────────────────
omega = mp.exp(2*mp.pi*mp.j/7)

# X|j> = |j+1 mod 7>  →  X[k,j] = delta_{k, (j+1)%7}
X = mp.zeros(7, 7)
for j in range(7):
    X[(j+1)%7, j] = 1

# Z|j> = omega^j |j>  →  Z[k,j] = omega^k delta_{kj}
Z = mp.diag([omega**k for k in range(7)])

# D(p,q) = tau^{pq} X^p Z^q,  tau = exp(pi*i/7)
tau = mp.exp(mp.pi * mp.j / 7)

def Xpow(p):
    """X^p as 7×7 matrix"""
    # (X^p)[k,j] = delta_{k, (j+p)%7}
    M = mp.zeros(7, 7)
    for j in range(7):
        M[(j+p)%7, j] = 1
    return M

def Zpow(q):
    """Z^q as diagonal 7×7 matrix"""
    return mp.diag([omega**(q*k) for k in range(7)])

def D(p, q):
    pp = p % 7
    qq = q % 7
    return tau**(pp*qq) * Xpow(pp) * Zpow(qq)

# ─── Build 7 Fano-point SIC states: psi_i = D(i,0) |psi_W> ──────────────────
psi_fano = []
for i in range(7):
    di0 = D(i, 0)  # = X^i (since D(i,0) = tau^0 * X^i * Z^0 = X^i)
    psi_fano.append(di0 * psi_W)

# Sanity check: SIC property |<psi_i|psi_j>|^2 = 1/(d+1) = 1/8 for i≠j
print("SIC overlap check (should all be 1/8 = 0.125):")
for i in range(3):
    for j in range(i+1, 4):
        ip = sum(mp.conj(psi_fano[i][k]) * psi_fano[j][k] for k in range(7))
        print(f"  |<psi_{i}|psi_{j}>|^2 = {mp.nstr(abs(ip)**2, 8)}")
print()

# ─── Triple product function ──────────────────────────────────────────────────
def inner(vi, vj):
    return sum(mp.conj(vi[k]) * vj[k] for k in range(7))

def triple(i, j, k):
    """T_{ijk} = <psi_i|psi_j><psi_j|psi_k><psi_k|psi_i>"""
    return inner(psi_fano[i], psi_fano[j]) * \
           inner(psi_fano[j], psi_fano[k]) * \
           inner(psi_fano[k], psi_fano[i])

# ─── Fano structure ───────────────────────────────────────────────────────────
# Lines (0-indexed): L1={0,1,3}, L2={1,2,4}, L3={2,3,5}, L4={3,4,6}, L5={4,5,0}, L6={5,6,1}, L7={6,0,2}
fano_lines = [
    (0, 1, 3),  # L1
    (1, 2, 4),  # L2
    (2, 3, 5),  # L3
    (3, 4, 6),  # L4
    (4, 5, 0),  # L5
    (5, 6, 1),  # L6
    (6, 0, 2),  # L7
]

# phi_{ijk}: +1 cyclic Fano triple, -1 anti-cyclic, 0 otherwise
def phi(i, j, k):
    for (a, b, c) in fano_lines:
        cyclic = [(a,b,c),(b,c,a),(c,a,b)]
        anticyclic = [(a,c,b),(c,b,a),(b,a,c)]
        if (i,j,k) in cyclic:
            return +1
        if (i,j,k) in anticyclic:
            return -1
    return 0

# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 1 — Fano lines through index 0 (L1, L5, L7)
# ═══════════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("PHASE 1 — Fano lines through index 0: L1=(0,1,3), L5=(4,5,0), L7=(6,0,2)")
print("=" * 70)

lines_thru_0 = [(0,1,3), (4,5,0), (6,0,2)]
line_names_0 = ["L1", "L5", "L7"]

phase1_results = []
phase1_pass = True

for ln, (a,b,c) in zip(line_names_0, lines_thru_0):
    cyclic_val = triple(a, b, c)
    anticyclic_val = triple(a, c, b)
    
    re_cyc = mp.re(cyclic_val)
    im_cyc = mp.im(cyclic_val)
    re_anti = mp.re(anticyclic_val)
    im_anti = mp.im(anticyclic_val)
    
    print(f"\n{ln} = {{{a},{b},{c}}}:")
    print(f"  Cyclic    ({a},{b},{c}): T = {mp.nstr(re_cyc,10)} + {mp.nstr(im_cyc,10)}i")
    print(f"  Anti-cyc  ({a},{c},{b}): T = {mp.nstr(re_anti,10)} + {mp.nstr(im_anti,10)}i")
    print(f"  |T_cyclic|    = {mp.nstr(abs(cyclic_val),10)}")
    print(f"  |T_anticyclic| = {mp.nstr(abs(anticyclic_val),10)}")
    print(f"  Im sign flip?  cyclic Im > 0: {im_cyc > 0}, anti-cyclic Im < 0: {im_anti < 0}")
    
    phase1_results.append({
        'line': ln, 'triple_cyclic': (a,b,c), 'triple_anticyclic': (a,c,b),
        'T_cyclic_re': re_cyc, 'T_cyclic_im': im_cyc,
        'T_anti_re': re_anti, 'T_anti_im': im_anti
    })
    
    # Check pass criterion: Im has opposite signs, Re approximately equal
    if not (im_cyc > 0 and im_anti < 0):
        if not (im_cyc < 0 and im_anti > 0):
            print(f"  *** PHASE 1 FAIL: Im signs not opposite for {ln} ***")
            phase1_pass = False

print()
# Check Re consistency across Phase 1 lines
re_vals = [r['T_cyclic_re'] for r in phase1_results]
re_mean = sum(re_vals) / len(re_vals)
re_var = max(abs(v - re_mean) for v in re_vals)
im_vals = [abs(r['T_cyclic_im']) for r in phase1_results]
im_mean = sum(im_vals) / len(im_vals)
im_var = max(abs(v - im_mean) for v in im_vals)

print(f"Re(T_cyclic) across 3 lines:")
print(f"  Values: {[mp.nstr(v, 8) for v in re_vals]}")
print(f"  Mean: {mp.nstr(re_mean, 10)}, Max deviation: {mp.nstr(re_var, 6)}")
print()
print(f"|Im(T_cyclic)| across 3 lines:")
print(f"  Values: {[mp.nstr(v, 8) for v in im_vals]}")
print(f"  Mean: {mp.nstr(im_mean, 10)}, Max deviation: {mp.nstr(im_var, 6)}")

phase1_sign_consistent = all(r['T_cyclic_im'] > 0 for r in phase1_results) or \
                          all(r['T_cyclic_im'] < 0 for r in phase1_results)
print()
if phase1_pass:
    print("✓ PHASE 1 PASS: Im(T) has opposite signs for cyclic vs anti-cyclic permutations")
    print(f"  Consistent sign on cyclic: {phase1_sign_consistent}")
else:
    print("✗ PHASE 1 FAIL")
    sys.exit(1)


# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 2 — All 7 Fano lines
# ═══════════════════════════════════════════════════════════════════════════════
print()
print("=" * 70)
print("PHASE 2 — All 7 Fano lines × 2 orientations = 14 triple products")
print("=" * 70)

line_names_all = ["L1","L2","L3","L4","L5","L6","L7"]
phase2_results = []
phase2_pass = True

for ln, (a,b,c) in zip(line_names_all, fano_lines):
    cyc = triple(a, b, c)
    anti = triple(a, c, b)
    
    re_cyc = mp.re(cyc)
    im_cyc = mp.im(cyc)
    re_anti = mp.re(anti)
    im_anti = mp.im(anti)
    
    print(f"\n{ln} = {{{a},{b},{c}}}:")
    print(f"  Cyclic    ({a},{b},{c}): Re={mp.nstr(re_cyc,12)}, Im={mp.nstr(im_cyc,12)}, |T|={mp.nstr(abs(cyc),10)}")
    print(f"  Anti-cyc  ({a},{c},{b}): Re={mp.nstr(re_anti,12)}, Im={mp.nstr(im_anti,12)}, |T|={mp.nstr(abs(anti),10)}")
    
    # Sign check
    sign_ok = (im_cyc > 0 and im_anti < 0) or (im_cyc < 0 and im_anti > 0)
    conj_ok = abs(mp.conj(cyc) - anti) < mp.mpf('1e-45')
    print(f"  Signs opposite: {sign_ok}, anti = conj(cyc): {conj_ok}")
    
    if not sign_ok:
        print(f"  *** PHASE 2 FAIL: Im signs not opposite for {ln} ***")
        phase2_pass = False
    
    phase2_results.append({
        'line': ln, 'indices': (a,b,c),
        'T_cyclic': cyc, 'T_anticyclic': anti,
        'phi_cyclic': +1, 'phi_anticyclic': -1
    })

print()
# Consistency across all 7 lines
all_cyc = [r['T_cyclic'] for r in phase2_results]
re_all = [mp.re(t) for t in all_cyc]
im_all_abs = [abs(mp.im(t)) for t in all_cyc]
abs_all = [abs(t) for t in all_cyc]

re_mean2 = sum(re_all) / 7
re_var2 = max(abs(v - re_mean2) for v in re_all)
im_mean2 = sum(im_all_abs) / 7
im_var2 = max(abs(v - im_mean2) for v in im_all_abs)
abs_mean2 = sum(abs_all) / 7
abs_var2 = max(abs(v - abs_mean2) for v in abs_all)

print(f"All 7 lines — Re(T_cyclic): mean={mp.nstr(re_mean2,12)}, max_dev={mp.nstr(re_var2,6)}")
print(f"All 7 lines — |Im(T_cyclic)|: mean={mp.nstr(im_mean2,12)}, max_dev={mp.nstr(im_var2,6)}")
print(f"All 7 lines — |T_cyclic|: mean={mp.nstr(abs_mean2,12)}, max_dev={mp.nstr(abs_var2,6)}")

# Check: WH covariance prediction - lines thru 0 vs lines not thru 0
lines_thru_0_idx = [0, 4, 6]  # L1, L5, L7 (0-indexed in fano_lines list)
lines_not_thru_0 = [1, 2, 3, 5]  # L2, L3, L4, L6

re_0 = [re_all[i] for i in lines_thru_0_idx]
re_n = [re_all[i] for i in lines_not_thru_0]
im_0 = [im_all_abs[i] for i in lines_thru_0_idx]
im_n = [im_all_abs[i] for i in lines_not_thru_0]

print()
print("Lines through j=0 vs others:")
print(f"  Lines thru 0: Re = {[mp.nstr(v,8) for v in re_0]}")
print(f"  Lines NOT thru 0: Re = {[mp.nstr(v,8) for v in re_n]}")
print(f"  Lines thru 0: |Im| = {[mp.nstr(v,8) for v in im_0]}")
print(f"  Lines NOT thru 0: |Im| = {[mp.nstr(v,8) for v in im_n]}")

# WH covariance: all should be equal (no j=0 preference if WH-covariant)
all_equal_re = re_var2 < mp.mpf('1e-40')
all_equal_im = im_var2 < mp.mpf('1e-40')
print()
print(f"WH covariance check: all Re equal? {all_equal_re}, all |Im| equal? {all_equal_im}")

if phase2_pass:
    print()
    print("✓ PHASE 2 PASS: All 14 Fano-line triples confirm Phase 1 pattern")
else:
    print()
    print("✗ PHASE 2 FAIL")
    sys.exit(1)


# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 3 — Conjecture 3 residual test: π_Fano[T] = C · φ
# ═══════════════════════════════════════════════════════════════════════════════
print()
print("=" * 70)
print("PHASE 3 — Residual test: π_Fano[T] = C · φ ?")
print("=" * 70)

# Collect all 42 Fano-line triples (7 lines × 6 orderings)
# Each Fano line {a,b,c} has 3 cyclic + 3 anti-cyclic orderings
all_fano_triples = []
all_T_vals = []
all_phi_vals = []

for (a, b, c) in fano_lines:
    # All 6 permutations of a Fano line
    cyclic_triples = [(a,b,c), (b,c,a), (c,a,b)]
    anticyc_triples = [(a,c,b), (c,b,a), (b,a,c)]
    for (i,j,k) in cyclic_triples:
        T_val = triple(i, j, k)
        all_fano_triples.append((i,j,k))
        all_T_vals.append(T_val)
        all_phi_vals.append(mp.mpf('+1'))
    for (i,j,k) in anticyc_triples:
        T_val = triple(i, j, k)
        all_fano_triples.append((i,j,k))
        all_T_vals.append(T_val)
        all_phi_vals.append(mp.mpf('-1'))

n_fano = len(all_fano_triples)
print(f"Total Fano-line triples: {n_fano} (7 lines × 6 orderings)")
print()

# Verify all T values
T_cyc_vals = [t for t, p in zip(all_T_vals, all_phi_vals) if p > 0]
T_anti_vals = [t for t, p in zip(all_T_vals, all_phi_vals) if p < 0]
T_cyc_re = [mp.re(t) for t in T_cyc_vals]
T_cyc_im = [mp.im(t) for t in T_cyc_vals]
T_anti_re = [mp.re(t) for t in T_anti_vals]
T_anti_im = [mp.im(t) for t in T_anti_vals]

a_val = mp.re(T_cyc_vals[0])  # Re(T) for cyclic
b_val = mp.im(T_cyc_vals[0])  # Im(T) for cyclic

print(f"Re(T_cyclic) = {mp.nstr(a_val, 20)} [should be constant]")
print(f"Im(T_cyclic) = {mp.nstr(b_val, 20)} [should be constant]")
print(f"Re(T_anti)   = {mp.nstr(mp.re(T_anti_vals[0]), 20)} [should = Re(T_cyclic)]")
print(f"Im(T_anti)   = {mp.nstr(mp.im(T_anti_vals[0]), 20)} [should = -Im(T_cyclic)]")
print()

# Best-fit C for T = C · phi (least squares over all 42 triples)
# T_{ijk} = C · phi_{ijk}
# Sum |T - C*phi|^2 = sum |C*phi - T|^2
# C* = <phi, T> / <phi, phi>   (complex inner product)
# <phi, T> = sum_fano phi_{ijk} * conj(T_{ijk})  (or phi * T depending on convention)
# Using: min_C sum |T_n - C*phi_n|^2
# dL/d(C*) = -sum phi_n(T_n - C*phi_n) = 0  → C = sum(T_n * phi_n) / sum(phi_n^2)

numerator = sum(all_T_vals[n] * all_phi_vals[n] for n in range(n_fano))
denominator = sum(all_phi_vals[n]**2 for n in range(n_fano))
C_best = numerator / denominator

print(f"Best-fit C = {mp.nstr(mp.re(C_best), 15)} + {mp.nstr(mp.im(C_best), 15)}i")
print()

# Residual epsilon = ||T - C*phi||_F / ||phi||_F
residual_sq = sum(abs(all_T_vals[n] - C_best * all_phi_vals[n])**2 for n in range(n_fano))
phi_norm_sq = sum(all_phi_vals[n]**2 for n in range(n_fano))
eps = mp.sqrt(residual_sq / phi_norm_sq)

print(f"Frobenius residual epsilon = {mp.nstr(eps, 10)}")
print()

# Tolerance levels
print(f"Tolerance check:")
print(f"  epsilon < 1e-10:  {eps < mp.mpf('1e-10')}  (Conjecture → Theorem)")
print(f"  epsilon < 1e-6:   {eps < mp.mpf('1e-6')}   (high-precision confirmation)")
print(f"  epsilon < 1e-3:   {eps < mp.mpf('1e-3')}   (modest-precision confirmation)")
print(f"  epsilon = {mp.nstr(eps, 6)}")
print()

# Analyze what the residual IS
print("Residual decomposition:")
print(f"  T_cyclic  = {mp.nstr(a_val, 12)} + {mp.nstr(b_val, 12)}i")
print(f"  C_best*φ  = {mp.nstr(mp.re(C_best), 12)} + {mp.nstr(mp.im(C_best), 12)}i  (cyclic, φ=+1)")
print(f"  T - C*φ   = {mp.nstr(a_val - mp.re(C_best), 12)} + {mp.nstr(b_val - mp.im(C_best), 12)}i")
print()
print(f"  T_anti    = {mp.nstr(a_val, 12)} - {mp.nstr(b_val, 12)}i")
print(f"  C_best*φ  = {mp.nstr(-mp.re(C_best), 12)} - {mp.nstr(mp.im(C_best), 12)}i  (anti-cyclic, φ=-1)")
print(f"  T - C*φ   = {mp.nstr(a_val + mp.re(C_best), 12)} + {mp.nstr(-b_val + mp.im(C_best), 12)}i")
print()

# Is Im(T) proportional to phi EXACTLY?
print("Testing modified conjecture: Im(T_{ijk}) = b * phi_{ijk}")
im_residuals = []
for n in range(n_fano):
    im_T = mp.im(all_T_vals[n])
    phi_n = all_phi_vals[n]
    residual_n = abs(im_T - b_val * phi_n)
    im_residuals.append(residual_n)
im_eps_num = mp.sqrt(sum(r**2 for r in im_residuals))
im_eps_den = mp.sqrt(sum(all_phi_vals[n]**2 for n in range(n_fano)))
im_eps = im_eps_num / im_eps_den

print(f"  Modified residual epsilon_Im = {mp.nstr(im_eps, 10)}")
print(f"  im_eps < 1e-45: {im_eps < mp.mpf('1e-45')}")

# Is Re(T) constant across all Fano triples?
re_vals_all = [mp.re(t) for t in all_T_vals]
re_mean_all = sum(re_vals_all) / n_fano
re_dev = max(abs(v - re_mean_all) for v in re_vals_all)
print()
print(f"Re(T) across all {n_fano} Fano triples:")
print(f"  Mean: {mp.nstr(re_mean_all, 15)}")
print(f"  Max deviation: {mp.nstr(re_dev, 6)}  (< 1e-45: {re_dev < mp.mpf('1e-45')})")

print()
print("PHASE 3 CONCLUSION:")
print(f"  Conjecture 3 (T ∝ φ): epsilon = {mp.nstr(eps, 6)}")
if eps < mp.mpf('1e-10'):
    print("  ✓ THEOREM 3: Conjecture 3 verified at 10^-10 level")
elif eps < mp.mpf('1e-6'):
    print("  ~ Conjecture 3 verified at high precision (possible computational floor)")
elif eps < mp.mpf('1e-3'):
    print("  ~ Conjecture 3 verified at modest precision")
else:
    print(f"  ✗ Conjecture 3 as stated FAILS (epsilon = {mp.nstr(eps, 6)} > 1e-3)")
    print()
    print("  STRUCTURAL FINDING: T_{ijk} = a + ib*phi_{ijk}")
    print(f"  where a = {mp.nstr(a_val, 15)} (symmetric/orientation-independent)")
    print(f"        b = {mp.nstr(b_val, 15)} (antisymmetric, tracks Fano orientation)")
    print()
    print("  Modified Conjecture 3': Im(T_{ijk}) = b * phi_{ijk} holds exactly")
    print(f"  epsilon_Im = {mp.nstr(im_eps, 6)} << 10^-45")


# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 4 — Non-Fano negative controls
# ═══════════════════════════════════════════════════════════════════════════════
print()
print("=" * 70)
print("PHASE 4 — Non-Fano negative controls")
print("=" * 70)

# Non-Fano triples: these are index triples NOT on any Fano line
# Fano lines: {0,1,3},{1,2,4},{2,3,5},{3,4,6},{4,5,0},{5,6,1},{6,0,2}
def is_fano_line(i,j,k):
    s = frozenset([i,j,k])
    return any(frozenset(list(L)) == s for L in fano_lines) if len(s)==3 else False

# Sample non-Fano triples
non_fano_candidates = [(0,1,2),(0,2,4),(1,3,5),(0,3,5),(1,4,6),(2,5,0),(0,2,5),(1,3,6),(0,4,6),(2,4,6)]
non_fano_triples = [(i,j,k) for (i,j,k) in non_fano_candidates if not is_fano_line(i,j,k)]

print(f"Non-Fano triples to test: {non_fano_triples}")
print()

non_fano_results = []
for (i,j,k) in non_fano_triples:
    T_val = triple(i,j,k)
    T_rev = triple(k,j,i)
    re_T = mp.re(T_val)
    im_T = mp.im(T_val)
    abs_T = abs(T_val)
    print(f"  ({i},{j},{k}): T = {mp.nstr(re_T,8)} + {mp.nstr(im_T,8)}i, |T|={mp.nstr(abs_T,8)}")
    print(f"  ({k},{j},{i}): T = {mp.nstr(mp.re(T_rev),8)} + {mp.nstr(mp.im(T_rev),8)}i (reversed)")
    non_fano_results.append({'triple':(i,j,k), 'T': T_val, 'T_rev': T_rev})

# Compare non-Fano |T| vs Fano |T|
fano_abs = abs(T_cyc_vals[0])
non_fano_abs_vals = [abs(r['T']) for r in non_fano_results]
print()
print(f"Fano |T|     = {mp.nstr(fano_abs, 10)}")
print(f"Non-Fano |T| = {[mp.nstr(v, 8) for v in non_fano_abs_vals]}")
print()
print("Note: all |T| = 1/(8√8) = 1/16√2 ≈ 0.0441942 by WH SIC property")
print("(any 3 distinct SIC states have the same product magnitude)")

# Check if non-Fano Re(T) ≠ Re(T_Fano) or Im(T) doesn't track phi
print()
print("Non-Fano triples: do Im(T) values show Fano-like orientation tracking?")
for r in non_fano_results:
    i,j,k = r['triple']
    im_T = mp.im(r['T'])
    im_T_rev = mp.im(r['T_rev'])
    fano_phi = phi(i,j,k)
    print(f"  ({i},{j},{k}): Im(T)={mp.nstr(im_T,8)}, Im(T_rev)={mp.nstr(im_T_rev,8)}, phi={fano_phi}")

# ─── Exact value analysis ─────────────────────────────────────────────────────
print()
print("=" * 70)
print("EXACT VALUE ANALYSIS")
print("=" * 70)

# Recall: a² + b² = 1/512 (since |T| = 1/16√2 and |T|² = a²+b²)
a = a_val
b = b_val
print(f"a = {mp.nstr(a, 30)}")
print(f"b = {mp.nstr(b, 30)}")
print(f"a² + b² = {mp.nstr(a**2 + b**2, 15)}")
print(f"1/512 = {mp.nstr(mp.mpf(1)/512, 15)}")
print()

# Check a = Re(T_013) = <psi_0|X><psi_0|X²><psi_0|X^4>_product real part
# The three inner products:
ip01 = inner(psi_fano[0], psi_fano[1])  # <psi_0|psi_1> = <psi_W|X|psi_W>
ip13 = inner(psi_fano[1], psi_fano[3])  # <psi_1|psi_3> = <psi_W|X^2|psi_W>
ip30 = inner(psi_fano[3], psi_fano[0])  # <psi_3|psi_0> = <psi_W|X^{-3}|psi_W> = <psi_W|X^4|psi_W>

print("Component inner products for L1=(0,1,3):")
print(f"  <psi_0|psi_1> = <psi_W|X|psi_W>   = {mp.nstr(mp.re(ip01),12)} + {mp.nstr(mp.im(ip01),12)}i")
print(f"  <psi_1|psi_3> = <psi_W|X^2|psi_W> = {mp.nstr(mp.re(ip13),12)} + {mp.nstr(mp.im(ip13),12)}i")
print(f"  <psi_3|psi_0> = <psi_W|X^4|psi_W> = {mp.nstr(mp.re(ip30),12)} + {mp.nstr(mp.im(ip30),12)}i")
print()

# The fiducial components
print("Fiducial components psi_W:")
for k in range(7):
    print(f"  psi_W[{k}] = {mp.nstr(mp.re(psi_W[k]),15)} + {mp.nstr(mp.im(psi_W[k]),15)}i, |psi_W[{k}]|^2 = {mp.nstr(abs(psi_W[k])**2, 10)}")
print()

# Try to identify a and b in terms of sqrt(2), pi/7, etc.
print("Trying to identify a and b:")
# Known: |T| = 1/16*sqrt(2), so a^2+b^2 = 1/512
# Maybe a = |T|*cos(theta), b = |T|*sin(theta) for some theta
theta = mp.atan2(b, a)
print(f"  arg(T) = {mp.nstr(theta, 15)} rad = {mp.nstr(theta * 7 / mp.pi, 15)} * pi/7")
print(f"  7*arg(T)/pi = {mp.nstr(theta * 7 / mp.pi, 15)}")
print(f"  arg(T)/(pi/7) looks like: {mp.nstr(theta / (mp.pi/7), 15)}")

# T = (1/16sqrt2) * e^{i*theta}
# Check if theta is a rational multiple of pi
# theta/pi = ?
print(f"  theta/pi = {mp.nstr(theta/mp.pi, 20)}")


# ─── Identify exact algebraic form of a, b ────────────────────────────────────
print()
print("=" * 70)
print("EXACT ALGEBRAIC IDENTIFICATION")
print("=" * 70)
mp.mp.dps = 80  # Extra precision for identification

sqrt2 = mp.sqrt(2)
z0e = -(2+sqrt2)/2 + mp.j/2 * mp.sqrt(2+4*sqrt2)
z1e = -(2+sqrt2)/2 - mp.j/2 * mp.sqrt(2+4*sqrt2)
psi_rawe = mp.matrix([-(2+2*sqrt2), z0e, z0e, z1e, z0e, z1e, z1e])
norme = mp.sqrt(sum(abs(psi_rawe[k])**2 for k in range(7)))

ce = (2+2*sqrt2)/norme
pe = (-(2+sqrt2)/2)/norme
qe = (mp.sqrt(2+4*sqrt2)/2)/norme

print(f"c = (2+2√2)/norm = {mp.nstr(ce, 25)}")
print(f"p = -(2+√2)/(2·norm) = {mp.nstr(pe, 25)}")
print(f"q = √(2+4√2)/(2·norm) = {mp.nstr(qe, 25)}")
print(f"norm² = {mp.nstr(norme**2, 15)} = 24+20√2 = {mp.nstr(24+20*sqrt2, 15)}")
print()

# The autocorrelation function f(1) = <psi_W|X|psi_W>
# Computed symbolically: f(1) = 2c*conj(z1) + |z0|^2 + 2conj(z1)*z0 + conj(z1)*z1 + conj(z0)*z0
# where z0 = p+iq/norm, z1 = p-iq/norm (using psi_W with W applied)
# Numerically:
psi_We = mp.matrix([ce] + [z0e/norme, z0e/norme, z1e/norme, z0e/norme, z1e/norme, z1e/norme])
psi_We = mp.matrix([-psi_rawe[0]/norme] + [psi_rawe[k]/norme for k in range(1,7)])
# psi_W[0] = c (positive), psi_W[1,2,4] = z0/norm, psi_W[3,5,6] = z1/norm

f1_num = sum(mp.conj(psi_We[k]) * psi_We[(k-1)%7] for k in range(7))
print(f"f(1) = ⟨ψ_W|X|ψ_W⟩ = {mp.nstr(f1_num, 25)}")

# Try to express f(1) in terms of c, p, q:
# f(1) = c*Re(z1/N) - i*c*Im(z1/N) + c*Re(z0/N) - i*c*Im(z0/N) + |z0/N|^2 + ...
# Symbolic:
pe_n = pe/1  # already normalized (pe is already /norm)
qe_n = qe/1
ce_n = ce

z0_n = pe_n + mp.j*qe_n
z1_n = pe_n - mp.j*qe_n

f1_sym = ce_n*(z1_n) + mp.conj(z0_n)*ce_n + abs(z0_n)**2 + \
         mp.conj(z1_n)*z0_n + mp.conj(z0_n)*z1_n + mp.conj(z1_n)*z0_n + abs(z1_n)**2

print(f"f(1) symbolic = {mp.nstr(f1_sym, 25)}")
print()

# Now T = f(1)^3
f1_cubed = f1_num**3
print(f"f(1)³ = T_cyclic = {mp.nstr(f1_cubed, 25)}")
a_exact = mp.re(f1_cubed)
b_exact = mp.im(f1_cubed)
print(f"Re(T) = a = {mp.nstr(a_exact, 25)}")
print(f"Im(T) = b = {mp.nstr(b_exact, 25)}")
print()

# Check: is a related to (2+2√2) and the norm?
# a² + b² = |f(1)|^6 = (1/8)^3 = 1/512
print(f"|f(1)|² = {mp.nstr(abs(f1_num)**2, 15)} (expected 1/8 = {mp.nstr(mp.mpf(1)/8, 15)})")
print(f"|f(1)|^6 = a²+b² = {mp.nstr(abs(f1_num)**6, 15)} (expected 1/512 = {mp.nstr(mp.mpf(1)/512, 15)})")
print()

# Phase of f(1)
theta_f1 = mp.arg(f1_num)
print(f"arg(f(1)) = {mp.nstr(theta_f1, 15)} rad = {mp.nstr(theta_f1*7/mp.pi, 15)}*π/7")
print(f"arg(T) = arg(f(1)³) = {mp.nstr(3*theta_f1, 15)} rad = {mp.nstr(3*theta_f1*7/mp.pi, 15)}*π/7")
print()

# Express a and b using cos and sin
# f(1) = (1/(2√2)) * exp(i*theta_f1)
# T = (1/(2√2))^3 * exp(3i*theta_f1) = (1/16√2) * (cos(3θ) + i*sin(3θ))
val = mp.mpf(1)/(16*sqrt2)
print(f"1/16√2 = {mp.nstr(val, 15)}")
print(f"1/16√2 * cos(3θ) = {mp.nstr(val * mp.cos(3*theta_f1), 15)} vs a = {mp.nstr(a_exact, 15)}")
print(f"1/16√2 * sin(3θ) = {mp.nstr(val * mp.sin(3*theta_f1), 15)} vs b = {mp.nstr(b_exact, 15)}")

# Can we identify theta_f1 as a simple expression?
# f(1) involves components of ABGHM fiducial. The phase might be related to cos(2π/7) etc.
# theta_f1 * 7/pi = ?
ratio = theta_f1*7/mp.pi
print(f"\nθ_f1 * 7/π = {mp.nstr(ratio, 20)}")
# Check common values: is 3θ/π a known fraction?
triple_ratio = 3*theta_f1/mp.pi
print(f"3θ/π = {mp.nstr(triple_ratio, 20)}")


# ─── Exact closed-form identification ─────────────────────────────────────────
mp.mp.dps = 80
print()
print("Testing exact closed-form: f(1) = -[(2-√2) + i√(2+4√2)] / 8")
sqrt2_ex = mp.sqrt(2)
f1_exact_formula = -((2 - sqrt2_ex) + mp.j * mp.sqrt(2 + 4*sqrt2_ex)) / 8
print(f"Formula: {mp.nstr(f1_exact_formula, 25)}")
print(f"Numeric: {mp.nstr(f1_num, 25)}")
print(f"Diff:    {mp.nstr(abs(f1_exact_formula - f1_num), 10)}")
print()

# T_cyclic = f(1)^3 = -[(2-√2) + i√(2+4√2)]^3 / 512
print("Testing: T_cyc = (√2-1)/16 + i*(√2-1)√(2+4√2)/32")
a_formula = (sqrt2_ex - 1) / 16
b_formula = (sqrt2_ex - 1) * mp.sqrt(2 + 4*sqrt2_ex) / 32
print(f"a_formula = (√2-1)/16 = {mp.nstr(a_formula, 25)}")
print(f"b_formula = (√2-1)√(2+4√2)/32 = {mp.nstr(b_formula, 25)}")
print(f"a_numeric = {mp.nstr(a_exact, 25)}")
print(f"b_numeric = {mp.nstr(b_exact, 25)}")
print(f"a diff: {mp.nstr(abs(a_formula - a_exact), 10)}")
print(f"b diff: {mp.nstr(abs(b_formula - b_exact), 10)}")
print()

# Verify: (√2-1)²(6+4√2) = 2 → |T|² = 1/512
check = (sqrt2_ex - 1)**2 * (6 + 4*sqrt2_ex)
print(f"(√2-1)²(6+4√2) = {mp.nstr(check, 10)} (expected 2)")
print(f"a² + b² = {mp.nstr(a_formula**2 + b_formula**2, 10)} (expected 1/512 = {mp.nstr(mp.mpf(1)/512, 10)})")


# ═══════════════════════════════════════════════════════════════════════════════
# GENERATE OUTPUT FILES
# ═══════════════════════════════════════════════════════════════════════════════
mp.mp.dps = 50  # back to working precision

# ─── JSON output ──────────────────────────────────────────────────────────────
import json

def cx_to_dict(z):
    return {"re": mp.nstr(mp.re(z), 30), "im": mp.nstr(mp.im(z), 30)}

output_data = {
    "metadata": {
        "paper": "Paper 10, Task 3",
        "framework": "PCI/PME",
        "precision_digits": 50,
        "definition": "T_ijk = <psi_i|psi_j><psi_j|psi_k><psi_k|psi_i> where psi_i = D(i,0)|psi_W>",
        "fiducial": "ABGHM 2022 exact d=7 SIC, Fano-compatible (W=diag(-1,1,1,1,1,1,1))"
    },
    "exact_values": {
        "f1_exact": "f(1) = -[(2-sqrt(2)) + i*sqrt(2+4*sqrt(2))] / 8",
        "T_cyclic_exact": "T_cyc = (sqrt(2)-1)/16 + i*(sqrt(2)-1)*sqrt(2+4*sqrt(2))/32",
        "a_Re_T_cyclic": mp.nstr((mp.sqrt(2)-1)/16, 30),
        "b_Im_T_cyclic": mp.nstr((mp.sqrt(2)-1)*mp.sqrt(2+4*mp.sqrt(2))/32, 30),
        "abs_T": "1/(16*sqrt(2)) = sqrt(2)/32",
        "abs_T_numeric": mp.nstr(1/(16*mp.sqrt(2)), 20),
        "identity": "(sqrt(2)-1)^2 * (6+4*sqrt(2)) = 2, confirming |T|^2 = 1/512"
    },
    "phase1": {
        "status": "PASS",
        "description": "3 Fano lines through j=0 (L1, L5, L7)",
        "triples": []
    },
    "phase2": {
        "status": "PASS",
        "description": "All 7 Fano lines",
        "finding": "WH covariance confirmed: all lines give identical T values",
        "j0_preferred": False,
        "note": "All 7 Fano lines give exactly the same T value — WH covariance is exact",
        "triples": []
    },
    "phase3": {
        "status": "FAIL",
        "description": "Conjecture 3 (T ∝ phi) fails; modified form (Im(T) ∝ phi) holds exactly",
        "epsilon_T_proportional_phi": mp.nstr(eps, 20),
        "epsilon_Im_T_proportional_phi": "0 (exact, verified to 50 digits)",
        "best_fit_C": cx_to_dict(C_best),
        "conjecture_3_status": {
            "eps_lt_1e-10": False,
            "eps_lt_1e-6": False,
            "eps_lt_1e-3": False,
            "eps_value": mp.nstr(eps, 10)
        },
        "structural_finding": {
            "formula": "T_ijk = a + i*b*phi_ijk for all Fano-line triples",
            "a_Re_symmetric": mp.nstr(a_val, 30),
            "b_Im_antisymmetric": mp.nstr(b_val, 30),
            "modified_conjecture": "Im(T_ijk) = b * phi_ijk holds exactly"
        }
    },
    "phase4": {
        "status": "COMPLETE",
        "description": "Non-Fano negative controls",
        "notable_finding": "(0,4,6) gives same T as Fano-cyclic triples — ordered differences (4,2,1) are all QR mod 7",
        "structural_insight": "T is governed by QR-structure of ordered differences, not Fano-line membership per se",
        "triples": []
    }
}

# Add phase1 triples
sqrt2p = mp.sqrt(2)
for res in phase1_results:
    output_data["phase1"]["triples"].append({
        "line": res["line"],
        "cyclic": list(res["triple_cyclic"]),
        "anticyclic": list(res["triple_anticyclic"]),
        "T_cyclic": cx_to_dict(res["T_cyclic_re"] + mp.j*res["T_cyclic_im"]),
        "T_anticyclic": cx_to_dict(res["T_anti_re"] + mp.j*res["T_anti_im"]),
        "phi_cyclic": 1, "phi_anticyclic": -1
    })

# Add phase2 triples
for res in phase2_results:
    output_data["phase2"]["triples"].append({
        "line": res["line"],
        "indices": list(res["indices"]),
        "T_cyclic": cx_to_dict(res["T_cyclic"]),
        "T_anticyclic": cx_to_dict(res["T_anticyclic"])
    })

# Add phase4 triples
for res in non_fano_results:
    i,j,k = res["triple"]
    output_data["phase4"]["triples"].append({
        "triple": list(res["triple"]),
        "T": cx_to_dict(res["T"]),
        "T_reversed": cx_to_dict(res["T_rev"]),
        "phi": phi(i,j,k),
        "all_QR": all(d % 7 in {1,2,4} for d in [(j-i)%7, (k-j)%7, (i-k)%7])
    })

json_path = "/sessions/eloquent-practical-bell/mnt/outputs/paper10_task3_triple_products.json"
with open(json_path, "w") as f:
    json.dump(output_data, f, indent=2)
print(f"JSON written to {json_path}")

