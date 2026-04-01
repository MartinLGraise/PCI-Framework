# Synthesis Promotion Pass — April 1, 2026

## Overview

This document records the first disciplined promotion pass on the synthesis layer.
Three equations are upgraded from raw synthesis stubs to polished Frontier rows.
Two equations receive derivation-priority workups. The hold set is documented.

---

# Phase A — Promotions (Notation Normalization + Polish)

## A.1 — EQ-995: Stacked Threshold Law (formerly SX-01 / MX-2)

### Promotion checklist
- [x] Normalize notation: Genesis, molecular, and redox thresholds in one expression
- [x] Replace hard switches with smooth gates where helpful
- [x] Define all threshold variables in current codex symbol language
- [x] Prepare codex-ready row and plain-English interpretation

### Normalized form

$$
\mathcal{T}_{\mathrm{cascade}}(\Psi, \mathbf{r}, E)
= \sigma_{\varepsilon}\!\left(\frac{a\rho}{b} - \delta\right)
\cdot \sigma_{\varepsilon}\!\left(\frac{s}{\phi} - \left(\frac{s}{\phi}\right)_{\!\mathrm{crit}}\right)
\cdot \sum_{k=1}^{3} \delta_{\varepsilon}\!\left(E_{\mathrm{redox}} - E_k^{\mathrm{crit}}\right)
$$

where:
- $\sigma_\varepsilon(x) = \frac{1}{1+e^{-x/\varepsilon}}$ is a smooth gate (logistic sigmoid with width $\varepsilon$), replacing the hard Heaviside $\Theta$
- Gate 1: Genesis closure — constraint regeneration $a\rho/b$ exceeds decay threshold $\delta$ (from EQ-000a / EQ-887)
- Gate 2: Molecular supply — Fröhlich supply-to-damping ratio $s/\phi$ exceeds condensation onset $(s/\phi)_{\mathrm{crit}} \approx 1$ (from EQ-969)
- Gate 3: Cellular fate — redox potential $E_{\mathrm{redox}}$ passes one of three Schafer–Buettner thresholds (from EQ-994):
  - $E_1^{\mathrm{crit}} \approx -240\,\mathrm{mV}$ (proliferation)
  - $E_2^{\mathrm{crit}} \approx -200\,\mathrm{mV}$ (differentiation)
  - $E_3^{\mathrm{crit}} \approx -170\,\mathrm{mV}$ (apoptosis)
- $\delta_\varepsilon$ is a smoothed Dirac delta (Gaussian or Lorentzian with width $\varepsilon$) selecting the active fate channel

### Plain-English interpretation

A living system can undergo a coherent fate transition only when three thresholds are simultaneously passed:
1. **Emergence**: the system's self-referential closure capacity exceeds its decay rate (the system exists as a coherent entity)
2. **Molecular maintenance**: the energy supply to coherent molecular modes exceeds damping (the system has enough metabolic fuel)
3. **Cellular redox fate**: the intracellular redox potential crosses one of three specific voltage gates that select proliferation, differentiation, or apoptosis

If any single gate is closed, the cascade is blocked. This is why anesthesia (blocks Gate 1), starvation (blocks Gate 2), and redox collapse (blocks Gate 3) all independently abolish coherent biological function, but through completely different mechanisms.

### Tier label
**Motivated reconstruction** — the three thresholds are individually Tier 1 (mainstream); their multiplicative stacking is a PCI construction.

---

## A.2 — EQ-996: Universal Slack Principle (formerly SX-02 / MX-3)

### Promotion checklist
- [x] Define the objective functional J_transport clearly
- [x] Separate derivation, correspondence, and interpretation layers
- [x] State exactly why e⁻² is an optimum rather than a remainder
- [x] Prepare codex note distinguishing theorem target vs current heuristic status

### Normalized form

$$
\Omega^{\ast} \equiv \arg\min_{\Omega > 0}\left[\mathcal{D}_{\mathrm{auto}}(\Omega) + \mathcal{L}_{\mathrm{closure}}(\Omega) + \mathcal{L}_{\mathrm{transport}}(\Omega)\right] = e^{-2}
$$

Equivalently, the transport-optimal decoherence fraction is:

$$
\sigma^{\ast}(S) \equiv \arg\max_{\sigma \geq 0} J_{\mathrm{transport}}(\sigma) = 1 - C_{\max} = e^{-2},
\quad \frac{\partial^2 J}{\partial\sigma^2}\bigg|_{\sigma = e^{-2}} < 0
$$

