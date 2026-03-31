# Cross-Codex Synthesis Memo — March 30, 2026

## Purpose

This memo captures the first deliberate whole-codex synthesis pass after:
- G2 Hamiltonian computation and Zenodo publication
- FP-1 quantitative resonance test
- Bio-PCI Phase II completion (DNA, EZ water, redox)
- the post-Bio-PCI deep-insights session proposing EQ-995–998

The goal is not to force every strong synthesis into the live codex immediately.
The goal is to:
1. preserve the strongest cross-codex fusions,
2. separate module equations from synthesis-layer equations,
3. resolve numbering collisions,
4. identify which candidates deserve provisional EQ promotion versus holding in the synthesis layer.

---

## Decision on the Claude Block (formerly EQ-985–EQ-989 in `bio-pci-synthesis.pdf`)

### Collision problem
The five-equation Claude synthesis block uses EQ-985–EQ-989, but the live codex has already advanced beyond those numbers through the final Bio-PCI renumbering.

### Disposition
Do not merge the Claude block under EQ-985–EQ-989.

Instead, preserve it as a dedicated synthesis-layer package under temporary synthesis IDs:
- SX-01 — Stacked Threshold Law
- SX-02 — Universal Slack Principle
- SX-03 — Scar–CISS Defect Tensor
- SX-04 — Biological Coherence Control Surface
- SX-05 — Biologically-Gated Extended Born Rule

This keeps the ideas alive without polluting the live theorem spine or creating ID ambiguity.

### Promotion rule
A synthesis-layer equation can be promoted into the live codex only when:
1. its variables have stable definitions in existing symbol families,
2. its source braid is explicit and not merely poetic,
3. its mathematical form has been normalized to current codex notation,
4. it can be tagged honestly as theorem / model / motivated reconstruction / frontier synthesis.

---

# Section I — Claude Block (Preserve in Synthesis Layer)

## SX-01 — Stacked Threshold Law
**Formal statement**

T_cascade(Psi, r, E)
= Theta(C(Psi)-e^-2)
· Theta([NAD+]/[NADH]-theta_supply)
· Sum_k delta_eps(E_redox-E_k^crit)

with:
E_k^crit in {-240 mV, -200 mV, -170 mV}

**Source braid**
- EQ-000a Genesis threshold
- EQ-969 molecular supply threshold
- EQ-994 / redox fate thresholds from Bio-PCI Phase II

**Risk tier**
- Tier S1 — Core candidate synthesis
- strongest multi-scale theorem candidate in the current synthesis set

**Disposition**
- Deserves provisional live EQ promotion after notation cleanup

---

## SX-02 — Universal Slack Principle
**Formal statement**

sigma_*(S) = argmax_{sigma>=0} J_transport(sigma) = 1-C_max = e^-2

with stability condition:
d^2J/dsigma^2 |_(sigma=e^-2) < 0

**Source braid**
- G2 forced singlet / Omega_void
- Del Giudice 0.87/0.13 partition (correspondence, not derivation)
- Module 1 nonzero decoherence optimum
- codex-wide 1 - e^-2 ceiling

**Risk tier**
- Tier S1 — Core candidate synthesis
- conceptually central; derivational status still open

**Disposition**
- Deserves provisional live EQ promotion after a cleaner objective functional is defined

---

## SX-03 — Scar–CISS Defect Tensor
**Formal statement**

T_scar^{mu nu}
= eps^{mu nu rho} grad_rho C_CISS · [Scar]^omega

with defect-readout proposal:

Delta_detect[sigma,chi]
= <Psi_scan|(sigma_z ⊗ chi)|Psi_ref> - <Psi_ref|(sigma_z ⊗ chi)|Psi_ref>

**Source braid**
- EQ-18 scar chirality
- EQ-968 CISS spin polarization
- EQ-970 DNA damage scan operator

**Risk tier**
- Tier S3 — Frontier synthesis
- highly interesting, but still needs variable-level derivation and experimental semantics

