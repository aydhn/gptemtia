"""Run script: Entity and Taxonomy Registries for Phase 132 Macro/Event/News Regime Context Expansion."""

import sys
from advanced_macro_event_news_regime.macro_event_news_regime_pipeline import (
    MacroEventNewsRegimePipeline,
)
from advanced_macro_event_news_regime.macro_event_news_regime_report_builder import (
    build_macro_event_news_entity_markdown_report,
)
from reports.report_builder import build_macro_event_news_entity_text_report


def main():
    print("Executing Phase 132 Entities and Context Taxonomy Registries...")
    pipeline = MacroEventNewsRegimePipeline()
    ent_dfs, ent_summaries = pipeline.build_profiles_domains_entities(save=True)
    tax_dfs, tax_summaries = pipeline.build_context_taxonomies(save=True)

    print(f"Macro Entities: {len(ent_dfs['macro_entities'])}")
    print(f"Event Entities: {len(ent_dfs['event_entities'])}")
    print(f"News Metadata Entities: {len(ent_dfs['news_metadata_entities'])}")
    print(f"Macro Taxonomies: {len(tax_dfs['macro_taxonomy'])}")
    print(f"Event Taxonomies: {len(tax_dfs['event_taxonomy'])}")
    print(f"News Taxonomies: {len(tax_dfs['news_taxonomy'])}")

    combined_summary = {
        "total_entities": len(ent_dfs["macro_entities"]) + len(ent_dfs["event_entities"]) + len(ent_dfs["news_metadata_entities"]),
        "macro_entities": len(ent_dfs["macro_entities"]),
        "event_entities": len(ent_dfs["event_entities"]),
        "news_metadata_entities": len(ent_dfs["news_metadata_entities"]),
        "all_non_signal": True,
    }

    txt_rep = build_macro_event_news_entity_text_report(combined_summary)
    md_rep = build_macro_event_news_entity_markdown_report(combined_summary, ent_dfs["macro_entities"])

    print("\n--- Entities Summary ---")
    print(txt_rep)
    print("\nSUCCESS: Phase 132 Entities and Taxonomies generated and saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
