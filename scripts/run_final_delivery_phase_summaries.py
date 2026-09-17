# -*- coding: utf-8 -*-
"""Phase 160: Run Final Delivery Phase Summaries Script.

Builds and persists phase map, Phase 1-100 MVP summary, Phase 101-160 advanced summary,
backtest, portfolio, full-system block summaries, and operator handover registry.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_delivery.final_delivery_config import (
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_phase_map import (
    build_final_delivery_phase_map_registry,
)
from advanced_final_delivery.final_delivery_phase_1_100_mvp_summary import (
    build_final_delivery_phase_1_100_mvp_summary_registry,
)
from advanced_final_delivery.final_delivery_phase_101_160_advanced_summary import (
    build_final_delivery_phase_101_160_advanced_summary_registry,
)
from advanced_final_delivery.final_delivery_backtest_block_summary import (
    build_final_delivery_backtest_block_summary_registry,
)
from advanced_final_delivery.final_delivery_portfolio_block_summary import (
    build_final_delivery_portfolio_block_summary_registry,
)
from advanced_final_delivery.final_delivery_full_system_block_summary import (
    build_final_delivery_full_system_block_summary_registry,
)
from advanced_final_delivery.final_delivery_operator_handover import (
    build_final_delivery_operator_handover_registry,
)
from advanced_final_delivery.final_delivery_report_builder import (
    build_final_delivery_phase_map_markdown_report,
    build_final_operator_handover_markdown_report,
)
from reports.report_builder import (
    build_final_operator_handover_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_delivery_profile()

    df_map, s_map = build_final_delivery_phase_map_registry(profile)
    df_mvp, s_mvp = build_final_delivery_phase_1_100_mvp_summary_registry(profile)
    df_adv, s_adv = build_final_delivery_phase_101_160_advanced_summary_registry(profile)
    df_bt, s_bt = build_final_delivery_backtest_block_summary_registry(profile)
    df_port, s_port = build_final_delivery_portfolio_block_summary_registry(profile)
    df_sys, s_sys = build_final_delivery_full_system_block_summary_registry(profile)
    df_hand, s_hand = build_final_delivery_operator_handover_registry(profile)

    if "--no-save" not in sys.argv and settings.final_delivery_save_reports:
        data_lake.save_final_delivery_phase_map_registry(df_map, s_map)
        data_lake.save_final_delivery_phase_1_100_mvp_summary_registry(df_mvp, s_mvp)
        data_lake.save_final_delivery_phase_101_160_advanced_summary_registry(df_adv, s_adv)
        data_lake.save_final_delivery_backtest_block_summary_registry(df_bt, s_bt)
        data_lake.save_final_delivery_portfolio_block_summary_registry(df_port, s_port)
        data_lake.save_final_delivery_full_system_block_summary_registry(df_sys, s_sys)
        data_lake.save_final_delivery_operator_handover_registry(df_hand, s_hand)

    out_dir = Path("reports/output/advanced_final_delivery")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_map = build_final_delivery_phase_map_markdown_report(s_map, df_map)
    md_hand = build_final_operator_handover_markdown_report(s_hand, df_hand)
    txt_hand = build_final_operator_handover_text_report(s_hand, df_hand)

    if "--no-save" not in sys.argv:
        with open(out_dir / "phase_map.md", "w", encoding="utf-8") as f:
            f.write(md_map)
        with open(out_dir / "operator_handover.md", "w", encoding="utf-8") as f:
            f.write(md_hand)
        with open(out_dir / "operator_handover.txt", "w", encoding="utf-8") as f:
            f.write(txt_hand)

    print("=" * 70)
    print("PHASE 160: FINAL DELIVERY PHASE SUMMARIES & HANDOVER INITIALIZED")
    print("=" * 70)
    print(f"Total Blocks: {s_map['total_blocks']} | Handover Rules: {s_hand['handover_item_count']}")
    print(f"Status: {s_map['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
