# -*- coding: utf-8 -*-
"""Phase 141: Run Calibration & Uncertainty Validation & Handoff Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_calibration_uncertainty.calibration_uncertainty_validation import (
    build_calibration_uncertainty_validation_report,
)
from advanced_calibration_uncertainty.phase_142_handoff import (
    build_phase_142_model_drift_monitoring_handoff_report,
    summarize_phase_142_handoff,
)
from reports.report_builder import ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    df_val, s_val = build_calibration_uncertainty_validation_report()
    data_lake.save_calibration_uncertainty_validation_report(df_val, s_val)

    df_hnd, s_hnd = build_phase_142_model_drift_monitoring_handoff_report()
    data_lake.save_phase_142_handoff(df_hnd, s_hnd)

    print("=" * 70)
    print("PHASE 141: CALIBRATION & UNCERTAINTY VALIDATION & PHASE 142 HANDOFF")
    print("=" * 70)
    print(ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Validation Checks Total    : {s_val.get('total_checks', len(df_val))}")
    print(f"Validation Overall Status  : {s_val.get('validation_status', 'VALID')}")
    print(f"Handoff Target Phase       : {s_hnd.get('next_phase', 142)}")
    print(f"Handoff Target Name        : {s_hnd.get('next_phase_name', 'Model Drift Monitoring and Data/Feature Drift Linkage')}")
    print(f"Handoff Prerequisites Met  : {s_hnd.get('all_prerequisites_met', True)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
