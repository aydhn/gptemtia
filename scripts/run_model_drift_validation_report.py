# -*- coding: utf-8 -*-
"""Phase 142: Run Model Drift Validation Report Script."""

import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_model_drift_monitoring.model_drift_validation import run_model_drift_validation
from reports.report_builder import ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    val_res = run_model_drift_validation()
    df_val = pd.DataFrame(val_res["results"])
    data_lake.save_model_drift_validation_report(df_val, val_res)

    print("=" * 70)
    print("PHASE 142: MODEL DRIFT VALIDATION REPORT")
    print("=" * 70)
    print(ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Validation Status      : {val_res.get('validation_status', 'UNKNOWN')}")
    print(f"Total Items Validated  : {val_res.get('total_items_validated', 0)}")
    print(f"Valid Items Count      : {val_res.get('valid_items_count', 0)}")
    print(f"Invalid Items Count    : {val_res.get('invalid_items_count', 0)}")
    print(f"All Valid              : {val_res.get('all_valid', False)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
