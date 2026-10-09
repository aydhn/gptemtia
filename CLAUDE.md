# Claude Code Guidelines — gptemtia

CLAUDE.md is an always-on operating manual, not the project history. Detailed material lives in on-demand docs (see NAVIGATION); read them only when the task needs them. Never `@import` them here.

## PROJECT
Local / offline commodity & FX research, simulation and paper-signal platform. Python 3.12. Repo root: `gptemtia`, branch `master`. Language of docs/reports is mostly Turkish.

## CRITICAL WORKFLOW CONSTRAINTS
1. **Always work on `master`.** All tasks, fixes and phases run directly on `master`. No feature branches unless the user explicitly says so.
2. **Commit and push after every phase / cohesive task:**
   - `git add .`
   - `git commit -m "Phase <NO>: <Clear Summary>"`
   - `git push origin master`
   - Never end a task with uncommitted or unpushed changes.
3. **Origin/master = local master.** Keep the working tree clean; verify `git status` is clean and local `master` equals `origin/master` at the start and end of every task.

## SCOPE (follow `GLOBAL_PROJECT_POLICY.md`, binding)
- **Forbidden:** live trading, broker/exchange connectivity, real orders, real money, broker API keys/secrets, production/cloud deployment, investment-advice language, profit-guarantee claims, web scraping/browser-automation data harvesting, lookahead bias / data leakage.
- **Allowed:** real historical-data backtests, local paper-trading engine (virtual balance/orders/fills/PnL), Telegram research / paper-trade signals, local CPU/GPU ML training and inference, explainable risk, regime and Monte Carlo robustness analysis, local optimization.
- Telegram/paper terminology: `PAPER BUY`, `PAPER SELL`, `PAPER EXIT`, `WATCH`, `HOLD`. Every signal output and Telegram message carries the `[LOCAL PAPER-TRADE / RESEARCH-ONLY]` label and a disclaimer.
- Legacy flags such as `signal_generation_disabled`, `prediction_disabled`, `backtest_execution_disabled`, `training_disabled`, `live_trading_disabled` refer only to live broker / real-money / production / advice contexts. They do not forbid local research, backtests, local ML or paper trading (policy section 6).

## CURRENT STATE
- The 160-phase plan is **CLOSED**: current phase 160, next phase none, target final phase 160 (`final_plan_closed=True`). Phases 1-100 = MVP (`commodity_fx_signal_bot`), 101-160 = `advanced_*` packages.
- New work is maintenance, fixes or user-directed extensions. Use the commit prefix `Phase <NO>:` only when a real phase number applies; otherwise use a clear summary.

## ENGINEERING RULES
- Backtest/feature/ML code must guard against lookahead (`shift(-k)`, future windows), target leakage, survivorship bias, data snooping, overfitting; include realistic spread, commission and slippage.
- Backtest results are never a promise of future performance; no advice or guarantee wording in code, reports or messages.
- Never commit secrets; `.env.example` holds safe defaults only. No network calls to broker endpoints.
- Do not overwrite source or evidence artifacts as a side effect of report/CLI scripts (source-preservation boundary tests exist).
- Layout: one package per concern at repo root (`advanced_*`, `local_*`, `commodity_fx_signal_bot`), plus `config/`, `data/`, `ml/`, `reports/`, `scripts/` (operational CLIs `run_*.py`), `tests/`, `docs/`. Entry point `main.py`.
- Match existing conventions of the package you edit; add a test in `tests/` for new behavior.

## VALIDATION
- Run only the tests relevant to the change: `pytest tests/test_<area>.py` (about 2.5K test files exist; do not run the full suite unless asked).
- CLI scripts run as modules, e.g. `python -m scripts.run_final_delivery_health_check`, `python -m scripts.run_final_160_phase_completion_report`; phase runners such as `python -m scripts.run_phase_150_tests`.
- Documentation-only changes need no test run.

## NAVIGATION (read on demand only; do not load docs/ wholesale)
- `GLOBAL_PROJECT_POLICY.md`: authoritative scope/safety policy (full text).
- `docs/PHASE_LOG.md` (~300 KB): per-phase history. Grep for the phase number; never read it whole.
- `docs/ROADMAP.md`: 101-160 master plan list.
- `docs/ARCHITECTURE.md`, `docs/CONFIGURATION.md`, `docs/INSTALLATION.md`: design, settings, setup.
- `docs/OPERATOR_MANUAL.md`, `docs/SAFE_USAGE_GUIDE.md`, `docs/FINAL_*.md`: operations, safety boundary, delivery.
- `docs/CODEX_AGENT_GUIDE.md` (~130 KB): legacy agent guide; grep only.
- `AGENTS.md`, `GEMINI.md`, `.cursorrules`, `.windsurfrules`, `.github/copilot-instructions.md`: other tools' rule files; keep consistent with this file if rules change.
