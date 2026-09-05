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

    status_df, overall_sum = pipeline.build_feature_engine_status(save=True)

    print("=" * 70)
    print("PHASE 116: ADVANCED INDICATOR/FEATURE/FACTOR ENGINE STATUS")
    print("=" * 70)
    print(f"Current Phase      : {overall_sum['current_phase']}")
    print(f"Phase Name         : {overall_sum['phase_name']}")
    print(f"Target Final Phase : {overall_sum['target_final_phase']}")
    print(f"Next Phase         : {overall_sum['next_phase']}")
    print(f"All Ready          : {overall_sum['all_subsystems_ready']}")
    print(f"Total Subsystems   : {overall_sum['total_subsystems']}")
    print(f"Non-Signal         : {overall_sum['non_signal']}")
    print("-" * 70)
    for _, row in status_df.iterrows():
        print(f" - {row['component']:<30} : {row['status']} ({row['records']} records)")
    print("=" * 70)


if __name__ == "__main__":
    main()
