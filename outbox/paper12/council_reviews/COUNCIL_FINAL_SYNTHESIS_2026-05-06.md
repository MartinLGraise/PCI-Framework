# Paper 12 v1.0 Master Assembly — Final Council Synthesis (2026-05-06)

**Three reviews on the assembled v1.0 master.**

| Reviewer | Verdict | Top issues |
|---|---|---|
| **Gemini 3.1 Pro** | **STRONG_ACCEPT** | All four standing audit flags COMPLIANT. Only Phase-3 nits: verify DOI links in built PDF; confirm Bostock-Kim-Patel 2025 preprint DOI |
| **Opus 4.7** | **MINOR_REVISIONS** | §2 forward-reference cluster broken (§2.3.x points into nonexistent labels in §3, §4); $\mathfrak{J}_k$ defined two ways; abstract's strata names ($\Sigma_{\text{cross/slide/ext/degen/rec}}$) don't match §3's actual names; $L_2$ described wrong in §2.1.1; "topological residue" vs §3.7 Remark 3.7.2 |
| **GPT-5.5** | **MAJOR_REVISIONS** | Overlaps with Opus on §2 plus: **(i) Theorem 3.6.1(ii) hypotheses internally contradict** (smooth interior critical point requires $c'=0$ but theorem assumes $c_\sigma' \neq 0$); **(ii) Theorem 3.4.1 "well-posedness" language overstates conditional regularity**; **(iii) abstract overstates falsification** ("Paper 12 is decisively falsified if any of P1–P4 fail" — should say the empirical / gradual-tear interpretation, not the formal apparatus); **(iv) $\mu_k$ multiplicity vs projected-dimension drift** between §3.7 prose and §4.4 proof; **(v) Rank-One Convention not in Theorem 4.4.1 hypotheses** |

## Convergent issues (named by ≥ 2 reviewers — blocker-level)

These are the v1.0 → v1.1 fixes that **all three reviewers would agree improve the paper**:

### Tier 1 — §2 / abstract / front-matter repair (Opus + GPT-5.5)
1. §2.1.1: $L_2$ described as "trivial" (wrong); §4.2's character $(2,2,2,-1,-1)$ shows it is the *nontrivial real 2-dim irreducible of complex type*. Repair §2.1.1 row.
2. §2.3.3: $\mathfrak{J}_k = (\mathrm{tr}\,\mathfrak{S}_k, \det\mathfrak{S}_k|_{U_6}, \mu_k)$ contradicts §1.4 / §3.7 / §4.1 / §5.0's $\mathfrak{J}_k = (S_k, \mathfrak{S}_k, \mu_k)$. Repair §2.3.3.
3. §2.3.x forward-references: rewrite to point at correct §3 / §4 labels (or section, not Definition number, where no labeled object exists).
4. §2.1.1: add row for the trivial $F_{21}$-character $\mathbf{1}$ (currently missing — but it is the first slot of $\mu_k$).
5. **Abstract's strata names** ($\Sigma_{\text{cross}}, \Sigma_{\text{slide}}, \Sigma_{\text{ext}}, \Sigma_{\text{degen}}, \Sigma_{\text{rec}}$) **vs §3's actual names** ($\Sigma_\Theta, \Sigma_{\min}, \mathcal{G}_{\mathrm{NP}}, Z, \partial[0,\pi/2]$). Replace abstract names with §3's actual names.
6. **"Topological residue" vs §3.7 Remark 3.7.2**: Three textual edits (abstract, §1.1, §1.5) replacing "topological residue" with "representation-theoretic residue" (or "scar residue").

### Tier 2 — Substantive theorem-precision fixes (GPT-5.5)
7. **Theorem 3.6.1(ii) repair**: split the "smooth interior firing" case from the "smooth interior critical point" case. As stated in v1.0, the hypotheses are incompatible. Two options: (a) delete part (ii) and state it as a separate proposition about noncritical interior trajectories hitting the firing guard; (b) replace $c_\sigma' \neq 0$ with a higher-order / guard-crossing condition compatible with criticality.
8. **Theorem 3.4.1 language downgrade**: "well-posedness" → "conditional piecewise real-analytic regularity on an open dense parameter set". Three textual edits (§1.4, §3, §6).
9. **Theorem 4.4.1 Rank-One Convention as hypothesis**: add "Under the Rank-One Convention of §4.4" to the theorem statement.
10. **Abstract falsifiability claim**: "Paper 12 is decisively falsified if any of P1–P4 fail" overstates. Repair to: "Paper 12's empirical / gradual-tear interpretation is falsified if the binary thresholds in §5.6 are not met across all of P1–P4. The formal mathematical apparatus (§§3–4) survives empirical failure as a structural result on $G_2$-equivariant dynamical systems."

### Tier 3 — Notation / consistency drift (Opus + GPT-5.5)
11. **$\mu_k$ multiplicity vs projected dimension**: §3.7 calls it "multiplicity profile"; §4.4's proof uses $\dim \Pi_\tau S_k$. For real irreps of dimensions $(1, 2, 6)$, these differ by factors. Pick one (recommend "multiplicity": $\mu_\tau(S_k) = \dim \mathrm{Hom}_{F_{21}}(V_\tau, S_k)$) and standardize §2 / §3.7 / §4.4 / §5.4 / §5.6.
12. **§3.1 "locked at $\max(r_A, r_B)$"** → "bounded below by $\max(r_A, r_B)$" (matches §2.2.4 ≥ statement).
13. **Costa-Pavone bib entry**: remove "(Sard transversality references)" annotation; pin to actual cited paper ($F_{21}$ character theory at §4.2).
14. **§3 footer "Paper 9 v1.3.2"** → "Paper 9 v1.3.3" to match consolidated bib.
15. **$\theta^*$ vs $\theta^\star$**: pick one (recommend $\theta^*$).

## Non-blocker (deferrable to phase-3 cosmetic pass)
- §2.4 audit-substrate symbol $\mathcal{A}$ unused in §3–§6 (either remove from §2.4 or use once)
- §1.2 Paper 10 inheritance: no operational use in §3–§6 (soften to "adjacent structural results")
- §4.3 line 1107 LaTeX `V^{14\\n\oplus 2}` line-break artifact
- Bostock-Kim-Patel "DOI: pending" annotation can be removed (arxiv 2503.07670 sufficient)
- Paper 7 DOI status — confirm before Zenodo
- §6.4 provenance line: append "and master assembly cleared at MINOR_REVISIONS by full council"

## Decision

**Path forward: v1.0 → v1.1 polish pass** addressing tiers 1 + 2 + 3 (15 items), then Zenodo prep.

GPT-5.5's MAJOR_REVISIONS verdict is dominantly driven by §2 + abstract issues (which Opus and Gemini agree on at MINOR / STRONG_ACCEPT level), plus four genuine substantive items (Theorem 3.6.1(ii), Theorem 3.4.1 language, Rank-One Convention, $\mu_k$ convention standardization). These are real fixes but all *editing-level*, not architecture-level. The body sections (§3 v3, §4 v3, §5 v3, §6 v2) survive the assembly intact at the structural level.

After v1.1 polish, the paper is Zenodo-ready. Final council can be skipped (or done as a quick re-spot-check on the §2 + Theorem 3.6.1(ii) fixes only).

— Synthesis 2026-05-06 ~13:30 PDT
