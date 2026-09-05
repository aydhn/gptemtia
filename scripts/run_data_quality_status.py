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


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_quality_profile()
    lake = DataLake()
    pipeline = DataQualityPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    status_df, summary = pipeline.build_data_quality_status(save=True)

    out_dir = root / "reports" / "output" / "advanced_data_quality"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    status_df.to_csv(out_dir / "csv" / "pipeline_status.csv", index=False)
    with open(out_dir / "txt" / "pipeline_status_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Phase: {summary.get('current_phase')}\n")
        f.write(f"Pipeline Status: {summary.get('pipeline_status')}\n")
        f.write(f"Total Findings: {summary.get('total_findings')}\n")
        f.write(f"Manual Review Items: {summary.get('manual_review_items')}\n")

    print(f"Data quality engine status: {summary.get('pipeline_status')}. Findings: {summary.get('total_findings')}")


if __name__ == "__main__":
    main()
