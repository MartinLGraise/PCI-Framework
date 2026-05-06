## Conflation patches verification
1. **§4.7 measurement-vs-instrument drift:** PATCHED. The v2 draft explicitly states " notably the TMS-EEG pipeline used by Massimini and collaborators for the *distinct* clinical-PCI measurement, which we adapt rather than identify." This tightens the distinction nicely.
2. **Paradox-mass → NP-amplitude bridging sentence:** PATCHED. §3.3.1 now includes "We identify $p_\sigma$ with the squared *paradox mass* of the Paper 12 thesis memo: a non-negative, branch-wise real-analytic quantity that accumulates wherever the coherence functional changes rapidly."
3. **"Tear" linguistic ambiguity:** PARTIALLY PATCHED. The connection between discrete jumps and gradual accumulation is addressed structurally through the introduction of the invariant $(S_k, \mathfrak{S}_k, \mu_k)$ in §3.7, which acts as a ledger. However, the narrative explanation explicitly linking the word "gradual" to this continuous ledgering over multiple discrete "tears" is still slightly understated in the prose, though the math now supports it.

## Citation integration check
- **di Bernardo:** ✓ (Cited in References and explicitly attached to Definitions 3.3.3 and 3.3.5)
- **Filippov:** ✓ (Cited in References and explicitly attached to the equivalent-control formula 3.4.A)
- **Goebel-Sanfelice-Teel (GST):** ✓ (Cited in References and explicitly attached to hybrid-jump semantics in Def 3.3.4)
- **Clarke:** ✓ (Cited in References and explicitly attached to generalized-gradient in Def 3.5.2)
- **Costa-Pavone:** ✓ (Cited in References and explicitly attached to the $F_{21}$ character table in Theorem 4.2.1)
- **ATLAS:** ✓ (Cited in References and explicitly attached to the $F_{21}$ character table in Theorem 4.2.1)
- **Serre:** ✓ (Cited in References and explicitly attached to Frobenius reciprocity in Proposition 4.5.1)

All seven references are integrated correctly and at the appropriate load-bearing theoretical joints.

## Audit-flags compliance
- **Theorem 9.1 vs 9.2 conflation:** COMPLIANT. The text correctly refers to Paper 9 Note 9.6 and Theorem 9.2 regarding the linear joint rate lock. It avoids confusing this with Theorem 9.1.
- **PCI/PCI homonym:** COMPLIANT. Remark 4.6.4 and the revised §4.7 bridge rigorously disambiguate the theoretical framework from the clinical measurement instrument.
- **13% numerology:** COMPLIANT. No mention of the 13% numerology or FCC packing fractions is present in these sections.
- **FTW attribution:** COMPLIANT. There is zero drift into FTW terminology (no GOLEM, no NK3 rudders).

## v2 claim-scope spot check
- **Boundary-KKT escape:** The revision to Theorem 3.6.1(iii) is excellent and carefully scoped. By stating that the boundary state is *fixed* under the linear $\xi_\star$ and explicitly requiring "supplementary nonlinear mechanisms beyond the Schur-derived $\xi_\star$" for escape, it exactly matches the audit findings (24/28 seeds showing interior-sup < boundary). It does not over-claim gain; in fact, the new audit paragraph explicitly walks back generic gain, framing it instead as a "non-trivial trajectory continuation" whose coherence consequences are seed-dependent. This is highly rigorous.
- **Commensurability:** The downgrade of Corollary 4.5.2 to a *sufficient* condition (removing the "if and only if") and the explicit map-existence reformulation of (C2) in Theorem 4.4.1 prevent over-claiming. The converses are properly shown to fail with explicit witnesses.
- **Audit numbers:** The 24/28 and 4/28 numbers are cited accurately matching the stated findings.

## Hostile-reviewer simulation (synthesis-level)
**The sharpest remaining objection:** "You claim the L1 test (Definition 4.6.1) is a falsifiable screen for your theory. But if the biological substrate's $F_{21}$-content is merely a 'hypothetical microtubule mode collection' (as you mention in your witness for (C2) not implying (C1)), and you admit in §4.7 that the physical mechanism is deferred to 'Paper 13+', then L1 is currently unfalsifiable. You cannot measure a $\mu_k^{\mathrm{bio}}$ profile if you don't even know what physical subsystem is supposedly carrying the $F_{21}$ representation. A test requiring a measurement of an unspecified biological structure isn't a methodology deferral; it's a category error."

*Response to the simulated reviewer:* This objection highlights the heavy lifting deferred to the methodology paper. While the L1 protocol conceptually adapts TMS-EEG, the actual identification of the $F_{21}$ action on the EEG response subspace *must* eventually be grounded in physical biology. The drafts are honest about this deferral, but a hostile reader will exploit the gap between a precise mathematical definition ($\mu_k$) and an unlocated biological referent.

## Overall verdict
STRONG_ACCEPT.

The v2 revisions are highly successful. The Opus rigor fixes have repaired the load-bearing mathematical gaps (especially the critical boundary-KKT sign fix, which was handled elegantly by restricting the linear claim rather than forcing a broken mechanism). The literature integration is exactly as requested, grounding the hybrid dynamics and representation theory. The text is disciplined regarding the known audit flags and gracefully defers appropriate questions to Paper 11 (rates) and methodologies (L2 implementation). The framework is now robust, rigorously scoped, and ready for integration.
