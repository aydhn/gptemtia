"""Phase 122: Run Macro, Event, News & Cross-Asset Factor Families Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_factor_metadata.factor_metadata_config import get_default_factor_metadata_profile
from advanced_factor_metadata.macro_context_factor_families import build_macro_context_factor_family_registry
from advanced_factor_metadata.calendar_event_factor_families import build_calendar_event_factor_family_registry
from advanced_factor_metadata.news_attention_factor_families import build_news_attention_factor_family_registry
from advanced_factor_metadata.cross_asset_context_factor_families import build_cross_asset_context_factor_family_registry
from advanced_factor_metadata.regime_prep_factor_placeholders import build_regime_prep_factor_placeholder_registry
from advanced_factor_metadata.composite_factor_placeholders import build_composite_factor_placeholder_registry
from advanced_factor_metadata.factor_metadata_report_builder import build_macro_event_news_factor_markdown_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_factor_metadata_profile()

    df_macro, s_macro = build_macro_context_factor_family_registry(profile)
    df_event, s_event = build_calendar_event_factor_family_registry(profile)
    df_news, s_news = build_news_attention_factor_family_registry(profile)
    df_cross, s_cross = build_cross_asset_context_factor_family_registry(profile)
    df_regime, s_regime = build_regime_prep_factor_placeholder_registry(profile)
    df_comp, s_comp = build_composite_factor_placeholder_registry(profile)

    data_lake.save_macro_context_factor_family_registry(df_macro, s_macro)
    data_lake.save_calendar_event_factor_family_registry(df_event, s_event)
    data_lake.save_news_attention_factor_family_registry(df_news, s_news)
    data_lake.save_cross_asset_context_factor_family_registry(df_cross, s_cross)
    data_lake.save_regime_prep_factor_placeholder_registry(df_regime, s_regime)
    data_lake.save_composite_factor_placeholder_registry(df_comp, s_comp)

    md_report = build_macro_event_news_factor_markdown_report(s_macro, df_macro)
    reports_dir = Path("reports/output/advanced_factor_metadata")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "macro_event_news_factor_families.md", "w", encoding="utf-8") as f:
        f.write(md_report)

    print("=" * 70)
    print("PHASE 122: MACRO, EVENT, NEWS & CROSS-ASSET FACTOR FAMILIES")
    print("=" * 70)
    print(f"Macro Context Factors   : {s_macro['total_factors']}")
    print(f"Calendar Event Factors  : {s_event['total_factors']}")
    print(f"News Attention Factors  : {s_news['total_factors']}")
    print(f"Cross-Asset Context     : {s_cross['total_factors']}")
    print(f"Regime Prep Placeholders: {s_regime['total_factors']}")
    print(f"Composite Placeholders  : {s_comp['total_factors']}")
    print(f"Metadata-Only News      : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
