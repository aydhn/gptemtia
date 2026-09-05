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
    print("PHASE 119: CROSS-ASSET ALIGNMENT HEALTH CHECK")
    print("=" * 70)
    print(f"Health Status          : {summary['health_check']['health_status']}")
    print(f"Total Components       : {summary['health_check']['total_components']}")
    print(f"Healthy Components     : {summary['health_check']['healthy_components']}")
    print(f"Unhealthy Components   : {summary['health_check']['unhealthy_components']}")
    print(f"Prior Phases Healthy   : {summary['health_check']['prior_phases_healthy']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
