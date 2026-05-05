import numpy as np

np.set_printoptions(suppress=True, precision=6)


def rand_orth(n, seed):
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(n, n))
    Q, R = np.linalg.qr(A)
    signs = np.sign(np.diag(R))
    signs[signs == 0] = 1
    Q = Q @ np.diag(signs)
    return Q


def test_closed_form():
    n = 4
    r = 0.7
    R = rand_orth(n, 123)
    bA = np.array([1.0, -2.0, 0.5, 3.0])
    bB = np.array([-1.5, 0.25, 4.0, -0.5])
    M = np.block([
        [np.eye(n), r * R],
        [-r * R, np.eye(n)],
    ])
    rhs = np.concatenate([bA, bB])
    sol = np.linalg.solve(M, rhs)
    x, y = sol[:n], sol[n:]
    x_formula = np.linalg.solve(np.eye(n) + r**2 * (R @ R), bA - r * (R @ bB))
    y_formula = np.linalg.solve(np.eye(n) + r**2 * (R @ R), r * (R @ bA) + bB)
    return {
        'x_residual': float(np.linalg.norm(x - x_formula)),
        'y_residual': float(np.linalg.norm(y - y_formula)),
    }


def test_linear_response():
    n = 4
    rA, rB = 0.6, 0.7
    RA, RB = rand_orth(n, 1), rand_orth(n, 2)
    bA = np.array([1.2, -0.4, 0.9, 0.3])
    bB = np.array([-0.7, 1.0, 0.2, -1.1])
    xA = np.linalg.solve(np.eye(n) - rA * RA, bA)
    yB = np.linalg.solve(np.eye(n) - rB * RB, bB)
    eps = 1e-7
    c, s = np.cos(eps), np.sin(eps)
    M = np.block([
        [np.eye(n) - rA * c * RA, rA * s * RA],
        [-rB * s * RB, np.eye(n) - rB * c * RB],
    ])
    rhs = np.concatenate([bA, bB])
    sol = np.linalg.solve(M, rhs)
    xeps, yeps = sol[:n], sol[n:]
    dx_num = (xeps - xA) / eps
    dy_num = (yeps - yB) / eps
    dx_pred = -rA * np.linalg.solve(np.eye(n) - rA * RA, RA @ yB)
    dy_pred = +rB * np.linalg.solve(np.eye(n) - rB * RB, RB @ xA)
    return {
        'dx_residual': float(np.linalg.norm(dx_num - dx_pred)),
        'dy_residual': float(np.linalg.norm(dy_num - dy_pred)),
    }


def test_rate_lock():
    n = 5
    rA, rB = 0.55, 0.8
    RA, RB = rand_orth(n, 11), rand_orth(n, 12)
    theta = 0.83
    c, s = np.cos(theta), np.sin(theta)
    Psi = np.block([
        [c*np.eye(n), -s*np.eye(n)],
        [s*np.eye(n),  c*np.eye(n)],
    ])
    D = np.block([
        [rA * RA, np.zeros((n, n))],
        [np.zeros((n, n)), rB * RB],
    ])
    L = D @ Psi
    op_norm = float(np.linalg.svd(L, compute_uv=False)[0])
    return {'op_norm': op_norm, 'expected': max(rA, rB)}


def test_RI_opposed_bias():
    r = 0.7
    theta_vals = np.linspace(0, np.pi/2, 5)
    bA = np.array([1.0, 0.0])
    bB = -bA
    vals = []
    for theta in theta_vals:
        c, s = np.cos(theta), np.sin(theta)
        M = np.block([
            [np.eye(2) - r*c*np.eye(2), r*s*np.eye(2)],
            [-r*s*np.eye(2), np.eye(2) - r*c*np.eye(2)],
        ])
        sol = np.linalg.solve(M, np.concatenate([bA, bB]))
        x = sol[:2]
        coh = abs(np.dot(x/np.linalg.norm(x), bA/np.linalg.norm(bA)))
        vals.append((float(theta), float(coh), x.tolist()))
    return vals


if __name__ == '__main__':
    import json
    out = {
        'closed_form': test_closed_form(),
        'linear_response': test_linear_response(),
        'rate_lock': test_rate_lock(),
        'R_equals_I_opposed_bias': test_RI_opposed_bias(),
    }
    print(json.dumps(out, indent=2))
