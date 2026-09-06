"""Run script: Profile and Domain Registry for Phase 132 Macro/Event/News Regime Context Expansion."""

import sys
from advanced_macro_event_news_regime.macro_event_news_regime_pipeline import (
    MacroEventNewsRegimePipeline,
)
from advanced_macro_event_news_regime.macro_event_news_regime_report_builder import (
    build_macro_event_news_regime_profile_markdown_report,
)
from reports.report_builder import build_macro_event_news_regime_text_report


def main():
    print("Executing Phase 132 Macro/Event/News Regime Profile and Domain Registry...")
    pipeline = MacroEventNewsRegimePipeline()
    dfs, summaries = pipeline.build_profiles_domains_entities(save=True)

    print(f"Profiles Registered: {len(dfs['profiles'])}")
    print(f"Domains Registered: {len(dfs['domains'])}")
    print(f"Macro Entities Registered: {len(dfs['macro_entities'])}")
    print(f"Event Entities Registered: {len(dfs['event_entities'])}")
    print(f"News Metadata Entities Registered: {len(dfs['news_metadata_entities'])}")

    txt_rep = build_macro_event_news_regime_text_report(summaries)
    md_rep = build_macro_event_news_regime_profile_markdown_report(summaries, dfs["profiles"])

    print("\n--- Profile Summary ---")
    print(txt_rep)
    print("\nSUCCESS: Phase 132 Profiles, Domains, and Entities generated and saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
