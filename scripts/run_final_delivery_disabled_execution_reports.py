# -*- coding: utf-8 -*-
"""Phase 160: Run Final Delivery Disabled Execution Reports Script.

Builds and persists reports documenting that all execution mechanisms are disabled.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_delivery.final_delivery_config import (
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_execution_disabled import (
    build_final_delivery_execution_disabled_report,
)
from advanced_final_delivery.final_delivery_live_trading_disabled import (
    build_final_delivery_live_trading_disabled_report,
)
from advanced_final_delivery.final_delivery_broker_execution_disabled import (
    build_final_delivery_broker_execution_disabled_report,
)
from advanced_final_delivery.final_delivery_order_generation_disabled import (
    build_final_delivery_order_generation_disabled_report,
)
from advanced_final_delivery.final_delivery_signal_generation_disabled import (
    build_final_delivery_signal_generation_disabled_report,
)
from advanced_final_delivery.final_delivery_model_training_disabled import (
    build_final_delivery_model_training_disabled_report,
)
from advanced_final_delivery.final_delivery_prediction_disabled import (
    build_final_delivery_prediction_disabled_report,
)
from advanced_final_delivery.final_delivery_deployment_disabled import (
    build_final_delivery_deployment_disabled_report,
)
from advanced_final_delivery.final_delivery_report_builder import (
    build_final_delivery_disabled_execution_markdown_report,
)
from reports.report_builder import (
    build_final_delivery_disabled_execution_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_delivery_profile()

    df_exec, s_exec = build_final_delivery_execution_disabled_report(profile)
    df_live, s_live = build_final_delivery_live_trading_disabled_report(profile)
    df_brk, s_brk = build_final_delivery_broker_execution_disabled_report(profile)
    df_ord, s_ord = build_final_delivery_order_generation_disabled_report(profile)
    df_sig, s_sig = build_final_delivery_signal_generation_disabled_report(profile)
    df_trn, s_trn = build_final_delivery_model_training_disabled_report(profile)
    df_prd, s_prd = build_final_delivery_prediction_disabled_report(profile)
    df_dep, s_dep = build_final_delivery_deployment_disabled_report(profile)

    if "--no-save" not in sys.argv and settings.final_delivery_save_reports:
        data_lake.save_final_delivery_execution_disabled_report(df_exec, s_exec)
        data_lake.save_final_delivery_live_trading_disabled_report(df_live, s_live)
        data_lake.save_final_delivery_broker_execution_disabled_report(df_brk, s_brk)
        data_lake.save_final_delivery_signal_generation_disabled_report(df_sig, s_sig)
        data_lake.save_final_delivery_prediction_disabled_report(df_prd, s_prd)
        data_lake.save_final_delivery_deployment_disabled_report(df_dep, s_dep)

    out_dir = Path("reports/output/advanced_final_delivery")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_dis = build_final_delivery_disabled_execution_markdown_report(s_exec, df_exec)
    txt_dis = build_final_delivery_disabled_execution_text_report(s_exec, df_exec)

    if "--no-save" not in sys.argv:
        with open(out_dir / "disabled_execution.md", "w", encoding="utf-8") as f:
            f.write(md_dis)
        with open(out_dir / "disabled_execution.txt", "w", encoding="utf-8") as f:
            f.write(txt_dis)

    print("=" * 70)
    print("PHASE 160: FINAL DELIVERY DISABLED EXECUTION REPORTS INITIALIZED")
    print("=" * 70)
    print(f"Execution Code: {s_exec['execution_code']}")
    print(f"Status: {s_exec['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
