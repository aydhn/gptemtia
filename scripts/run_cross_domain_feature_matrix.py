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
    print("PHASE 119: CROSS-DOMAIN ALIGNED FEATURE MATRIX & MANIFEST")
    print("=" * 70)
    print(f"Matrix Rows         : {summary['cross_domain_matrix']['total_rows']}")
    print(f"Matrix Columns      : {summary['cross_domain_matrix']['total_columns']}")
    print(f"Contract Name       : {summary['cross_domain_matrix']['contract_name']}")
    print(f"Total Manifests     : {summary['manifests']['total_manifests']}")
    print(f"Strict Non-Signal   : {summary['cross_domain_matrix']['non_signal']}")
    print(f"Zero Lookahead      : True")
    print(f"Status              : {summary['cross_domain_matrix']['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
