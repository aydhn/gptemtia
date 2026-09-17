# -*- coding: utf-8 -*-
"""Phase 160: Run Final Delivery Health Check Script.

Builds and persists the comprehensive health check for all system components.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_delivery.final_delivery_config import (
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_health import (
    build_final_delivery_health_check,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_delivery_profile()
    project_root = Path(__file__).resolve().parent.parent

    df_hlth, s_hlth = build_final_delivery_health_check(project_root, profile)

    if "--no-save" not in sys.argv and settings.final_delivery_save_reports:
        data_lake.save_final_delivery_health_check(df_hlth, s_hlth)

    out_dir = Path("reports/output/advanced_final_delivery")
    out_dir.mkdir(parents=True, exist_ok=True)

    if "--no-save" not in sys.argv:
        with open(out_dir / "health_check.md", "w", encoding="utf-8") as f:
            f.write(f"# Phase 160: Health Check\n\nOverall Status: {s_hlth['overall_status']}\nTotal Checks: {s_hlth['total_checks']}\n\n{df_hlth.to_markdown(index=False)}")
        with open(out_dir / "health_check.txt", "w", encoding="utf-8") as f:
            f.write(f"Overall Status: {s_hlth['overall_status']}\nTotal Checks: {s_hlth['total_checks']}\nHealthy Checks: {s_hlth['healthy_checks']}")

    print("=" * 70)
    print("PHASE 160: FINAL DELIVERY HEALTH CHECK INITIALIZED")
    print("=" * 70)
    print(f"Overall Health: {s_hlth['overall_status']}")
    print(f"Passed Checks: {s_hlth['healthy_checks']}/{s_hlth['total_checks']}")
    print(f"Status: {s_hlth['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
