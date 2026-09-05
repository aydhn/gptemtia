import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_engine_health import (
    build_feature_engine_health_check,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_feature_engine_profile()

    df, summary = build_feature_engine_health_check(project_root, profile)
    data_lake.save_feature_engine_health_check(df, summary)

    print("=" * 70)
    print("PHASE 116: FEATURE ENGINE HEALTH CHECK")
    print("=" * 70)
    print(f"Overall Status : {summary['overall_status']}")
    print(f"Total Checks   : {summary['total_checks']}")
    print(f"Passed Checks  : {summary['passed_checks']}")
    print(f"Failed Checks  : {summary['failed_checks']}")
    print(f"All Passed     : {summary['all_passed']}")
    print("-" * 70)
    for _, row in df.iterrows():
        print(f" - [{row['status']}] {row['check_id']:<40} : {row['description']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
