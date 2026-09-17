# AGENT INSTRUCTIONS & REPOSITORY RULES — GPTEMTİA

## 1. CORE & IMMUTABLE RULE: MASTER BRANCH & COMMIT+PUSH AFTER EVERY PHASE
This rule is the highest priority operational requirement for ALL AI agents, tools, and conversations:

1. **ALWAYS WORK ON `master` BRANCH:**
   - All tasks, phases, bugfixes, refactoring, tests, and documentation MUST be developed directly on the `master` branch.
   - Never create feature branches, test branches, or switch away from `master` unless explicitly instructed by the user.

2. **MANDATORY COMMIT AND PUSH AFTER EVERY SINGLE PHASE:**
   - After completing each phase, sub-phase, feature, or logical chunk of work:
     - Stage all changes: `git add .` (or specific files)
     - Create a meaningful commit: `git commit -m "Phase <NO>: <Short Description>"`
     - Immediately push to remote: `git push origin master`
   - No task or phase is considered complete without a successful commit and push.

3. **ORIGIN/MASTER = LOCAL MASTER (KEEP 100% CLEAN & SYNCHRONIZED):**
   - The working directory must NEVER be left in a dirty state (`git status` must be clean).
   - Local `master` and `origin/master` must always stay aligned and synchronized.
   - At the beginning of any session/task, verify alignment (`git pull origin master` or fetch check).
   - At the end of any session/task, verify `git push origin master` succeeds and `git status` reports working tree clean.

---

## 2. REPOSITORY POLICIES
All agents must strictly comply with `GLOBAL_PROJECT_POLICY.md`:
- **STRICTLY FORBIDDEN:** Live broker/exchange connectivity, live order routing, real-money trading, production deployment, financial/investment advice language, web scraping, lookahead bias / data leakage.
- **ALLOWED & TARGETED:** Real historical market data backtests, local paper trading simulation engine (virtual balances, virtual fills, virtual PnL), Telegram research/paper-trade signals (`PAPER BUY`, `PAPER SELL`, `PAPER EXIT`, `WATCH`, `HOLD`), local ML training/inference (CPU/GPU), explainable risk, regime, and robustness analyses.
