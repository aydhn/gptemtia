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

    results, summary = pipeline.run_basic_computation_rehearsal(save=True)
    df = results["rehearsal_output"]

    print("=" * 70)
    print("PHASE 116: BASIC FEATURE COMPUTATION REHEARSAL")
    print("=" * 70)
    print(f"Features Computed   : {summary['features_computed_count']}")
    print(f"Validation Passed   : {summary['validation_passed']}")
    print(f"Input Mutation Free : {summary['input_mutation_free']}")
    print(f"Non-Signal          : {summary['non_signal']}")
    print(f"Output DataFrame    : {df.shape[0]} rows x {df.shape[1]} columns")
    print("-" * 70)
    print("Computed Columns:")
    for col in summary["computed_columns"]:
        non_null = int(df[col].notna().sum())
        print(f" - {col:<25} : {non_null}/{len(df)} non-null values")
    print("=" * 70)


if __name__ == "__main__":
    main()
