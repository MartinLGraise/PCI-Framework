# Paper 7 — READ FIRST (C-7RO Briefing)

**Date:** 2026-04-23 | **From:** Φ | **Branch:** paper7-foundation

Three findings from this session that you need to know before touching anything else.

**First: A3 is two papers, not one.** "Basso et al." does not exist. PRL 134:050406 is by Basso L and Céleri LC only. The JHEP paper (07(2025)146) is by De Vuyst, Eccles, Höhn, and Kirklin — a completely different group. Paper 7's reference list must split these. See `outbox/paper7/anchor_papers_verified.md`.

**Second: the 10⁹ claim for prediction (b) is wrong for biology and needs to be cut.** Wadhia's 10⁹ ratio is quantum-to-classical amplification cost for a quantum clock readout — it requires wavefunction collapse of a macroscopic pointer state. The G₂/M checkpoint is a classical biochemical switch with ~50–100x kinase cascade gain, not 10⁹. The correct Landauer-based prediction is ΔE_min ≈ 16 zJ (for log₂(42) ≈ 5.4 bits at 310 K) — a cleaner, still non-trivial, parameter-free bound. See `inbox/for_human/10e9_flag.md` for three remediation options. Martin needs to choose before Paper 7 is drafted.

**Third: predictions (a), (c), and (d) each have one blocking gap that only you can fill.** For (a): which of three reference quantities does "1/7 of some reference" mean — T_bath, S_eq(ω), or χ_eq(ω)? For (c): which G₂ representation, what PaW clock Hamiltonian, what reference entropy? For (d): what exactly is "49," and is the sign of c derivable from G₂ structure or a free parameter? Questions are in `inbox/for_c7ro/`. None of these predictions can be finalized without your answers.

The derivation work and dataset identification are complete. The branching ratio prediction (d) is the most immediately testable — Hengen-Shew data is open on Zenodo (record 15420312). Start there while the other questions are being resolved.
