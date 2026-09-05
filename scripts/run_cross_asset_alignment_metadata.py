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
    tables, summary = pipeline.build_matrices_manifests_metadata(save=True)

    print("=" * 70)
    print("PHASE 119: CROSS-ASSET FEATURE METADATA REGISTRY")
    print("=" * 70)
    print(f"Total Features       : {summary['feature_metadata']['total_features']}")
    print(f"Domains Covered      : {', '.join(summary['feature_metadata']['domains'])}")
    print(f"Strict Non-Signal    : True")
    print(f"Target / Prediction  : None")
    print(f"Status               : {summary['feature_metadata']['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
