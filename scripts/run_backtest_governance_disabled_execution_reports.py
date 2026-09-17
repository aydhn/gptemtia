# -*- coding: utf-8 -*-
"""Phase 150: Run Backtest Governance Disabled Execution Reports Script.

Builds and persists all disabled execution reports (governance execution, result claim,
metric calculation, optimizer, model training, prediction, live trading, broker execution, deployment).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_governance_execution_disabled import (
    build_backtest_governance_execution_disabled_report,
)
from advanced_backtest_governance.backtest_result_claim_disabled import (
    build_backtest_result_claim_disabled_report,
)
from advanced_backtest_governance.backtest_metric_calculation_disabled import (
    build_backtest_metric_calculation_disabled_report,
)
from advanced_backtest_governance.backtest_optimizer_disabled import (
    build_backtest_optimizer_disabled_report,
)
from advanced_backtest_governance.backtest_model_training_disabled import (
    build_backtest_model_training_disabled_report,
)
from advanced_backtest_governance.backtest_prediction_disabled import (
    build_backtest_prediction_disabled_report,
)
from advanced_backtest_governance.backtest_live_trading_disabled import (
    build_backtest_live_trading_disabled_report,
)
from advanced_backtest_governance.backtest_broker_execution_disabled import (
    build_backtest_broker_execution_disabled_report,
)
from advanced_backtest_governance.backtest_deployment_disabled import (
    build_backtest_deployment_disabled_report,
)
from advanced_backtest_governance.backtest_governance_report_builder import (
    build_backtest_disabled_execution_markdown_report,
)
from reports.report_builder import (
    build_backtest_disabled_execution_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_backtest_governance_profile()

    df_d_exec, s_d_exec = build_backtest_governance_execution_disabled_report(profile)
    df_d_claim, s_d_claim = build_backtest_result_claim_disabled_report(profile)
    df_d_calc, s_d_calc = build_backtest_metric_calculation_disabled_report(profile)
    df_d_opt, s_d_opt = build_backtest_optimizer_disabled_report(profile)
    df_d_train, s_d_train = build_backtest_model_training_disabled_report(profile)
    df_d_pred, s_d_pred = build_backtest_prediction_disabled_report(profile)
    df_d_live, s_d_live = build_backtest_live_trading_disabled_report(profile)
    df_d_brk, s_d_brk = build_backtest_broker_execution_disabled_report(profile)
    df_d_dep, s_d_dep = build_backtest_deployment_disabled_report(profile)

    data_lake.save_backtest_governance_execution_disabled_report(df_d_exec, s_d_exec)
    data_lake.save_backtest_result_claim_disabled_report(df_d_claim, s_d_claim)
    data_lake.save_backtest_metric_calculation_disabled_report(df_d_calc, s_d_calc)
    data_lake.save_backtest_optimizer_disabled_report(df_d_opt, s_d_opt)
    data_lake.save_backtest_model_training_disabled_report(df_d_train, s_d_train)
    data_lake.save_backtest_prediction_disabled_report(df_d_pred, s_d_pred)
    data_lake.save_backtest_live_trading_disabled_report(df_d_live, s_d_live)
    data_lake.save_backtest_broker_execution_disabled_report(df_d_brk, s_d_brk)
    data_lake.save_backtest_deployment_disabled_report(df_d_dep, s_d_dep)

    out_dir = Path("reports/output/advanced_backtest_governance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "disabled_execution.md", "w", encoding="utf-8") as f:
        f.write(build_backtest_disabled_execution_markdown_report(s_d_exec, df_d_exec))
    with open(out_dir / "disabled_execution.txt", "w", encoding="utf-8") as f:
        f.write(build_backtest_disabled_execution_text_report(s_d_exec, df_d_exec))

    print("Phase 150 disabled execution reports successfully built.")


if __name__ == "__main__":
    main()
