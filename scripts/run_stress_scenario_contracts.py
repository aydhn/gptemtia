# -*- coding: utf-8 -*-
"""Phase 148: Run Stress Scenario Contracts Script.

Builds and persists core stress scenario contracts, historical and hypothetical scenarios,
regime/volatility/liquidity/spread shock contracts, and unified scenario library.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_scenario_contracts import (
    build_stress_scenario_contract_registry,
)
from advanced_stress_testing.historical_stress_scenario_contracts import (
    build_historical_stress_scenario_contract_registry,
)
from advanced_stress_testing.hypothetical_stress_scenario_contracts import (
    build_hypothetical_stress_scenario_contract_registry,
)
from advanced_stress_testing.regime_shock_scenario_contracts import (
    build_regime_shock_scenario_contract_registry,
)
from advanced_stress_testing.volatility_shock_scenario_contracts import (
    build_volatility_shock_scenario_contract_registry,
)
from advanced_stress_testing.liquidity_shock_scenario_contracts import (
    build_liquidity_shock_scenario_contract_registry,
)
from advanced_stress_testing.spread_widening_scenario_contracts import (
    build_spread_widening_scenario_contract_registry,
)
from advanced_stress_testing.stress_scenario_library import (
    build_stress_scenario_library_registry,
)
from advanced_stress_testing.stress_testing_report_builder import (
    build_stress_scenario_contract_markdown_report,
)
from reports.report_builder import build_stress_scenario_contract_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_stress_testing_profile()

    df_core, s_core = build_stress_scenario_contract_registry(profile)
    df_hist, s_hist = build_historical_stress_scenario_contract_registry(profile)
    df_hypo, s_hypo = build_hypothetical_stress_scenario_contract_registry(profile)
    df_reg, s_reg = build_regime_shock_scenario_contract_registry(profile)
    df_vol, s_vol = build_volatility_shock_scenario_contract_registry(profile)
    df_liq, s_liq = build_liquidity_shock_scenario_contract_registry(profile)
    df_spr, s_spr = build_spread_widening_scenario_contract_registry(profile)
    df_lib, s_lib = build_stress_scenario_library_registry(profile)

    data_lake.save_stress_scenario_contract_registry(df_core, s_core)
    data_lake.save_historical_stress_scenario_contract_registry(df_hist, s_hist)
    data_lake.save_hypothetical_stress_scenario_contract_registry(df_hypo, s_hypo)
    data_lake.save_regime_shock_scenario_contract_registry(df_reg, s_reg)
    data_lake.save_volatility_shock_scenario_contract_registry(df_vol, s_vol)
    data_lake.save_liquidity_shock_scenario_contract_registry(df_liq, s_liq)
    data_lake.save_spread_widening_scenario_contract_registry(df_spr, s_spr)
    data_lake.save_stress_scenario_library_registry(df_lib, s_lib)

    md_report = build_stress_scenario_contract_markdown_report(s_core, df_core)
    txt_report = build_stress_scenario_contract_text_report(s_core, df_core)

    out_dir = Path("reports/output/advanced_stress_testing")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "scenario_contracts.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "scenario_contracts.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("Stress scenario contracts and libraries successfully built and persisted.")


if __name__ == "__main__":
    main()
