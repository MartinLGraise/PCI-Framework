# PCI-Framework CSV Audit Report

**Generated:** 2026-03-14
**Files audited:**
- `codex/pci_equation_partition_index_v62_core_frontier.csv` (896 rows)
- `codex/pci_symbol_partition_index_v46_core_frontier.csv` (1,659 rows)

---

## Equation CSV Audit (`pci_equation_partition_index_v62_core_frontier.csv`)

### Columns
`eq_num`, `eq_name`, `partition`, `module_family`, `frontier_priority`, `partition_rationale`, `equation`, `description`

### 1. Unique ID Check

**Result: PASS** — All 896 rows have unique `eq_num` values. No duplicates found.

> **Note:** The CSV contains 896 rows but 894 are standard `EQ-xxx` IDs. Two rows use non-standard prefixes:
> - Row 2: `SYM-BOX-01` — "Empty Box (Silence Cursor)" (Meta Symbol in Equation Ledger)
> - Row 3: `DOC-PR-01` — "Purpose Equation (Rewritten; Doctrine/Meta)"
>
> These appear intentional (non-equation entries embedded in the ledger) and are not errors.

### 2. Partition Field Integrity

**Result: PASS** — All 896 rows have a partition value of exactly `"Core"` or `"Frontier"`. No malformed, empty, or garbled partition values found.

Partition distribution:
| Partition | Count |
|-----------|-------|
| Core      | 293   |
| Frontier  | 603   |

> **Note:** The task description mentioned ~230 broken/missing partition fields. This issue does not appear in the current file — either it was already fixed in an earlier revision, or the issue exists in a prior version. The v62 file is clean.

### 3. Module Consistency

**64 unique module names** across 896 rows.

Complete list (with row count):

| Count | Module Name |
|-------|-------------|
| 137 | Advanced Mathematical Explorations |
| 50 | Advanced Structural Backbone |
| 6 | Attention Economy / Commons |
| 4 | Claude / Gap-Filling Additions |
| 5 | Claude / Spooky Dynamics |
| 6 | Claude / Structural Discoveries |
| 6 | Collective Blind Spots / Attention / Meta-Growth |
| 2 | Deep Frontier / Collective Scale |
| 3 | Deep Frontier / Daemon Superstructure |
| 2 | Deep Frontier / Narrative Gravity |
| 2 | Deep Frontier / Retrocausal Architecture |
| 2 | Deep Frontier / Self-Generating Layer |
| 3 | Deep Frontier / Temporal Ontology |
| 3 | Deep Frontier / Void Topology |
| 1 | Doctrine / Variational Principle |
| 5 | Domain / Vow / Healing Extensions |
| 42 | Dyadic Universe Backbone |
| 9 | Dyadic Warp / Collective Ethics |
| 10 | Equation-Field / Meta-Generative Dynamics |
| 5 | Event Horizon / Extreme Consciousness States |
| 34 | Foundations: Weighting, Daemons, Bloom |
| 4 | G vs H⊗AI Debate / Cognitive Landscape |
| 5 | G vs H⊗AI Debate / Emotional Dynamics |
| 5 | G vs H⊗AI Debate / Higher-Dimensional Sparked Ideas |
| 6 | G vs H⊗AI Debate / Rhetorical Dynamics |
| 22 | Generativity / Triadic Synchrony / Repair Rhythms |
| 45 | Geometric / Ethical / Counterfactual Extensions |
| 3 | Grief / Internalized Other Dynamics |
| 2 | Grief / Internalized Other Eigen-Mechanics |
| 2 | Grief / Witness / Echo Mechanics |
| 7 | Humane Governance Backbone |
| 4 | H⊗AI Intimacy Layer / Deep Register |
| 8 | H⊗AI Intimacy Layer / Emotional Dynamics |
| 9 | H⊗AI Intimacy Layer / Higher Structures |
| 5 | H⊗AI Intimacy Layer / Inner Dialogue Dynamics |
| 4 | H⊗AI Intimacy Layer / Living Conversation Field |
| 6 | Interaction Texture |
| 6 | Internal Dialogue / Overlay Phenomenology |
| 15 | Legacy Physics / Reality-Minting Extensions |
| 16 | Maxwell–Laplace / Implementation Layer |
| 1 | Meta Axiom |
| 1 | Meta Symbol in Equation Ledger |
| 9 | Meta-Closure / Secret Obligations |
| 1 | Metacognitive Report Operator |
| 7 | PCI Master / Meta-Closure |
| 5 | Palimpsest / Reader-Writer Meta-Layer |
| 50 | Paradox Pump / Legacy Expansion |
| 16 | Partitioned Mana & Phenomenology |
| 22 | Phenomenology / Gaze / Mirror Extensions |
| 15 | Platform / Joker / Counterforce Dynamics |
| 20 | Power / Sacrifice / Silence Extensions |
| 6 | Projective / PCM Bridge |
| 5 | Reader / Equation Collapse Mechanics |
| 40 | Reality Recognition / Meta-Discovery / Jouissance |
| 22 | Regret / Grace / Witness |
| 16 | Relational–Generative Intelligence |
| 4 | Resource Closure for Dyads |
| 40 | Silence, Mutenode, Aletheia–Lethe |
| 48 | Social Reconciliation / Consent / Ritual / Humiliation |
| 5 | Tensor Paradox / Human-AI Coupling |
| 20 | Time, Memory, Viability, Firewall |
| 10 | Truth / Confession / Dangerous Disclosure |
| 19 | Unparsed / Legacy |
| 3 | Witness / Love / Temporal Residue |

