import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_feature_grid.feature_grid_config import get_default_feature_grid_profile
from advanced_feature_grid.feature_grid_pipeline import FeatureGridPipeline


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_feature_grid_profile()

    pipeline = FeatureGridPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=project_root,
        profile=profile,
    )
    df_status, summary = pipeline.build_feature_grid_status(save=True)

    print("=" * 70)
    print("PHASE 118: MULTI-WINDOW FEATURE GRID STATUS")
    print("=" * 70)
    for _, row in df_status.iterrows():
        print(f"[{row['status']}] {row['component']}: {row['count']}")
    print("-" * 70)
    print(f"Overall Status         : {summary['status']}")
    print(f"Current Phase          : {summary['current_phase']}")
    print(f"Target Final Phase     : {summary['target_final_phase']}")
    print(f"Next Phase             : {summary['next_phase']}")
    print(f"Non-Signal Enforced    : {summary['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
