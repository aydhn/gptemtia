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
    tables, summary = pipeline.build_parameter_naming_schema_policies(save=True)

    print("=" * 70)
    print("PHASE 118: INDICATOR PARAMETER GRIDS & NAMING REGISTRY")
    print("=" * 70)
    print(f"Total Parameter Grids  : {summary['parameter_grids']['total_grids']}")
    print(f"Expected Features      : {summary['parameter_grids']['total_expected_features']}")
    print(f"Naming Conventions     : {summary['naming']['total_rules']}")
    print(f"Output Schemas         : {summary['output_schema']['total_schemas']}")
    print(f"Status                 : {summary['parameter_grids']['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
