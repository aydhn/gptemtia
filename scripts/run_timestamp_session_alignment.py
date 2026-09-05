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
    tables, summary = pipeline.build_namespaces_timestamps_session_contracts(save=True)

    print("=" * 70)
    print("PHASE 119: TIMESTAMP & SESSION CALENDAR ALIGNMENT")
    print("=" * 70)
    print(f"Timestamp Contracts : {summary['timestamps']['total_contracts']}")
    print(f"Session Policies    : {summary['sessions']['total_policies']}")
    print(f"Namespaces Defined  : {summary['namespaces']['total_features']}")
    print(f"UTC Standardization : Enforced")
    print(f"Status              : {summary['timestamps']['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
