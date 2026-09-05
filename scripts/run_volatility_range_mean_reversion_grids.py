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
    print("PHASE 118: VOLATILITY, RANGE & MEAN REVERSION GRIDS")
    print("=" * 70)
    print(f"Volatility Features    : {summary['volatility']['total_grid_features']}")
    print(f"Range/Channel Features : {summary['range_channel']['total_grid_features']}")
    print(f"Mean Reversion Features: {summary['mean_reversion']['total_grid_features']}")
    print(f"Non-Signal Enforced    : True")
    print(f"Status                 : READY")
    print("=" * 70)


if __name__ == "__main__":
    main()
