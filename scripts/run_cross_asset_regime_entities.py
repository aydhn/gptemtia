"""Run script: Entities, Pairs, and Relationship Taxonomy for Phase 131."""

import sys
from advanced_cross_asset_regime_context.cross_asset_regime_pipeline import (
    CrossAssetRegimePipeline,
)
from advanced_cross_asset_regime_context.cross_asset_regime_report_builder import (
    build_cross_asset_entity_pair_markdown_report,
    build_cross_asset_relationship_taxonomy_markdown_report,
)
from reports.report_builder import (
    build_cross_asset_entity_pair_text_report,
    build_cross_asset_relationship_taxonomy_text_report,
)


def main():
    print("Executing Phase 131 Cross-Asset Regime Entities and Pairs Registry...")
    pipeline = CrossAssetRegimePipeline()
    dfs, summaries = pipeline.build_profiles_domains_entities(save=True)

    print(f"Entities: {len(dfs['entities'])}")
    print(f"Pairs: {len(dfs['pairs'])}")
    print(f"Taxonomy: {len(dfs['taxonomy'])}")

    txt_pairs = build_cross_asset_entity_pair_text_report(summaries["pairs"])
    txt_tax = build_cross_asset_relationship_taxonomy_text_report(summaries["taxonomy"])

    print("\n--- Entities & Pairs Summary ---")
    print(txt_pairs)
    print("\n--- Taxonomy Summary ---")
    print(txt_tax)
    print("\nSUCCESS: Phase 131 Entities, Pairs, and Taxonomy generated and saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
