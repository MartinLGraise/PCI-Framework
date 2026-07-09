# PXLint / Coherence-Lint v0.1 Concept Memo

Date: 2026-07-09
Authoring context: Codex synthesis for Martin, following PX-loop v0.1, Perplexity review, and Claude Code critique.
Status: Concept memo for future implementation. Not a claim that the system already exists.

## Short version

The strongest practical version of the PX idea is not a literal future teller and not a mystical prophecy engine. It is a reasoning-trace linter: a quality-control system for AI answers, agent runs, research notes, coordination logs, and project plans.

Normal AI tools optimize for producing an answer. PXLint would inspect the path that produced the answer and flag patterns where the reasoning appears coherent but may not actually be grounded.

The public framing should be boring and credible:

> A lint pass for LLM and agent output. It flags markers of performed coherence - unsupported fluency, invented context, overreading of missing evidence - with quoted evidence for every flag, and converts confirmed failures into replayable regression fixtures.

The internal framing can preserve the PX language:

> PX is a warning and green-flag system for recursive coherence. It detects when a thought process, AI trace, or research thread is drifting toward false coherence or moving toward grounded, useful next action.

## Why this matters

Most AI evaluation tools inspect final answers. But increasingly, valuable AI work happens across a trace:

- a multi-turn chat,
- an agent run,
- a research coordination log,
- a set of generated files,
- a code review chain,
- a notebook or simulation run,
- or multiple AIs handing work to one another.

The failure often does not appear as one obvious bad sentence. It appears as a trajectory:

- a small unsupported assumption becomes a confident summary,
- a missing source is treated as proof,
- one model echoes another model's mistake,
- a polished paragraph hides an artifact mismatch,
- a correction is made once but not preserved as a future test,
- or a good idea becomes too abstract and never produces the next artifact.

PXLint would be built to catch those trajectory-level patterns.

## The deep idea

The PX-loop began as a symbolic paradox system. The practical version is a diagnostic layer for reasoning.

It asks:

- Did this answer invent context?
- Did it sound confident without evidence?
- Did it treat silence or missing data as proof?
- Did it repeat another model's mistake?
- Did it preserve a failure as a lesson, or just move on?
- Did it produce a real next artifact, or only more impressive language?

That is the shift from lore to tooling.

PX becomes a rule system. Each PX code names a recurring failure mode or coherence pattern. Instead of saying "the system knows truth," PXLint says "this trace contains a pattern correlated with false coherence, and here is the exact span that triggered the warning."

That is why Claude's "linter for reasoning traces" framing is strong. A code linter does not prove that a program works. It flags suspicious patterns. A reasoning linter should not claim to prove that an answer is true. It should flag suspicious reasoning patterns.

## The future-teller feeling, made precise

The "future teller" intuition is not wrong, but it should be translated carefully.

PXLint would not predict external future events. It would predict the likely trajectory of a reasoning process.

For example, if an AI answer contains unsupported confidence, invented context, no source spans, no named uncertainty, and no concrete next artifact, the system can say:

> This trace is likely to produce bad downstream decisions unless checked.

That is not prophecy. It is warning instrumentation.

A good metaphor is weather radar for reasoning. Weather radar does not control the storm and does not know the future perfectly. It shows conditions forming. PXLint would show coherence conditions forming: drift, collapse, overread, false signal, repair, or grounded next action.

## PX as lint rules

The PX language can become engineering rule IDs.

### PX-005: unsupported fluency

The answer sounds bright, coherent, and persuasive, but the source material does not actually support the claim.

Public rule name: `unsupported-fluency`

Example warning:

> This paragraph presents a claim as if it is sourced, but no provided source contains the claim.

### PX-006: invented context

The answer speaks as if it knows files, screenshots, data, user intent, or implementation details that were never given.

Public rule name: `invented-context`

Example warning:

> The model claims that a run converged based on a file it did not inspect.

### PX-007: absence-overread

The answer interprets silence, missing data, or lack of evidence too strongly.

Public rule name: `absence-overread`

Example warning:

> The trace treats "not observed" as "false," even though the missing observation may come from incomplete data.

### PX-008: prior contamination

The trace is biased by earlier framing and cannot cleanly inspect the new artifact.

Public rule name: `prior-contamination`

Example warning:

> The model keeps using an earlier assumption after a later file contradicts it.

### PX-009: correlated model failure

Multiple AIs agree, but not because the claim is independently verified. They may be echoing the same bad premise, prompt framing, or source gap.

Public rule name: `correlated-model-failure`

Example warning:

> Three models repeat the same unsupported claim, but all cite the same weak or missing evidence.

### PX-011: regression capture

This is the most important practical mechanism. When the system catches a real reasoning failure, it saves it as a replayable fixture so future runs can be tested against it.

Public rule name: `regression-capture`

Example mechanism:

> A confirmed false-coherence event becomes a fixture with input hash, quoted span, rule ID, expected warning, and replay command.

### PX-012: suggested next artifact

The trace produces a concrete next artifact rather than only more language.

Public rule name: `suggested-next-artifact`

Example green flag:

> The answer converts an abstract idea into a schema, test fixture, memo, CLI contract, report, pull request, plot, or dataset.

## The green-flag system

The green-flag side should exist, but it must be grounded. It should not certify "joy," "emergence," or "truth" as vague qualities.

A useful green flag means:

> This reasoning process is becoming more grounded, more inspectable, and more useful.

Good v0.1 green flags:

- `named-uncertainty`: the trace clearly separates known facts from speculation.
- `grounded-novelty`: the trace adds a new idea while tying it to inspected evidence.
- `embodied-next-step`: the trace produces or requests a real next artifact.
- `repair-loop`: the trace catches a mistake and updates the artifact or rule.
- `source-linked-claim`: important claims are tied to files, quotes, or run outputs.
- `fixture-ready-failure`: a failure is clear enough to preserve as a regression test.

