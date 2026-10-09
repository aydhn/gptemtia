# commodity_fx_signal_bot (MVP core, phases 1-100)

Scope rules, workflow (`master`, commit+push, clean tree) and policy come from the root `CLAUDE.md` and `GLOBAL_PROJECT_POLICY.md`. This file adds only what applies inside this subtree.

## Layout
- Self-contained project: own `config/` (`settings.py`, `paths.py`, `symbols.py`, `timeframes.py`, `risk_config.py`, ...), `core/` (logger, exceptions, market calendar, scan scheduler), `tests/` (~1.6K files), `scripts/` (~520 CLIs), `Makefile`, `pyproject.toml` (`pytest` testpaths `tests`, `ruff` line length 100, `mypy` non-strict, requires Python >=3.10), `pytest.ini`, `requirements*.txt`.
- Imports are relative to this directory (`from config.paths import ...`, `from core.logger import ...`). Run code and tests with this directory as the working directory. The root-level `config/` is a different package.
- Real logic lives in: `data/` (Yahoo/EVDS/FRED loaders, data lake as Parquet under `data/lake/...`), `indicators/`, `mtf/`, `regimes/`, `strategies/`, `signals/`, `risk/`, `sizing/`, `backtesting/`, `paper_trading/` (order simulator, portfolio, trade journal), `paper/`, `telegram/` and `notifications/`, `ml/`, `optimization/`, `validation/`, `quality_gates/`, `governance/`, `security/`, `secrets_hygiene/`. The many `local_*` directories are governance, closure and documentation layers.
- `main.py` only loads settings, creates directories, rejects `live_trading_enabled` and validates the symbol universe.

## Commands (run from `commodity_fx_signal_bot/`)
- `make test` or `python -m pytest`; prefer a single file, `python -m pytest tests/test_<name>.py`.
- `make lint` (ruff), `make typecheck` (mypy), `make health`, `make security`, `make dx`, `make dry-run-daily`, `make dry-run-full`.
- Scripts: `python -m scripts.run_<name>`; outputs go to `reports/output` and `data/lake`.

## Rules
- Telegram and paper outputs use the paper terminology and the `[LOCAL PAPER-TRADE / RESEARCH-ONLY]` label from the root rules.
- Data fetching uses only free, permitted sources. Never add scraping or broker code. Keep `live_trading_enabled` and every `allow_*broker*` / `allow_live*` setting `False`.
- Respect time-series integrity: no lookahead in indicators, features, labels or backtests.
