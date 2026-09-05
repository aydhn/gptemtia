import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from advanced_news_metadata.news_pipeline import NewsMetadataPipeline

def main():
    print("Running news provider profile registry script...")
    pipeline = NewsMetadataPipeline(None, None, Path("."))
    profiles, _ = pipeline.build_news_profiles_and_domains(save=False)
    caps, _ = pipeline.build_news_provider_metadata_and_capabilities(save=False)
    
    out_dir = Path("reports/output/advanced_news_metadata")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(parents=True, exist_ok=True)
    (out_dir / "markdown").mkdir(parents=True, exist_ok=True)
    (out_dir / "txt").mkdir(parents=True, exist_ok=True)
    
    profiles["profiles"].to_csv(out_dir / "csv/news_profiles.csv", index=False)
    profiles["domains"].to_csv(out_dir / "csv/news_domains.csv", index=False)
    caps["capabilities"].to_csv(out_dir / "csv/news_capabilities.csv", index=False)
    
    with open(out_dir / "txt/news_profiles_summary.txt", "w", encoding="utf-8") as f:
        f.write("Phase 111 News Provider Profile Registry generated successfully.\n")
    with open(out_dir / "markdown/news_profiles_summary.md", "w", encoding="utf-8") as f:
        f.write("# Phase 111 News Provider Profile Registry\n\nMetadata only; no scraping; no trading signal.\n")
    print("Done news provider profile registry script.")

if __name__ == "__main__":
    main()