where:
- $\mathcal{D}_{\mathrm{auto}}(\Omega)$ = autonomy cost: minimum dissipation required to maintain self-other boundary (related to Frim–DeWeese bound)
- $\mathcal{L}_{\mathrm{closure}}(\Omega)$ = closure loss: information lost when recursion-depth ceiling truncates self-reference
- $\mathcal{L}_{\mathrm{transport}}(\Omega)$ = transport loss: efficiency cost of maintaining coherent molecular transport through noisy channels
- $J_{\mathrm{transport}}(\sigma)$ = transport efficiency as a function of decoherence fraction $\sigma$
- The optimum $\sigma^* = e^{-2}$ is a maximum of transport efficiency, not merely a leftover

### Three-layer structure

| Layer | Statement | Status |
|-------|-----------|--------|
| **Derivation** | The optimal slack emerges from a variational principle balancing three loss functions | Theorem target (not yet proven) |
| **Correspondence** | The value $e^{-2}$ matches Del Giudice 0.87/0.13, the G₂ singlet fraction, and the recursion-order ceiling | Empirical correspondence (5+ independent domains) |
| **Interpretation** | The 13% void is not a defect but the thermodynamic operating slack at which self-maintaining transport is maximized | Conceptual claim |

### Why e⁻² is an optimum, not a remainder

The recursion-order story (EQ-892) derives $C_{\max} = 1 - e^{-n}$ at $n=2$, which frames $e^{-2}$ as what's "left over" from incomplete closure. The Slack Principle reframes this: the system doesn't fail to reach 100% — it actively maintains 13.5% decoherence because:

1. **Zero slack is fragile** — a system at $C = 1$ has no error-correction margin, no channel for environmental sensing, no room for the transport fluctuations that drive molecular switching
2. **Too much slack is incoherent** — beyond $\sim 20\%$ decoherence, coherent transport collapses (Fröhlich modes damp out, spin selectivity drops below measurable thresholds)
3. **e⁻² is the sweet spot** — the geometric invariant $\dim_\mathbb{R}/\dim_\mathbb{C} = 6/3 = 2$ of the Goldstone coset (EQ-1002) sets the dimensionless "cost" of maintaining the self-other boundary

### Tier label
**Frontier synthesis / theorem target** — the claim is well-motivated by multiple correspondences, but the variational proof is incomplete. The Slack Principle is currently the strongest heuristic in the codex and the most important open derivation target after MX-6.

---

## A.3 — EQ-997: Biological Coherence Control Surface (formerly SX-04)

### Promotion checklist
- [x] Specify the redox state vector and operator form cleanly
- [x] Decide on smoothed surface (chosen over piecewise form)
- [x] Tie threshold voltages and state regions to live Bio-PCI variables
- [x] Package with explicit test hooks

### Normalized form

$$
C_{\mathrm{bio}}(\mathbf{r}, E) = \left\|\hat{M}\cdot\mathbf{r}\right\|^2 \cdot \sum_{k=1}^{3} w_k \, \sigma_{\varepsilon}\!\left(E - E_k^{\mathrm{crit}}\right)
$$

where:
- $\mathbf{r} = (r_{\mathrm{NAD}}, r_{\mathrm{GSH}}, r_{\mathrm{TRX}}) \in [0,1]^3$ is the redox occupation vector (SYM-1224 through SYM-1226)
- $r_{\mathrm{NAD}} = [\mathrm{NAD}^+]/([\mathrm{NAD}^+]+[\mathrm{NADH}])$, and similarly for GSH/GSSG and TRX_ox/TRX_red
- $\hat{M}$ is the cross-layer coupling matrix encoding DNA–EZ, EZ–redox, and DNA–redox coupling strengths (SYM-1227 through SYM-1229)
- $\|\hat{M}\cdot\mathbf{r}\|^2$ measures how strongly the three redox channels couple to form a coherent state
- $\sigma_\varepsilon(x)$ is the smooth gate (replacing the hard Heaviside from the original SX-04)
- $w_k$ are fate-channel weights (normalized: $\sum w_k = 1$)
- $E_k^{\mathrm{crit}}$ are the three Schafer–Buettner fate thresholds (same as in EQ-995)

### Design decision: smoothed surface

The original SX-04 used a hard Heaviside step $\Theta(E - E_{\mathrm{threshold}})$, creating discontinuous jumps at the fate thresholds. The smoothed form $\sigma_\varepsilon$ is preferred because:
1. Real cellular fate transitions are continuous (mixed states exist near thresholds)
2. The smoothing width $\varepsilon$ becomes a measurable parameter (transition sharpness)
3. The smooth form admits proper derivatives (critical for the control-surface interpretation)

