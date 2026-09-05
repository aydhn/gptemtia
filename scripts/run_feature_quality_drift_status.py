"""Phase 123: Run Feature Quality and Drift Status Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_quality_drift.feature_quality_drift_config import get_default_feature_quality_drift_profile
from advanced_feature_quality_drift.feature_quality_drift_pipeline import FeatureQualityDriftPipeline


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_feature_quality_drift_profile()
    pipeline = FeatureQualityDriftPipeline(data_lake, settings, Path("."), profile)

    df_status, summary = pipeline.build_feature_quality_drift_status(save=False)

    print("=" * 70)
    print("PHASE 123: FEATURE QUALITY AND DRIFT SYSTEM STATUS")
    print("=" * 70)
    print(f"Active Profile       : {summary['active_profile']}")
    print(f"Total Subsystems     : {summary['total_subsystems']}")
    print(f"Passed / Ready Count : {summary['passed_subsystems']}")
    print(f"Current Phase        : {summary['current_phase']}")
    print(f"Target Final Phase   : {summary['target_final_phase']}")
    print(f"Next Phase           : {summary['next_phase']}")
    print(f"Non-Signal Mandate   : {summary['non_signal']}")
    print("-" * 70)
    for _, row in df_status.iterrows():
        print(f"  [{row['subsystem']:<32}] active={row['active']} status={row['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
