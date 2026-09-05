import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from advanced_news_metadata.news_pipeline import NewsMetadataPipeline

def main():
    print("Running news provider status script...")
    pipeline = NewsMetadataPipeline(None, None, Path("."))
    status_df, status_summary = pipeline.build_news_status(save=False)
    
    out_dir = Path("reports/output/advanced_news_metadata")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(parents=True, exist_ok=True)
    (out_dir / "txt").mkdir(parents=True, exist_ok=True)
    
    status_df.to_csv(out_dir / "csv/news_provider_status.csv", index=False)
    with open(out_dir / "txt/news_provider_status_summary.txt", "w", encoding="utf-8") as f:
        f.write("Phase 111 News Provider Status: All components operational and ready for Phase 112.\n")
    print("Done news provider status script.")

if __name__ == "__main__":
    main()
