# -*- coding: utf-8 -*-
"""Phase 150: Run Backtest Bias Controls Script.

Builds and persists Phase 150 bias control contracts and individual bias registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_bias_control_contracts import (
    build_backtest_bias_control_contract_registry,
)
from advanced_backtest_governance.lookahead_bias_controls import (
    build_lookahead_bias_control_registry,
)
from advanced_backtest_governance.survivorship_bias_controls import (
    build_survivorship_bias_control_registry,
)
from advanced_backtest_governance.data_snooping_bias_controls import (
    build_data_snooping_bias_control_registry,
)
from advanced_backtest_governance.overfitting_bias_controls import (
    build_overfitting_bias_control_registry,
)
from advanced_backtest_governance.multiple_testing_bias_controls import (
    build_multiple_testing_bias_control_registry,
)
from advanced_backtest_governance.parameter_fishing_bias_controls import (
    build_parameter_fishing_bias_control_registry,
)
from advanced_backtest_governance.benchmark_selection_bias_controls import (
    build_benchmark_selection_bias_control_registry,
)
from advanced_backtest_governance.regime_coverage_bias_controls import (
    build_regime_coverage_bias_control_registry,
)
from advanced_backtest_governance.sample_coverage_bias_controls import (
    build_sample_coverage_bias_control_registry,
)
from advanced_backtest_governance.backtest_governance_report_builder import (
    build_backtest_bias_control_contract_markdown_report,
)
from reports.report_builder import (
    build_backtest_bias_control_contract_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_backtest_governance_profile()

    df_bias, s_bias = build_backtest_bias_control_contract_registry(profile)
    df_look, s_look = build_lookahead_bias_control_registry(profile)
    df_surv, s_surv = build_survivorship_bias_control_registry(profile)
    df_snoop, s_snoop = build_data_snooping_bias_control_registry(profile)
    df_over, s_over = build_overfitting_bias_control_registry(profile)
    df_mult, s_mult = build_multiple_testing_bias_control_registry(profile)
    df_fish, s_fish = build_parameter_fishing_bias_control_registry(profile)
    df_bench, s_bench = build_benchmark_selection_bias_control_registry(profile)
    df_reg, s_reg = build_regime_coverage_bias_control_registry(profile)
    df_samp, s_samp = build_sample_coverage_bias_control_registry(profile)

    data_lake.save_backtest_bias_control_contracts(df_bias, s_bias)
    data_lake.save_lookahead_bias_controls(df_look, s_look)
    data_lake.save_survivorship_bias_controls(df_surv, s_surv)
    data_lake.save_data_snooping_bias_controls(df_snoop, s_snoop)
    data_lake.save_overfitting_bias_controls(df_over, s_over)
    data_lake.save_multiple_testing_bias_controls(df_mult, s_mult)
    data_lake.save_parameter_fishing_bias_controls(df_fish, s_fish)
    data_lake.save_benchmark_selection_bias_controls(df_bench, s_bench)
    data_lake.save_regime_coverage_bias_controls(df_reg, s_reg)
    data_lake.save_sample_coverage_bias_controls(df_samp, s_samp)

    out_dir = Path("reports/output/advanced_backtest_governance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "bias_controls.md", "w", encoding="utf-8") as f:
        f.write(build_backtest_bias_control_contract_markdown_report(s_bias, df_bias))
    with open(out_dir / "bias_controls.txt", "w", encoding="utf-8") as f:
        f.write(build_backtest_bias_control_contract_text_report(s_bias, df_bias))

    print("Phase 150 bias controls and registries successfully built.")


if __name__ == "__main__":
    main()
