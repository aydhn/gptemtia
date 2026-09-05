import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from advanced_news_metadata.news_pipeline import NewsMetadataPipeline

def main():
    print("Running news metadata contracts script...")
    pipeline = NewsMetadataPipeline(None, None, Path("."))
    sources_and_schemas, _ = pipeline.build_news_sources_and_schemas(save=False)
    tags, _ = pipeline.build_news_tags_and_linkages(save=False)
    reqs, _ = pipeline.build_news_requirements(save=False)
    
    out_dir = Path("reports/output/advanced_news_metadata")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(parents=True, exist_ok=True)
    (out_dir / "markdown").mkdir(parents=True, exist_ok=True)
    (out_dir / "txt").mkdir(parents=True, exist_ok=True)
    
    sources_and_schemas["metadata_schema"].to_csv(out_dir / "csv/news_metadata_schema.csv", index=False)
    sources_and_schemas["item_reference_schema"].to_csv(out_dir / "csv/news_item_ref_schema.csv", index=False)
    tags["asset_tags"].to_csv(out_dir / "csv/news_asset_tags.csv", index=False)
    tags["macro_tags"].to_csv(out_dir / "csv/news_macro_tags.csv", index=False)
    tags["commodity_tags"].to_csv(out_dir / "csv/news_commodity_tags.csv", index=False)
    tags["fx_tags"].to_csv(out_dir / "csv/news_fx_tags.csv", index=False)
    tags["event_linkage"].to_csv(out_dir / "csv/news_event_linkage.csv", index=False)
    reqs["sentiment"].to_csv(out_dir / "csv/news_sentiment_requirements.csv", index=False)
    reqs["impact"].to_csv(out_dir / "csv/news_impact_requirements.csv", index=False)
    reqs["freshness"].to_csv(out_dir / "csv/news_freshness_requirements.csv", index=False)
    reqs["deduplication"].to_csv(out_dir / "csv/news_dedup_requirements.csv", index=False)
    
    with open(out_dir / "txt/news_contracts_summary.txt", "w", encoding="utf-8") as f:
        f.write("Phase 111 News Metadata Contracts generated successfully.\n")
    with open(out_dir / "markdown/news_contracts_summary.md", "w", encoding="utf-8") as f:
        f.write("# Phase 111 News Metadata Contracts\n\nStrict schema definitions and requirement contracts.\n")
    print("Done news metadata contracts script.")

if __name__ == "__main__":
    main()
