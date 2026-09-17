# -*- coding: utf-8 -*-
"""Phase 151: Run Evaluation Disabled Execution Reports Script.

Builds and persists all 11 negative invariant disabled execution reports
(benchmark report execution, strategy evaluation execution, metric calculation,
result claim, strategy approval, optimizer, training, prediction, live trading, broker, deployment).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_report_execution_disabled import (
    build_benchmark_report_execution_disabled_report,
)
from advanced_benchmark_evaluation.strategy_evaluation_execution_disabled import (
    build_strategy_evaluation_execution_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_metric_calculation_disabled import (
    build_evaluation_metric_calculation_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_result_claim_disabled import (
    build_evaluation_result_claim_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_strategy_approval_disabled import (
    build_evaluation_strategy_approval_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_optimizer_disabled import (
    build_evaluation_optimizer_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_model_training_disabled import (
    build_evaluation_model_training_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_prediction_disabled import (
    build_evaluation_prediction_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_live_trading_disabled import (
    build_evaluation_live_trading_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_broker_execution_disabled import (
    build_evaluation_broker_execution_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_deployment_disabled import (
    build_evaluation_deployment_disabled_report,
)
from advanced_benchmark_evaluation.benchmark_evaluation_report_builder import (
    build_benchmark_evaluation_disabled_execution_markdown_report,
)
from reports.report_builder import (
    build_benchmark_evaluation_disabled_execution_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_benchmark_evaluation_profile()

    df_d_br, s_d_br = build_benchmark_report_execution_disabled_report(profile)
    df_d_se, s_d_se = build_strategy_evaluation_execution_disabled_report(profile)
    df_d_mc, s_d_mc = build_evaluation_metric_calculation_disabled_report(profile)
    df_d_rc, s_d_rc = build_evaluation_result_claim_disabled_report(profile)
    df_d_sa, s_d_sa = build_evaluation_strategy_approval_disabled_report(profile)
    df_d_opt, s_d_opt = build_evaluation_optimizer_disabled_report(profile)
    df_d_trn, s_d_trn = build_evaluation_model_training_disabled_report(profile)
    df_d_prd, s_d_prd = build_evaluation_prediction_disabled_report(profile)
    df_d_lt, s_d_lt = build_evaluation_live_trading_disabled_report(profile)
    df_d_brk, s_d_brk = build_evaluation_broker_execution_disabled_report(profile)
    df_d_dep, s_d_dep = build_evaluation_deployment_disabled_report(profile)

    data_lake.save_benchmark_report_execution_disabled_report(df_d_br, s_d_br)
    data_lake.save_strategy_evaluation_execution_disabled_report(df_d_se, s_d_se)
    data_lake.save_evaluation_metric_calculation_disabled_report(df_d_mc, s_d_mc)
    data_lake.save_evaluation_result_claim_disabled_report(df_d_rc, s_d_rc)
    data_lake.save_evaluation_strategy_approval_disabled_report(df_d_sa, s_d_sa)
    data_lake.save_evaluation_live_trading_disabled_report(df_d_lt, s_d_lt)
    data_lake.save_evaluation_broker_execution_disabled_report(df_d_brk, s_d_brk)

    out_dir = Path("reports/output/advanced_benchmark_evaluation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "disabled_execution.md", "w", encoding="utf-8") as f:
        f.write(build_benchmark_evaluation_disabled_execution_markdown_report(s_d_br, df_d_br))
    with open(out_dir / "disabled_execution.txt", "w", encoding="utf-8") as f:
        f.write(build_benchmark_evaluation_disabled_execution_text_report(s_d_br, df_d_br))

    print("Phase 151 disabled execution reports successfully built and saved.")


if __name__ == "__main__":
    main()
