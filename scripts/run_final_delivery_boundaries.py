# -*- coding: utf-8 -*-
"""Phase 160: Run Final Delivery Boundaries Script.

Builds and persists no-go, go, safety, non-production, dry-run, no-live, no-broker,
no-investment-advice, no-prediction, no-deployment, no-scraping boundaries, and forbidden column policies.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_delivery.final_delivery_config import (
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_no_go_boundaries import (
    build_final_delivery_no_go_boundary_registry,
)
from advanced_final_delivery.final_delivery_go_boundaries import (
    build_final_delivery_go_boundary_registry,
)
from advanced_final_delivery.final_delivery_safety_boundaries import (
    build_final_delivery_safety_boundary_registry,
)
from advanced_final_delivery.final_delivery_forbidden_column_policies import (
    build_final_delivery_forbidden_column_policy_registry,
)
from advanced_final_delivery.final_delivery_report_builder import (
    build_final_delivery_boundary_markdown_report,
)
from reports.report_builder import (
    build_final_delivery_boundary_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_delivery_profile()

    df_no_go, s_no_go = build_final_delivery_no_go_boundary_registry(profile)
    df_go, s_go = build_final_delivery_go_boundary_registry(profile)
    df_saf, s_saf = build_final_delivery_safety_boundary_registry(profile)
    df_forb, s_forb = build_final_delivery_forbidden_column_policy_registry(profile)

    if "--no-save" not in sys.argv and settings.final_delivery_save_reports:
        data_lake.save_final_delivery_no_go_boundary_registry(df_no_go, s_no_go)
        data_lake.save_final_delivery_go_boundary_registry(df_go, s_go)
        data_lake.save_final_delivery_safety_boundary_registry(df_saf, s_saf)
        data_lake.save_final_delivery_forbidden_column_policy_registry(df_forb, s_forb)

    out_dir = Path("reports/output/advanced_final_delivery")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_bnd = build_final_delivery_boundary_markdown_report(s_no_go, df_no_go)
    txt_bnd = build_final_delivery_boundary_text_report(s_no_go, df_no_go)

    if "--no-save" not in sys.argv:
        with open(out_dir / "boundaries.md", "w", encoding="utf-8") as f:
            f.write(md_bnd)
        with open(out_dir / "boundaries.txt", "w", encoding="utf-8") as f:
            f.write(txt_bnd)

    print("=" * 70)
    print("PHASE 160: FINAL DELIVERY BOUNDARIES INITIALIZED")
    print("=" * 70)
    print(f"NO-GO Rules: {s_no_go['no_go_rule_count']} | Safe-GO: {s_go['safe_go_action_count']}")
    print(f"Forbidden Columns: {s_forb['forbidden_column_count']}")
    print(f"Status: {s_no_go['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
