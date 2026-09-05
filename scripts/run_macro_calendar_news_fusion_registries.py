import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_fusion.macro_calendar_fusion import get_macro_calendar_fusion_summary
from advanced_feature_fusion.macro_news_fusion import get_macro_news_fusion_summary
from advanced_feature_fusion.calendar_news_fusion import get_calendar_news_fusion_summary
from advanced_feature_fusion.cross_domain_context_fusion import get_cross_domain_context_fusion_summary


def main():
    data_lake = DataLake()

    mc_summary = get_macro_calendar_fusion_summary()
    mn_summary = get_macro_news_fusion_summary()
    cn_summary = get_calendar_news_fusion_summary()
    cd_summary = get_cross_domain_context_fusion_summary()

    cross_fusion_registry = {
        "macro_calendar": mc_summary,
        "macro_news": mn_summary,
        "calendar_news": cn_summary,
        "cross_domain": cd_summary,
    }

    data_lake.save_macro_calendar_news_fusion_registries(cross_fusion_registry)

    print("=" * 70)
    print("PHASE 120: MACRO / CALENDAR / NEWS CROSS FUSION REGISTRIES")
    print("=" * 70)
    print(f"Macro-Calendar Fusion : {mc_summary['fusion_type']} (backward={mc_summary['join_direction']})")
    print(f"Macro-News Fusion     : {mn_summary['fusion_type']} (metadata_only={mn_summary['strictly_metadata_only']})")
    print(f"Calendar-News Fusion  : {cn_summary['fusion_type']} (policy={cn_summary['policy']})")
    print(f"Cross-Domain Engine   : {cd_summary['engine']}")
    print(f"Zero Signals Mandate  : {cd_summary['is_signal'] is False}")
    print("=" * 70)


if __name__ == "__main__":
    main()
