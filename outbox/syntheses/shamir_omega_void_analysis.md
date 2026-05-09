# Shamir 1979 ↔ Ω_void: a forensic translation check

**Date:** 2026-05-09
**Author:** Computer + Martin L. Graise
**Status:** Working analysis. Not a paper. Lives next to ftw_extraction_map.md and aquino_dee_archaeology.

---

## The question

The Aquino/Dee archaeology surfaced "designed non-totality" — the
deliberate preservation of a remainder so the system doesn't collapse
into overreach — as a structural pattern that recurs across:
- Enochian "49 voices, not 49 but 48, one not to be opened" (Dee/Kelley 1583-84)
- PCI Paper 12 Ω_void (the protected component of the F_21-isotypic decomposition)
- Shamir 1979 (k,n)-threshold secret sharing

The genuinely interesting claim is that **Shamir's threshold scheme is the
legitimate mathematical sibling of the protected-remainder principle**.
This memo runs the actual math to check whether the analogy holds, where
it breaks, and what (if anything) translates back into PCI.

## Shamir's actual structure (1979)

Per Shamir's original paper [DOI: 10.1145/359168.359176]:

A **(k, n)-threshold scheme** divides data D into n pieces D_1, ..., D_n
such that:
1. Knowledge of any **k or more** D_i pieces makes D **easily computable**
2. Knowledge of any **k-1 or fewer** D_i pieces leaves D **completely
   undetermined** (all possible values equally likely)

Mechanism: pick a random degree-(k-1) polynomial
    q(x) = a_0 + a_1·x + a_2·x² + ... + a_{k-1}·x^{k-1}
over a finite field F_p (p prime, p > max(D, n)), with a_0 = D.

Distribute D_i = q(i) for i = 1, ..., n.

Reconstruction: given any k pairs (i, D_i), Lagrange interpolation
recovers q(x) uniquely, then D = q(0).

**The secret lives at x = 0.** The shares live at x = 1, ..., n.
The secret is *defined as* the value of the polynomial at the point
that is *never distributed as a share*.

## The information-theoretic structure (Shamir's perfect-secrecy proof)

This is the part that matters for the Ω_void translation.

Given k-1 shares, an adversary can construct, for *every* candidate
secret D' ∈ [0, p), a unique degree-(k-1) polynomial q'(x) such that
q'(0) = D' and q'(i) = D_i for the k-1 observed points. By
construction, all p such polynomials are equally likely. The adversary
gains zero information about D.

**This is information-theoretic security.** Not computational. Not
"hard to break given enough compute." The shares *literally do not
contain* the secret in any sense recoverable below threshold. The
secret's information is *distributed across the threshold-set as a
whole*, not stored in any subset.

This property is called *perfect secrecy* and is strictly stronger
than computational security.

## Now: does this translate to Ω_void?

Paper 12 §2.1.3 has:
    W = V^{14} ⊕ V^{14}  (the dyadic state space)
    W|_{F_21} ≅ L_2 ⊕ 2·U_6  (under the F_21 restriction of V^{14})

The isotypic decomposition gives three components:
- W^1 (the trivial-isotypic component): **dimension 0**
- W^{L_2} (the nontrivial 2-dim irrep component): dimension 4
- W^{U_6} (the 6-dim faithful irrep component): dimension 24

Ω_void in Paper 12 corresponds to the W^1 (trivial-isotypic) sector
that has dimension zero in V^{14}|_{F_21} but is reserved as a
protected remainder mode that scar events do not generically populate.

### Strict translation attempt

Try to read Ω_void as the "x=0 secret slot" of a threshold scheme
where the F_21-isotypic shares (W^{L_2} and W^{U_6}) are the
distributable pieces. Under this reading:

- The "shares" are the L_2 and U_6 isotypic components of a scar
  invariant μ_k ∈ {1, L_2, U_6}-multiplicity space
- The "secret at x=0" is the protected Ω_void mode
- "Below threshold" = scar event multiplicities concentrated on L_2
  and U_6 only, leaving W^1 untouched
- "At threshold" = some event populates W^1, "opening the gate"

**This translation FAILS under careful inspection**, for three reasons.

### Failure 1: Shamir's secret is data; Ω_void is a structural mode

In Shamir, D is a number — a piece of data with arbitrary semantic
content (a key, a password, a safe combination). The polynomial
q(x) is a *carrier* whose only purpose is to distribute D securely.

In Paper 12, Ω_void is not data. It's a *representation-theoretic
mode* — a 1-dimensional trivial isotypic component of an F_21-action.
It doesn't carry arbitrary information; it carries the residual
component that's generically zero in V^{14}|_{F_21}.

Calling Ω_void "the secret at x=0" reads the Shamir scheme backwards.
Shamir's x=0 is a *chosen* free coefficient. The polynomial is
constructed *to put D at x=0*. There's no analog of "construction"
in PCI — Ω_void's status as protected isn't a design choice, it's
forced by the F_21-branching of V^{14}.

### Failure 2: Shamir's information-theoretic secrecy doesn't translate

