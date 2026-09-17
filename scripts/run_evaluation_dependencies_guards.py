# -*- coding: utf-8 -*-
"""Phase 151: Run Evaluation Dependencies and Guards Script.

Builds and persists evaluation input data contracts, upstream phase dependencies,
and strict boundary guards (no-lookahead, claim guards, forbidden columns, etc.).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.evaluation_input_data_contracts import (
    build_evaluation_input_data_contract_registry,
)
from advanced_benchmark_evaluation.evaluation_feature_input_contracts import (
    build_evaluation_feature_input_contract_registry,
)
from advanced_benchmark_evaluation.evaluation_signal_input_contracts import (
    build_evaluation_signal_input_contract_registry,
)
from advanced_benchmark_evaluation.evaluation_backtest_dependencies import (
    build_evaluation_backtest_dependency_registry,
)
from advanced_benchmark_evaluation.evaluation_walk_forward_dependencies import (
    build_evaluation_walk_forward_dependency_registry,
)
from advanced_benchmark_evaluation.evaluation_stress_dependencies import (
    build_evaluation_stress_dependency_registry,
)
from advanced_benchmark_evaluation.evaluation_monte_carlo_dependencies import (
    build_evaluation_monte_carlo_dependency_registry,
)
from advanced_benchmark_evaluation.evaluation_governance_dependencies import (
    build_evaluation_governance_dependency_registry,
)
from advanced_benchmark_evaluation.evaluation_benchmark_dependencies import (
    build_evaluation_benchmark_dependency_registry,
)
from advanced_benchmark_evaluation.evaluation_no_lookahead_guards import (
    build_evaluation_no_lookahead_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_result_claim_guards import (
    build_evaluation_result_claim_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_performance_claim_guards import (
    build_evaluation_performance_claim_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_strategy_approval_guards import (
    build_evaluation_strategy_approval_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_benchmark_selection_bias_guards import (
    build_evaluation_benchmark_selection_bias_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_data_snooping_bias_guards import (
    build_evaluation_data_snooping_bias_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_overfitting_guards import (
    build_evaluation_overfitting_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_multiple_testing_guards import (
    build_evaluation_multiple_testing_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_metadata_only_news_guards import (
    build_evaluation_metadata_only_news_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_source_preservation_guards import (
    build_evaluation_source_preservation_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_forbidden_column_policies import (
    build_evaluation_forbidden_column_policy_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_report_builder import (
    build_evaluation_guard_markdown_report,
)
from reports.report_builder import (
    build_evaluation_guard_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_benchmark_evaluation_profile()

    df_inp_d, s_inp_d = build_evaluation_input_data_contract_registry(profile)
    df_inp_f, s_inp_f = build_evaluation_feature_input_contract_registry(profile)
    df_inp_s, s_inp_s = build_evaluation_signal_input_contract_registry(profile)

    df_dep_bt, s_dep_bt = build_evaluation_backtest_dependency_registry(profile)
    df_dep_wf, s_dep_wf = build_evaluation_walk_forward_dependency_registry(profile)
    df_dep_st, s_dep_st = build_evaluation_stress_dependency_registry(profile)
    df_dep_mc, s_dep_mc = build_evaluation_monte_carlo_dependency_registry(profile)
    df_dep_gov, s_dep_gov = build_evaluation_governance_dependency_registry(profile)
    df_dep_bench, s_dep_bench = build_evaluation_benchmark_dependency_registry(profile)

    df_g_look, s_g_look = build_evaluation_no_lookahead_guard_registry(profile)
    df_g_res, s_g_res = build_evaluation_result_claim_guard_registry(profile)
    df_g_perf, s_g_perf = build_evaluation_performance_claim_guard_registry(profile)
    df_g_app, s_g_app = build_evaluation_strategy_approval_guard_registry(profile)
    df_g_bsel, s_g_bsel = build_evaluation_benchmark_selection_bias_guard_registry(profile)
    df_g_dsnoop, s_g_dsnoop = build_evaluation_data_snooping_bias_guard_registry(profile)
    df_g_overfit, s_g_overfit = build_evaluation_overfitting_guard_registry(profile)
    df_g_mtest, s_g_mtest = build_evaluation_multiple_testing_guard_registry(profile)
    df_g_news, s_g_news = build_evaluation_metadata_only_news_guard_registry(profile)
    df_g_src, s_g_src = build_evaluation_source_preservation_guard_registry(profile)
    df_forbid, s_forbid = build_evaluation_forbidden_column_policy_registry(profile)

    data_lake.save_evaluation_result_claim_guard_registry(df_g_res, s_g_res)
    data_lake.save_evaluation_performance_claim_guard_registry(df_g_perf, s_g_perf)
    data_lake.save_evaluation_strategy_approval_guard_registry(df_g_app, s_g_app)
    data_lake.save_evaluation_forbidden_column_policy_registry(df_forbid, s_forbid)

    out_dir = Path("reports/output/advanced_benchmark_evaluation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "dependencies_and_guards.md", "w", encoding="utf-8") as f:
        f.write(build_evaluation_guard_markdown_report(s_g_look, df_g_look))
    with open(out_dir / "dependencies_and_guards.txt", "w", encoding="utf-8") as f:
        f.write(build_evaluation_guard_text_report(s_g_look, df_g_look))

    print("Phase 151 evaluation dependencies and guards successfully built and saved.")


if __name__ == "__main__":
    main()