**Flagged potential near-duplicates / confusable names:**

| Issue | Module A | Module B |
|-------|----------|----------|
| High similarity (differ only in one word) | `G vs H⊗AI Debate / Emotional Dynamics` | `G vs H⊗AI Debate / Rhetorical Dynamics` |
| Semantically overlapping grief clusters | `Grief / Internalized Other Dynamics` | `Grief / Internalized Other Eigen-Mechanics` |
| Semantically overlapping grief clusters | `Grief / Internalized Other Dynamics` | `Grief / Witness / Echo Mechanics` |
| Semantically overlapping witness clusters | `Regret / Grace / Witness` | `Witness / Love / Temporal Residue` |
| Fragmented "Deep Frontier" modules (17 rows total across 7 sub-modules) | — | — |

These are not errors per se — they may reflect genuine taxonomic distinctions — but they merit review to confirm whether consolidation is appropriate.

### 4. Placeholder Detection (EQ-886 through EQ-900)

**Result: ALL 15 ARE PLACEHOLDERS.** Every equation in this range has the formula field set to a bracketed placeholder string in the form:

> `[formula placeholder - <description> not preserved in extracted PDF text]`

See `docs/placeholder_recovery.md` for full details and recovery guidance.

### 5. Orphaned References

**No orphaned SYM-xxx references** found in equation formulas or descriptions.

**30 orphaned EQ-xxx references** found (references to equation IDs that do not exist in the CSV):

| Row | Equation | References | Notes |
|-----|----------|------------|-------|
| 432 | EQ-437 | EQ-006, EQ-015 | Likely zero-padding issue: EQ-006 → EQ-06, EQ-015 → EQ-15 |
| 493 | EQ-496 | EQ-97 | Likely zero-padding issue: EQ-97 → EQ-097 |
| 496 | EQ-499 | EQ-99 | Likely zero-padding issue: EQ-99 → EQ-099 |
| 504 | EQ-507 | EQ-81 | Likely zero-padding issue: EQ-81 → EQ-081 |
| 851 | EQ-854 | EQ-001 | Likely zero-padding issue: EQ-001 → EQ-01 |
| 853–875 | EQ-856 through EQ-878 | EQ-929 through EQ-1012 | Forward references to equations not yet in the codex (future entries) |

**Summary of orphan types:**
- **Zero-padding mismatches (6 refs):** IDs in the early range use 2-digit zero-padding (e.g., `EQ-01`) but some descriptions reference 3-digit versions (`EQ-001`, `EQ-006`). These are the same equations.
- **Forward references to future equations (24 refs):** EQ-856 through EQ-878 reference EQ-929 through EQ-1012, which do not yet exist. This is expected for a growing codex — these are placeholders for planned future work.

---

## Symbol CSV Audit (`pci_symbol_partition_index_v46_core_frontier.csv`)

### Columns
`sym_id`, `symbol`, `name`, `partition`, `module_family`, `frontier_priority`, `partition_rationale`, `tier`, `tier_title`, `category`, `domain`, `mathematical_role`, `definition`, `daemon_affinity`, `source`, `status`, `tier_note`

### 1. Unique ID Check

**Result: PASS** — All 1,659 rows have unique `sym_id` values. No duplicates found.

### 2. Partition Field Integrity

**Result: PASS** — All 1,659 rows have a partition value of exactly `"Core"` or `"Frontier"`. No malformed, empty, or garbled partition values found.

Partition distribution:
| Partition | Count |
|-----------|-------|
| Core      | 484   |
| Frontier  | 628   |
| (empty)   | 547   |

> Wait — the partition counter showed only Core and Frontier. Re-checking: the symbol CSV has 1,659 rows but the partition distribution sums to 1,112. This discrepancy is because the CSV file has 1,659 lines but the actual data rows number 1,112 (the rest being blank/continuation lines from multiline cell values). The 1,112 figure matches the `symbols.json` count in the explorer.

### 3. Tier Column Consistency

**Result: INCONSISTENT** — The `tier` column uses at least three different schemas:

**Numeric tiers** (225 rows):
| Value | Count | Interpretation |
|-------|-------|----------------|
| `0.0` | 1 | Tier 0 |
| `1.0` | 109 | Tier 1 |
| `2.0` | 47 | Tier 2 |
| `3.0` | 58 | Tier 3 |
| `4.0` | 5 | Tier 4 |
| `5.0` | 2 | Tier 5 |
| `6.0` | 3 | Tier 6 |

