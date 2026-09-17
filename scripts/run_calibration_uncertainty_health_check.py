# -*- coding: utf-8 -*-
"""Phase 141: Run Calibration & Uncertainty Health Check & Safety Boundary Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_calibration_uncertainty.calibration_uncertainty_health import (
    build_calibration_uncertainty_health_check,
    summarize_calibration_uncertainty_health,
)
from advanced_calibration_uncertainty.calibration_uncertainty_safety_boundary import (
    build_calibration_uncertainty_safety_boundary,
    summarize_calibration_uncertainty_safety_boundary,
)
from reports.report_builder import ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    df_hlth, s_hlth = build_calibration_uncertainty_health_check()
    data_lake.save_calibration_uncertainty_health_check(df_hlth, s_hlth)

    df_safe, s_safe = build_calibration_uncertainty_safety_boundary()
    data_lake.save_calibration_uncertainty_safety_boundary(df_safe, s_safe)

    print("=" * 70)
    print("PHASE 141: CALIBRATION & UNCERTAINTY HEALTH CHECK & SAFETY BOUNDARY")
    print("=" * 70)
    print(ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Health Checks Total        : {s_hlth.get('total_checks', len(df_hlth))}")
    print(f"Health Status Overall      : {s_hlth.get('status', 'HEALTHY')}")
    print(f"Safety Boundaries Checked  : {s_safe.get('no_go_count', 0) + s_safe.get('safe_go_count', 0)}")
    print(f"All Boundaries Enforced    : {s_safe.get('safety_status', 'ENFORCED') == 'ENFORCED'}")
    print("=" * 70)


if __name__ == "__main__":
    main()
