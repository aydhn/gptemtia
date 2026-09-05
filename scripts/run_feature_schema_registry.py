import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_schema_registry import build_feature_schema_registry
from advanced_feature_engine.factor_schema_registry import build_factor_schema_registry


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_feature_engine_profile()

    fs_df, fs_sum = build_feature_schema_registry(profile)
    data_lake.save_feature_schema_registry(fs_df, fs_sum)

    fact_df, fact_sum = build_factor_schema_registry(profile)
    data_lake.save_factor_schema_registry(fact_df, fact_sum)

    print("=" * 70)
    print("PHASE 116: CANONICAL FEATURE & FACTOR SCHEMA REGISTRY")
    print("=" * 70)
    print(f"Total Feature Schemas: {fs_sum['total_schemas']}")
    print(f"Total Factor Schemas : {fact_sum['total_factor_schemas']}")
    print(f"Feature Types        : {', '.join(fs_sum['feature_types'])}")
    print(f"Factor Types         : {', '.join(fact_sum['factor_types'])}")
    print(f"Non-Signal           : {fs_sum['all_non_signal'] and fact_sum['all_non_signal']}")
    print("-" * 70)
    print("Feature Schemas (sample):")
    for _, row in fs_df.head(8).iterrows():
        print(f" - {row['feature_name']:<25} | Type: {row['feature_type']:<30} | Out: {row['output_field']}")
    print("-" * 70)
    print("Factor Schemas:")
    for _, row in fact_df.iterrows():
        print(f" - {row['factor_name']:<35} | Type: {row['factor_type']:<22} | Owner: {row['future_phase_owner']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
