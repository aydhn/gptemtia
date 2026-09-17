# -*- coding: utf-8 -*-
"""Phase 160: Run Final Delivery Validation Report Script.

Builds and persists final delivery validation report and safety boundary reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_delivery.final_delivery_config import (
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_manifest import (
    build_final_delivery_manifest,
)
from advanced_final_delivery.final_delivery_validation import (
    build_final_delivery_validation_report,
)
from advanced_final_delivery.final_delivery_safety_boundary import (
    build_final_delivery_safety_boundary,
)
from advanced_final_delivery.final_delivery_report_builder import (
    build_final_delivery_validation_markdown_report,
    build_final_delivery_safety_markdown_report,
)
from reports.report_builder import (
    build_final_delivery_validation_text_report,
    build_final_delivery_safety_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_delivery_profile()

    df_mnf, s_mnf = build_final_delivery_manifest(profile)
    tables = {"manifest": df_mnf, "summary": s_mnf}

    df_val, s_val = build_final_delivery_validation_report(tables, profile)
    df_saf, s_saf = build_final_delivery_safety_boundary(profile)

    if "--no-save" not in sys.argv and settings.final_delivery_save_reports:
        data_lake.save_final_delivery_validation_report(df_val, s_val)
        data_lake.save_final_delivery_safety_boundary(df_saf, s_saf)

    out_dir = Path("reports/output/advanced_final_delivery")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_val = build_final_delivery_validation_markdown_report(s_val, df_val)
    txt_val = build_final_delivery_validation_text_report(s_val, df_val)
    md_saf = build_final_delivery_safety_markdown_report(s_saf, df_saf)
    txt_saf = build_final_delivery_safety_text_report(s_saf, df_saf)

    if "--no-save" not in sys.argv:
        with open(out_dir / "validation.md", "w", encoding="utf-8") as f:
            f.write(md_val)
        with open(out_dir / "validation.txt", "w", encoding="utf-8") as f:
            f.write(txt_val)
        with open(out_dir / "safety.md", "w", encoding="utf-8") as f:
            f.write(md_saf)
        with open(out_dir / "safety.txt", "w", encoding="utf-8") as f:
            f.write(txt_saf)

    print("=" * 70)
    print("PHASE 160: FINAL DELIVERY VALIDATION & SAFETY INITIALIZED")
    print("=" * 70)
    print(f"Validation: {s_val['validation_status']} | Checks Passed: {s_val['passed_checks']}/{s_val['total_checks']}")
    print(f"Safety: {s_saf['safety_status']} | Total Rules: {s_saf['total_rules']}")
    print(f"Status: {s_val['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
