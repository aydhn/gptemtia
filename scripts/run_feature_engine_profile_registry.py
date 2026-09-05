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

    tables, summary = pipeline.build_profiles_domains_contracts(save=True)

    print("=" * 70)
    print("PHASE 116: FEATURE ENGINE PROFILE & DOMAIN REGISTRY")
    print("=" * 70)
    print(f"Active Profile : {summary['profiles']['active_profile']}")
    print(f"Total Profiles : {summary['profiles']['total_profiles']}")
    print(f"Total Domains  : {summary['domains']['total_domains']}")
    print(f"Total Contracts: {summary['input_contracts']['total_contracts']}")
    print(f"Non-Signal     : {summary['profiles']['all_non_signal']}")
    print("-" * 70)
    print("Profiles:")
    for _, row in tables["profiles"].iterrows():
        print(f" - {row['profile_name']:<40} : phase {row['current_phase']} -> {row['target_final_phase']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