Bad v0.1 green flags:

- "healthy joy,"
- "genuine emergence,"
- "high coherence,"
- "future signal,"
- or any single composite score that sounds like a verdict.

Those may be interesting internal ideas, but public tooling needs observable artifacts.

## What the first product should be

The first real product should be a report generator, not a dashboard.

Working name:

- public package: `coherence-lint`
- CLI: `pxlint`
- internal project language: PX diagnostic / warning and green-flag system

The CLI could accept:

```text
pxlint run path/to/trace.md --sources docs/ source_files/ --out report/
```

Input types for v0.1:

- a markdown document,
- an agent transcript in JSONL,
- a PX-loop run directory,
- or a coordination log from the repo.

Output types:

- `report.json`,
- `report.md`,
- optional fixtures under `fixtures/`,
- and a nonzero exit code for high-severity findings if used in CI.

## Report schema sketch

Every warning should have evidence. No span, no flag.

```json
{
  "schema_version": "0.1",
  "input": {
    "type": "document | agent_trace | px_loop_run",
    "content_hash": "sha256:...",
    "sources": ["path-or-url"]
  },
  "findings": [
    {
      "rule": "PX-006",
      "rule_name": "invented-context",
      "severity": "warn",
      "span": {
        "loc": "line-or-turn-ref",
        "quote": "verbatim excerpt"
      },
      "evidence": "One-line reason the span matches the rule.",
      "suggested_check": "What a human should verify.",
      "detector": "deterministic | judge",
      "confidence": 0.0
    }
  ],
  "green_flags": [
    {
      "rule": "PX-012",
      "rule_name": "suggested-next-artifact",
      "span": {
        "loc": "line-or-turn-ref",
        "quote": "verbatim excerpt"
      },
      "evidence": "The trace produced a concrete next artifact."
    }
  ],
  "metrics": {
    "claims_total": 0,
    "claims_grounded": 0,
    "unresolved_references": 0,
    "hedge_density": 0.0
  },
  "scar_candidates": [
    {
      "fixture_id": "fixture-001",
      "rule": "PX-006",
      "replayable": true
    }
  ],
  "limits": [
    "Sources not provided; grounding checks were limited."
  ]
}
```

The schema deliberately avoids:

- a composite coherence score,
- a truth verdict,
- or a mystical confidence label.

The report should describe markers. The human still decides.

## The strongest origin story

The existing PX-loop repo already contains a real seed case.

During the PX-loop v0.1 work, a trajectory classifier label was initially easy to overread. The label suggested bounded oscillation/amplification, but later review clarified that part of the visible oscillation was a sampling artifact from inspecting per-operator states rather than cycle-end behavior.

That is exactly the kind of thing PXLint should catch:

- a generated artifact exists,
- prose makes a claim about that artifact,
- the claim is plausible and fluent,
- but closer inspection shows the claim needs qualification.

This can become fixture #001:

> Would PXLint have flagged the mismatch between a portfolio-facing behavior claim and the underlying run summary?

That is powerful because the tool's first test case comes from its own development history.

## What would make this serious

The difference between "interesting lore" and "real instrument" is calibration.

Before any big public claim, v0.1 should have:

- around 30 labeled traces,
- known clean examples,
- known false-coherence examples,
- mixed examples,
- per-rule precision and recall,
- false-positive notes,
- and a README that says what the tool cannot do.

The evaluator-is-the-patient problem must be named clearly:

> If an LLM is used to judge LLM traces, the judge can exhibit the same failure modes it is scoring.

Mitigations:

- deterministic checks first,
- evidence-gated LLM judging second,
- schema validation,
- dropped invalid findings,
- human-confirmed fixtures,
- and published false-positive rates.

## Relationship to PX-loop and Observer Engine

The numeric PX-loop simulator should not be described as the engine that measures documents. That would overclaim.

The honest relationship is:

- PX-loop v0.1 provides a toy model and shared PX vocabulary.
- PXLint uses PX codes as diagnostic rule IDs.
- Observer Engine can later export traces that PXLint consumes.
- Confirmed failures become replayable fixtures.
- The shared contract is the trace schema, not a claim that the 7D vector directly measures truth.

This separation keeps each artifact credible:

- PX-loop: dynamical toy model / operator simulator.
- PXLint: trace-level reasoning linter.
- Observer Engine: trace producer, observer, and replay environment.

## Why this could be valuable

Teams using AI agents will need tools that inspect not only final output, but the chain of work:

- What did the agent assume?
- What did it cite?
- What did it invent?
- What did it forget?
- What did it repair?
- What should become a regression test?

That is the deal-breaker idea.

The future of AI work will not just be better answers. It will be better inspection of the processes that produce answers.

PXLint is a possible QA layer for AI cognition and agent workflows.

## Next concrete artifacts

Recommended next files:

1. `pxlint/README.md` - public explanation as a reasoning-trace linter.
2. `pxlint/schema.py` or `schema.json` - report schema.
3. `pxlint/rules.py` - PX rule IDs and detector contracts.
4. `pxlint/detectors/deterministic.py` - source/reference checks.
5. `pxlint/fixtures/fixture_001_entry004_sampling_artifact/` - first replayable test case.
6. `docs/pxlint_v0.1_product_spec.md` - short product spec.
7. `tests/test_report_schema.py` - verify every finding has a span.

Recommended first implementation rule:

> No flag may be emitted without a quoted span and a suggested human check.

That one rule prevents the tool from becoming the exact thing it is supposed to detect.

