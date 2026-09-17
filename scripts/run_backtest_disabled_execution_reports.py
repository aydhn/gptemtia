# -*- coding: utf-8 -*-
"""Phase 146: Run Backtest Disabled Execution Reports Script.

Builds and records formal disabling reports for:
backtest execution, optimizer execution, walk-forward execution, benchmark execution,
live trading, broker execution, model training, model prediction, and performance claims.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_execution_disabled import (
    build_backtest_execution_disabled_report,
)
from advanced_realistic_backtest.backtest_optimizer_disabled import (
    build_backtest_optimizer_disabled_report,
)
from advanced_realistic_backtest.backtest_walk_forward_disabled import (
    build_backtest_walk_forward_disabled_report,
)
from advanced_realistic_backtest.backtest_benchmark_disabled import (
    build_backtest_benchmark_disabled_report,
)
from advanced_realistic_backtest.backtest_live_trading_disabled import (
    build_backtest_live_trading_disabled_report,
)
from advanced_realistic_backtest.backtest_broker_execution_disabled import (
    build_backtest_broker_execution_disabled_report,
)
from advanced_realistic_backtest.backtest_model_training_disabled import (
    build_backtest_model_training_disabled_report,
)
from advanced_realistic_backtest.backtest_prediction_disabled import (
    build_backtest_prediction_disabled_report,
)
from advanced_realistic_backtest.backtest_performance_claim_disabled import (
    build_backtest_performance_claim_disabled_report,
)
from advanced_realistic_backtest.realistic_backtest_report_builder import (
    build_backtest_disabled_execution_markdown_report,
)
from reports.report_builder import build_backtest_disabled_execution_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_realistic_backtest_profile()

    df_bex, s_bex = build_backtest_execution_disabled_report(profile)
    df_opt, s_opt = build_backtest_optimizer_disabled_report(profile)
    df_wf, s_wf = build_backtest_walk_forward_disabled_report(profile)
    df_bm, s_bm = build_backtest_benchmark_disabled_report(profile)
    df_live, s_live = build_backtest_live_trading_disabled_report(profile)
    df_brk, s_brk = build_backtest_broker_execution_disabled_report(profile)
    df_train, s_train = build_backtest_model_training_disabled_report(profile)
    df_pred, s_pred = build_backtest_prediction_disabled_report(profile)
    df_claim, s_claim = build_backtest_performance_claim_disabled_report(profile)

    data_lake.save_backtest_execution_disabled_report(df_bex, s_bex)
    data_lake.save_backtest_optimizer_disabled_report(df_opt, s_opt)
    data_lake.save_backtest_walk_forward_disabled_report(df_wf, s_wf)
    data_lake.save_backtest_benchmark_disabled_report(df_bm, s_bm)
    data_lake.save_backtest_live_trading_disabled_report(df_live, s_live)
    data_lake.save_backtest_broker_execution_disabled_report(df_brk, s_brk)
    data_lake.save_backtest_model_training_disabled_report(df_train, s_train)
    data_lake.save_backtest_prediction_disabled_report(df_pred, s_pred)
    data_lake.save_backtest_performance_claim_disabled_report(df_claim, s_claim)

    md_report = build_backtest_disabled_execution_markdown_report(s_bex, df_bex)
    txt_report = build_backtest_disabled_execution_text_report(s_bex, df_bex)

    out_dir = Path("reports/output/advanced_realistic_backtest")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "disabled_execution.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "disabled_execution.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 146: DISABLED EXECUTION & TRADING ENFORCEMENT")
    print("=" * 70)
    print(f"Backtest Execution     : DISABLED")
    print(f"Optimizer Execution    : DISABLED")
    print(f"Walk-Forward Execution : DISABLED (Deferred to Phase 147)")
    print(f"Benchmark Execution    : DISABLED (Deferred to Phase 147)")
    print(f"Live Trading           : DISABLED")
    print(f"Broker Orders          : DISABLED")
    print(f"Model Training         : DISABLED")
    print(f"Predictions            : DISABLED")
    print(f"Performance Claims     : DISABLED")
    print(f"Non-Signal Invariant   : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
