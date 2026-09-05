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
    result = pipeline.run_full_pipeline(save=True)

    print("=" * 70)
    print("PHASE 119: CROSS-ASSET FEATURE ALIGNMENT STATUS")
    print("=" * 70)
    print(f"Current Phase          : {result['phase']}")
    print(f"Target Final Phase     : {result['target_final_phase']}")
    print(f"Next Phase             : {result['next_phase']}")
    print(f"Active Profile         : {result['profile']}")
    print(f"Pipeline Status        : {result['pipeline_status']}")
    print(f"Tables Generated       : {result['total_tables_generated']}")
    print(f"Strict Non-Signal      : {result['non_signal']}")
    print(f"Future Data Allowed    : {result['future_data_allowed']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