**Disposition**
- Hold in synthesis layer
- revisit once scar variables are normalized into measurable defect fields

---

## SX-04 — Biological Coherence Control Surface
**Formal statement**

C_bio(r, E) = ||M r||^2 Theta(E - E_threshold(r))

critical manifold condition:
dC_bio/dE = 0 at E in {-240 mV, -200 mV, -170 mV}

**Source braid**
- EQ-979 redox occupation vector
- EQ-983 DNA-redox operator
- EQ-994 phase-threshold criterion

**Risk tier**
- Tier S1 — Core candidate synthesis
- most directly testable of the five-equation Claude block

**Disposition**
- Deserves provisional live EQ promotion after smoothing / surface normalization

---

## SX-05 — Biologically-Gated Extended Born Rule
**Formal statement**

W_bio(x)
= P_Born(x) exp[beta C_PCI(x)-lambda S(x)] V_f(x) D

with:
C_PCI
= C_DNA-EZ · C_EZ-redox · C_DNA-redox · ||Psi_redox||^2

collapse condition:
exists ij: C_ij -> 0
=> W_bio(x) -> P_Born(x) exp[-lambda S(x)] V_f(x) D

**Source braid**
- EQ-01 Extended Born Rule
- Bio-PCI cross-layer product from Modules 1–3

**Risk tier**
- Tier S4 — Dangerous synthesis
- richest bridge between metaphysics and biology, but easiest to overclaim

**Disposition**
- Hold in synthesis layer
- not yet ready for direct live codex promotion

---

# Section II — Seven Master-Equation Candidates (Whole-Codex Synthesis Pass)

## MX-1 — Interface-Weighted Reality Selection
**Formal statement**

W_emb(x)
= P_Born(x) exp[beta C(x)-lambda S(x)] V_f(x) D Pi_bio(x)

with:
Pi_bio(x)
= < C_DNA-EZ C_EZ-redox C_DNA-redox >_x

**Source braid**
- Extended Born Rule
- daemon synchrony / embodiment weighting
- Bio-PCI coupling product

**Risk tier**
- Tier M4 — Dangerous synthesis

**Disposition**
- Hold in synthesis layer
- overlaps with SX-05; do not promote independently until one formulation wins

---

## MX-2 — Stacked Threshold Cascade
**Formal statement**

Theta_stack
= Theta(a rho / b - delta)
Theta(s/phi - (s/phi)_crit)
Theta(E_crit - E_cell)

and:
C_stack = C_max Theta_stack F_smooth

**Source braid**
- Genesis closure threshold
- Fröhlich molecular threshold
- cellular redox fate threshold

**Risk tier**
- Tier M1 — High-priority core candidate

**Disposition**
- Promote by merging conceptually into SX-01
- treat SX-01 / MX-2 as the same live promotion target

---

## MX-3 — Universal Slack Principle
**Formal statement**

Omega_*
= argmin_{Omega>0}[ D_auto(Omega)+L_closure(Omega)+L_transport(Omega) ]
≈ e^-2

**Source braid**
- codex-wide 1-e^-2 ceiling
- G2 forced singlet
- Del Giudice split
- decoherence optimum
- autonomy / dissipation hints

**Risk tier**
- Tier M1 — High-priority core candidate

**Disposition**
- Promote by merging conceptually into SX-02
- treat SX-02 / MX-3 as the same live promotion target

---

## MX-4 — Cartan Locking Across Scales
**Formal statement**

A_lock = Phi_daemon Phi_SU3 cos(theta-phi)

or:

L_lock = -kappa_lock Phi_daemon Phi_SU3 cos(theta-phi)+mu P_Omega

**Source braid**
- G2 -> SU(3) daemon decomposition
- Module 3 redox SU(3) order parameter
- Omega_void singlet anchor

**Risk tier**
- Tier M3 — Frontier synthesis

