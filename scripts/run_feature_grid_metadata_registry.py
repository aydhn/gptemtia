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
    tables, summary = pipeline.build_metadata_dependency_quality(save=True)
    w_tables, w_summary = pipeline.build_window_grid_registries(save=True)

    print("=" * 70)
    print("PHASE 118: FEATURE GRID METADATA & DEPENDENCY REGISTRY")
    print("=" * 70)
    print(f"Metadata Entries       : {summary['metadata']['total_metadata_entries']}")
    print(f"Dependencies           : {summary['dependencies']['total_dependencies']}")
    print(f"Validation Rules       : {summary['validation_rules']['total_rules']}")
    print(f"Quality Handoff Items  : {summary['quality_handoff']['total_handoff_items']}")
    print(f"Quote Placeholders     : {len(w_tables['quote_placeholders'])}")
    print(f"Macro Placeholders     : {len(w_tables['macro_placeholders'])}")
    print(f"Calendar Placeholders  : {len(w_tables['calendar_placeholders'])}")
    print(f"News Placeholders      : {len(w_tables['news_placeholders'])}")
    print(f"Status                 : {summary['metadata']['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
