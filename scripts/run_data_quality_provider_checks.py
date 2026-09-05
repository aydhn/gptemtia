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
    build_provider_quality_score_markdown_report,
    build_manual_review_queue_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_quality_profile()
    lake = DataLake()
    pipeline = DataQualityPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    findings_tables, findings_sum = pipeline.build_findings_and_manual_review(save=True)
    scoring_tables, scoring_sum = pipeline.build_quality_scores(save=True)

    out_dir = root / "reports" / "output" / "advanced_data_quality"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    prov_score_df = scoring_tables.get("provider_quality_scores")
    review_df = findings_tables.get("manual_review_queue")

    if prov_score_df is not None:
        prov_score_df.to_csv(out_dir / "csv" / "provider_quality_scores.csv", index=False)
        md = build_provider_quality_score_markdown_report(scoring_sum.get("provider_score_summary", {}), prov_score_df)
        with open(out_dir / "markdown" / "provider_quality_score_report.md", "w", encoding="utf-8") as f:
            f.write(md)

    if review_df is not None:
        review_df.to_csv(out_dir / "csv" / "manual_review_queue.csv", index=False)
        rev_md = build_manual_review_queue_markdown_report(findings_sum.get("manual_review_summary", {}), review_df)
        with open(out_dir / "markdown" / "manual_review_queue_report.md", "w", encoding="utf-8") as f:
            f.write(rev_md)

    with open(out_dir / "txt" / "provider_checks_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Scored Providers: {len(prov_score_df) if prov_score_df is not None else 0}\n")
        f.write(f"Review Items: {len(review_df) if review_df is not None else 0}\n")

    print(f"Provider checks completed. Scored providers: {len(prov_score_df) if prov_score_df is not None else 0}")


if __name__ == "__main__":
    main()
