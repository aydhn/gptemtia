# -*- coding: utf-8 -*-
"""Phase 148: Run Stress Disabled Execution Reports Script.

Builds and persists reports certifying disabled live trading, disabled broker execution,
disabled stress testing execution, disabled scenario simulation, and disabled metric calculation.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_execution_disabled import (
    build_stress_execution_disabled_report,
)
from advanced_stress_testing.scenario_simulation_disabled import (
    build_scenario_simulation_disabled_report,
)
from advanced_stress_testing.stress_metric_calculation_disabled import (
    build_stress_metric_calculation_disabled_report,
)
from advanced_stress_testing.stress_live_trading_disabled import (
    build_stress_live_trading_disabled_report,
)
from advanced_stress_testing.stress_broker_execution_disabled import (
    build_stress_broker_execution_disabled_report,
)
from advanced_stress_testing.stress_testing_report_builder import (
    build_stress_disabled_execution_markdown_report,
)
from reports.report_builder import build_stress_disabled_execution_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_stress_testing_profile()

    df_stress, s_stress = build_stress_execution_disabled_report(profile)
    df_scen, s_scen = build_scenario_simulation_disabled_report(profile)
    df_calc, s_calc = build_stress_metric_calculation_disabled_report(profile)
    df_live, s_live = build_stress_live_trading_disabled_report(profile)
    df_brok, s_brok = build_stress_broker_execution_disabled_report(profile)

    data_lake.save_stress_execution_disabled_report(df_stress, s_stress)
    data_lake.save_scenario_simulation_disabled_report(df_scen, s_scen)
    data_lake.save_stress_metric_calculation_disabled_report(df_calc, s_calc)
    data_lake.save_stress_live_trading_disabled_report(df_live, s_live)
    data_lake.save_stress_broker_execution_disabled_report(df_brok, s_brok)

    summary = {
        "live_trading_disabled": True,
        "broker_execution_disabled": True,
        "optimizer_disabled": True,
        "stress_test_disabled": True,
        "scenario_simulation_disabled": True,
        "metric_calculation_disabled": True,
    }

    md_report = build_stress_disabled_execution_markdown_report(summary, df_stress)
    txt_report = build_stress_disabled_execution_text_report(summary, df_stress)

    out_dir = Path("reports/output/advanced_stress_testing")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "disabled_execution.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "disabled_execution.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("Disabled execution reports successfully built and persisted.")


if __name__ == "__main__":
    main()
