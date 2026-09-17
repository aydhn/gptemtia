# -*- coding: utf-8 -*-
"""Phase 151: Run Evaluation Summary Placeholders Script.

Builds and persists evaluation summary placeholders, risk/cost/slippage/regime/stress/monte carlo
summary placeholders, limitation placeholders, and disclaimers.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.strategy_evaluation_summary_placeholders import (
    build_strategy_evaluation_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.benchmark_comparison_summary_placeholders import (
    build_benchmark_comparison_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.metric_summary_placeholders import (
    build_metric_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.risk_summary_placeholders import (
    build_risk_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.cost_impact_summary_placeholders import (
    build_cost_impact_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.slippage_impact_summary_placeholders import (
    build_slippage_impact_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.regime_performance_summary_placeholders import (
    build_regime_performance_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.stress_result_summary_placeholders import (
    build_stress_result_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.monte_carlo_result_summary_placeholders import (
    build_monte_carlo_result_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.strategy_limitation_placeholders import (
    build_strategy_limitation_placeholder_registry,
)
from advanced_benchmark_evaluation.benchmark_limitation_placeholders import (
    build_benchmark_limitation_placeholder_registry,
)
from advanced_benchmark_evaluation.report_disclaimers import (
    build_report_disclaimer_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_report_builder import (
    build_evaluation_summary_placeholder_markdown_report,
)
from reports.report_builder import (
    build_evaluation_summary_placeholder_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_benchmark_evaluation_profile()

    df_ss, s_ss = build_strategy_evaluation_summary_placeholder_registry(profile)
    df_bs, s_bs = build_benchmark_comparison_summary_placeholder_registry(profile)
    df_ms, s_ms = build_metric_summary_placeholder_registry(profile)
    df_rs, s_rs = build_risk_summary_placeholder_registry(profile)
    df_ci, s_ci = build_cost_impact_summary_placeholder_registry(profile)
    df_si, s_si = build_slippage_impact_summary_placeholder_registry(profile)
    df_rp, s_rp = build_regime_performance_summary_placeholder_registry(profile)
    df_st, s_st = build_stress_result_summary_placeholder_registry(profile)
    df_mc, s_mc = build_monte_carlo_result_summary_placeholder_registry(profile)
    df_sl, s_sl = build_strategy_limitation_placeholder_registry(profile)
    df_bl, s_bl = build_benchmark_limitation_placeholder_registry(profile)
    df_dc, s_dc = build_report_disclaimer_registry(profile)

    data_lake.save_strategy_evaluation_summary_placeholder_registry(df_ss, s_ss)
    data_lake.save_benchmark_comparison_summary_placeholder_registry(df_bs, s_bs)
    data_lake.save_metric_summary_placeholder_registry(df_ms, s_ms)
    data_lake.save_risk_summary_placeholder_registry(df_rs, s_rs)
    data_lake.save_cost_impact_summary_placeholder_registry(df_ci, s_ci)
    data_lake.save_slippage_impact_summary_placeholder_registry(df_si, s_si)
    data_lake.save_regime_performance_summary_placeholder_registry(df_rp, s_rp)
    data_lake.save_stress_result_summary_placeholder_registry(df_st, s_st)
    data_lake.save_monte_carlo_result_summary_placeholder_registry(df_mc, s_mc)
    data_lake.save_strategy_limitation_placeholder_registry(df_sl, s_sl)
    data_lake.save_benchmark_limitation_placeholder_registry(df_bl, s_bl)

    out_dir = Path("reports/output/advanced_benchmark_evaluation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "summary_placeholders.md", "w", encoding="utf-8") as f:
        f.write(build_evaluation_summary_placeholder_markdown_report(s_ss, df_ss))
    with open(out_dir / "summary_placeholders.txt", "w", encoding="utf-8") as f:
        f.write(build_evaluation_summary_placeholder_text_report(s_ss, df_ss))

    print("Phase 151 evaluation summary placeholders successfully built and saved.")


if __name__ == "__main__":
    main()
