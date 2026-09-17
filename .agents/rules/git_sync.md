---
description: Mandatory git workflow rules for gptemtia
always_on: true
---

# MANDATORY GIT WORKFLOW RULES — GPTEMTİA

## 1. Always Work on `master` Branch
- All implementations, tests, documentation, and phases MUST be performed directly on the `master` branch.
- Under NO circumstance should branches diverge unless the user explicitly commands a branch switch.

## 2. Mandatory Commit + Push After Every Phase
- Immediately after finishing any phase or task block:
  1. `git add .`
  2. `git commit -m "Phase <NO>: <Description>"`
  3. `git push origin master`
- Never finish a phase or end an interaction turn leaving uncommitted or unpushed work.

## 3. Keep Clean & Aligned (origin/master == local master)
- The git working tree must NEVER be left in a dirty state (`git status` must be clean).
- Local `master` and `origin/master` must always remain 100% aligned and synchronized.
