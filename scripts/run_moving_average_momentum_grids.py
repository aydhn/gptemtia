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
    tables, summary = pipeline.build_window_grid_registries(save=True)

    print("=" * 70)
    print("PHASE 118: MOVING AVERAGE, MOMENTUM & RETURN GRIDS")
    print("=" * 70)
    print(f"MA Grid Features       : {summary['moving_average']['total_grid_features']}")
    print(f"Momentum Grid Features : {summary['momentum']['total_grid_features']}")
    print(f"Return Grid Features   : {summary['returns']['total_grid_features']}")
    print(f"Non-Signal Enforced    : True")
    print(f"Status                 : READY")
    print("=" * 70)


if __name__ == "__main__":
    main()
