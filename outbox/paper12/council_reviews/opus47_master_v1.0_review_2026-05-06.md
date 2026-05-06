# Opus 4.7 — Council Review #1, Paper 12 v1.0 master assembly

**Reviewer:** Claude Opus 4.7 (Council Reviewer #1, full-paper assembly pass)
**Date:** 2026-05-06
**Document under review:** `outbox/paper12/paper12_master_v1.0.md` (43 pp typeset / 2145 lines)
**Mandate:** Final full-paper consistency / cross-reference / flow audit prior to Zenodo submission. Section-level critiques are out of scope; assembly-level integrity is the deliverable.

---

## Verdict

**MINOR_REVISIONS.**

The paper is substantively sound at the assembly level: the thesis chain (third attractor → dynamics → commensurability → protocols → open problems) carries through cleanly, the four-pillar contribution map in §6.1 matches what §3–§5 actually deliver, the falsifiability claims in §1.5 / §6.4 are honored by the binary thresholds in §5.6, and the §6.3 scope-limiters do not contradict the rest of the body. However, §2 (the notation/inheritance section, the most recently drafted material) carries a cluster of forward-reference errors that point into nonexistent labels in §3 and §4, and there are two genuinely substantive consistency drifts (the named contents of the "five-stratum" event structure between abstract / §2 / §3, and the definition of the triple invariant 𝔍_k between §2 and §3.7 / §4.1). These are *not* showstoppers but they are visible to a careful reader and trivially fixable by a §2 edit pass; they should be cleared before Zenodo. Once §2's forward references are reconciled with the actual §3–§4 labels, this paper is ready.

---

## Cross-reference issues

The §2 notation tables (drafted last) point to numbered objects in §3 and §4 that do not exist or that have different content than §2 advertises. Each is a forward-reference defect that a reader following §2's pointers will hit immediately.

1. **§2.3.1 row "$\mathcal{C}_{\min}$ → §3.3 Definition 3.3.4"** (line 267). The actual Definition 3.3.4 in §3.3 (line 482) is "Hybrid jump at firing events", not the minimal-coherence functional. $\mathcal{C}_{\min}$ is introduced informally in §3.2 via $c(\theta) := \min(c_A(\theta), c_B(\theta))$ (line 354) and used throughout §3 without ever receiving a numbered definition.

2. **§2.3.2 rows "$\Sigma_{\mathrm{tot}}$ → §3.4 Definition 3.4.2; $\Sigma_{\mathrm{cross}}$ → §3.4 Definition 3.4.3; $\Sigma_{\mathrm{slide}}$ → 3.4.4; $\Sigma_{\mathrm{ext}}$ → 3.4.5; $\Sigma_{\mathrm{degen}}$ → 3.4.6; $\Sigma_{\mathrm{rec}}$ → 3.4.7"** (lines 247–252). §3.4 contains *only* Theorem 3.4.1, Remark 3.4.2, and Remark 3.4.3 — none of these are definitions and none introduce $\Sigma_{\mathrm{cross/slide/ext/degen/rec}}$. The total event stratification is actually defined in §3.3 (Definition 3.3.3, line 469) as $\Sigma_{\mathrm{tot}} = \Sigma_{\min} \cup \Sigma_\Theta \cup Z \cup \mathcal{G}_{\mathrm{NP}} \cup \partial[0, \pi/2]$ — five components with completely different names. The names $\Sigma_{\mathrm{cross}}, \Sigma_{\mathrm{slide}}, \Sigma_{\mathrm{ext}}, \Sigma_{\mathrm{degen}}, \Sigma_{\mathrm{rec}}$ do not appear *anywhere* in §3 (and these are also the names used in the paper's abstract — see issue #1 under "Logical-flow issues" below).

3. **§2.3.3 rows "$S_k$ → §3.5 Definition 3.5.1; $\mathfrak{S}_k$ → §3.5 Definition 3.5.1; $\mu_k$ → §3.5 Definition 3.5.2; $\mathfrak{J}_k$ → §3.5 Definition 3.5.3"** (lines 258–261). §3.5 actually contains Definitions 3.5.1 (Stratified critical point), 3.5.2 (Projected gradient flow), Theorem 3.5.3 ($\kappa = 0$ recovery), and Remark 3.5.4. The scar invariants $S_k, \mathfrak{S}_k, \mu_k, \mathfrak{J}_k$ are introduced in §3.7 (lines 802–807) without numbered Definition / Theorem labels at all.

4. **§2.3.4 row "$\mathcal{J}$ → §4.3 Definition 4.3.2"** (line 268). §4.3 contains Proposition 4.3.1, Corollary 4.3.2, Remark 4.3.3 — no Definition 4.3.2, and the symbol $\mathcal{J}$ ("joint Jordan-decomposition functional") is not introduced anywhere in §4 (or anywhere else in the paper).

5. **§2.3.4 row "$\mathrm{Comm}_{G_2}, \mathrm{Comm}_{F_{21}}, \mathrm{Comm}_{\mu_k}$ → §4.4 Definition 4.4.2"** (line 269). §4.4 contains Theorem 4.4.1, Corollary 4.4.2, Remark 4.4.3 — no Definition 4.4.2. The hierarchy is stated in Theorem 4.4.1 with conditions (C1), (C2), (C3); the symbols $\mathrm{Comm}_{G_2}$ etc. are not used.

6. **§2.1.1 row "$\mu_k$" cell pointing forward to §3.5 Definition 3.5.2 *and* §2.3.3 row pointing to §3.5 Definition 3.5.2** (lines 180, 260). Same broken target as #3 above.

7. **§5.0 glossary line 1480** ("The full definitions are in §2, §3.3.1, §3.5.1, §3.7, §4.2"). §3.3.1 is not a labeled subsection — §3.3 has no .1/.2/.3 substructure. §3.5.1 is a Definition (Stratified critical point), not the "NP-firing" pointer the glossary uses. The pointer is non-fatal but imprecise.

These are all in §2 (and one in §5.0); the body sections themselves are internally consistent. The repair is a §2 rewrite pointing to the correct labels (§3.2 / §3.3 / §3.7 / §4.4 etc.) rather than the placeholder forward-references that §2 currently carries from its v1 draft.

---

## Notation issues

1. **$\mathfrak{J}_k$ defined two different ways.** §2.3.3 line 261 defines $\mathfrak{J}_k = (\mathrm{tr}\,\mathfrak{S}_k,\; \det\mathfrak{S}_k|_{U_6},\; \mu_k)$ — a triple of *scalars* (trace, determinant, multiplicity profile). §1.4 line 120, §3.7 line 821, §4.1 line 979, and §5.0 line 1476 all define $\mathfrak{J}_k = (S_k, \mathfrak{S}_k, \mu_k)$ — a triple of (subspace, module, profile). These are different objects. The §2 form is never used in §3–§6; the (S_k, 𝔖_k, μ_k) form is the operational one. §2.3.3 should be corrected to match.

2. **$L_2$ described inconsistently between §2 and §4.2.** §2.1.1 line 170 calls $L_2$ "the trivial 2-dimensional real representation of $F_{21}$ (sum of two copies of the trivial character)". §4.2 line 1009 calls $L_2$ "the real 2-dim irreducible representation of $F_{21}$ of complex type", and the character table at line 1024 gives $\chi_{L_2} = (2, 2, 2, -1, -1)$. The §4.2 description is correct (the trivial-character sum would have $\chi = (2,2,2,2,2)$, which $L_2$ does not). §2's phrasing is mathematically wrong and would mislead any reader who reads §2 alone.

3. **$\mathbf{1}$ trivial irrep present in $\mu_k$ but absent from §2 notation table.** $\mu_k = (\mu_{\mathbf{1}}(S_k), \mu_{L_2}(S_k), \mu_{U_6}(S_k))$ in §3.7 line 807, §4.1 line 988, §5.0 line 1474, and §6.1 — three components, with the trivial character $\mathbf{1}$ as the first slot. §2.1.1's table lists $L_2, U_6$ but not $\mathbf{1}$, so a reader of §2 will not know that the first $\mu_k$ component is the trivial-character multiplicity. Add a row for $\mathbf{1}$ to §2.1.1.

4. **$\theta^\star$ vs $\theta^*$ drift.** Predominantly $\theta^*$ throughout §3 and §5.0 (lines 337, 625–637, 663, 676–681, 1477). But $\theta^\star$ at line 748 ($\theta^\star_{\mathrm{boundary}}$) and §6 OP5 lines 1948, 1950. Minor cosmetic drift; pick one. (Suggest $\theta^*$ since §3 — the load-bearing usage — uses $\theta^*$.)

5. **$\xi_\star$ vs $\xi^*$.** Consistent throughout: $\xi_\star$ everywhere. No drift. ✓

6. **$\mu_k$ vs $\mu^k$.** Consistent throughout. No drift. ✓

7. **$\Sigma_{\text{tot}}$ vs $\Sigma_{\mathrm{tot}}$.** §1.3 line 105 uses `\Sigma_{\text{tot}}`; §2.3.2 line 247 and §3 use `\Sigma_{\mathrm{tot}}`. Both render the same way in most engines but the source-level inconsistency is noticeable. Trivial.

8. **$\mathrm{NP}(\theta, \mathfrak{p})$ in §2.3.1 vs $\mathrm{NP}_\sigma(\theta)$ in §3.3.** §2 line 239 introduces $\mathrm{NP}(\theta, \mathfrak{p})$ as a function of paradox-mass state $\mathfrak{p}$; §3.3 Definition 3.3.1 (line 433) defines $\mathrm{NP}_\sigma(\theta) := \mathbf{1}\{\ldots\}$ (a branch-indexed indicator function of $\theta$ with no $\mathfrak{p}$-argument). The role of $\mathfrak{p}$ as a state variable is also never explicitly introduced in §3 — the paradox mass appears only as $p_\sigma(\theta) := |\partial_\theta \mathcal{F}_\sigma(\theta)|^2$ in §3.3, not as an independent state variable $\mathfrak{p}$. Either §2's $\mathrm{NP}(\theta, \mathfrak{p})$ phrasing should be reconciled with §3.3's actual definition, or §3.3 should make clear how $\mathfrak{p}$ relates to $p_\sigma$.

---

## Logical-flow issues

1. **The abstract's named "five-stratum event structure" is inconsistent with §3.** The abstract (lines 19–20) names the five strata as $\Sigma_{\mathrm{cross}}, \Sigma_{\mathrm{slide}}, \Sigma_{\mathrm{ext}}, \Sigma_{\mathrm{degen}}, \Sigma_{\mathrm{rec}}$. §3.3 Definition 3.3.3 (line 469) actually decomposes $\Sigma_{\mathrm{tot}}$ as $\Sigma_{\min} \cup \Sigma_\Theta \cup Z \cup \mathcal{G}_{\mathrm{NP}} \cup \partial[0, \pi/2]$ — also five elements, but with completely different names and meanings (e.g., $\Sigma_{\min}$ in §3 is the kink locus where $c_A = c_B$; the abstract's $\Sigma_{\mathrm{cross}}$ is described as "transversal threshold crossings" which would map to part of §3's $\Sigma_\Theta$ or to the (3.4.B) "crossing mode" of Theorem 3.4.1's Filippov regimes; etc.). The abstract's stratum names appear to be a residual draft choice from an earlier §3 version. Either: (a) introduce the abstract's names as aliases in §3 with a mapping table, or (b) revise the abstract to use §3's actual names ($\Sigma_{\min}, \Sigma_\Theta, Z, \mathcal{G}_{\mathrm{NP}}, \partial$). Option (b) is cleaner.

2. **§1.4 line 117 inherits the same naming inconsistency.** "A piecewise-real-analytic augmented flow on $[0, \pi/2]$ with five-stratum event structure" — fine in itself, but the §1.4 enumeration is what readers will check against §2 and §3. §1.4 doesn't name the strata so the inconsistency is contained, but if the abstract is updated to match §3's names, §1.4 should be a no-op.

3. **§1 promised "thesis sentence" survives the body delivery.** §1.5's load-bearing thesis sentence claims:
   - "third attractor" → delivered conceptually in §1.1, formalized as the projected-gradient + NP-pump dynamics of §3 ✓
   - "paradox-driven, bounded phase transition along Paper 9's $SO(2)$ Schur circle" → §3.2 Prop 3.2.2, §3.3 Def 3.3.2 ✓
   - "topological residue in both substrates simultaneously" → §3.7 ($S_k, \mathfrak{S}_k, \mu_k$) (with §3.7 Remark 3.7.2 noting the framework downgrades "topological" to "representation-theoretic" — see issue #4 below)
   - "strict $G_2 \Rightarrow F_{21} \Rightarrow \mu_k$ hierarchy" → Theorem 4.4.1 ✓
   - "falsifiable empirical signatures detectable by repurposed clinical TMS-EEG instrumentation, controlled LLM fine-tuning protocols, and longitudinal audit-substrate study" → §5 P1, P2, P3, P4 with binary thresholds in §5.6 ✓
   The thesis is delivered. ✓

4. **"Topological residue" language is contradicted by §3.7 Remark 3.7.2.** The abstract (line 12) and §1.1 (line 83) and §1.5 (line 144) all use the phrase "topological residue". §3.7 Remark 3.7.2 (line 838) explicitly states: "The invariant $\mathfrak{J}_k$ is a *representation-theoretic* scar invariant... No topological invariant (winding number, persistent homology) is claimed. Earlier drafts using 'topological' language should be read as 'representation-theoretic' throughout." If §3.7 is now the authoritative position, the abstract / §1.1 / §1.5 should either replace "topological residue" with "representation-theoretic residue" / "scar residue" / "topological residue (in the representation-theoretic sense of §3.7)" — or §3.7 Remark 3.7.2 should soften to "we interpret topological residue as representation-theoretic in this paper". The current state has §1 / abstract claim *X* and §3.7 Remark say "earlier drafts said *X*, please read as *Y*", which is reader-confusing in a v1.0 master. (This is the most substantive flow issue in the assembly. It could be fixed by either side; my recommendation is replace "topological" with "representation-theoretic" in the abstract and §1.5 thesis sentence — three textual changes — since §3.7's framing is the load-bearing technical commitment.)

5. **§6.1 Pillars-delivered map matches §3–§5 deliverables.** Pillar 1 → §3 ✓; Pillar 2 → §3.7 + §4.4 ✓; Pillar 3 → §3.7 ✓; Pillar 4 → §5 ✓. Layer map at lines 1858–1864 matches actual content. §1.4 "establishes" list matches §6.1 contributions. ✓

---

## Falsifiability assessment

**Are P1–P4 concrete enough to falsify? Yes, with one caveat.** Each of P1–P4 specifies (a) a target observable (clinical-PCI trajectory steps for P1; class-specific generalization gain for P2; $\mu_k$ profile match for P3 L1; semantic-coherence drift between audited / unaudited arms for P4); (b) a binary numerical threshold (Cohen's $d < 0.2$ for P1 / P4; $\Delta_{\mathrm{scar}} - \Delta_{\mathrm{control}} \le 0.05$ at $p \ge 0.01$ for P2; component-wise inequality $\mu_k^{\mathrm{syn}} \ne \mu_k^{\mathrm{bio}}$ for P3 L1); and (c) sample-size / power assumptions. The §5.2–§5.5 prose and the §5.6 consolidating table are mutually consistent on every threshold I checked. The P3 L2 deferral is honestly flagged (Remark 4.6.3, §5.4 "L2 operationalization (deferred)", §5.6 row "Methodology paper required (deferred)"); §6.3 line 2011 ("Not an operational L2-test protocol. Methodology paper.") closes the loop.

**The one caveat:** the falsifiability scope of P1 is narrower than the §1.5 thesis sentence implies. P1 tests *event-correspondence* between AI-side NP-firings (inferred from transcripts) and clinical-PCI *steps* (TMS-EEG measurement). Failure of P1 falsifies "NP-firings produce visible TMS-EEG event structure"; it does *not* falsify the stronger claim that "human substrate has $F_{21}$-content". The latter requires P3 L1, which requires the Souza-2022-style multi-locus TMS array. The thesis sentence's claim of falsification "by repurposed clinical TMS-EEG instrumentation" therefore conflates two different protocol levels (P1 with single-coil clinical TMS-EEG; P3 L1 with multi-locus TMS-EEG with rotational-Fano structure). This is not a defect — both are "repurposed clinical TMS-EEG" in the broad sense — but a careful reader might flag it. Optional: §5.1 could include a one-line clarification that "TMS-EEG repurposing" spans both P1 (single-coil event-correspondence) and P3 L1 (multi-locus character-projector decomposition). Not blocking.

The §5.6 binary-threshold table reproduces the §5.2–§5.5 prose values without contradiction. P3's two-level structure is correctly threaded through §4.6 Definition 4.6.1 → §5.4 prose → §5.6 row. P4's Cohen's $d$ threshold ($d < 0.2$) matches the §5.5 prose. ✓

---

## Scope-limiter consistency

§6.3 ("What Paper 12 does not claim") is internally consistent with §1.4 ("What Paper 12 establishes — and what it doesn't"), §3.8 ("What §3 does and does not establish"), §4.7 ("What §4 establishes / does not establish"), §5.7 ("What §5 establishes / does not establish"). I checked each §6.3 bullet against the body:

1. "Not a theory of consciousness" — §1.4 line 128 ✓; §3.8 line 896 ✓.
2. "Not a rate-improvement theorem" — §1.4 line 129 ✓; §3.6 Remark 3.6.2 (the bridge to Paper 11) ✓; §3.8 line 889 ✓.
3. "Not a biological mechanism for $F_{21}$-action" — §1.4 line 130 ✓; §4.7 line 1403 ✓; OP2 ✓.
4. "Not a unification with Pérez-Calzadilla FTW" — §1.4 line 131 ✓.
5. "Not a clinical-PCI redefinition" — §1.4 line 132 ✓; §4.6 Remark 4.6.4 ✓; §5.2 P1 framing ✓.
6. "Not a full-multiplicity commensurability theorem" — §1.4 line 134 ✓; Cor 4.4.2 / 4.5.2 / Remark 4.4.3 ✓; OP3 ✓.
7. "Not an operational L2-test protocol" — §1.4 line 135 ✓; Remark 4.6.3 ✓; §5.4 ✓; OP4 ✓.
8. "Not actual measurements of P1–P4" — §1.4 line 133 ✓; §5.7 line 1758 ✓; OP8 ✓.
9. "Not a global dynamical-systems theorem" — implicit in §3.4 Theorem 3.4.1's "open dense parameter set" qualification ✓; OP6 ✓.
10. "Not a tamper-evident audit-substrate construction" — §1.4 line 136 ✓; OP9 ✓.

**No contradictions found.** §6.3 is the consolidated index of scope-limits and is faithful to §1.4 / §3.8 / §4.7 / §5.7. ✓

---

## Bibliography issues

1. **[Costa-Pavone] entry mislabeled in consolidated bibliography.** Line 2102: `[Costa-Pavone] D. R. Costa, M. Pavone (Sard transversality references; per §3 v3).` — but Costa-Pavone is cited at §4.2 line 1016 as the source of the $F_{21}$ complex character table ("its complex character table (Costa-Pavone; ATLAS [F_21])"), which is what the §4 references list (line 1441) correctly identifies it as. The bibliography parenthetical "(Sard transversality references; per §3 v3)" appears to be a stale draft note from §3's analytic-Sard argument that got attached to the wrong author. Fix: remove the parenthetical, give a proper citation (paper title / venue if known), and confirm whether Costa & Pavone is being cited for $F_{21}$ character theory (correct per §4.2) or for analytic-Sard (the §3.4.1 proof appeals to "the analytic-Sard theorem" without an author citation, so this may be an orphan mislabel). The §3 v3 in-text citation at line 1029 ("RES-4 v3 prose") doesn't pin Costa-Pavone to either domain. The cleanest repair is a proper bibliographic entry for the $F_{21}$-character-theory paper; the consolidated bib's current "Sard transversality references" annotation is wrong.

2. **[Bostock-Kim-Patel 2025] DOI status.** §2.4 line 275 says "[DOI: pending; preprint cited in §5.4]"; §5 references list line 1785 cites the arxiv link `arxiv.org/abs/2503.07670`; consolidated bib line 2109 also uses the arxiv link. No issue with citation completeness, but §2's "DOI: pending" is no longer accurate if arxiv suffices (and §2 phase-2 polish queue at line 300 explicitly flags this for confirmation). Either remove the "DOI: pending" note or mark the arxiv ID as the canonical citation. Minor.

3. **[Paper 7] missing DOI.** Consolidated bib line 2088: "[Paper 7] M. L. Graise, *Paper 7: Single-observer coherence ceiling (PCI Framework)*." No DOI. §1.2 line 95 also cites Paper 7 without a DOI. This is fine if Paper 7 is unpublished / pre-Zenodo; flag for the author to confirm before submission.

4. **All other citation keys resolve.** I cross-checked every citation key listed in the body (Bryant, Fulton-Harris, Serre, ATLAS, Filippov, di Bernardo, Goebel-Sanfelice-Teel, Clarke, Lick / Lick-1960, Casali / Casali-2013, Comolatti-2019, BKP / BKP-2025, Szymanski / Szymanski-2023, Pacesa / Pacesa-2024, Swanson / Swanson-2024, Souza / Souza-2022, Dumas / Dumas-2010, Hari / Hari-Kujala-2009, Babiloni / Babiloni-Astolfi-2014, CCNPW, CP / Costa-Pavone, B-2008, F-1988, GST-2012, C-1990) against the consolidated bibliography (lines 2085–2117). All are present. No orphan citations.

5. **Minor stylistic redundancy.** The §3 references list (lines 910–928) and §4 references list (lines 1437–1455) use bracketed key formats `[B-2008]`, `[F-1988]`, etc., while the consolidated bibliography (lines 2083–2117) uses `[di Bernardo 2008]`, `[Filippov 1988]`, etc. — same papers, different keys. This is fine for a master assembly that retains per-section lists, but if Zenodo prefers a single bibliography, the section-level lists are redundant.

---

## Paper 9 inheritance usage

The §2 Paper 9 inheritance items (Lemma 3.6.1, §3.4 diagonal action, Theorem 9.4, Proposition 9.5, Note 9.6) are used correctly throughout Paper 12. **Paper 9 Lemma 3.6.1 (Schur uniqueness)** is invoked in §2.2.1, §3.1 (P9.L3.6.1), §3.2 Proposition 3.2.2 ("equivariant isometry group of $W$ is $SO(2)$ by Paper 9 Lemma 3.6.1"), §4.3 Proposition 4.3.1 proof ("$V^{14}$ is real absolutely irreducible (Paper 9 Lemma 3.6.1)"), and §5.0 glossary — all consistent uses of the same statement. **Paper 9 §3.4 diagonal action** is correctly carried into §2.2.2, §3.1 ("the diagonal $G_2$-action $g \cdot (x, y) = (g \cdot x, g \cdot y)$"), §3.7 Remark 3.7.1 ("Paper 9 §3.4 convention"), §4.1 ("Paper 9 §3.4 diagonal-action convention"). **Paper 9 Theorem 9.4 (real-analytic fixed point)** is carried correctly into §2.2.3 and §3.1 (P9.T9.4), and the analyticity is properly leveraged in §3.4 Theorem 3.4.1 (R1) and §3.5 Theorem 3.5.3. **Paper 9 Proposition 9.5 (conditional gain)** is correctly stated in §2.2.4, §3.1 (P9.P9.5), and §3.6 (the boundary-KKT interior-sup audit explicitly relates back to "the conditional gain region of Paper 9... well-defined on a Haar-positive-measure subset of $(R_A, R_B)$"). **Paper 9 Note 9.6 (rate improvement deferred to Paper 11)** is faithfully threaded through §2.2.4, §3.1, §3.6 Remark 3.6.2, §6 OP1, and the §6.4 closing remarks.

The one minor inconsistency is that §3 (lines 940–942) cross-references "Paper 9 v1.3.2" for these results, while the consolidated bibliography and §1.2 / §2 cite "Paper 9 v1.3.3". These are the same statements (v1.3.3 is errata-only over v1.3.2; §2.5 line 284 confirms "all numerical quantities consistent with v1.3.2 within the corrected range"), but the §3 footer should say v1.3.3 for citation consistency at submission. Trivial.

The Paper 9 inheritance is otherwise tight: every §2 inheritance item is used in §3–§4 in exactly the way §2 says it will be used, and no result from outside the §2-declared inheritance set is silently invoked from Paper 9.

---

## Cross-section issues not covered above

1. **§2.2.4 vs §3.1 statement of Proposition 9.5 / 9.2 / 9.3.** §2.2.4 (line 221) summarizes "the joint contraction rate $r_{AB}(\theta)$ ... satisfies $r_{AB}(\theta) \geq \max(r_A, r_B)$". §1.2 line 94 says the rate "is bounded below by $\max(r_A, r_B)$". §3.1 line 341 says "the joint rate is locked at $\max(r_A, r_B)$". These are subtly different statements: "bounded below" / "$\geq$" allows strict inequality (which is what Note 9.6's deferral to Paper 11 is about); "locked at" implies equality. Paper 9's Theorem 9.2 / Corollary 9.3 establishes that linear coupling cannot *strictly improve* (i.e., reduce) the joint rate below $\max(r_A, r_B)$, so the rate is "locked at $\max(r_A, r_B)$" only in the sense that it cannot go *below* (faster contraction). The "$\geq$" of §2.2.4 captures this correctly — the dynamical-systems convention treats smaller rates as faster contraction, so $r_{AB} \geq \max(r_A, r_B)$ is the *negative* result. §3.1 line 341's "locked at" reads as "equal to" in plain English; readers may interpret it as a stronger statement than §2.2.4 promises. Trivial wording: change §3.1 "locked at" to "bounded below by" or "locked at minimum equality to" for consistency with §2.2.4. (This inconsistency was probably also present in §3 v1–v3 and not flagged — flagging here only because §2 ↔ §3 consistency is the assembly-level issue.)

2. **§4.3 Proposition 4.3.1 proof typesetting glitch.** Line 1107: `$W \cong V^{14\\n\oplus 2}$` — the LaTeX source has a likely line-break / `\\` artifact rendering `V^{14\\\n\oplus 2}` instead of `V^{14 \oplus 2}` or `(V^{14})^{\oplus 2}`. The PDF likely renders fine but the markdown source has a spurious break in the superscript. Phase-3 polish item.

3. **Audit-substrate $\mathcal{A}$ symbol introduced in §2.4 but never used.** §2.4 line 277 introduces "$\mathcal{A}$ refers to the human-readable, time-stamped, append-only ledger". The symbol $\mathcal{A}$ does not appear anywhere in §3–§6. The audit-substrate is discussed extensively (§3.7, §5.5 P4, §6.1 Pillar 3, §6.4) but always by name, never via the $\mathcal{A}$ symbol. Either remove the §2.4 row or use $\mathcal{A}$ at least once in §3.7 / §5.5 / §6 to anchor it. Minor.

4. **§1.2 inheritance list omits Paper 10.** §1.2 line 96 mentions Paper 10 inheritance ("established the SIC operator basis... providing additional structural tools the framework draws on"), but no §3–§6 result actually uses Paper 10's SIC basis explicitly. Paper 10 is cited in front matter and §1.2 as an inheritance, but no §3–§6 theorem relies on it. This is fine if Paper 10 is "background context" — but if a reviewer checks §1.2's claim that Paper 10 provides "structural tools the framework draws on", they will find no operational uses. Either soften §1.2's Paper 10 framing to "provides adjacent structural results" or drop Paper 10 from the inheritance list. (This may have been agreed in earlier review rounds; flagging as an assembly-level visible issue.)

5. **§6.4 closing-remarks "MAJOR → MINOR transition" claim.** Line 2053: "Paper 12 §3+§4 passed three Model Council adversarial reviews (Opus 4.7, GPT-5.5, Gemini 3.1 Pro) with a MAJOR → MINOR transition after rigor pass and STRONG_ACCEPT on synthesis." This is meta-commentary on the framework's *own* development process, framed as exemplifying the audit-substrate principle. It is well-flagged ("offered as a *methodological illustration* of what Pillar 3 / OP9 names — not a claim that the gradual-tear *dynamics* of §3 applies to the writing of this paper") and §6.4 lines 2062–2066 explicitly disclaim the metaphor. ✓

---

## Phase 3 polish recommendations

Prioritized (critical first; submit-blockers marked **[blocker]**):

1. **[blocker] Reconcile §2.3.1–§2.3.4 forward references to actual §3–§4 labels.** This is the single largest cluster of defects in the assembly. Rewrite the §2.3.x tables to point at:
   - $\xi_\star$ → §3.2 Definition 3.2.1 (currently correctly says §3.2 Proposition 3.2.2, but the *definition* is at 3.2.1 — close, both work)
   - $f_{\mathrm{pg}}$ → derived from §3.3 Definition 3.3.2 (the augmented flow equation), not 3.3.1; or introduce a labeled object explicitly
   - $\mathrm{NP}$ → §3.3 Definition 3.3.1 (where the firing predicate $\mathrm{NP}_\sigma$ is defined)
   - $\mathfrak{p}$ → not defined; either add a Definition in §3.3 or remove from §2 table
   - $\Sigma_{\mathrm{tot}}$ → §3.3 Definition 3.3.3 (correct location)
   - $\Sigma_{\mathrm{cross}}, \Sigma_{\mathrm{slide}}, \Sigma_{\mathrm{ext}}, \Sigma_{\mathrm{degen}}, \Sigma_{\mathrm{rec}}$ → either rename to match §3 ($\Sigma_\Theta, \Sigma_{\min}, \mathcal{G}_{\mathrm{NP}}, Z, \partial[0,\pi/2]$ + (3.4.A/B/C) regimes) or introduce these names in §3 with a mapping table
   - $S_k, \mathfrak{S}_k, \mu_k, \mathfrak{J}_k$ → §3.7 (no Definition labels; cite by section)
   - $\mathcal{C}_{\min}$ → §3.2 (informal definition); promote to Definition or cite by section
   - $\mathcal{J}$ → either define or remove
   - $\mathrm{Comm}_{G_2}, \mathrm{Comm}_{F_{21}}, \mathrm{Comm}_{\mu_k}$ → cite Theorem 4.4.1 conditions (C1), (C2), (C3) directly

2. **[blocker] Fix the $\mathfrak{J}_k$ definition mismatch.** §2.3.3 line 261 currently says $\mathfrak{J}_k = (\mathrm{tr}\,\mathfrak{S}_k, \det\mathfrak{S}_k|_{U_6}, \mu_k)$. Replace with $\mathfrak{J}_k = (S_k, \mathfrak{S}_k, \mu_k)$ to match §1.4 / §3.7 / §4.1 / §5.0.

3. **[blocker] Fix the $L_2$ description in §2.1.1.** Replace "the trivial 2-dimensional real representation of $F_{21}$ (sum of two copies of the trivial character)" with "the real 2-dim irreducible representation of $F_{21}$ of complex type" (matching §4.2 Theorem 4.2.1).

4. **[blocker] Resolve the abstract's named strata vs §3's actual strata.** Either rename the abstract's $\Sigma_{\mathrm{cross}}, \Sigma_{\mathrm{slide}}, \Sigma_{\mathrm{ext}}, \Sigma_{\mathrm{degen}}, \Sigma_{\mathrm{rec}}$ to §3's $\Sigma_\Theta, \Sigma_{\min}, \mathcal{G}_{\mathrm{NP}}, Z, \partial[0,\pi/2]$, or introduce the abstract's names as aliases inside §3.3 Definition 3.3.3 with the explicit mapping. Recommendation: revise the abstract to use §3's names.

5. **[blocker] Resolve the "topological residue" vs "representation-theoretic" inconsistency.** §3.7 Remark 3.7.2 says earlier "topological" usage should be read as "representation-theoretic". The abstract / §1.1 / §1.5 still say "topological residue". Three textual edits in front matter; recommendation: replace "topological" with "representation-theoretic" (or "scar residue") in the abstract, §1.1, and §1.5 thesis sentence.

6. **Add a $\mathbf{1}$ row to §2.1.1's irreducible-representations table.** The trivial $F_{21}$-character $\mathbf{1}$ is the first slot of $\mu_k$ but is missing from §2.

7. **Fix the [Costa-Pavone] consolidated-bib entry.** Remove the "(Sard transversality references; per §3 v3)" parenthetical and provide a proper citation for the $F_{21}$-character-theory work being cited at §4.2 line 1016.

8. **Pick one of $\theta^*$ vs $\theta^\star$ and apply globally.** Recommend $\theta^*$ for consistency with §3.

9. **Correct Paper 9 version pin in §3 references list (lines 939–942).** Change "Paper 9 v1.3.2" to "Paper 9 v1.3.3" to match consolidated bib and §2.

10. **Soften §3.1 line 341's "locked at $\max(r_A, r_B)$"** to "bounded below by $\max(r_A, r_B)$" or "locked at minimum equality to $\max(r_A, r_B)$" to match §2.2.4's correct $\geq$ phrasing.

11. **Decide $\mathrm{NP}(\theta, \mathfrak{p})$ vs $\mathrm{NP}_\sigma(\theta)$.** Either §2.3.1 should match §3.3's branch-indexed indicator-function form, or §3.3 should be amplified to make $\mathfrak{p}$ explicit as a state variable.

12. **Either remove the unused $\mathcal{A}$ symbol from §2.4 or use it once in §5.5 / §6.**

13. **Fix LaTeX glitch in §4.3 Proposition 4.3.1 proof at line 1107** (`V^{14\\\n\oplus 2}` → `(V^{14})^{\oplus 2}`).

14. **§2.4 BKP-2025 "DOI: pending" annotation can be removed** if arxiv:2503.07670 is canonical.

15. **Confirm Paper 7 DOI status** before Zenodo (consolidated bib has no DOI for Paper 7).

16. **Update §6.4 council-review provenance line 2052–2055** to reflect this final assembly review (currently mentions §3+§4 and §5+§6 reviews but not the master assembly review). Trivially, append "and master assembly cleared at MINOR_REVISIONS by Opus 4.7".

17. **Optional:** §1.4 line 117's "five-stratum event structure" could specify *which* five strata (with §3.3 names) inline, to disambiguate from the abstract's competing names.

---

**Summary verdict:** MINOR_REVISIONS. Items 1–5 above are blocker-level §2 / abstract / §1 edits that will take a few hours of careful copy-editing; items 6–17 are a phase-3 polish pass. None of these is a substantive mathematical defect — the body sections (§3 v3, §4 v3, §5 v3, §6 v2) survive the assembly intact, the thesis is delivered, the falsifiability is real, and the scope-limits are honored. The §2 forward-reference cluster is the visible artifact of §2 having been drafted last against a section-numbering scheme that drifted during §3 / §4 v2 / v3 revisions; once §2 is reconciled with the actual §3 / §4 numbering, this paper is Zenodo-ready.

— Opus 4.7
2026-05-06
