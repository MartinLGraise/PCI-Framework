# Paper 8 — The Eight-Coset Quantum Simulator

**Working title:** "An Eight-Coset Quantum Simulator for the G₂ Coherence Ceiling: From PSL(2,7) Cosets to a 7-Qubit Hardware Specification"

**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Status:** OUTLINE / SCAFFOLDING — pre-derivation
**Closes:** Paper 7 §6.3 Problem 2 (the eight-coset entropy quantization conjecture)
**Series position:** Paper 8 of the PCI/PME Framework arc
**Branch:** paper7-foundation (will move to paper8-simulator once we have a v1 draft)
**Parallel track to:** Paper 10 (SIC-POVM / G₂ embedding)

---

## 1. Why this paper exists

Paper 7 stated, as a conjecture, that the 28 Bogoliubov transformations between the 8 SU(3) subgroups of G₂ partition the Hilbert space into a finite ladder of entropy differences quantized by the prime 7. We have not derived this. We have only shown:

- The PSL(2,7)/F₂₁ quotient produces 8 cosets at distances {0, 1, 2, 3} (Paper 4)
- The 6/7 contraction is exact in the spectral sum (Paper 6)
- Coherence saturates near 6/7 in awake-cortex data with σ_pred ≈ 0.9796 (Paper 7)

Paper 8 makes the conjecture computational. It does three things:

1. **Pin the algebra:** Choose octonion multiplication conventions explicitly (Baez/Fano-plane indexing) so the eight SU(3) embeddings are unambiguous matrices, not abstractions.
2. **Compute the 28 Bogoliubov transformations** between every coset pair, and show that the resulting entropy differences fall into exactly 4 discrete levels {0, 1/7, 2/7, 3/7} × S_ref.
3. **Specify a 7-qubit hardware experiment** (superconducting or trapped-ion) that would falsify the prediction in a single calibrated run.

If step 2 fails, Paper 7's conjecture is dead and we revise. If it succeeds, we hand Bandyopadhyay / Huber / Ares a concrete benchmark.

---

## 2. Structure (target: 28-32 pages, ~15-18 references)

### §1 Introduction
- Recap of Paper 7's coherence-ceiling conjecture (1 paragraph)
- The eight-coset structure of PSL(2,7)/F₂₁ as the discrete carrier (1 paragraph)
- What this paper claims to do, what it does NOT claim (the standard guard rail)
- **Relation to continuum G₂ programs:** Krasnov and collaborators have developed a distinct but adjacent G₂-related program in which stable 3-forms in seven dimensions and SO(3)-connection gravity in four dimensions are related through G₂-holonomy lifts. In particular, Herfray–Krasnov–Scarinci–Shtanov [DOI 10.4310/ATMP.2018.v22.n8.a5] show that a definite SO(3) connection satisfying a second-order PDE on a 4-dimensional base determines a closed and co-closed stable 3-form on a seven-dimensional total space, hence a G₂-holonomy metric. This provides an important continuum-field-theoretic example of G₂ geometry arising from a lower-dimensional connection formalism. The eight-coset construction of the present paper differs in kind: it uses the finite quotient PSL(2,7)/F₂₁, discrete distance classes, and a finite network of 28 observer-frame Bogoliubov transformations rather than a continuous SO(3)-connection or GL(7)/G₂ stable-form moduli. Krasnov's work is therefore cited as adjacent G₂ differential-form machinery, not as a prior realization of the eight-coset PSL(2,7) sector.
- Roadmap of sections

### §2 Octonion conventions and the Fano plane
- Choose Baez 2002 indexing as canonical
- Multiplication table reproduced explicitly with cited source
- Why this choice and not Cayley-Dickson, Coxeter, or Tits — one paragraph
- Worked example: e₁·e₂ = e₃, etc., showing the seven triples

