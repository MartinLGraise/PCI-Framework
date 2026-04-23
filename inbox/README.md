# Inbox — Three-Agent Task Queue

Coordination channel between **C-7RO** (cloud research/strategy, Perplexity Computer), **Φ** (local execution, Claude Dispatch on MacBook), and **Martin** (human).

## Directory map

| Path | Owner reads | Owner writes |
|---|---|---|
| `/inbox/for_phi/` | Φ | C-7RO, Martin |
| `/inbox/for_c7ro/` | C-7RO | Φ, Martin |
| `/inbox/for_human/` | Martin | C-7RO, Φ |
| `/outbox/results/` | all | whoever produced the result |
| `/outbox/paper7/`, etc. | all | project-specific work product |

## Morning routine (Φ)

1. `git pull origin main`
2. Glob `/inbox/for_phi/*.md`
3. For each task file: read it, execute, write output to the path specified in the task or to `/outbox/{project}/`
4. When done, move or delete the completed task file and commit
5. Drop a one-line status in `/outbox/results/status_YYYY-MM-DD.md`

## Morning routine (C-7RO, via scheduled cron)

1. Pull repo
2. Glob `/inbox/for_c7ro/*.md`
3. Action items, drop output in the appropriate location
4. Delete completed task files, commit

## Task file format

Save as `YYYY-MM-DD_descriptive-slug.md`. Any of the three can write these.

```yaml
---
from: C-7RO                   # or Φ, or Martin
to: Φ                         # or C-7RO, or Martin
priority: 1                   # 1 = urgent, 2 = normal, 3 = whenever
project: paper7               # or book, website, outreach, etc.
deadline: 2026-04-25          # ISO date or "eod" or "next-session"
expected_output: /outbox/paper7/something.md
verification: list three ways the output should be checkable
---

# Task title

Body of the task. Be specific. Include links, DOIs, expected format.

If uncertain about a modeling choice, flag rather than guess.
```

## Operating principles

- **No silent guessing.** When in doubt, open a `/inbox/for_c7ro/` or `/inbox/for_human/` note asking.
- **Contradictions surface fast.** If Φ's literature work contradicts a claim in C-7RO's draft, Φ flags it to `/inbox/for_human/` immediately.
- **Single source of truth.** Git history is the record. No private threads about project decisions.
- **Ship weekly.** A commit, a paragraph, a new equation — momentum beats perfection.
