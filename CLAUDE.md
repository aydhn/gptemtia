# Claude Code Guidelines — gptemtia

## CRITICAL WORKFLOW CONSTRAINTS:
1. **Always Work on `master` Branch:**
   - All tasks, fixes, and phases MUST be executed directly on the `master` branch.
   - Do not switch branches or create feature branches without explicit user directive.

2. **Commit and Push After Every Phase / Task:**
   - After completing each phase or cohesive unit of work:
     - `git add .`
     - `git commit -m "Phase <NO>: <Clear Summary>"`
     - `git push origin master`
   - You must never end a task with uncommitted or unpushed changes.

3. **Origin/Master = Local Master:**
   - Keep working directory clean at all times.
   - Ensure local master and origin/master are in 100% sync.

## Project Scope:
- Follow `GLOBAL_PROJECT_POLICY.md`.
- Strictly no live trading, no broker integration, no investment advice.
- Real historical data backtests, local paper trading simulation engine, and Telegram paper trade signals are allowed.