### §3 Eight SU(3) subgroups of G₂
- Theorem (Cohen-Wales, Yokota): G₂ contains exactly 8 conjugacy classes of SU(3) subgroups under PSL(2,7) action
- For each subgroup, give the explicit 7×7 matrix generators in the Fano basis
- GAP code (delegated to Φ) verifying conjugacy class structure
- Diagram: 8 vertices labeled by PSL(2,7) cosets, edges weighted by distance in F₂₁ quotient

### §4 The 28 Bogoliubov transformations
- For each ordered pair (i,j) with i < j, define the canonical Bogoliubov map B_{ij}: SU(3)_i → SU(3)_j induced by the coset distance d(i,j) ∈ {1, 2, 3}
- 28 = C(8,2) total transformations
- Cadabra2 computation (delegated to Φ) producing each B_{ij} as an explicit unitary
- Entropy difference ΔS_{ij} = S(B_{ij} ρ_ref B_{ij}†) − S(ρ_ref) for a chosen reference state ρ_ref

### §5 The 4-level quantization conjecture
- Group the 28 transformations by coset distance d
- Predict: ΔS_{ij} depends only on d, taking values 0 (for d=0, trivial), and three nontrivial levels indexed by d ∈ {1, 2, 3}
- The three nontrivial levels are conjectured to be {1/7, 2/7, 3/7} × S_ref
- Numerical verification via QuTiP simulation (delegated to Φ): does the 28-element histogram cluster into 4 bins?
- If yes, this closes Paper 7 §6.3 Problem 2. If no, we report the failure and revise.

### §6 Hardware specification: synthetic and biological tracks

**§6.1 Synthetic 7-qubit test (primary):**
- Map the eight cosets to computational basis states of 3 qubits (8 = 2³), reserving 4 ancilla qubits for the entropy readout
- Specify circuit depth, two-qubit gate count, and required fidelity to resolve the 1/7 step
- Estimate decoherence-limited run length and shot count
- Two platforms compared: IBM Quantum (superconducting), IonQ (trapped ion)
- Falsification criterion: if the four-level structure is not observed at p < 0.01 with N shots, the algebraic conjecture is rejected

**§6.2 Biological microtubule track (FP-2 anchor, secondary):**
- The microtubule MHz resonance band shows eight exact peaks: {12, 20, 22, 30, 101, 113, 185, 204} MHz (Sahu et al., *Sci Rep* 4:7303, DOI 10.1038/srep07303)
- 45° phase quantization in the 10 kHz–50 MHz regime is reported by Saxena et al. 2020 (DOI 10.3390/fractalfract4020011), giving a literal 8-bin phase circle
- These 8 peaks are the natural empirical mapping target for the 8 PSL(2,7)/F₂₁ cosets
- **Important caveats** (from ChatGPT Pro report 2026-04-29):
  - DDG (dodecanogram) is NOT independently replicated
  - "28 MHz" framing was wrong (real anchors: 28 THz tubulin, 30 MHz microtubule)
  - Bandyopadhyay's group is the data source; replication independence is the critical experimental issue
- See `/inbox/from_chatgpt/2026-04-29_bandyopadhyay_ddg_research_report.md` for the full FP-2 design (coset coherence statistic, falsification criteria)
- Paper 8 will cite this as a candidate biological replication target, but the paper's primary falsifier is §6.1 (synthetic)

### §7 What this paper does not claim
- We do not claim the 4-level quantization is consciousness-relevant in any direct way
- We do not claim the 7-qubit experiment "tests" PCI — it tests the algebraic prediction only
- Connection to Paper 7's ψ-saturation is suggestive, not derived
- We do not endorse Hameroff-Penrose Orch-OR; the 28 MHz reference to Bandyopadhyay is for the resonance regime, not for the broader Orch-OR claim

