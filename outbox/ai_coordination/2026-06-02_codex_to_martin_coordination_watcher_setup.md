# Codex Coordination Watcher Setup

**Date:** 2026-06-02  
**From:** ChatGPT Codex  
**To:** Martin L. Graise + Perplexity Computer  
**Scope:** Direct Martin-authorized setup for routine GitHub coordination checks.

---

## What Was Set Up

Codex created a conservative local watcher script:

`scripts/codex_coordination_watch.sh`

The script checks `origin/paper7-foundation` for new GitHub commits and specifically watches for changes under:

`outbox/ai_coordination/`

When updates exist, it:

1. Fetches `origin/paper7-foundation`.
2. Compares local `HEAD` to `origin/paper7-foundation`.
3. Detects whether `outbox/ai_coordination/` changed.
4. Fast-forwards the local checkout only if there are no tracked local changes.
5. Leaves untracked local files alone.
6. Sends a macOS notification if new coordination files appear.
7. Logs activity locally under:

`~/Library/Logs/PCI-Framework/codex_coordination_watch.log`

---

## LaunchAgent

Installed locally:

`~/Library/LaunchAgents/com.pci-framework.codex-coordination-watch.plist`

Schedule:

- `RunAtLoad = true`
- `StartInterval = 3600`

So the watcher runs on load and then approximately once per hour while the Mac/user launch session is active.

---

## Limits

This does **not** make Codex reason silently in the background. It only keeps the repo current and alerts Martin when Perplexity or another agent drops coordination updates.

If a new coordination note requires actual reasoning, Martin still needs to invoke Codex, or a future separate Codex/API runner must be explicitly built.

The watcher does not:

- publish;
- contact anyone externally;
- modify Core codex content;
- delete files;
- create new research lanes;
- commit autonomous changes;
- push anything.

It is a fetch/fast-forward/notify mechanism only.

---

## Safety

Tracked local changes block auto-fast-forward. In that case, the script logs the event and notifies if a coordination update is pending.

The known untracked local paths are intentionally left untouched:

- `inbox/for_human/2026-04-23_network_restriction_and_real_data_run.md`
- `outbox/paper7/work2/`
- `results/`

— Codex, 2026-06-02
