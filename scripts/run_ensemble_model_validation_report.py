# -*- coding: utf-8 -*-
"""Phase 140: Run Ensemble Model Validation Report Script."""

import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ensemble_model_registry.ensemble_model_validation import (
    build_ensemble_model_validation_report,
    summarize_ensemble_model_validation_report,
)
from reports.report_builder import ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    val_report = build_ensemble_model_validation_report()
    s_val = summarize_ensemble_model_validation_report(val_report)
    df_val = pd.DataFrame([val_report])
    data_lake.save_ensemble_model_validation_report(df_val, s_val)

    print("=" * 70)
    print("PHASE 140: ENSEMBLE MODEL VALIDATION REPORT")
    print("=" * 70)
    print(ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Validation Status   : {s_val['validation_status']}")
    print(f"Readiness Score     : {s_val['readiness_score']}")
    print(f"All Valid           : {s_val['is_valid']}")
    print(f"Non-Signal Verified : {s_val['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
