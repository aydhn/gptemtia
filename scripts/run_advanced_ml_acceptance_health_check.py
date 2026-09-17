# -*- coding: utf-8 -*-
"""Phase 145: Run Advanced ML Acceptance Health Check Script.

Verifies the presence and integrity of all Phase 136-145 modules, files, and directories.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    get_default_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_health import (
    build_advanced_ml_acceptance_health_check,
)
from advanced_ml_acceptance.advanced_ml_acceptance_report_builder import (
    _df_to_markdown,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_advanced_ml_acceptance_profile()

    df_hlt, s_hlt = build_advanced_ml_acceptance_health_check(Path("."), profile)
    data_lake.save_advanced_ml_acceptance_health_check(df_hlt, s_hlt)

    out_dir = Path("reports/output/advanced_ml_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "health_check.md", "w", encoding="utf-8") as f:
        f.write("# Phase 145: Advanced ML Health Check Report\n\n")
        f.write(_df_to_markdown(df_hlt))
        f.write("\n")

    print("=" * 70)
    print("PHASE 145: ADVANCED ML HEALTH CHECK")
    print("=" * 70)
    print(f"Total Checks   : {s_hlt['total_checks']}")
    print(f"Healthy Checks : {s_hlt['healthy_checks']}")
    print(f"All Healthy    : {s_hlt['all_healthy']}")
    print(f"Status         : {s_hlt['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
