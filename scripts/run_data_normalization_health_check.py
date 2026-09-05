import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from config.settings import Settings
from config.paths import ensure_project_directories
from data.storage.data_lake import DataLake
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile
from advanced_data_normalization.data_normalization_pipeline import DataNormalizationPipeline
from advanced_data_normalization.data_normalization_report_builder import (
    build_data_normalization_health_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_normalization_profile()
    lake = DataLake()
    pipeline = DataNormalizationPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    tables, summary = pipeline.build_health_validation_safety_and_handoff(save=True)
    health_df = tables.get("health_check")

    out_dir = root / "reports" / "output" / "advanced_data_normalization"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    if health_df is not None:
        health_df.to_csv(out_dir / "csv" / "data_normalization_health_check.csv", index=False)

    md = build_data_normalization_health_markdown_report(summary.get("health_summary", {}), health_df)
    with open(out_dir / "markdown" / "data_normalization_health_report.md", "w", encoding="utf-8") as f:
        f.write(md)

    with open(out_dir / "txt" / "health_check_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Total Health Checks: {summary.get('health_summary', {}).get('total_checks', 0)}\n")
        f.write(f"Passed: {summary.get('health_summary', {}).get('pass_count', 0)}\n")
        f.write(f"Overall Status: {summary.get('health_summary', {}).get('overall_status', 'PASS')}\n")

    print(f"Data normalization health check finished: {summary.get('health_summary', {}).get('overall_status', 'PASS')}")


if __name__ == "__main__":
    main()
