# -*- coding: utf-8 -*-
"""Phase 147: Run Validation Disabled Execution Reports Script.

Builds and records formal disabling reports for:
walk-forward execution, OOS benchmark execution, benchmark metric calculation,
optimizer execution, model training, prediction, live trading, broker execution,
and performance claims.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.walk_forward_execution_disabled import (
    build_walk_forward_execution_disabled_report,
)
from advanced_walk_forward_validation.oos_benchmark_execution_disabled import (
    build_oos_benchmark_execution_disabled_report,
)
from advanced_walk_forward_validation.benchmark_metric_calculation_disabled import (
    build_benchmark_metric_calculation_disabled_report,
)
from advanced_walk_forward_validation.validation_optimizer_disabled import (
    build_validation_optimizer_disabled_report,
)
from advanced_walk_forward_validation.validation_model_training_disabled import (
    build_validation_model_training_disabled_report,
)
from advanced_walk_forward_validation.validation_prediction_disabled import (
    build_validation_prediction_disabled_report,
)
from advanced_walk_forward_validation.validation_live_trading_disabled import (
    build_validation_live_trading_disabled_report,
)
from advanced_walk_forward_validation.validation_broker_execution_disabled import (
    build_validation_broker_execution_disabled_report,
)
from advanced_walk_forward_validation.validation_performance_claim_disabled import (
    build_validation_performance_claim_disabled_report,
)
from advanced_walk_forward_validation.walk_forward_report_builder import (
    build_validation_disabled_execution_markdown_report,
)
from reports.report_builder import build_validation_disabled_execution_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_walk_forward_profile()

    df_wf, s_wf = build_walk_forward_execution_disabled_report(profile)
    df_bm, s_bm = build_oos_benchmark_execution_disabled_report(profile)
    df_mc, s_mc = build_benchmark_metric_calculation_disabled_report(profile)
    df_opt, s_opt = build_validation_optimizer_disabled_report(profile)
    df_train, s_train = build_validation_model_training_disabled_report(profile)
    df_pred, s_pred = build_validation_prediction_disabled_report(profile)
    df_live, s_live = build_validation_live_trading_disabled_report(profile)
    df_brk, s_brk = build_validation_broker_execution_disabled_report(profile)
    df_claim, s_claim = build_validation_performance_claim_disabled_report(profile)

    data_lake.save_walk_forward_execution_disabled_report(df_wf, s_wf)
    data_lake.save_oos_benchmark_execution_disabled_report(df_bm, s_bm)
    data_lake.save_benchmark_metric_calculation_disabled_report(df_mc, s_mc)
    data_lake.save_validation_optimizer_disabled_report(df_opt, s_opt)
    data_lake.save_validation_model_training_disabled_report(df_train, s_train)
    data_lake.save_validation_prediction_disabled_report(df_pred, s_pred)
    data_lake.save_validation_live_trading_disabled_report(df_live, s_live)
    data_lake.save_validation_broker_execution_disabled_report(df_brk, s_brk)
    data_lake.save_validation_performance_claim_disabled_report(df_claim, s_claim)

    md_report = build_validation_disabled_execution_markdown_report(s_wf, df_wf)
    txt_report = build_validation_disabled_execution_text_report(s_wf, df_wf)

    out_dir = Path("reports/output/advanced_walk_forward_validation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "disabled_execution.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "disabled_execution.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 147: DISABLED EXECUTION & TRADING ENFORCEMENT")
    print("=" * 70)
    print(f"Walk-Forward Execution     : DISABLED (Contract Only)")
    print(f"OOS Benchmark Execution    : DISABLED (Contract Only)")
    print(f"Metric Calculation         : DISABLED (Placeholder Only)")
    print(f"Optimizer Execution        : DISABLED")
    print(f"Model Training             : DISABLED")
    print(f"Predictions                : DISABLED")
    print(f"Live Trading               : DISABLED")
    print(f"Broker Orders              : DISABLED")
    print(f"Performance Claims         : DISABLED")
    print(f"Non-Signal Invariant       : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
