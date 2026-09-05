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
    p_tables, p_summary = pipeline.build_profiles_domains_contracts(save=True)
    c_tables, c_summary = pipeline.build_parameter_naming_schema_policies(save=True)

    print("=" * 70)
    print("PHASE 118: WINDOW GRID CONTRACTS & LOOKAHEAD GUARD REGISTRY")
    print("=" * 70)
    print(f"Total Contracts        : {p_summary['window_contracts']['total_contracts']}")
    print(f"Warmup Policies        : {c_summary['warmup_nan']['total_policies']}")
    print(f"No-Lookahead Rules     : {c_summary['no_lookahead']['total_guard_rules']}")
    print(f"Duplicate Checks       : {c_summary['duplicates']['total_checks']}")
    print(f"Status                 : {p_summary['window_contracts']['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
