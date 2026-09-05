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
    tables, summary = pipeline.run_feature_grid_computation_rehearsal(save=True)

    print("=" * 70)
    print("PHASE 118: FEATURE GRID COMPUTATION REHEARSAL SUITE")
    print("=" * 70)
    print(f"Total Rehearsals       : {summary['rehearsal']['total_rehearsals']}")
    print(f"All Rehearsals Passed  : {summary['rehearsal']['all_passed']}")
    print(f"In-Place Mutation Free : {summary['rehearsal']['no_mutation_guaranteed']}")
    print(f"Features Generated     : {summary['rehearsal']['total_features_generated']}")
    print(f"Status                 : {summary['rehearsal']['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
