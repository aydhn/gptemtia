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
    tables, summary = pipeline.build_health_validation_safety_handoff(save=True)

    print("=" * 70)
    print("PHASE 118: MULTI-WINDOW FEATURE GRID HEALTH CHECK")
    print("=" * 70)
    print(f"Health Status          : {summary['health']['health_status']}")
    print(f"Total Components       : {summary['health']['total_components']}")
    print(f"Healthy Components     : {summary['health']['healthy_components']}")
    print(f"All Healthy            : {summary['health']['all_healthy']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
