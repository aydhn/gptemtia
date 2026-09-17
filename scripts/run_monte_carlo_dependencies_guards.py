# -*- coding: utf-8 -*-
"""Phase 149: Run Monte Carlo Dependencies and Guards Script.

Builds and persists linkages, dependencies, and bias/lookahead guards.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_monte_carlo_robustness.monte_carlo_config import (
    get_default_monte_carlo_profile,
)
from advanced_monte_carlo_robustness.scenario_resampling_linkage import (
    build_scenario_resampling_linkage_registry,
)
from advanced_monte_carlo_robustness.stress_monte_carlo_linkage import (
    build_stress_monte_carlo_linkage_registry,
)
from advanced_monte_carlo_robustness.walk_forward_monte_carlo_linkage import (
    build_walk_forward_monte_carlo_linkage_registry,
)
from advanced_monte_carlo_robustness.realistic_backtest_monte_carlo_dependencies import (
    build_realistic_backtest_monte_carlo_dependency_registry,
)
from advanced_monte_carlo_robustness.transaction_cost_monte_carlo_dependencies import (
    build_transaction_cost_monte_carlo_dependency_registry,
)
from advanced_monte_carlo_robustness.slippage_monte_carlo_dependencies import (
    build_slippage_monte_carlo_dependency_registry,
)
from advanced_monte_carlo_robustness.regime_monte_carlo_dependencies import (
    build_regime_monte_carlo_dependency_registry,
)
from advanced_monte_carlo_robustness.governance_monte_carlo_dependencies import (
    build_governance_monte_carlo_dependency_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_no_lookahead_guards import (
    build_monte_carlo_no_lookahead_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_resampling_leakage_guards import (
    build_monte_carlo_resampling_leakage_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_data_snooping_bias_guards import (
    build_monte_carlo_data_snooping_bias_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_overfitting_guards import (
    build_monte_carlo_overfitting_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_survivorship_bias_guards import (
    build_monte_carlo_survivorship_bias_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_multiple_testing_guards import (
    build_monte_carlo_multiple_testing_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_metadata_only_news_guards import (
    build_monte_carlo_metadata_only_news_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_source_preservation_guards import (
    build_monte_carlo_source_preservation_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_forbidden_column_policies import (
    build_monte_carlo_forbidden_column_policy_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_report_builder import (
    build_monte_carlo_dependency_markdown_report,
    build_monte_carlo_guard_markdown_report,
)
from reports.report_builder import build_monte_carlo_guards_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_monte_carlo_profile()

    df_scn, s_scn = build_scenario_resampling_linkage_registry(profile)
    df_str, s_str = build_stress_monte_carlo_linkage_registry(profile)
    df_wf, s_wf = build_walk_forward_monte_carlo_linkage_registry(profile)
    df_bt, s_bt = build_realistic_backtest_monte_carlo_dependency_registry(profile)
    df_cst, s_cst = build_transaction_cost_monte_carlo_dependency_registry(profile)
    df_slp, s_slp = build_slippage_monte_carlo_dependency_registry(profile)
    df_reg, s_reg = build_regime_monte_carlo_dependency_registry(profile)
    df_gov, s_gov = build_governance_monte_carlo_dependency_registry(profile)

    df_g1, s_g1 = build_monte_carlo_no_lookahead_guard_registry(profile)
    df_g2, s_g2 = build_monte_carlo_resampling_leakage_guard_registry(profile)
    df_g3, s_g3 = build_monte_carlo_data_snooping_bias_guard_registry(profile)
    df_g4, s_g4 = build_monte_carlo_overfitting_guard_registry(profile)
    df_g5, s_g5 = build_monte_carlo_survivorship_bias_guard_registry(profile)
    df_g6, s_g6 = build_monte_carlo_multiple_testing_guard_registry(profile)
    df_g7, s_g7 = build_monte_carlo_metadata_only_news_guard_registry(profile)
    df_g8, s_g8 = build_monte_carlo_source_preservation_guard_registry(profile)
    df_g9, s_g9 = build_monte_carlo_forbidden_column_policy_registry(profile)

    data_lake.save_scenario_resampling_linkage(df_scn, s_scn)
    data_lake.save_stress_monte_carlo_linkage(df_str, s_str)
    data_lake.save_walk_forward_monte_carlo_linkage(df_wf, s_wf)
    data_lake.save_realistic_backtest_monte_carlo_dependencies(df_bt, s_bt)
    data_lake.save_transaction_cost_monte_carlo_dependencies(df_cst, s_cst)
    data_lake.save_slippage_monte_carlo_dependencies(df_slp, s_slp)
    data_lake.save_regime_monte_carlo_dependencies(df_reg, s_reg)
    data_lake.save_governance_monte_carlo_dependencies(df_gov, s_gov)

    data_lake.save_monte_carlo_no_lookahead_guards(df_g1, s_g1)
    data_lake.save_monte_carlo_resampling_leakage_guards(df_g2, s_g2)
    data_lake.save_monte_carlo_data_snooping_bias_guards(df_g3, s_g3)
    data_lake.save_monte_carlo_overfitting_guards(df_g4, s_g4)
    data_lake.save_monte_carlo_survivorship_bias_guards(df_g5, s_g5)
    data_lake.save_monte_carlo_multiple_testing_guards(df_g6, s_g6)
    data_lake.save_monte_carlo_metadata_only_news_guards(df_g7, s_g7)
    data_lake.save_monte_carlo_source_preservation_guards(df_g8, s_g8)
    data_lake.save_monte_carlo_forbidden_column_policies(df_g9, s_g9)

    out_dir = Path("reports/output/advanced_monte_carlo_robustness")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "dependencies.md", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_dependency_markdown_report(s_bt, df_bt))
    with open(out_dir / "guards.md", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_guard_markdown_report(s_g1, df_g1))
    with open(out_dir / "guards.txt", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_guards_text_report(s_g1, df_g1))

    print("Monte Carlo dependencies, linkages, and guards successfully built.")


if __name__ == "__main__":
    main()
