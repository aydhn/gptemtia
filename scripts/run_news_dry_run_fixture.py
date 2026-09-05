import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from advanced_news_metadata.news_pipeline import NewsMetadataPipeline

def main():
    print("Running news dry run fixture script...")
    pipeline = NewsMetadataPipeline(None, None, Path("."))
    dry_df, _ = pipeline.build_news_dry_run_fixture(save=False)
    placeholders, _ = pipeline.build_news_placeholders(save=False)
    
    out_dir = Path("reports/output/advanced_news_metadata")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(parents=True, exist_ok=True)
    (out_dir / "markdown").mkdir(parents=True, exist_ok=True)
    (out_dir / "txt").mkdir(parents=True, exist_ok=True)
    
    dry_df.to_csv(out_dir / "csv/news_dry_run_fixture_report.csv", index=False)
    placeholders["manual"].to_csv(out_dir / "csv/news_manual_file_placeholder.csv", index=False)
    placeholders["local_cache"].to_csv(out_dir / "csv/news_local_cache_placeholder.csv", index=False)
    placeholders["official_api"].to_csv(out_dir / "csv/news_official_api_placeholder.csv", index=False)
    placeholders["licensed"].to_csv(out_dir / "csv/news_licensed_placeholder.csv", index=False)
    placeholders["public_dataset"].to_csv(out_dir / "csv/news_public_dataset_placeholder.csv", index=False)
    
    with open(out_dir / "txt/news_dry_run_summary.txt", "w", encoding="utf-8") as f:
        f.write("Phase 111 News Dry Run Fixture executed successfully without network calls or scraping.\n")
    with open(out_dir / "markdown/news_dry_run_summary.md", "w", encoding="utf-8") as f:
        f.write("# Phase 111 News Dry Run Fixture\n\nPurely local synthetic execution for testing.\n")
    print("Done news dry run fixture script.")

if __name__ == "__main__":
    main()
