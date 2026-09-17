# -*- coding: utf-8 -*-
"""Phase 160: Run Final 160-Phase Completion Report Script.

Builds and persists the official 160-phase completion report and final summary reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_delivery.final_delivery_config import (
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_160_phase_completion import (
    build_final_160_phase_completion_report,
)
from advanced_final_delivery.final_delivery_phase_map import (
    build_final_delivery_phase_map_registry,
)
from advanced_final_delivery.final_delivery_operator_handover import (
    build_final_delivery_operator_handover_registry,
)
from advanced_final_delivery.final_delivery_manual_review_evidence import (
    build_final_delivery_manual_review_evidence_registry,
)
from advanced_final_delivery.final_delivery_safety_evidence import (
    build_final_delivery_safety_evidence_registry,
)
from advanced_final_delivery.final_delivery_package_contracts import (
    build_final_delivery_package_contract_registry,
)
from advanced_final_delivery.final_delivery_report_builder import (
    build_final_160_phase_completion_markdown_report,
    build_final_system_summary_markdown_report,
    build_final_operator_handover_markdown_report,
)
from reports.report_builder import (
    build_final_160_phase_completion_text_report,
    build_final_system_summary_text_report,
    build_final_operator_handover_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_delivery_profile()

    df_cmp, s_cmp = build_final_160_phase_completion_report(profile)
    df_map, s_map = build_final_delivery_phase_map_registry(profile)
    df_pkg, s_pkg = build_final_delivery_package_contract_registry(profile)
    df_man, s_man = build_final_delivery_manual_review_evidence_registry(profile)
    df_saf, s_saf = build_final_delivery_safety_evidence_registry(profile)
    df_hnd, s_hnd = build_final_delivery_operator_handover_registry(profile)

    if "--no-save" not in sys.argv and settings.final_delivery_save_reports:
        data_lake.save_final_160_phase_completion_report(df_cmp, s_cmp)
        data_lake.save_final_system_summary_report(df_map, s_map)
        data_lake.save_final_local_offline_package_summary_report(df_pkg, s_pkg)
        data_lake.save_final_manual_review_summary_report(df_man, s_man)
        data_lake.save_final_no_live_no_broker_safety_summary_report(df_saf, s_saf)
        data_lake.save_final_operator_handover_report(df_hnd, s_hnd)

    out_dir = Path("reports/output/advanced_final_delivery")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_cmp = build_final_160_phase_completion_markdown_report(s_cmp, df_cmp)
    txt_cmp = build_final_160_phase_completion_text_report(s_cmp, df_cmp)
    md_sys = build_final_system_summary_markdown_report(s_cmp, df_map)
    txt_sys = build_final_system_summary_text_report(s_cmp, df_map)
    md_hnd = build_final_operator_handover_markdown_report(s_hnd, df_hnd)
    txt_hnd = build_final_operator_handover_text_report(s_hnd, df_hnd)

    if "--no-save" not in sys.argv:
        with open(out_dir / "160_phase_completion.md", "w", encoding="utf-8") as f:
            f.write(md_cmp)
        with open(out_dir / "160_phase_completion.txt", "w", encoding="utf-8") as f:
            f.write(txt_cmp)
        with open(out_dir / "system_summary.md", "w", encoding="utf-8") as f:
            f.write(md_sys)
        with open(out_dir / "system_summary.txt", "w", encoding="utf-8") as f:
            f.write(txt_sys)
        with open(out_dir / "final_operator_handover.md", "w", encoding="utf-8") as f:
            f.write(md_hnd)
        with open(out_dir / "final_operator_handover.txt", "w", encoding="utf-8") as f:
            f.write(txt_hnd)

    print("=" * 70)
    print("PHASE 160: 160-PHASE PLAN OFFICIAL COMPLETION REPORT INITIALIZED")
    print("=" * 70)
    print(f"Plan Status: {s_cmp['plan_status']}")
    print(f"MVP Block: {s_cmp['mvp_block_status']} | Advanced Block: {s_cmp['advanced_block_status']}")
    print(f"Declaration: {s_cmp['declaration'][:80]}...")
    print(f"Status: {s_cmp['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