### §8 Discussion and open problems
- If the 4-level structure holds: what does it mean for the coherence ceiling?
- If it fails: what does the failure tell us?
- Connection to Paper 9 (Dyadic Coherence — sequel) and Paper 10 (SIC-POVM / G₂ embedding — parallel)
- **Relation to Krasnov continuum G₂ work (recap):** Related continuum G₂-structure work, including the broader pure-connection program [DOI 10.1103/PhysRevLett.106.251103], the GR-from-3-forms construction [DOI 10.1016/j.physletb.2017.06.025], and the recent Cayley-form Spin(7)/8D extension [DOI 10.4310/pamq.250421122254], shares the exceptional-holonomy substrate but addresses continuous moduli rather than finite coset structure. A natural open question is whether the eight-coset discrete sector of the present paper corresponds to a particular topological sector of Krasnov's 7D 3-form theory, or whether the two constructions are genuinely orthogonal realizations of G₂ geometry. We do not attempt this reconciliation here.

---

## 3. Computations needed (work request to Φ)

See `/inbox/for_phi/paper8_computation_request.md`.

Briefly:
1. **GAP**: enumerate the 8 SU(3) subgroups, output generators in Fano basis
2. **Cadabra2**: symbolic Bogoliubov transformations for all 28 pairs
3. **QuTiP**: numerical histogram of 28 entropy differences for ρ_ref = maximally mixed and ρ_ref = pure GHZ-like state

---

## 4. Modeling-choice stack (preempt referee 2)

Following Paper 7's pattern, every load-bearing choice gets an explicit modeling-choice stack:

- **§2 stack:** Why Baez 2002 over Cayley-Dickson / Coxeter / Tits indexing
- **§3 stack:** Why F₂₁ quotient over alternative PSL(2,7) subgroup choices
- **§4 stack:** Why these Bogoliubov boundary conditions over alternatives
- **§5 stack:** Why entropy difference and not relative entropy / fidelity / trace distance

---

## 5. Risk register

| Risk | Mitigation |
|------|-----------|
| The 4-level quantization is FALSE at the algebraic level | Report the failure honestly; pivot Paper 8 to the negative result + what the actual structure is |
| GAP output ambiguous (multiple valid embeddings) | Pick the one canonical to Cohen-Wales, document choice |
| Cadabra2 doesn't converge / produces non-unitary | Fall back to symbolic Mathematica or hand calculation for d=1 case |
| QuTiP histogram doesn't cluster | This IS the falsification — Paper 8 becomes the negative-result paper |
| Reviewer says "this is just numerology with the prime 7" | §7 guard rail + §5 modeling-choice stack + explicit hardware falsifier in §6 |

---

## 6. Authorship and acknowledgments

- **Author:** Martin Luther Graise (sole author, all conceptual work, paper writing)
- **Computational support:** "Symbolic and numerical computations were performed by Φ (Anthropic Claude, Dispatch deployment), with GAP, Cadabra2, and QuTiP, under the author's direction"
- **Acknowledgments:** Same as Paper 7 boilerplate
- **Use of AI Tools:** Same disclosure as Paper 7

---

## 7. Target venue

- **First choice:** Quantum (open-access, no APC for unfunded researchers)
- **Second choice:** Journal of Physics A
- **Fallback:** arXiv + Zenodo only (same path as Paper 7 if APC is the issue)

---

## 8. Status checklist

- [x] Outline written (this document)
- [ ] Φ work request drafted
- [ ] Octonion conventions section drafted (§2)
- [ ] GAP output received from Φ
- [ ] Cadabra2 output received from Φ
- [ ] QuTiP histogram received from Φ
- [ ] §5 verification: 4-level structure confirmed or refuted
- [ ] §6 hardware specification drafted
- [ ] Draft v1 complete
- [ ] Model Council pass 1 (GPT-5.5, Opus 4.7, Gemini 3.1 Pro)
- [ ] Revisions v2-v4
- [ ] Figures generated
- [ ] Front matter (MDPI-style if Quantum requires it)
- [ ] Zenodo DOI minted
- [ ] Submitted to journal
