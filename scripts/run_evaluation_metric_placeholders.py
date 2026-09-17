# -*- coding: utf-8 -*-
"""Phase 151: Run Evaluation Metric Placeholders Script.

Builds and persists uncalculated evaluation metric placeholders across strategy,
benchmark, relative, risk-adjusted, cost-adjusted, and robustness metrics.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.strategy_evaluation_metric_placeholders import (
    build_strategy_evaluation_metric_placeholder_registry,
)
from advanced_benchmark_evaluation.benchmark_comparison_metric_placeholders import (
    build_benchmark_comparison_metric_placeholder_registry,
)
from advanced_benchmark_evaluation.relative_performance_metric_placeholders import (
    build_relative_performance_metric_placeholder_registry,
)
from advanced_benchmark_evaluation.risk_adjusted_metric_placeholders import (
    build_risk_adjusted_metric_placeholder_registry,
)
from advanced_benchmark_evaluation.cost_adjusted_metric_placeholders import (
    build_cost_adjusted_metric_placeholder_registry,
)
from advanced_benchmark_evaluation.robustness_metric_placeholders import (
    build_robustness_metric_placeholder_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_report_builder import (
    build_evaluation_metric_placeholder_markdown_report,
)
from reports.report_builder import (
    build_evaluation_metric_placeholder_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_benchmark_evaluation_profile()

    df_sm, s_sm = build_strategy_evaluation_metric_placeholder_registry(profile)
    df_bm, s_bm = build_benchmark_comparison_metric_placeholder_registry(profile)
    df_rm, s_rm = build_relative_performance_metric_placeholder_registry(profile)
    df_ram, s_ram = build_risk_adjusted_metric_placeholder_registry(profile)
    df_cam, s_cam = build_cost_adjusted_metric_placeholder_registry(profile)
    df_rob, s_rob = build_robustness_metric_placeholder_registry(profile)

    data_lake.save_strategy_evaluation_metric_placeholder_registry(df_sm, s_sm)
    data_lake.save_benchmark_comparison_metric_placeholder_registry(df_bm, s_bm)
    data_lake.save_relative_performance_metric_placeholder_registry(df_rm, s_rm)
    data_lake.save_risk_adjusted_metric_placeholder_registry(df_ram, s_ram)
    data_lake.save_cost_adjusted_metric_placeholder_registry(df_cam, s_cam)
    data_lake.save_robustness_metric_placeholder_registry(df_rob, s_rob)

    out_dir = Path("reports/output/advanced_benchmark_evaluation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "metric_placeholders.md", "w", encoding="utf-8") as f:
        f.write(build_evaluation_metric_placeholder_markdown_report(s_sm, df_sm))
    with open(out_dir / "metric_placeholders.txt", "w", encoding="utf-8") as f:
        f.write(build_evaluation_metric_placeholder_text_report(s_sm, df_sm))

    print("Phase 151 evaluation metric placeholders successfully built and saved.")


if __name__ == "__main__":
    main()
