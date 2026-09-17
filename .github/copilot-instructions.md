# GitHub Copilot Instructions — gptemtia

## Essential Development Guidelines:
1. **Always Work on `master` Branch:**
   - Develop and apply all code and phase changes directly on the `master` branch.
   - Do not switch to or propose other branches.

2. **Commit and Push After Every Phase / Task:**
   - After completing any phase or logical task:
     - Stage changes: `git add .`
     - Commit changes: `git commit -m "Phase <NO>: <Description>"`
     - Push to remote: `git push origin master`
   - Never leave uncommitted changes in the working directory.

3. **Origin/Master = Local Master:**
   - Keep working directory clean (`git status` clean).
   - Ensure local master and origin/master are aligned and synchronized at all times.

## Core Policy:
- Consult `GLOBAL_PROJECT_POLICY.md`.
- No live trading, broker connectivity, or investment advice.
- Real historical data backtests, local paper trading engine, and Telegram paper trade signals are allowed.
