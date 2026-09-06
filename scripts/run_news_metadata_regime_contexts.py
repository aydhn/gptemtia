"""Run script: News Metadata Regime Context Registries (Metadata-Only)."""

import sys
from advanced_macro_event_news_regime.macro_event_news_regime_pipeline import (
    MacroEventNewsRegimePipeline,
)
from advanced_macro_event_news_regime.macro_event_news_regime_report_builder import (
    build_news_metadata_context_markdown_report,
)
from reports.report_builder import build_news_metadata_context_text_report


def main():
    print("Executing Phase 132 News Metadata Contexts (Metadata-Only)...")
    pipeline = MacroEventNewsRegimePipeline()
    dfs, summaries = pipeline.build_news_metadata_contexts(save=True)

    print(f"News Topics: {len(dfs['news_topics'])}")
    print(f"News Asset Tags: {len(dfs['news_asset_tags'])}")
    print(f"News Macro Tags: {len(dfs['news_macro_tags'])}")
    print(f"News Event Linkages: {len(dfs['news_event_linkages'])}")
    print(f"News Freshness Placeholders: {len(dfs['news_freshness'])}")
    print(f"Metadata Boundary Rules: {len(dfs['metadata_boundary'])}")

    combined_summary = {
        "total_topic_contexts": len(dfs["news_topics"]),
        "all_non_signal": True,
    }

    txt_rep = build_news_metadata_context_text_report(combined_summary)
    md_rep = build_news_metadata_context_markdown_report(combined_summary, dfs["news_topics"])

    print("\n--- News Metadata Context Summary ---")
    print(txt_rep)
    print("\nSUCCESS: Phase 132 News Metadata Contexts generated and saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
