import sys
import json
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
    build_data_quality_validation_markdown_report,
    build_data_quality_safety_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_quality_profile()
    lake = DataLake()
    pipeline = DataQualityPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    health_tables, health_sum = pipeline.build_health_and_validation(save=True)
    val_df = health_tables.get("validation_report")
    safety_df = health_tables.get("safety_boundary")

    out_dir = root / "reports" / "output" / "advanced_data_quality"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "json").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    val_summary = health_sum.get("validation_summary", {})
    with open(out_dir / "json" / "validation_summary.json", "w", encoding="utf-8") as f:
        json.dump(val_summary, f, ensure_ascii=False, indent=2)

    if val_df is not None:
        md = build_data_quality_validation_markdown_report(val_summary, val_df)
        with open(out_dir / "markdown" / "data_quality_validation_report.md", "w", encoding="utf-8") as f:
            f.write(md)

    if safety_df is not None:
        saf_md = build_data_quality_safety_markdown_report(health_sum.get("safety_summary", {}), safety_df)
        with open(out_dir / "markdown" / "data_quality_safety_report.md", "w", encoding="utf-8") as f:
            f.write(saf_md)

    with open(out_dir / "txt" / "validation_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Validation Valid: {val_summary.get('valid')}\n")
        f.write(f"Total Validations: {val_summary.get('total_validations')}\n")

    print("Data quality validation report generated.")


if __name__ == "__main__":
    main()