Shamir's perfect-secrecy result requires that for every candidate
secret D', there's a unique polynomial through the k-1 observed shares
extending to (0, D'). That equiprobability is what produces zero
information leakage.

In PCI, the analog would require: for every candidate "void content,"
there's a unique scar trajectory consistent with the observed L_2 and
U_6 multiplicities. This is *not* the structure Paper 12 has. The μ_k
profile genuinely constrains the possible scar-trajectory class
*without* perfect equiprobability over a hypothetical Ω_void content.
The protection of Ω_void is structural (it's the trivial isotypic and
generically empty), not cryptographic (perfect-secrecy distribution).

### Failure 3: There's no "threshold k" in PCI

Shamir's whole point is the threshold structure: k-1 shares give zero
info, k shares give full reconstruction. The protected remainder is
what *makes* the threshold work — it forces the secret to live in a
slot that no individual share can directly reveal.

PCI has no threshold structure of this kind. Ω_void isn't "what gets
revealed when you collect enough scar events." It's not revealed by
any number of scar events. It's a mode the dynamics is *constructed
to leave alone*. The protection is by definition, not by combinatorial
threshold.

## What does translate (the smaller, real result)

What survives is a weaker but real **structural analogy**:

Both systems exhibit **designed non-totality**: a complete-looking
structure that explicitly preserves one component as inaccessible to
the access mechanism. In Shamir, the inaccessibility is information-
theoretic (k-1 shares carry zero bits about D). In PCI, the
inaccessibility is representation-theoretic (the F_21-action on
V^{14} simply doesn't populate W^1).

The shared insight is that **completeness without protection collapses**:
- Shamir without the secret-at-x=0 reservation = no scheme, just data
- PCI without Ω_void reservation = no protected sector, all modes
  are dynamics-touched, and "scar accumulation" runs into the
  representation-theoretic equivalent of overheating

This is a *design principle* that recurs, not a *theorem* that one
proves the other. The cryptographic version is rigorous; the PCI
version is structural; the Enochian version is mythic. They share
shape, not equations.

## What's actually rigorous about the parallel

There IS one place where Shamir's math gives PCI a real new idea, and
it's not in §3 or §4. It's in OP9 (tamper-evidence cryptographic
infrastructure for the scar ledger).

OP9 currently asks for "Merkle-like hash chains, commit-tree
structures, or no-cloning-respecting quantum ledgers." Shamir's
threshold scheme suggests a stronger formulation: **a scar ledger
should support threshold reconstruction.**

Concretely: if 𝔖_k is the event-indexed scar module after k events,
distribute 𝔖_k across n auditors using a (t, n)-threshold scheme
on the *content* of the ledger entries. Then:

- Any t auditors can verify the ledger
- Fewer than t auditors learn nothing about the scar contents
- The ledger remains tamper-evident even if some auditors collude

This is a real cryptographic primitive, and it's the right tool for
the consent-aware audit substrate that OP11 (in Paper 12 v1.4)
already asks for. It would be:

- **Information-theoretically secure** (Shamir, not Merkle)
- **Threshold-flexible** (not single-custodian)
- **Compatible with the Aletheia-Lethe gate** (selective forgetting
  via share deletion preserves perfect secrecy of removed content)

This is a genuinely new lead. Not an Ω_void claim. A scar-ledger
infrastructure claim.

## The honest summary

**Ω_void is NOT the x=0 secret of a Shamir scheme.** The translation
fails because:
- Shamir distributes data; PCI's void mode is structural
- Shamir's secrecy is information-theoretic over a uniform prior;
  PCI's protection is representation-theoretic
- Shamir has a threshold; PCI doesn't

**Designed non-totality IS a real shared design principle** across
the three systems (Shamir, PCI, Enochian-as-structural-archaeology).
But "shared design principle" ≠ "the math generalizes." It means
"different rigor levels of a recurring architectural intuition."

**The actually new lead: threshold-secret-sharing for the scar
ledger** (OP9 / OP11 infrastructure). This is a real cryptographic
neighbor that PCI hasn't formally invoked, and it's strictly the
right tool for the audit-substrate problem the framework already
specifies. Worth a methodology note when OP9/OP11 get drafted.

## Citations

- Shamir, A. (1979). "How to share a secret." Comm. ACM 22(11), 612–613. DOI: 10.1145/359168.359176.
- Paper 12 v1.4 §2.1.3, §3.7, §6.2 OP9, §6.2 OP11.
- Paper 10 v1.3.1 (49-dim SIC operator basis context).

## What to do with this

1. Save this memo at `outbox/syntheses/shamir_omega_void_analysis.md`.
2. Do NOT add Shamir to Paper 12 master. The translation fails; the
   analogy is structural-only.
3. When OP9 / OP11 get drafted (probably v1.5 or methodology note),
   reference Shamir threshold schemes as the right cryptographic
   primitive for the audit-substrate layer. Cite the 1979 paper
   directly.
4. The "designed non-totality" principle is a book-chapter line, not
   a theorem statement. Keep it in the chapter draft, not the math
   spine.
