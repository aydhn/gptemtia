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
    print("PHASE 118: FEATURE GRID VALIDATION & SAFETY REPORT")
    print("=" * 70)
    print(f"Validation Status      : {summary['validation']['validation_status']}")
    print(f"Rules Checked          : {summary['validation']['rules_checked']}")
    print(f"Violations Count       : {summary['validation']['violations_count']}")
    print(f"Safety Status          : {summary['safety']['safety_status']}")
    print(f"No-Go Conditions       : {summary['safety']['total_no_go']}")
    print(f"Safe-Go Conditions     : {summary['safety']['total_safe_go']}")
    print(f"Phase 119 Handoff Items: {summary['phase_119_handoff']['total_handoff_items']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
