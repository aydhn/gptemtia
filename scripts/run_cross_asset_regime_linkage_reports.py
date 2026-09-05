"""Run script: Linkage, Divergence, Convergence, and Placeholder Reports for Phase 131."""

import sys
from advanced_cross_asset_regime_context.cross_asset_regime_pipeline import (
    CrossAssetRegimePipeline,
)
from advanced_cross_asset_regime_context.cross_asset_regime_report_builder import (
    build_cross_asset_linkage_markdown_report,
    build_divergence_convergence_markdown_report,
)
from reports.report_builder import (
    build_cross_asset_linkage_text_report,
)


def main():
    print("Executing Phase 131 Linkage and Diagnostic Placeholders...")
    pipeline = CrossAssetRegimePipeline()
    dfs, summaries = pipeline.build_linkage_reports(save=True)

    print(f"Transition Alignments: {len(dfs['transition_alignment'])}")
    print(f"Volatility Linkages: {len(dfs['volatility_linkage'])}")
    print(f"Trend Linkages: {len(dfs['trend_linkage'])}")
    print(f"Range Linkages: {len(dfs['range_linkage'])}")
    print(f"Divergences: {len(dfs['divergence'])}")
    print(f"Convergences: {len(dfs['convergence'])}")
    print(f"Correlation Placeholders: {len(dfs['correlation'])}")
    print(f"Lead-Lag Placeholders: {len(dfs['lead_lag'])}")

    txt_link = build_cross_asset_linkage_text_report(summaries["volatility_linkage"])
    print("\n--- Volatility Linkage Summary ---")
    print(txt_link)
    print("\nSUCCESS: Phase 131 Linkage and Diagnostic Reports generated and saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
