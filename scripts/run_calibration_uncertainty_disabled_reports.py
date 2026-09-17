# -*- coding: utf-8 -*-
"""Phase 141: Run Calibration & Uncertainty Disabled Guarantees Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_calibration_uncertainty.calibration_execution_disabled import (
    build_calibration_execution_disabled_report,
    summarize_calibration_execution_disabled,
)
from advanced_calibration_uncertainty.calibration_fit_disabled import (
    build_calibration_fit_disabled_report,
    summarize_calibration_fit_disabled,
)
from advanced_calibration_uncertainty.calibration_transform_disabled import (
    build_calibration_transform_disabled_report,
    summarize_calibration_transform_disabled,
)
from advanced_calibration_uncertainty.probability_prediction_disabled import (
    build_probability_prediction_disabled_report,
    summarize_probability_prediction_disabled,
)
from advanced_calibration_uncertainty.uncertainty_execution_disabled import (
    build_uncertainty_execution_disabled_report,
    summarize_uncertainty_execution_disabled,
)
from reports.report_builder import ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    df_exec, s_exec = build_calibration_execution_disabled_report()
    data_lake.save_calibration_execution_disabled_registry(df_exec, s_exec)

    df_fit, s_fit = build_calibration_fit_disabled_report()
    data_lake.save_calibration_fit_disabled_registry(df_fit, s_fit)

    df_tr, s_tr = build_calibration_transform_disabled_report()
    data_lake.save_calibration_transform_disabled_registry(df_tr, s_tr)

    df_pred, s_pred = build_probability_prediction_disabled_report()
    data_lake.save_probability_prediction_disabled_registry(df_pred, s_pred)

    df_uexec, s_uexec = build_uncertainty_execution_disabled_report()
    data_lake.save_uncertainty_execution_disabled_registry(df_uexec, s_uexec)

    print("=" * 70)
    print("PHASE 141: CALIBRATION & UNCERTAINTY DISABLED GUARANTEES")
    print("=" * 70)
    print(ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Calibration Exec Disabled : {s_exec.get('all_disabled', True)}")
    print(f"Calibration Fit Disabled  : {s_fit.get('all_disabled', True)}")
    print(f"Calibration Transform Dis.: {s_tr.get('all_disabled', True)}")
    print(f"Probability Pred. Disabled: {s_pred.get('all_disabled', True)}")
    print(f"Uncertainty Exec. Disabled: {s_uexec.get('all_disabled', True)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