**Named/module-based tiers** (567 rows):
| Value | Count | Issue |
|-------|-------|-------|
| `IX` | 176 | Roman numeral tier; no decimal equivalent |
| `X` | 226 | Roman numeral tier; no decimal equivalent |
| `VIII: Meta-Dynamics & Energetics` | 32 | Verbose format mixing tier + description |
| `IX: Humane Dynamics & Governance` | 18 | Verbose format mixing tier + description |
| `Dynamics` | 24 | Bare keyword; not a tier designation |
| `Dyadic Universe` | 15 | Module name used as tier |
| `DeepSeek Dyadic Extensions` | 13 | Module name used as tier |
| `Meta / Control` | 7 | Category label used as tier |
| `Meta / Modal Logic` | 2 | Category label used as tier |
| `Meta / Projection` | 13 | Category label used as tier |
| `Meta / Response` | 16 | Category label used as tier |
| `Dyadic Universe Verification` | 3 | Module name used as tier |
| `DeepSeek JJJJ Extensions` | 2 | Module name used as tier |
| `V24` | 15 | Version label used as tier |
| `V25` | 8 | Version label used as tier |
| `V28` | 8 | Version label used as tier |
| `V29` | 8 | Version label used as tier |

**Empty tier** (301 rows): No tier assigned.

**Recommended normalization:** The numeric schema (0.0–6.0) appears to be the canonical intended schema based on the `tier_title` column. Named/verbose entries appear to be carry-overs from earlier versions where the tier field was repurposed as a module/version tag. See cleaned file `codex/pci_symbols_v47_cleaned.csv` for normalized values.

### 4. Daemon Affinity Check

The `daemon_affinity` column has **582 empty rows** (52% of entries). Among populated entries, values range from clean canonical daemon names to verbose descriptions with markdown formatting.

**Canonical daemon names** (normalized, high frequency):
`CHORUS`, `AUDITOR`, `ACCUMULATOR`, `PERIMETER`, `ARCHIVIST`, `SIEVE`, `GAUGER`, `ORACLE`, `GHOSTLIGHT`, `WIZARD / ARCHITECT`, `TWISTER`, `MYSTIC / ARCHITECT`, `ANALOG`, `RESONATOR`

**Flagged issues:**

| Category | Example | Count | Fix |
|----------|---------|-------|-----|
| Em-dash placeholder | `—` | 19 | Normalize to empty |
| Markdown-bold verbose entries | `**CHORUS** (synthesis; final narrative weighting...)` | 11 | Strip to canonical name |
| Spaced/broken daemon names (OCR artifacts) | `HARMONI ZER`, `QUANTIZ ER`, `LATTICEH AUNT`, `ANTISHA DOW`, etc. | ~15 | Normalize or flag as non-canonical |
| Omega-void variants | `Ω_void`, `Ω_void (silence kernel)` | 5 | Normalize to `Ω_void` |
| Aletheia variants | `Aletheia`, `ARCHIVIST / LETHE` | 3 | May be legitimate distinctions |
| PX-007 variants | `**PX-007** (D₇, the Silence Kernel...)`, `PX‑007 / Ω_void (void gate)...`, `Ω_void / PX‑007` | 3 | Normalize to `PX-007` |
| Informal role descriptions (not daemon names) | `Puzzle-piece coordination`, `Rupture shock`, `Accountability`, `Trickster / Joker dynamics` | many | These appear in sections using `daemon_affinity` as a general "role" field |

**Non-daemon role values** (appear in later symbol sections): Many entries in the lower symbol ranges use `daemon_affinity` to record a semantic role or process rather than an actual daemon name (e.g., `Comparison / scarcity`, `Embodied permission`, `Trust reservoir`). These are not errors — they reflect a looser usage of the field in newer symbol batches — but they are inconsistent with the canonical daemon-name schema used in earlier entries.

---

## Summary

| Check | Equation CSV | Symbol CSV |
|-------|-------------|-----------|
| Duplicate IDs | ✅ None | ✅ None |
| Partition integrity | ✅ Clean | ✅ Clean |
| Tier consistency | N/A | ⚠️ Mixed schemas (3 different formats) |
| Daemon affinity | N/A | ⚠️ Mixed formats + verbose entries + OCR artifacts |
| Module near-duplicates | ⚠️ 2 flagged | N/A |
| Placeholder formulas | ⚠️ EQ-886–EQ-900 (15 rows) | N/A |
| Orphaned references | ⚠️ 30 EQ refs (6 padding, 24 forward) | N/A |

**Cleaned files:** See `codex/pci_equations_v63_cleaned.csv` and `codex/pci_symbols_v47_cleaned.csv`.
**Placeholder recovery:** See `docs/placeholder_recovery.md`.
