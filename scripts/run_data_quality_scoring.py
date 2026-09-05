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
    build_phase_113_handoff_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_quality_profile()
    lake = DataLake()
    pipeline = DataQualityPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    scoring_tables, scoring_sum = pipeline.build_quality_scores(save=True)

    out_dir = root / "reports" / "output" / "advanced_data_quality"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    handoff_df = scoring_tables.get("phase_113_handoff")
    if handoff_df is not None:
        handoff_df.to_csv(out_dir / "csv" / "phase_113_normalization_handoff.csv", index=False)
        md = build_phase_113_handoff_markdown_report(scoring_sum.get("phase_113_handoff_summary", {}), handoff_df)
        with open(out_dir / "markdown" / "phase_113_normalization_handoff_report.md", "w", encoding="utf-8") as f:
            f.write(md)

    with open(out_dir / "txt" / "scoring_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Provider Average Score: {scoring_sum.get('provider_score_summary', {}).get('average_score')}\n")
        f.write(f"Dataset Average Score: {scoring_sum.get('dataset_score_summary', {}).get('average_score')}\n")
        f.write(f"Phase 113 Normalization Areas: {len(handoff_df) if handoff_df is not None else 0}\n")

    print("Data quality scoring & Phase 113 handoff generated successfully.")


if __name__ == "__main__":
    main()
