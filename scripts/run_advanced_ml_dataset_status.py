"""Phase 137: Run Advanced ML Dataset Status Report Script.

Prints high-level operational status of Phase 137 dataset contract registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    get_default_advanced_ml_dataset_profile,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_pipeline import (
    AdvancedMlDatasetPipeline,
)
from reports.report_builder import ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_advanced_ml_dataset_profile()
    pipeline = AdvancedMlDatasetPipeline(data_lake=data_lake, profile=profile)

    df_status, s_status = pipeline.build_advanced_ml_dataset_status(save=False)

    print("=" * 70)
    print("PHASE 137: ADVANCED ML DATASET REGISTRY STATUS")
    print("=" * 70)
    print(ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Pipeline Status       : {s_status['pipeline_status']}")
    print(f"Current Phase         : {s_status['current_phase']}")
    print(f"Next Phase            : {s_status['next_phase']}")
    print(f"Dataset Materialized  : False")
    print(f"Model Training        : Blocked")
    print(f"Prediction / Signals  : Prohibited")
    print(f"Non-Signal Maintained : {s_status['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
