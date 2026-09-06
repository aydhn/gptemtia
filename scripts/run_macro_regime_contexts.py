"""Run script: Macro Indicator, Release, Revision, and Surprise Registries for Phase 132."""

import sys
from advanced_macro_event_news_regime.macro_event_news_regime_pipeline import (
    MacroEventNewsRegimePipeline,
)
from advanced_macro_event_news_regime.macro_event_news_regime_report_builder import (
    build_macro_context_markdown_report,
)
from reports.report_builder import build_macro_context_text_report


def main():
    print("Executing Phase 132 Macro Regime Contexts...")
    pipeline = MacroEventNewsRegimePipeline()
    dfs, summaries = pipeline.build_macro_contexts(save=True)

    print(f"Macro Indicator Contexts: {len(dfs['macro_indicators'])}")
    print(f"Macro Release Contexts: {len(dfs['macro_releases'])}")
    print(f"Macro Revision Contexts: {len(dfs['macro_revisions'])}")
    print(f"Macro Surprise Placeholders: {len(dfs['macro_surprises'])}")

    combined_summary = {
        "total_macro_contexts": len(dfs["macro_indicators"]) + len(dfs["macro_releases"]) + len(dfs["macro_revisions"]),
        "all_non_signal": True,
    }

    txt_rep = build_macro_context_text_report(combined_summary)
    md_rep = build_macro_context_markdown_report(combined_summary, dfs["macro_indicators"])

    print("\n--- Macro Context Summary ---")
    print(txt_rep)
    print("\nSUCCESS: Phase 132 Macro Contexts generated and saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
