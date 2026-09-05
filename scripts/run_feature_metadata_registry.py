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

    tables, summary = pipeline.build_metadata_and_windows(save=True)

    print("=" * 70)
    print("PHASE 116: FEATURE METADATA & ROLLING WINDOW CONTRACTS")
    print("=" * 70)
    print(f"Features Registered : {summary['feature_metadata']['total_features_registered']}")
    print(f"Factors Registered  : {summary['factor_metadata']['total_factors_registered']}")
    print(f"Standard Windows    : {summary['rolling_windows']['windows']}")
    print(f"Dependency Edges    : {summary['dependency_graph']['total_edges']}")
    print(f"All Lookahead Guard : {summary['rolling_windows']['all_lookahead_guarded']}")
    print(f"Non-Signal          : {summary['feature_metadata']['non_signal']}")
    print("-" * 70)
    print("Rolling Windows:")
    for _, row in tables["rolling_windows"].iterrows():
        print(f" - Window {row['window_size']:<3} | Warmup: {row['warmup_nan_count']:<3} rows | {row['description']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
