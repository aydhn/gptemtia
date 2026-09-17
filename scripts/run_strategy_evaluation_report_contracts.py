# -*- coding: utf-8 -*-
"""Phase 151: Run Strategy Evaluation Report Contracts Script.

Builds and persists strategy evaluation report contracts, strategy vs benchmark contracts,
cost/slippage/regime/walk-forward/oos/stress/monte carlo/governance evaluation contracts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.strategy_evaluation_report_contracts import (
    build_strategy_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.strategy_vs_benchmark_report_contracts import (
    build_strategy_vs_benchmark_report_contract_registry,
)
from advanced_benchmark_evaluation.cost_adjusted_evaluation_report_contracts import (
    build_cost_adjusted_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.slippage_adjusted_evaluation_report_contracts import (
    build_slippage_adjusted_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.regime_aware_evaluation_report_contracts import (
    build_regime_aware_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.walk_forward_evaluation_report_contracts import (
    build_walk_forward_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.oos_evaluation_report_contracts import (
    build_oos_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.stress_aware_evaluation_report_contracts import (
    build_stress_aware_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.monte_carlo_robustness_evaluation_report_contracts import (
    build_monte_carlo_robustness_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.governance_aware_evaluation_report_contracts import (
    build_governance_aware_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_report_builder import (
    build_strategy_evaluation_report_contract_markdown_report,
)
from reports.report_builder import (
    build_strategy_evaluation_report_contract_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_benchmark_evaluation_profile()

    df_se, s_se = build_strategy_evaluation_report_contract_registry(profile)
    df_svb, s_svb = build_strategy_vs_benchmark_report_contract_registry(profile)
    df_cost, s_cost = build_cost_adjusted_evaluation_report_contract_registry(profile)
    df_slip, s_slip = build_slippage_adjusted_evaluation_report_contract_registry(profile)
    df_reg, s_reg = build_regime_aware_evaluation_report_contract_registry(profile)
    df_wf, s_wf = build_walk_forward_evaluation_report_contract_registry(profile)
    df_oos, s_oos = build_oos_evaluation_report_contract_registry(profile)
    df_stress, s_stress = build_stress_aware_evaluation_report_contract_registry(profile)
    df_mc, s_mc = build_monte_carlo_robustness_evaluation_report_contract_registry(profile)
    df_gov, s_gov = build_governance_aware_evaluation_report_contract_registry(profile)

    data_lake.save_strategy_evaluation_report_contract_registry(df_se, s_se)
    data_lake.save_strategy_vs_benchmark_report_contract_registry(df_svb, s_svb)
    data_lake.save_cost_adjusted_evaluation_report_contract_registry(df_cost, s_cost)
    data_lake.save_slippage_adjusted_evaluation_report_contract_registry(df_slip, s_slip)
    data_lake.save_regime_aware_evaluation_report_contract_registry(df_reg, s_reg)
    data_lake.save_walk_forward_evaluation_report_contract_registry(df_wf, s_wf)
    data_lake.save_oos_evaluation_report_contract_registry(df_oos, s_oos)
    data_lake.save_stress_aware_evaluation_report_contract_registry(df_stress, s_stress)
    data_lake.save_monte_carlo_robustness_evaluation_report_contract_registry(df_mc, s_mc)
    data_lake.save_governance_aware_evaluation_report_contract_registry(df_gov, s_gov)

    out_dir = Path("reports/output/advanced_benchmark_evaluation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "strategy_evaluation_contracts.md", "w", encoding="utf-8") as f:
        f.write(build_strategy_evaluation_report_contract_markdown_report(s_se, df_se))
    with open(out_dir / "strategy_evaluation_contracts.txt", "w", encoding="utf-8") as f:
        f.write(build_strategy_evaluation_report_contract_text_report(s_se, df_se))

    print("Phase 151 strategy evaluation report contracts successfully built and saved.")


if __name__ == "__main__":
    main()
