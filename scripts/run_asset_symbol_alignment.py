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
    tables, summary = pipeline.build_profiles_domains_universes_symbols(save=True)

    print("=" * 70)
    print("PHASE 119: ASSET UNIVERSE & SYMBOL MAPPING ALIGNMENT")
    print("=" * 70)
    print(f"Total Universes : {summary['universes']['total_universes']}")
    print(f"Total Symbols   : {summary['symbols']['total_mappings']}")
    print(f"Asset Types     : {', '.join(summary['symbols']['asset_types'])}")
    print(f"Non-Signal      : True")
    print(f"Status          : {summary['symbols']['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
