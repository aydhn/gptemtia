import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from config.settings import Settings
from config.paths import ensure_project_directories
from data.storage.data_lake import DataLake
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.data_quality_pipeline import DataQualityPipeline
from advanced_data_quality.data_quality_report_builder import (
    build_quality_findings_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_quality_profile()
    lake = DataLake()
    pipeline = DataQualityPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    findings_tables, findings_sum = pipeline.build_findings_and_manual_review(save=True)
    findings_df = findings_tables.get("quality_findings")

    out_dir = root / "reports" / "output" / "advanced_data_quality"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    if findings_df is not None:
        news_findings = findings_df[findings_df["dataset_type"] == "dataset_news_metadata"]
        news_findings.to_csv(out_dir / "csv" / "news_quality_findings.csv", index=False)
        md = build_quality_findings_markdown_report(findings_sum.get("findings_summary", {}), news_findings)
        with open(out_dir / "markdown" / "news_quality_findings_report.md", "w", encoding="utf-8") as f:
            f.write(md)

    with open(out_dir / "txt" / "news_checks_summary.txt", "w", encoding="utf-8") as f:
        f.write("News Metadata & Copyright Safety Checks completed.\n")
        f.write("Full article body / scraped content strictly prohibited.\n")

    print("News metadata & copyright safety checks completed.")


if __name__ == "__main__":
    main()
