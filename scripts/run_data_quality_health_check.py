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
    build_data_quality_health_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_quality_profile()
    lake = DataLake()
    pipeline = DataQualityPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    health_tables, health_sum = pipeline.build_health_and_validation(save=True)
    health_df = health_tables.get("health_check")

    out_dir = root / "reports" / "output" / "advanced_data_quality"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    if health_df is not None:
        health_df.to_csv(out_dir / "csv" / "data_quality_health_check.csv", index=False)
        md = build_data_quality_health_markdown_report(health_sum.get("health_summary", {}), health_df)
        with open(out_dir / "markdown" / "data_quality_health_report.md", "w", encoding="utf-8") as f:
            f.write(md)

    with open(out_dir / "txt" / "health_check_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Health Checks Passed: {health_sum.get('health_summary', {}).get('passing_checks')}/{health_sum.get('health_summary', {}).get('total_checks')}\n")

    print("Data quality health check executed successfully.")


if __name__ == "__main__":
    main()
