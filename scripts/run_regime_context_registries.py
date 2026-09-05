"""Phase 126: Run Regime Environmental Context Registries Script.

Generates macro, event, metadata-only news, and cross-asset context registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_foundation.regime_foundation_config import (
    get_default_regime_foundation_profile,
)
from advanced_regime_foundation.macro_regime_context import (
    build_macro_regime_context_registry,
)
from advanced_regime_foundation.event_regime_context import (
    build_event_regime_context_registry,
)
from advanced_regime_foundation.news_metadata_regime_context import (
    build_news_metadata_regime_context_registry,
)
from advanced_regime_foundation.cross_asset_regime_context import (
    build_cross_asset_regime_context_registry,
)
from advanced_regime_foundation.regime_foundation_report_builder import (
    build_regime_context_markdown_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_regime_foundation_profile()

    df_macro, s_macro = build_macro_regime_context_registry(profile)
    df_event, s_event = build_event_regime_context_registry(profile)
    df_news, s_news = build_news_metadata_regime_context_registry(profile)
    df_cross, s_cross = build_cross_asset_regime_context_registry(profile)

    data_lake.save_macro_regime_context_registry(df_macro, s_macro)
    data_lake.save_event_regime_context_registry(df_event, s_event)
    data_lake.save_news_metadata_regime_context_registry(df_news, s_news)
    data_lake.save_cross_asset_regime_context_registry(df_cross, s_cross)

    md_macro = build_regime_context_markdown_report({"context_type": "Macro Context", **s_macro}, df_macro)
    md_event = build_regime_context_markdown_report({"context_type": "Event Context", **s_event}, df_event)
    md_news = build_regime_context_markdown_report({"context_type": "News Metadata Context", **s_news}, df_news)
    md_cross = build_regime_context_markdown_report({"context_type": "Cross-Asset Context", **s_cross}, df_cross)

    out_dir = Path("reports/output/advanced_regime_foundation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "macro_context.md", "w", encoding="utf-8") as f:
        f.write(md_macro)
    with open(out_dir / "event_context.md", "w", encoding="utf-8") as f:
        f.write(md_event)
    with open(out_dir / "news_metadata_context.md", "w", encoding="utf-8") as f:
        f.write(md_news)
    with open(out_dir / "cross_asset_context.md", "w", encoding="utf-8") as f:
        f.write(md_cross)

    print("=" * 70)
    print("PHASE 126: ENVIRONMENTAL CONTEXT REGISTRIES")
    print("=" * 70)
    print(f"Macro Contexts : {s_macro['total_contexts']}")
    print(f"Event Contexts : {s_event['total_contexts']}")
    print(f"News Contexts  : {s_news['total_contexts']}")
    print(f"Cross-Asset    : {s_cross['total_contexts']}")
    print(f"Metadata Only  : {s_news['all_metadata_only']}")
    print(f"Non-Signal     : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
