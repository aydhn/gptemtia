import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from advanced_news_metadata.news_pipeline import NewsMetadataPipeline

def main():
    print("Running news source registry script...")
    pipeline = NewsMetadataPipeline(None, None, Path("."))
    sources, _ = pipeline.build_news_sources_and_schemas(save=False)
    tags, _ = pipeline.build_news_tags_and_linkages(save=False)
    
    out_dir = Path("reports/output/advanced_news_metadata")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(parents=True, exist_ok=True)
    (out_dir / "markdown").mkdir(parents=True, exist_ok=True)
    (out_dir / "txt").mkdir(parents=True, exist_ok=True)
    
    sources["sources"].to_csv(out_dir / "csv/news_sources.csv", index=False)
    sources["categories"].to_csv(out_dir / "csv/news_categories.csv", index=False)
    tags["topic_taxonomy"].to_csv(out_dir / "csv/news_topic_taxonomy.csv", index=False)
    tags["region_currency"].to_csv(out_dir / "csv/news_region_currency.csv", index=False)
    
    with open(out_dir / "txt/news_source_summary.txt", "w", encoding="utf-8") as f:
        f.write("Phase 111 News Source Registry generated successfully.\n")
    with open(out_dir / "markdown/news_source_summary.md", "w", encoding="utf-8") as f:
        f.write("# Phase 111 News Source Registry\n\nNo scraping; canonical news sources and category metadata.\n")
    print("Done news source registry script.")

if __name__ == "__main__":
    main()