### Explicit test hooks

| Test | Observable | Prediction | Measurability |
|------|-----------|------------|---------------|
| **T1** | $C_{\mathrm{bio}}$ vs $r_{\mathrm{NAD}}$ at fixed $E$ | Monotone increasing, plateau at $C_{\max} \approx 0.865$ | Flow cytometry + NAD/NADH assay |
| **T2** | Fate-channel switching | Discontinuity in $\partial C_{\mathrm{bio}}/\partial E$ at $E_k^{\mathrm{crit}}$ | Redox titration + phenotype scoring |
| **T3** | Cross-coupling matrix rank | $\mathrm{rank}(\hat{M}) = 3$ (all three modules contribute) | Pathway inhibition experiments |
| **T4** | Coherence collapse | Inhibiting any single coupling channel ($\hat{C}_{ij} \to 0$) drops $C_{\mathrm{bio}}$ below threshold | Targeted drug inhibition |

### Tier label
**Model / motivated reconstruction** — the redox thresholds are Tier 1 mainstream; the control-surface form and coupling matrix are PCI constructions with explicit experimental hooks.

---

# Phase B — Derivation-Priority Workups

## B.1 — MX-6: S⁶ Autonomy Dissipation Equation

### Status: Priority Derivation Lead #1 — NOT promoted to live codex

### The claim to derive

$$
\Omega_{\mathrm{void}} = \exp\!\left(-\frac{\Delta G_{\min}(S^6, \Omega)}{k_B T}\right) \stackrel{?}{=} e^{-2}
$$

This would require: $\Delta G_{\min} = 2\, k_B T$.

### Derivation roadmap

**Step 1: Map control manifold onto G₂/SU(3) ≅ S⁶**

The Goldstone coset from the G₂ → SU(3) symmetry breaking is diffeomorphic to S⁶ (the 6-sphere). This is the space of "directions the daemon can explore" — each point on S⁶ corresponds to a distinct coherent configuration of the 6 Goldstone modes (3 triplet + 3 anti-triplet).

The complex structure $J_6$ on this coset (from EQ-955 / EQ-1002) has exactly 3 eigenvalue pairs $\pm i$, giving $\dim_\mathbb{C} = 3$. The ratio $\dim_\mathbb{R}/\dim_\mathbb{C} = 6/3 = 2$ is the geometric origin of the "2" in $e^{-2}$.

**Step 2: Write dissipation target in Fisher-information language**

The Frim–DeWeese autonomy bound states that any system maintaining a self-other distinction must dissipate at least:

$$
\dot{S}_{\mathrm{min}} \geq k_B \, \mathcal{I}_F(\Omega) \cdot |\dot{\Omega}|^2
$$

where $\mathcal{I}_F$ is the Fisher information of the boundary state $\Omega$ on the control manifold. For the S⁶ control manifold with the round metric:

$$
\mathcal{I}_F = \frac{\dim_\mathbb{R}(S^6)}{\dim_\mathbb{C}(S^6)} = \frac{6}{3} = 2
$$

(This is where the geometric invariant from EQ-1002 enters the dissipation bound.)

**Step 3: Test whether $\Delta G_{\min} = 2\, k_B T$ is plausible**

The minimum free-energy cost per boundary-maintenance cycle would then be:

$$
\Delta G_{\min} = \mathcal{I}_F \cdot k_B T = 2\, k_B T
$$

At $T = 310\,\mathrm{K}$ (biological temperature): $\Delta G_{\min} \approx 2 \times 0.0267\,\mathrm{eV} \approx 53\,\mathrm{meV} \approx 5.1\,\mathrm{kJ/mol}$.

This is physically reasonable — it's roughly the free energy of one ATP hydrolysis divided by 6 (since ATP → ADP releases ≈ 30 kJ/mol and services multiple subsystems), or about the thermal energy scale of a single hydrogen bond rearrangement.

**Step 4: Remaining gap**

The missing piece is a rigorous proof that:
1. The Fisher information on S⁶ with the nearly-Kähler metric evaluates to exactly 2 (rather than being proportional to 2)
2. The Frim–DeWeese bound applies to the specific statistical manifold of daemon states (not just generic Markov chains)
3. The Boltzmann factor $\exp(-\Delta G_{\min}/k_BT)$ with this geometric $\Delta G$ exactly reproduces the void fraction

