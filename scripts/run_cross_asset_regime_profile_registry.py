"""Run script: Profile and Domain Registry for Phase 131 Cross-Asset Regime Context Expansion."""

import sys
from advanced_cross_asset_regime_context.cross_asset_regime_pipeline import (
    CrossAssetRegimePipeline,
)
from advanced_cross_asset_regime_context.cross_asset_regime_report_builder import (
    build_cross_asset_regime_profile_markdown_report,
)
from reports.report_builder import build_cross_asset_regime_text_report


def main():
    print("Executing Phase 131 Cross-Asset Regime Profile and Domain Registry...")
    pipeline = CrossAssetRegimePipeline()
    dfs, summaries = pipeline.build_profiles_domains_entities(save=True)

    print(f"Profiles Registered: {len(dfs['profiles'])}")
    print(f"Domains Registered: {len(dfs['domains'])}")
    print(f"Entities Registered: {len(dfs['entities'])}")
    print(f"Pairs Registered: {len(dfs['pairs'])}")
    print(f"Taxonomy Items: {len(dfs['taxonomy'])}")

    txt_rep = build_cross_asset_regime_text_report(summaries["profiles"])
    md_rep = build_cross_asset_regime_profile_markdown_report(summaries["profiles"], dfs["profiles"])

    print("\n--- Profile Summary ---")
    print(txt_rep)
    print("\nSUCCESS: Phase 131 Profiles and Domains generated and saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
