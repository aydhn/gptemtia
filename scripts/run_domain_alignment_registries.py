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
    tables, summary = pipeline.build_domain_alignments(save=True)

    print("=" * 70)
    print("PHASE 119: 9 CROSS-DOMAIN ALIGNMENT REGISTRIES")
    print("=" * 70)
    print(f"FX - Commodity Alignments : {summary['fx_commodity']['total_alignments']}")
    print(f"FX - Macro Alignments     : {summary['fx_macro']['total_alignments']}")
    print(f"FX - Calendar Alignments  : {summary['fx_calendar']['total_alignments']}")
    print(f"FX - News Tag Alignments  : {summary['fx_news']['total_alignments']}")
    print(f"Cmd - Macro Alignments    : {summary['commodity_macro']['total_alignments']}")
    print(f"Cmd - Calendar Alignments : {summary['commodity_calendar']['total_alignments']}")
    print(f"Cmd - News Tag Alignments : {summary['commodity_news']['total_alignments']}")
    print(f"Macro - Calendar Mappings : {summary['macro_calendar']['total_alignments']}")
    print(f"Calendar - News Mappings  : {summary['calendar_news']['total_alignments']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