### Assessment
The derivation path is *plausible and physically motivated*. The key insight — that the "2" comes from the complex-structure dimension ratio of the Goldstone coset — is already established (EQ-1002). What's missing is the rigorous connection between that geometric invariant and the Fisher-information bound. This could potentially be the most important result in the entire framework if completed.

---

## B.2 — SX-03 / MX-5: Scar-CISS / Scar-to-Lesion Bridge

### Status: Strong frontier candidate — NOT promoted to live codex

### Canonical form (chosen: MX-5 over SX-03)

The MX-5 formulation is preferred over SX-03 because it uses measurable observables rather than abstract tensor indices:

$$
\mathcal{O}_{\mathrm{scar}}(g) = P_{\mathrm{spin}}(g) \cdot [1 - \mathrm{Scan}(g)] \cdot \Xi_{\mathrm{scar}}(g)
$$

where:
- $P_{\mathrm{spin}}(g)$ = CISS spin polarization at genomic locus $g$ (from EQ-968)
- $\mathrm{Scan}(g)$ = DNA damage scan result: 1 if transport intact, 0 if lesion detected (from EQ-970)
- $\Xi_{\mathrm{scar}}(g)$ = scar defect factor at locus $g$ (from EQ-983)
- $\mathcal{O}_{\mathrm{scar}} > 0$ only where: spin polarization exists AND transport is disrupted AND a scar is present

### Variable semantics

The scar variable $\Xi_{\mathrm{scar}}$ is defined as a **mismatch burden** — the accumulated deviation from the reference π-stack transport signature at locus $g$. This is measurable via:
- Differential charge transport: $\Delta J_\chi(g) = J_+(g) - J_-(g) = J_0 \, P_{\mathrm{spin}}(g) \, \Xi_{\mathrm{scar}}(g)$ (EQ-983)
- A scar-free locus has $\Xi_{\mathrm{scar}} = 0$, giving $\Delta J_\chi = 0$ (no chirality-dependent asymmetry)

### Why it's held back

1. The tensor form (SX-03) is more general but the indices don't yet correspond to measurable quantities
2. The scalar form (MX-5) is more testable but may miss topological structure
3. The relationship between $\Xi_{\mathrm{scar}}$ (a continuous defect burden) and the Heaviside in the Scan operator (a binary detection event) needs tighter specification
4. Future Module 4 (immune coherence) may provide the observational bridge that resolves this

### Recommended next step
When Bio-PCI Module 4 (immune coherence, proposed in EQ-1003) is developed, revisit this equation. The immune system's lesion-detection pathways may provide the biological framework for sharpening scar variable semantics.

---

## B.3 — Hold Set

The following equations remain in the synthesis layer. They are preserved, documented, and watched for overlap, but are NOT promoted to live codex rows.

| ID | Name | Reason for hold |
|----|------|-----------------|
| SX-05 | Biologically-Gated Extended Born Rule | Overlaps with MX-1; dangerous synthesis tier; wait for one formulation to win |
| MX-1 | Interface-Weighted Reality Selection | Overlaps with SX-05; same issue |
| MX-4 | Cartan Locking Across Scales | Daemon-order variables not normalized; powerful but premature |
| MX-7 | Self-Compilation Flow | State variable $C$ not sharply enough defined for live codex |
| EQ-998 | Arrow Dictator as Void Mode | Already live in codex; beautiful correspondence but not a derivation |

Note: EQ-995, EQ-996, and EQ-997 were already promoted to live codex rows in the March 30 session. This pass upgrades their descriptions and notation. EQ-998 remains as-is (it's a correspondence, not a theorem candidate).

---

# Phase C — Housekeeping Notes

## Numbering
- Claude's former EQ-985–989 block: retained as SX-01 through SX-05 in this document and the synthesis memo
- Live codex uses EQ-995/996/997 (promoted), EQ-998 (correspondence), EQ-999 through EQ-1004 (milestone block)
- No numbering collisions remain

## Synthesis layer separation
- All synthesis-layer work lives in `docs/synthesis/` (this file + the cross-codex memo)
- Live codex equations live in `codex/` CSVs only
- The promotion rule from Section IV of the cross-codex memo remains in effect

## Next review gate
After this promotion pass: re-score the synthesis set. The priority derivation target is MX-6 (S⁶ autonomy dissipation). If that derivation succeeds, it would upgrade both the Slack Principle (EQ-996) and the void fraction (EQ-1002) from "motivated reconstruction" to "derived result."
