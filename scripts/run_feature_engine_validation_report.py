import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_engine_pipeline import FeatureEnginePipeline


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_feature_engine_profile()

    pipeline = FeatureEnginePipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=project_root,
        profile=profile,
    )

    tables, summary = pipeline.build_validation_quality_safety(save=True)
    val_sum = summary["validation_report"]
    safe_sum = summary["safety"]
    val_df = tables["validation_report"]

    print("=" * 70)
    print("PHASE 116: FEATURE ENGINE VALIDATION & SAFETY REPORT")
    print("=" * 70)
    print(f"Validation Status       : {val_sum['validation_status']}")
    print(f"Total Checks            : {val_sum['total_checks']}")
    print(f"Passed Checks           : {val_sum['passed_checks']}")
    print(f"Forbidden Claims Found  : {val_sum['forbidden_claims_found']}")
    print(f"Safety Status           : {safe_sum['safety_status']}")
    print(f"Total No-Go Enforced    : {safe_sum['total_no_go_rules']}")
    print(f"Total Safe-Go Permitted : {safe_sum['total_safe_go_rules']}")
    print(f"Non-Signal              : {val_sum['non_signal']}")
    print("-" * 70)
    for _, row in val_df.iterrows():
        print(f" - [{ 'PASS' if row['valid'] else 'FAIL' }] {row['check']:<40} : {row['details']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
