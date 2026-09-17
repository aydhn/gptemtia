# -*- coding: utf-8 -*-
"""Phase 149: Run Monte Carlo Disabled Execution Reports Script.

Builds and persists all 10 disabled execution audit reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_monte_carlo_robustness.monte_carlo_config import (
    get_default_monte_carlo_profile,
)
from advanced_monte_carlo_robustness.monte_carlo_execution_disabled import (
    build_monte_carlo_execution_disabled_report,
)
from advanced_monte_carlo_robustness.bootstrap_execution_disabled import (
    build_bootstrap_execution_disabled_report,
)
from advanced_monte_carlo_robustness.parameter_optimization_disabled import (
    build_parameter_optimization_disabled_report,
)
from advanced_monte_carlo_robustness.parameter_sweep_execution_disabled import (
    build_parameter_sweep_execution_disabled_report,
)
from advanced_monte_carlo_robustness.monte_carlo_metric_calculation_disabled import (
    build_monte_carlo_metric_calculation_disabled_report,
)
from advanced_monte_carlo_robustness.monte_carlo_model_training_disabled import (
    build_monte_carlo_model_training_disabled_report,
)
from advanced_monte_carlo_robustness.monte_carlo_prediction_disabled import (
    build_monte_carlo_prediction_disabled_report,
)
from advanced_monte_carlo_robustness.monte_carlo_live_trading_disabled import (
    build_monte_carlo_live_trading_disabled_report,
)
from advanced_monte_carlo_robustness.monte_carlo_broker_execution_disabled import (
    build_monte_carlo_broker_execution_disabled_report,
)
from advanced_monte_carlo_robustness.monte_carlo_performance_claim_disabled import (
    build_monte_carlo_performance_claim_disabled_report,
)
from advanced_monte_carlo_robustness.monte_carlo_report_builder import (
    build_monte_carlo_disabled_execution_markdown_report,
)
from reports.report_builder import build_monte_carlo_disabled_execution_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_monte_carlo_profile()

    df_d1, s_d1 = build_monte_carlo_execution_disabled_report(profile)
    df_d2, s_d2 = build_bootstrap_execution_disabled_report(profile)
    df_d3, s_d3 = build_parameter_optimization_disabled_report(profile)
    df_d4, s_d4 = build_parameter_sweep_execution_disabled_report(profile)
    df_d5, s_d5 = build_monte_carlo_metric_calculation_disabled_report(profile)
    df_d6, s_d6 = build_monte_carlo_model_training_disabled_report(profile)
    df_d7, s_d7 = build_monte_carlo_prediction_disabled_report(profile)
    df_d8, s_d8 = build_monte_carlo_live_trading_disabled_report(profile)
    df_d9, s_d9 = build_monte_carlo_broker_execution_disabled_report(profile)
    df_d10, s_d10 = build_monte_carlo_performance_claim_disabled_report(profile)

    data_lake.save_monte_carlo_execution_disabled_report(df_d1, s_d1)
    data_lake.save_bootstrap_execution_disabled_report(df_d2, s_d2)
    data_lake.save_parameter_optimization_disabled_report(df_d3, s_d3)
    data_lake.save_parameter_sweep_execution_disabled_report(df_d4, s_d4)
    data_lake.save_monte_carlo_metric_calculation_disabled_report(df_d5, s_d5)
    data_lake.save_monte_carlo_model_training_disabled_report(df_d6, s_d6)
    data_lake.save_monte_carlo_prediction_disabled_report(df_d7, s_d7)
    data_lake.save_monte_carlo_live_trading_disabled_report(df_d8, s_d8)
    data_lake.save_monte_carlo_broker_execution_disabled_report(df_d9, s_d9)
    data_lake.save_monte_carlo_performance_claim_disabled_report(df_d10, s_d10)

    out_dir = Path("reports/output/advanced_monte_carlo_robustness")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "disabled_execution.md", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_disabled_execution_markdown_report(s_d1, df_d1))
    with open(out_dir / "disabled_execution.txt", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_disabled_execution_text_report(s_d1, df_d1))

    print("Monte Carlo disabled execution reports successfully built.")


if __name__ == "__main__":
    main()
