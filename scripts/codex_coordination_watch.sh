#!/bin/zsh
set -u

REPO="${PCI_REPO:-/Users/martinluthergraise/PCI-Framework}"
REMOTE="${PCI_REMOTE:-origin}"
BRANCH="${PCI_BRANCH:-paper7-foundation}"
LOG_DIR="${HOME}/Library/Logs/PCI-Framework"
STATE_DIR="${HOME}/Library/Application Support/PCI-Framework"
LOG_FILE="${LOG_DIR}/codex_coordination_watch.log"
LOCK_DIR="/tmp/pci-codex-coordination-watch.lock"

mkdir -p "$LOG_DIR" "$STATE_DIR"

log() {
  local stamp
  stamp="$(date '+%Y-%m-%d %H:%M:%S %Z')"
  printf '[%s] %s\n' "$stamp" "$*" >> "$LOG_FILE"
}

notify() {
  local title="$1"
  local body="$2"
  /usr/bin/osascript -e "display notification \"${body//\"/\\\"}\" with title \"${title//\"/\\\"}\"" >/dev/null 2>&1 || true
}

if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  exit 0
fi
trap 'rmdir "$LOCK_DIR" 2>/dev/null || true' EXIT

if [[ ! -d "$REPO/.git" ]]; then
  log "Repo not found at $REPO"
  notify "PCI Codex Watcher" "Repo not found: $REPO"
  exit 1
fi

cd "$REPO" || exit 1

local_head="$(git rev-parse HEAD 2>/dev/null || true)"
if [[ -z "$local_head" ]]; then
  log "Could not resolve local HEAD"
  notify "PCI Codex Watcher" "Could not resolve local HEAD"
  exit 1
fi

fetch_output="$(git fetch "$REMOTE" "$BRANCH" 2>&1)"
fetch_status=$?
if [[ $fetch_status -ne 0 ]]; then
  log "Fetch failed: $fetch_output"
  notify "PCI Codex Watcher" "Git fetch failed; check log."
  exit $fetch_status
fi

remote_head="$(git rev-parse "$REMOTE/$BRANCH" 2>/dev/null || true)"
if [[ -z "$remote_head" ]]; then
  log "Could not resolve $REMOTE/$BRANCH after fetch"
  notify "PCI Codex Watcher" "Could not resolve $REMOTE/$BRANCH"
  exit 1
fi

if [[ "$local_head" == "$remote_head" ]]; then
  exit 0
fi

changed_files="$(git diff --name-only "$local_head..$remote_head" -- outbox/ai_coordination 2>/dev/null || true)"
coordination_changed=0
if [[ -n "$changed_files" ]]; then
  coordination_changed=1
fi

if ! git diff --quiet -- || ! git diff --cached --quiet --; then
  log "Remote advanced to $remote_head, but tracked local changes block auto fast-forward."
  if [[ $coordination_changed -eq 1 ]]; then
    notify "PCI coordination update pending" "New coordination files exist, but tracked local changes block auto-pull."
  fi
  exit 0
fi

merge_output="$(git merge --ff-only "$REMOTE/$BRANCH" 2>&1)"
merge_status=$?
if [[ $merge_status -ne 0 ]]; then
  log "Fast-forward failed from $local_head to $remote_head: $merge_output"
  if [[ $coordination_changed -eq 1 ]]; then
    notify "PCI coordination update pending" "New coordination files exist; fast-forward failed."
  fi
  exit $merge_status
fi

log "Fast-forwarded $BRANCH from $local_head to $remote_head."

if [[ $coordination_changed -eq 1 ]]; then
  summary="$(printf '%s\n' "$changed_files" | sed 's#^outbox/ai_coordination/##' | head -5 | paste -sd ', ' -)"
  if [[ "$(printf '%s\n' "$changed_files" | wc -l | tr -d ' ')" -gt 5 ]]; then
    summary="${summary}, ..."
  fi
  log "Coordination update detected: ${changed_files//$'\n'/; }"
  notify "PCI coordination update" "$summary"
fi
