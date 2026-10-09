# Claude Code Guidelines — gptemtia

CLAUDE.md is an always-on operating manual, not the project history. Read the docs listed under NAVIGATION only when the task needs them. Never `@import` them here.

## PROJECT
Local / offline commodity & FX research, backtest, ML, paper-trading and paper-signal platform. Python 3.12, branch `master`. Docs and reports are mostly Turkish.

Two code bases live in this repo; check which one you are in before editing:
1. **`commodity_fx_signal_bot/`** is the self-contained MVP (phases 1-100). It has its own `config/`, `core/`, `tests/`, `scripts/`, `Makefile`, `pyproject.toml` and `requirements*.txt`. It is run from inside its own directory (see its `CLAUDE.md`).
2. **Root-level `advanced_*` and `local_*` packages** (phases 101-160, plus closure/governance), with the root `config/`, `data/`, `ml/`, `reports/`, `scripts/`, `tests/`. Entry point `main.py` is only a stub that prints "Project run complete."

## CRITICAL WORKFLOW CONSTRAINTS
1. **Always work on `master`.** No feature branches unless the user explicitly says so.
2. **Commit and push after every phase / cohesive task:**
   - `git add .`
   - `git commit -m "Phase <NO>: <Clear Summary>"`
   - `git push origin master`
   - Never end a task with uncommitted or unpushed changes.
3. **Origin/master = local master.** Working tree clean; verify `git status` and sync at the start and end of every task.

## SCOPE (`GLOBAL_PROJECT_POLICY.md` is binding)
- **Forbidden:** live trading, broker/exchange connectivity, real orders, real money, broker API keys/secrets, production/cloud deployment, investment-advice wording, profit-guarantee claims, web scraping / browser-automation harvesting, lookahead bias and data leakage.
- **Allowed:** real historical-data backtests, local paper-trading engine (virtual balance/orders/fills/PnL), Telegram research / paper-trade signals, local CPU/GPU ML training and inference, explainable risk, regime and Monte Carlo robustness analysis, local optimization.
- Paper terminology: `PAPER BUY`, `PAPER SELL`, `PAPER EXIT`, `WATCH`, `HOLD`. Every signal output and Telegram message carries `[LOCAL PAPER-TRADE / RESEARCH-ONLY]` plus a disclaimer.
- Flags such as `signal_generation_disabled`, `prediction_disabled`, `backtest_execution_disabled`, `training_disabled`, `live_trading_disabled` and the `*_disabled.py` modules mean "disabled in the live broker / real-money / production / advice sense". They do not forbid local research, backtests, local ML or paper trading (policy section 6).

## CURRENT STATE
- The 160-phase plan is **CLOSED**: current phase 160, next phase none, `final_plan_closed=True`. Work now is maintenance, fixes or user-directed extensions.
- Use the `Phase <NO>:` commit prefix only when a real phase number applies; otherwise write a clear summary.

## CODE MAP AND CONVENTIONS (root packages)
- Most `advanced_*` / `local_*` packages are contract-first scaffolding: config profiles, `*_labels`, `*_models`, `*_contracts`, `*_placeholders`, `*_guards`, `*_disabled`, `*_health`, `*_validation`, `*_findings`, `*_pipeline`, `*_report_builder`, ending in a `phase_NNN_handoff` or manifest. Follow this pattern and the package's `__init__.py` export list when adding modules.
- Packages with real computation (verify before assuming others have it): `advanced_technical_indicators`, `advanced_feature_engine/basic_feature_computations.py`, `advanced_feature_grid/feature_grid_computations.py`, `advanced_feature_quality_drift/feature_rolling_stability.py`, `advanced_data_quality/*_rules.py`, `advanced_gpu_ml_runtime/cuda_availability.py`, `advanced_macro_event_news_regime/macro_event_news_no_lookahead_guard.py`.
- Provider packages (`advanced_*_providers`, `advanced_data_providers`, `advanced_news_metadata`) are contracts and local/manual/cache stubs. They do no live fetching; keep it that way.
- `config/settings.py` is a pydantic `Settings` with safe defaults (live trading, broker, orders, advice, deployment, scraping, cloud publish are all `False`; dry-run and local-only are `True`). `.env.example` holds per-package toggles (about 4.3K lines, grep it, don't read it). Never loosen these defaults.
- `config/paths.py` holds path constants: reports go under `reports/output/<pkg>/`, data under `data/lake/<pkg>/`.
- `scripts/run_<topic>_<kind>.py` are operational CLIs (about 640), run as `python -m scripts.<name>`. They print results and mostly do not use argparse or `sys.exit`.
- Source-preservation boundary: report/CLI code must not overwrite source or evidence files.
- `__pycache__` is gitignored (3 stale tracked files); do not add more.

## ENGINEERING RULES
- Backtest/feature/ML code must guard against lookahead (`shift(-k)`, future windows), target leakage, survivorship bias, data snooping and overfitting, and must model spread, commission and slippage.
- Backtest results are never a promise of future performance; no advice or guarantee wording in code, reports or messages.
- No secrets in the repo; no calls to broker endpoints.
- New behavior gets a test in the matching `tests/` directory. Tests are named `test_<module>.py` and mirror source modules.

## VALIDATION
- Run only tests relevant to the change, for example `pytest tests/test_<area>.py`. The repo has about 2.5K root test files and 1.6K more inside `commodity_fx_signal_bot/tests`; never run the full suites unless asked.
- Root CLIs: `python -m scripts.run_final_delivery_health_check`, `python -m scripts.run_final_160_phase_completion_report`, phase runners like `python -m scripts.run_phase_150_tests`.
- No root `pytest.ini`, `pyproject.toml` or `conftest.py` exists. Documentation-only changes need no test run.

## NAVIGATION (read on demand; never load docs/ wholesale)
- `GLOBAL_PROJECT_POLICY.md`: full authoritative policy.
- `docs/PHASE_LOG.md` (~300 KB): per-phase history. Grep by phase number; never read it whole.
- `docs/ROADMAP.md`: 101-160 master plan. `docs/ARCHITECTURE.md`, `docs/CONFIGURATION.md`, `docs/INSTALLATION.md`: design, settings, setup.
- `docs/OPERATOR_MANUAL.md`, `docs/SAFE_USAGE_GUIDE.md`, `docs/FINAL_*.md`: operations, safety boundary, delivery.
- `docs/CODEX_AGENT_GUIDE.md` (~130 KB): legacy agent guide; grep only.
- `commodity_fx_signal_bot/README.md`: phase-by-phase MVP usage and commands.
- `AGENTS.md`, `GEMINI.md`, `.cursorrules`, `.windsurfrules`, `.github/copilot-instructions.md`: other tools' copies of the workflow and scope rules; keep them consistent if rules change.
