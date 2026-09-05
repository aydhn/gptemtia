import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_cross_asset_alignment.cross_asset_alignment_config import get_default_cross_asset_alignment_profile
from advanced_cross_asset_alignment.cross_asset_alignment_pipeline import CrossAssetAlignmentPipeline


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_cross_asset_alignment_profile()

    pipeline = CrossAssetAlignmentPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=project_root,
        profile=profile,
    )
    tables, summary = pipeline.build_governance_validation_health_safety(save=True)

    print("=" * 70)
    print("PHASE 119: CROSS-ASSET ALIGNMENT VALIDATION REPORT")
    print("=" * 70)
    print(f"Validation Status      : {summary['validation_report']['validation_status']}")
    print(f"Total Checks           : {summary['validation_report']['total_checks']}")
    print(f"Passed Checks          : {summary['validation_report']['passed_checks']}")
    print(f"Failed Checks          : {summary['validation_report']['failed_checks']}")
    print(f"Safety Status          : {summary['safety_boundary']['safety_status']}")
    print(f"NO-GO Rules Enforced   : {summary['safety_boundary']['no_go_count']}")
    print(f"SAFE-GO Rules Enabled  : {summary['safety_boundary']['safe_go_count']}")
    print(f"Phase 120 Handoff      : {summary['phase_120_handoff']['handoff_status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