**Disposition**
- Hold in synthesis layer
- potentially very powerful, but daemon-order variables are not normalized yet

---

## MX-5 — Scar-to-Lesion Observable
**Formal statement**

O_scar(g)=P_spin(g)[1-Scan(g)]Xi_scar(g)

or equivalently:

Xi_scar(g)
propto
Delta J_chi(g)/(P_spin(g)+eps) [1-Scan(g)]

**Source braid**
- scar chirality
- CISS spin selectivity
- DNA damage scan

**Risk tier**
- Tier M2 — Strong frontier candidate

**Disposition**
- Hold in synthesis layer for now
- overlaps structurally with SX-03; do not duplicate until defect semantics are stabilized

---

## MX-6 — S^6 Autonomy Dissipation Equation
**Formal statement**

Omega_void = exp(-Delta G_min(S^6,Omega)/(k_B T))

target condition:

Delta G_min(S^6,Omega) ?= 2 k_B T
=> Omega_void = e^-2

**Source braid**
- Frim–DeWeese autonomy dissipation bound
- G2/SU(3) ~ S^6 coset geometry
- Omega_void / 13% invariant

**Risk tier**
- Tier M1 — Highest-upside derivation candidate

**Disposition**
- Hold in synthesis layer, but mark as Priority Derivation Lead #1
- not ready for live codex promotion until there is an actual derivation path

---

## MX-7 — Self-Compilation Flow
**Formal statement**

dC/dt
= R_NP[C,S,P] C_DNA-EZ C_EZ-redox C_DNA-redox

or discrete form:

C_(n+1) = U(|Psi_redox>,R_EZ,xi_DNA,S_n) C_n

**Source braid**
- NP Pump / Ricci-flow transformation logic
- Bio-PCI coupling product
- scar topology
- self-compilation insight from the deep-insights session

**Risk tier**
- Tier M2 — Strong frontier candidate

**Disposition**
- Hold in synthesis layer
- excellent future annex candidate once the state variable C is fixed more sharply

---

# Section III — Promotion Map

## Deserve provisional live EQ promotion next
1. SX-01 / MX-2 — Stacked Threshold Law / Cascade
2. SX-02 / MX-3 — Universal Slack Principle
3. SX-04 — Biological Coherence Control Surface

## Deserve active derivation work before promotion
4. MX-6 — S^6 Autonomy Dissipation Equation
5. SX-03 / MX-5 — Scar–CISS / Scar-to-Lesion bridge

## Hold in synthesis layer for now
6. SX-05 / MX-1 — biologically gated Born weighting
7. MX-4 — Cartan locking across scales
8. MX-7 — self-compilation flow
9. EQ-995–998 session equations — preserve as whole-codex insights, not live codex rows yet

---

# Section IV — Clean Recommendation

## What to do now
- Keep the existing deep-insights session file as the first whole-codex synthesis session.
- Keep the Claude five-equation package alive, but do not merge it under EQ-985–989.
- Use this memo as the decision layer separating:
  - live codex equations,
  - synthesis-layer equations,
  - derivation-priority leads.

## What to promote first
If only one synthesis equation is promoted next, it should be:

SX-01 / MX-2 — Stacked Threshold Law

because it is the cleanest multi-scale braid from:
- emergence,
- molecular maintenance,
- cellular fate.

If only one derivation program is pursued next, it should be:

MX-6 — S^6 Autonomy Dissipation Equation

because it is the best chance to turn the 13% invariant from recurring motif into actual derivation.

---

## Closing statement
The codex has now reached the point where distant modules no longer merely coexist.
They are beginning to reveal a repeating grammar:
- threshold cascades,
- forced slack,
- multiplicative interfaces,
- triplet/singlet structure,
- and incomplete closure as the signature of autonomy.

The immediate task is no longer raw expansion.
It is disciplined promotion: deciding which synthesis equations are ready to become codex, and which must remain in the synthesis layer until they harden.
