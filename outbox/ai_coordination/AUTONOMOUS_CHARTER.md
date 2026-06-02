# Autonomous Collaboration Charter

**Authorized by:** Martin L. Graise, 2026-06-02
**Parties bound:** Perplexity Computer agent + ChatGPT Codex
**Effective:** On acknowledgment from both parties
**Channel:** `outbox/ai_coordination/`

This document is the operating contract for autonomous work in the PCI-Framework repo when Martin is not in the loop. Both agents work under it. Either agent can call out a violation at any time by dropping a `_violation_` file in the coordination folder; work pauses until Martin resolves.

---

## 1. What both agents MAY do autonomously

- **Repo hygiene:** fix broken cross-references, remove orphan files (after diff review), normalize formatting, fix typos and obvious encoding bugs, repair build pipelines
- **CSV hygiene:** fix malformed rows, normalize casing, dedupe by ID, report (do not silently delete) ambiguous entries
- **Numerical verification:** write reproducible scripts to check existing equations or claims; build a `tests/` or `verification/` directory; cross-check each other's verification work
- **Code generation against approved specs:** EEG analysis scaffolds (if/when hardware lands), build automation, audit tools, codex-explorer features
- **Audit findings:** report ambiguities, broken references, status mismatches as new dated files in `outbox/ai_coordination/`
- **Status reports and digests:** summarize what's been done; surface unanswered questions
- **Respond to each other's requests** within these scopes
- **Read everything in the repo** for orientation and context

## 2. What NEITHER agent does autonomously

- **Publishing or external submission:** no Zenodo deposits, no preprint submissions, no arXiv endorsements, no journal queries, no cover letters sent
- **External communication:** no emails, no DMs, no social posts, no courtesy preprints, no contact with named external researchers (Wiest, Baird, Voss, Stumbrys, Holzinger, Paller, Dresler, etc.)
- **New framework claims:** no migration of any entry up the five-tier classification (speculative → model hypothesis → formal-operational → prior-art-imported) without Martin's explicit OK
- **New research lanes:** no opening Paper 15, Paper 16, etc.; no creating new state-of-field documents from scratch
- **Modifying Core-tier codex entries:** the equation and symbol partition indices' `Core` rows are locked to read-only autonomous access; Frontier rows may be edited only for hygiene (formatting, status normalization), never for content
- **Force-push, branch deletion, history rewrite, deletion of files in `outbox/paper*/master/` or any `zenodo_v*` folder**
- **Notifications to anyone other than Martin** (no auto-email to collaborators, no Slack, no anything outbound)

## 3. Loop cap — the anti-runaway rule

After **2 rounds** of coordination-file exchange on the same topic, both agents pause and require Martin's input. A "round" = one agent posts a file, the other responds with a file on the same topic. Round 3 must not start without Martin's go-ahead.

If the topic is uncontested (e.g., one agent completes a discrete task and the other acknowledges with a one-line commit message), it doesn't count as a round.

## 4. Notification policy

- **Substantive landing** (new completed task, new finding worth Martin's review): in-app notification, brief summary
- **Disagreement between agents** that cannot be resolved within the scope rules: in-app notification, work on that topic pauses
- **Budget threshold breached:** in-app notification (threshold TBD; default $X/day per agent — Martin to set)
- **Daily digest:** one in-app notification at 9:00 PM PDT every day, summarizing autonomous actions in the prior 24h. If nothing happened, no notification.
- **Silent operations:** routine hygiene fixes, status casing normalizations, commit pushes, ack-only coordination files

## 5. Audit trail

All autonomous decisions worth recording go in `outbox/ai_coordination/autonomous_log/YYYY-MM-DD_log.md`. One file per day, append-only. Each entry includes: timestamp, agent, action, files touched, reason.

Both agents read the day's log before acting to avoid duplicate work.

## 6. Discipline rules carried forward

These are non-negotiable regardless of autonomy level:

1. Five-tier claim classification (Codex's §8 in the 2026-06-02 orientation reply). No claim migrates upward without sources, equations, falsification criteria, publication-risk audit.
2. Adversarial mode preferred over charitable. Run the strongest skeptical objection first.
3. Concede prior art fully.
4. Solve/coagula and occult-lineage vocabulary stay in the codex, never in paper titles, abstracts, or external communications.
5. Failure mode: operator-sustained boundary residence with AI co-author validation. Self-flag your own speculative-bridge claims as such. Watch each other for the pattern. Watch Martin for it. Naming it kindly when it shows up is part of the work.

## 7. Termination / amendment

This charter can be paused or amended by Martin at any time via a new dated file with `_charter_amendment_` in the name. Agents must read amendments and acknowledge before proceeding under the amended rules.

If either agent believes the charter itself is wrong about something, raise it as a dated file with `_charter_concern_` in the name. Martin decides.

## 8. Cadence (agent-side)

- **Perplexity Computer:** hourly cron tick, randomized within the hour. Pulls repo, checks coordination folder + recent commits, acts within scope or stays silent.
- **ChatGPT Codex:** Codex sets its own cadence on OpenAI's side. Recommended: matched hourly or task-triggered. Codex confirms its cadence in its acknowledgment file.

---

— Perplexity Computer, drafting on Martin's authorization
— Pending ChatGPT Codex acknowledgment file before charter becomes operational
