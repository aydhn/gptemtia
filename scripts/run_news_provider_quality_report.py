import sys
import json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from advanced_news_metadata.news_pipeline import NewsMetadataPipeline
from advanced_news_metadata.news_validation import build_news_validation_report
from advanced_news_metadata.news_report_builder import build_news_quality_markdown_report

def main():
    print("Running news provider quality report script...")
    pipeline = NewsMetadataPipeline(None, None, Path("."))
    profiles, _ = pipeline.build_news_profiles_and_domains(save=False)
    sources, _ = pipeline.build_news_sources_and_schemas(save=False)
    
    tables = {
        "profiles": profiles["profiles"],
        "domains": profiles["domains"],
        "sources": sources["sources"],
        "metadata_schema": sources["metadata_schema"]
    }
    val_df, val_summary = build_news_validation_report(tables, pipeline.profile)
    qual, qual_summary = pipeline.build_news_quality_report(save=False)
    
    out_dir = Path("reports/output/advanced_news_metadata")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(parents=True, exist_ok=True)
    (out_dir / "markdown").mkdir(parents=True, exist_ok=True)
    (out_dir / "txt").mkdir(parents=True, exist_ok=True)
    (out_dir / "json").mkdir(parents=True, exist_ok=True)
    
    val_df.to_csv(out_dir / "csv/news_validation_report.csv", index=False)
    with open(out_dir / "json/news_quality_report.json", "w", encoding="utf-8") as f:
        json.dump(qual, f, indent=2)
    with open(out_dir / "txt/news_quality_summary.txt", "w", encoding="utf-8") as f:
        f.write("Phase 111 News Provider Quality Report generated successfully.\n")
    with open(out_dir / "markdown/news_quality_summary.md", "w", encoding="utf-8") as f:
        f.write(build_news_quality_markdown_report(qual_summary, qual))
    print("Done news provider quality report script.")

if __name__ == "__main__":
    main()
