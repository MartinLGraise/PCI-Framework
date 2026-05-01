"""
Paper 10 figures — built from real computational outputs.

Figures:
  Figure 1: Fano plane with octonion multiplication structure
  Figure 2: 14×49 |α| coefficient tensor heatmap (Theorem 1)
  Figure 3: 128 sign-flip candidate histogram (Theorem 2)
  Figure 4: Triple-product complex-plane structure (Theorem 3)
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

HERE = Path(__file__).parent
COMP = HERE.parent / "computations"
OUT = HERE

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": False,
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

# ----------------------------------------------------------------------------
# Figure 1: Fano plane with octonion multiplication
# ----------------------------------------------------------------------------

def fig1_fano_plane():
    fig, ax = plt.subplots(figsize=(7, 7))
    # 7 vertices of the Fano plane positioned as triangle + midpoints + center
    # Use 0-indexed Baez 2002 labels matching Paper 10 §4.1
    # Lines: (0,1,3), (1,2,4), (2,3,5), (3,4,6), (0,4,5), (1,5,6), (0,2,6)
    pts = {
        0: (0.5, 0.92),       # top vertex
        1: (0.05, 0.18),      # bottom-left vertex
        2: (0.95, 0.18),      # bottom-right vertex
        3: (0.275, 0.55),     # left midpoint (between 0 and 1)
        4: (0.50, 0.18),      # bottom midpoint (between 1 and 2)
        5: (0.50, 0.43),      # center
        6: (0.725, 0.55),     # right midpoint (between 0 and 2)
    }
    lines = [(0,1,3), (1,2,4), (2,3,5), (3,4,6), (0,4,5), (1,5,6), (0,2,6)]
    line_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                   '#9467bd', '#8c564b', '#17becf']

    # Draw the six straight lines + the inscribed circle (line through 3,4,6)
    # We draw lines (0,1,3), (1,2,4), (2,3,5), (0,4,5), (1,5,6), (0,2,6) as polylines
    # and (3,4,6) as a circle through those three points.
    for idx, line in enumerate(lines):
        c = line_colors[idx]
        if line == (3, 4, 6):
            # Circle passing through points 3, 4, 6 — find center & radius
            (x1, y1), (x2, y2), (x3, y3) = pts[3], pts[4], pts[6]
            # circumcenter
            ax_, ay_ = x1 - x2, y1 - y2
            bx_, by_ = x1 - x3, y1 - y3
            d = 2 * (ax_ * by_ - bx_ * ay_)
            ux = ((x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2) * by_
                  - (x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2) * ay_) / d
            uy = ((x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2) * ax_
                  - (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2) * bx_) / d
            r = math.hypot(x1 - ux, y1 - uy)
            circ = plt.Circle((ux, uy), r, fill=False, color=c, lw=2.0, zorder=2)
            ax.add_patch(circ)
        else:
            xs = [pts[i][0] for i in line]
            ys = [pts[i][1] for i in line]
            ax.plot(xs, ys, color=c, lw=2.0, zorder=2)

    # Draw the seven points
    for i, (x, y) in pts.items():
        ax.add_patch(plt.Circle((x, y), 0.035,
                                facecolor='white', edgecolor='black',
                                lw=1.5, zorder=4))
        ax.text(x, y, f"$e_{i}$", ha='center', va='center',
                fontsize=12, fontweight='bold', zorder=5)

    # QR / NQR coloring annotation (compact legend at right margin)
    qr_txt = (r"Quadratic-residue partition of $\mathbb{Z}_7^*$:" "\n"
              r"  QR$_7 = \{1, 2, 4\}$" "\n"
              r"  NQR$_7 = \{3, 5, 6\}$" "\n\n"
              r"Each Fano line has all three" "\n"
              r"ordered differences in the same class.")
    ax.text(1.02, 0.5, qr_txt, transform=ax.transAxes,
            ha='left', va='center', fontsize=9,
            bbox=dict(facecolor='#f7f7f7', edgecolor='#888',
                      boxstyle='round,pad=0.5'))

    # Title
    ax.set_title("Fig. 1 — Fano plane indexing of $\\mathrm{Im}\\,\\mathbb{O}$\n"
                 "Seven imaginary octonion units; each line is a multiplication triple",
                 fontsize=11, pad=14)

    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.set_aspect('equal')
    ax.axis('off')

    out = OUT / "figure1_fano_plane.png"
    fig.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"Saved {out}")


# ----------------------------------------------------------------------------
# Figure 2: 14×49 coefficient tensor heatmap
# ----------------------------------------------------------------------------

def fig2_coefficient_heatmap():
    data = json.loads((COMP / "paper10_task1_g2_sic_coefficients.json").read_text())
    alpha = data["alpha_tensor"]
    # alpha[a]['p,q'] = {'re': ..., 'im': ...}
    M = np.zeros((14, 49))
    for a in range(14):
        for p in range(7):
            for q in range(7):
                key = f"{p},{q}"
                v = alpha[str(a)][key]
                re = float(v["re"])
                im = float(v["im"])
                M[a, p * 7 + q] = math.hypot(re, im)

    fig, ax = plt.subplots(figsize=(11, 4.2))
    im = ax.imshow(M, aspect='auto', cmap='magma',
                   interpolation='nearest', vmin=0, vmax=M.max())

    # Frobenius row norms (should all equal sqrt(8/7))
    row_norms = np.sqrt((M ** 2).sum(axis=1))
    target = math.sqrt(8 / 7)

    ax.set_xlabel("SIC projector index $7p + q$  ($p, q \\in \\mathbb{Z}_7$)")
    ax.set_ylabel("$G_2$ generator index $a$")
    ax.set_title(f"Fig. 2 — $|\\alpha^{{(a)}}_{{p,q}}|$ for $T_a = \\sum_{{p,q}}\\alpha^{{(a)}}_{{p,q}}\\Pi_{{p,q}}$,"
                 " $a = 1\\ldots 14$\n"
                 f"Frobenius row norms uniform at $\\sqrt{{8/7}} \\approx {target:.4f}$"
                 f"  (computed: mean = {row_norms.mean():.4f}, std = {row_norms.std():.2e})",
                 fontsize=10, pad=10)

    ax.set_yticks(range(14))
    ax.set_yticklabels([f"{a+1}" for a in range(14)], fontsize=8)
    ax.set_xticks(range(0, 49, 7))
    ax.set_xticklabels([f"{i}" for i in range(0, 49, 7)], fontsize=8)

    # vertical separators every 7 columns to highlight (p) blocks
    for p in range(1, 7):
        ax.axvline(p * 7 - 0.5, color='white', lw=0.4, alpha=0.5)

    cbar = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.015)
    cbar.set_label("$|\\alpha^{(a)}_{p,q}|$", rotation=270, labelpad=14)

    out = OUT / "figure2_coefficient_heatmap.png"
    fig.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"Saved {out}")


# ----------------------------------------------------------------------------
# Figure 3: W-correction enumeration histogram
# ----------------------------------------------------------------------------

def fig3_w_enumeration():
    """
    Of 128 sign-flip candidates W ∈ {±1}^7, exactly 2 produce 48/48 SIC overlaps
    for the ABGHM fiducial. Plot the categorical breakdown.
    """
    counts = {
        "6/48\n(pure-Z only)": 126,
        "48/48\n(Fano-compatible)": 2,
    }

    labels = list(counts.keys())
    values = list(counts.values())
    colors = ['#888888', '#d62728']

    fig, ax = plt.subplots(figsize=(10, 5.5))
    xs = np.arange(len(labels))
    bars = ax.bar(xs, values, color=colors, edgecolor='black', lw=0.8, width=0.5)

    ax.set_yscale('log')
    ax.set_ylim(0.7, 1000)
    ax.set_xlim(-0.7, 1.7)
    ax.set_xticks(xs)
    ax.set_xticklabels(labels, fontsize=11)
    ax.set_ylabel("Number of sign-flip candidates (log scale)")
    ax.set_title("Fig. 3 — Enumeration of $2^7 = 128$ diagonal sign-flip matrices $W \\in \\{\\pm 1\\}^7$\n"
                 "Exactly 2 (the pair $W$ and $-W$, global-phase equivalent) recover the SIC condition for the ABGHM fiducial",
                 fontsize=10, pad=12)

    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() * 1.18,
                str(v), ha='center', va='bottom', fontsize=14,
                fontweight='bold')

    # Place the explanatory text in the empty right margin
    txt = (
        "The two surviving candidates:\n\n"
        "  $W \\;= \\mathrm{diag}(-1, +1, +1, +1, +1, +1, +1)$\n"
        "  $-W = \\mathrm{diag}(+1, -1, -1, -1, -1, -1, -1)$\n\n"
        "They differ only by an overall sign,\n"
        "so they are equivalent under global phase\n"
        "$\\Rightarrow$ a unique physical Fano-compatible correction."
    )
    ax.text(0.98, 0.97, txt, transform=ax.transAxes,
            ha='right', va='top', fontsize=9.5,
            bbox=dict(facecolor='#fff3e0', edgecolor='#d62728',
                      boxstyle='round,pad=0.5'))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    out = OUT / "figure3_w_enumeration.png"
    fig.savefig(out, dpi=200, facecolor='white')  # no bbox_inches='tight'
    plt.close(fig)
    print(f"Saved {out}")


# ----------------------------------------------------------------------------
# Figure 4: Triple-product complex-plane structure
# ----------------------------------------------------------------------------

def fig4_triple_product():
    data = json.loads((COMP / "paper10_task3_triple_products.json"
                       ).read_text())

    fano_cyc = []
    fano_anti = []
    for ph in ["phase1", "phase2"]:
        for t in data[ph]["triples"]:
            tcy = t["T_cyclic"]
            ta = t["T_anticyclic"]
            fano_cyc.append((float(tcy["re"]), float(tcy["im"])))
            fano_anti.append((float(ta["re"]), float(ta["im"])))

    nonfano = []
    for t in data["phase4"]["triples"]:
        tT = t["T"]
        tR = t["T_reversed"]
        nonfano.append((float(tT["re"]), float(tT["im"])))
        nonfano.append((float(tR["re"]), float(tR["im"])))

    fig, ax = plt.subplots(figsize=(8, 7.5))

    # Universal-magnitude circle |T|^2 = 1/512
    R = 1 / math.sqrt(512)
    th = np.linspace(0, 2 * math.pi, 360)
    ax.plot(R * np.cos(th), R * np.sin(th),
            color='#888', lw=1.2, ls='--', zorder=1,
            label=f"$|T| = 1/(16\\sqrt{{2}}) \\approx {R:.4f}$")

    fano_cyc_arr = np.array(fano_cyc)
    fano_anti_arr = np.array(fano_anti)
    nonfano_arr = np.array(nonfano)

    ax.scatter(fano_cyc_arr[:, 0], fano_cyc_arr[:, 1],
               s=110, color='#2ca02c', edgecolor='black', lw=0.8,
               zorder=4, label=f"Fano cyclic ({len(fano_cyc_arr)} triples) — $\\varphi = +1$")
    ax.scatter(fano_anti_arr[:, 0], fano_anti_arr[:, 1],
               s=110, color='#1f77b4', edgecolor='black', lw=0.8,
               zorder=4, label=f"Fano anti-cyclic ({len(fano_anti_arr)} triples) — $\\varphi = -1$")
    ax.scatter(nonfano_arr[:, 0], nonfano_arr[:, 1],
               s=70, color='#d62728', marker='s', edgecolor='black', lw=0.6,
               alpha=0.85, zorder=3,
               label=f"Non-Fano sample ({len(nonfano_arr)} triples) — $\\varphi = 0$")

    # Axes & guides
    ax.axhline(0, color='#444', lw=0.5, zorder=0)
    ax.axvline(0, color='#444', lw=0.5, zorder=0)

    # The constants a, b
    a = (math.sqrt(2) - 1) / 16
    b = (math.sqrt(2) - 1) * math.sqrt(2 + 4 * math.sqrt(2)) / 32
    ax.scatter([a, a], [b, -b], s=200, marker='*',
               facecolor='gold', edgecolor='black', lw=0.8, zorder=5)

    # Annotations
    ax.annotate(f"$T = a + ib$\n$a = (\\sqrt{{2}}-1)/16 \\approx {a:.5f}$\n"
                f"$b = (\\sqrt{{2}}-1)\\sqrt{{2 + 4\\sqrt{{2}}}}/32 \\approx {b:.5f}$",
                xy=(a, b), xytext=(0.058, 0.052),
                fontsize=9, ha='left',
                bbox=dict(facecolor='#f0fff0', edgecolor='#2ca02c',
                          boxstyle='round,pad=0.4'),
                arrowprops=dict(arrowstyle='->', color='#2ca02c', lw=1))

    bp = b * (1 + math.sqrt(2)) / 2
    ax.annotate(f"$b'/b = (1+\\sqrt{{2}})/2 \\approx 1.2071$",
                xy=(nonfano_arr[0, 0], -bp),
                xytext=(-0.075, -0.062),
                fontsize=9, ha='left',
                bbox=dict(facecolor='#fff0f0', edgecolor='#d62728',
                          boxstyle='round,pad=0.4'),
                arrowprops=dict(arrowstyle='->', color='#d62728', lw=1))

    ax.set_xlabel("$\\mathrm{Re}(T_{ijk})$")
    ax.set_ylabel("$\\mathrm{Im}(T_{ijk})$")
    ax.set_title("Fig. 4 — SIC triple product $T_{ijk} = \\mathrm{tr}(\\Pi_i \\Pi_j \\Pi_k)$ in the complex plane\n"
                 "All triples on the universal-magnitude circle $|T|^2 = 1/512$;"
                 " phase angle distinguishes Fano vs non-Fano structure",
                 fontsize=10, pad=10)
    ax.set_aspect('equal')
    ax.set_xlim(-0.085, 0.085)
    ax.set_ylim(-0.085, 0.085)
    ax.grid(True, ls=':', alpha=0.3)
    ax.legend(loc='lower right', fontsize=8.5, framealpha=0.95)

    out = OUT / "figure4_triple_product.png"
    fig.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"Saved {out}")


if __name__ == "__main__":
    fig1_fano_plane()
    fig2_coefficient_heatmap()
    fig3_w_enumeration()
    fig4_triple_product()
    print("\nAll four figures generated.")
