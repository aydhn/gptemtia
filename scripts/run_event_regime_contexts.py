"""Run script: Event and Calendar Context Registries for Phase 132."""

import sys
from advanced_macro_event_news_regime.macro_event_news_regime_pipeline import (
    MacroEventNewsRegimePipeline,
)
from advanced_macro_event_news_regime.macro_event_news_regime_report_builder import (
    build_event_context_markdown_report,
)
from reports.report_builder import build_event_context_text_report


def main():
    print("Executing Phase 132 Event and Calendar Regime Contexts...")
    pipeline = MacroEventNewsRegimePipeline()
    dfs, summaries = pipeline.build_event_contexts(save=True)

    print(f"Calendar Events: {len(dfs['calendar_events'])}")
    print(f"Event Windows: {len(dfs['event_windows'])}")
    print(f"Pre-Events: {len(dfs['pre_events'])}")
    print(f"Post-Events: {len(dfs['post_events'])}")
    print(f"Event Importance Tiers: {len(dfs['event_importance'])}")
    print(f"Release Lags: {len(dfs['release_lag'])}")
    print(f"Release Alignments: {len(dfs['release_alignment'])}")

    combined_summary = {
        "total_calendar_events": len(dfs["calendar_events"]),
        "all_non_signal": True,
    }

    txt_rep = build_event_context_text_report(combined_summary)
    md_rep = build_event_context_markdown_report(combined_summary, dfs["calendar_events"])

    print("\n--- Event Context Summary ---")
    print(txt_rep)
    print("\nSUCCESS: Phase 132 Event Contexts generated and saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
