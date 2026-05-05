import numpy as np
N = 14
r = 0.7
def make_R(seed):
    rng = np.random.default_rng(seed)
    Q, _ = np.linalg.qr(rng.standard_normal((N, N)))
    return Q
RA = make_R(20260504)
RB = make_R(20260505)
e1 = np.zeros(N); e1[0] = 1.0
bA = e1.copy()
bB = -e1
I = np.eye(N)
def fp(theta):
    c, s = np.cos(theta), np.sin(theta)
    M = np.block([[I - r*c*RA,  r*s*RA],
                  [-r*s*RB,     I - r*c*RB]])
    z = np.linalg.solve(M, np.concatenate([bA, bB]))
    return z[:N], z[N:]
def cs(u,v): return float(np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v)))
# Signed cos similarity (no abs)
print("theta(deg)\tC1_signed\tC2_signed\tC1_abs\tC2_abs")
for th_deg in np.linspace(0, 90, 19):
    th = np.deg2rad(th_deg)
    x, y = fp(th)
    C1s = cs(x, bA); C2s = cs(y, bB)
    print(f"{th_deg:5.1f}\t{C1s:+.4f}\t{C2s:+.4f}\t{abs(C1s):.4f}\t{abs(C2s):.4f}")
