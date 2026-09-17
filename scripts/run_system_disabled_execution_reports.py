# -*- coding: utf-8 -*-
"""Phase 158: Run System Disabled Execution Reports Script.

Generates and persists disabled execution guarantee reports for all 13 subsystems.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_execution_disabled import (
    build_system_execution_disabled_report,
)
from advanced_full_system_integration.live_trading_disabled import (
    build_live_trading_disabled_report,
)
from advanced_full_system_integration.broker_execution_disabled import (
    build_broker_execution_disabled_report,
)
from advanced_full_system_integration.production_deployment_disabled import (
    build_production_deployment_disabled_report,
)
from advanced_full_system_integration.model_training_disabled import (
    build_model_training_disabled_report,
)
from advanced_full_system_integration.model_prediction_disabled import (
    build_model_prediction_disabled_report,
)
from advanced_full_system_integration.backtest_execution_disabled import (
    build_backtest_execution_disabled_report,
)
from advanced_full_system_integration.portfolio_execution_disabled import (
    build_portfolio_execution_disabled_report,
)
from advanced_full_system_integration.risk_execution_disabled import (
    build_risk_execution_disabled_report,
)
from advanced_full_system_integration.scenario_execution_disabled import (
    build_scenario_execution_disabled_report,
)
from advanced_full_system_integration.order_generation_disabled import (
    build_order_generation_disabled_report,
)
from advanced_full_system_integration.signal_generation_disabled import (
    build_signal_generation_disabled_report,
)
from advanced_full_system_integration.investment_advice_disabled import (
    build_investment_advice_disabled_report,
)
from advanced_full_system_integration.full_system_integration_report_builder import (
    build_system_disabled_execution_markdown_report,
)
from reports.report_builder import (
    build_system_disabled_execution_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_full_system_integration_profile()

    df_sed, s_sed = build_system_execution_disabled_report(profile)
    df_ltd, s_ltd = build_live_trading_disabled_report(profile)
    df_bed, s_bed = build_broker_execution_disabled_report(profile)
    df_pdd, s_pdd = build_production_deployment_disabled_report(profile)
    df_mtd, s_mtd = build_model_training_disabled_report(profile)
    df_mpd, s_mpd = build_model_prediction_disabled_report(profile)
    df_bxd, s_bxd = build_backtest_execution_disabled_report(profile)
    df_pxd, s_pxd = build_portfolio_execution_disabled_report(profile)
    df_rxd, s_rxd = build_risk_execution_disabled_report(profile)
    df_sxd, s_sxd = build_scenario_execution_disabled_report(profile)
    df_ogd, s_ogd = build_order_generation_disabled_report(profile)
    df_sgd, s_sgd = build_signal_generation_disabled_report(profile)
    df_iad, s_iad = build_investment_advice_disabled_report(profile)

    data_lake.save_system_execution_disabled_report(df_sed, s_sed)
    data_lake.save_live_trading_disabled_report(df_ltd, s_ltd)
    data_lake.save_broker_execution_disabled_report(df_bed, s_bed)
    data_lake.save_production_deployment_disabled_report(df_pdd, s_pdd)
    data_lake.save_model_training_disabled_report(df_mtd, s_mtd)
    data_lake.save_model_prediction_disabled_report(df_mpd, s_mpd)
    data_lake.save_order_generation_disabled_report(df_ogd, s_ogd)
    data_lake.save_signal_generation_disabled_report(df_sgd, s_sgd)
    data_lake.save_investment_advice_disabled_report(df_iad, s_iad)

    out_dir = Path("reports/output/advanced_full_system_integration")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_dis = build_system_disabled_execution_markdown_report(s_sed, df_sed)
    txt_dis = build_system_disabled_execution_text_report(s_sed, df_sed)

    with open(out_dir / "disabled_execution.md", "w", encoding="utf-8") as f:
        f.write(md_dis)
    with open(out_dir / "disabled_execution.txt", "w", encoding="utf-8") as f:
        f.write(txt_dis)

    print("=" * 70)
    print("PHASE 158: DISABLED EXECUTION GUARANTEES ENFORCED (13 SUBSYSTEMS)")
    print("=" * 70)
    print("Full System Execution : DISABLED")
    print("Live Trading          : DISABLED")
    print("Broker Execution      : DISABLED")
    print("Production Deploy     : DISABLED")
    print("Model Training        : DISABLED")
    print("Model Prediction      : DISABLED")
    print("Order Generation      : DISABLED")
    print("Signal Generation     : DISABLED")
    print("=" * 70)


if __name__ == "__main__":
    main()
