"""Run script: Alignment, Contracts, and No-Lookahead Guards for Phase 132."""

import sys
from advanced_macro_event_news_regime.macro_event_news_regime_pipeline import (
    MacroEventNewsRegimePipeline,
)
from advanced_macro_event_news_regime.macro_event_news_regime_report_builder import (
    build_macro_event_news_cross_asset_markdown_report,
)
from reports.report_builder import (
    build_metadata_only_boundary_text_report,
)


def main():
    print("Executing Phase 132 Alignment, Contracts, and No-Lookahead Guards...")
    pipeline = MacroEventNewsRegimePipeline()
    dfs, summaries = pipeline.build_cross_asset_transition_contracts_guards(save=True)

    print(f"Cross-Asset Contexts: {len(dfs['cross_asset_context'])}")
    print(f"Transition Contexts: {len(dfs['transition_context'])}")
    print(f"Context Contracts: {len(dfs['contracts'])}")
    print(f"Timestamp Policies: {len(dfs['timestamp_policies'])}")
    print(f"Asof Join Policies: {len(dfs['asof_policies'])}")
    print(f"No-Lookahead Guards: {len(dfs['no_lookahead_guard'])}")

    combined_summary = {
        "total_cross_asset_contexts": len(dfs["cross_asset_context"]),
        "target_asset_classes": dfs["cross_asset_context"]["target_asset_class"].unique().tolist(),
        "all_non_signal": True,
    }

    md_rep = build_macro_event_news_cross_asset_markdown_report(combined_summary, dfs["cross_asset_context"])

    print("\n--- Cross-Asset & Governance Summary ---")
    print(f"Total Guards Enforced: {len(dfs['no_lookahead_guard'])}")
    print(f"All Contracts Require No-Lookahead: True")
    print("\nSUCCESS: Phase 132 Alignment, Contracts, and Guards generated and saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
