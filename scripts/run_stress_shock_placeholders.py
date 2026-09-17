# -*- coding: utf-8 -*-
"""Phase 148: Run Stress Shock Placeholders Script.

Builds and persists gap risk, correlation breakdown, macro shock, cross-asset contagion,
transaction cost shock, and slippage shock placeholders and contracts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.gap_risk_scenario_placeholders import (
    build_gap_risk_scenario_placeholder_registry,
)
from advanced_stress_testing.correlation_breakdown_scenario_placeholders import (
    build_correlation_breakdown_scenario_placeholder_registry,
)
from advanced_stress_testing.macro_shock_scenario_placeholders import (
    build_macro_shock_scenario_placeholder_registry,
)
from advanced_stress_testing.cross_asset_contagion_scenario_placeholders import (
    build_cross_asset_contagion_scenario_placeholder_registry,
)
from advanced_stress_testing.transaction_cost_shock_contracts import (
    build_transaction_cost_shock_contract_registry,
)
from advanced_stress_testing.slippage_shock_contracts import (
    build_slippage_shock_contract_registry,
)
from advanced_stress_testing.stress_testing_report_builder import (
    build_shock_placeholder_markdown_report,
)
from reports.report_builder import build_shock_placeholder_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_stress_testing_profile()

    df_gap, s_gap = build_gap_risk_scenario_placeholder_registry(profile)
    df_corr, s_corr = build_correlation_breakdown_scenario_placeholder_registry(profile)
    df_macro, s_macro = build_macro_shock_scenario_placeholder_registry(profile)
    df_cont, s_cont = build_cross_asset_contagion_scenario_placeholder_registry(profile)
    df_cost, s_cost = build_transaction_cost_shock_contract_registry(profile)
    df_slip, s_slip = build_slippage_shock_contract_registry(profile)

    data_lake.save_gap_risk_scenario_placeholder_registry(df_gap, s_gap)
    data_lake.save_correlation_breakdown_scenario_placeholder_registry(df_corr, s_corr)
    data_lake.save_macro_shock_scenario_placeholder_registry(df_macro, s_macro)
    data_lake.save_cross_asset_contagion_scenario_placeholder_registry(df_cont, s_cont)
    data_lake.save_transaction_cost_shock_contract_registry(df_cost, s_cost)
    data_lake.save_slippage_shock_contract_registry(df_slip, s_slip)

    summary = {
        "total_shock_types": len(df_gap) + len(df_corr) + len(df_macro) + len(df_cont) + len(df_cost) + len(df_slip),
        "gap_risk_count": len(df_gap),
        "correlation_breakdown_count": len(df_corr),
        "macro_shock_count": len(df_macro),
        "contagion_count": len(df_cont),
        "cost_shock_count": len(df_cost),
        "slippage_shock_count": len(df_slip),
    }

    md_report = build_shock_placeholder_markdown_report(summary, df_gap)
    txt_report = build_shock_placeholder_text_report(summary, df_gap)

    out_dir = Path("reports/output/advanced_stress_testing")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "shock_placeholders.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "shock_placeholders.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("Stress shock placeholders and cost/slippage shock contracts successfully built and persisted.")


if __name__ == "__main__":
    main()
