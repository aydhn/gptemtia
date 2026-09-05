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
    build_normalization_score_markdown_report,
    build_phase_114_handoff_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_normalization_profile()
    lake = DataLake()
    pipeline = DataNormalizationPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    tables, summary = pipeline.build_normalization_scores_and_mapping(save=True)
    h_tables, h_summary = pipeline.build_health_validation_safety_and_handoff(save=True)

    score_df = tables.get("score_report")
    handoff_df = h_tables.get("phase_114_handoff")

    out_dir = root / "reports" / "output" / "advanced_data_normalization"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    if score_df is not None:
        score_df.to_csv(out_dir / "csv" / "normalization_score_report.csv", index=False)
    if handoff_df is not None:
        handoff_df.to_csv(out_dir / "csv" / "phase_114_lineage_provenance_handoff_report.csv", index=False)

    md_score = build_normalization_score_markdown_report(summary.get("score_summary", {}), score_df)
    with open(out_dir / "markdown" / "normalization_score_report.md", "w", encoding="utf-8") as f:
        f.write(md_score)

    md_handoff = build_phase_114_handoff_markdown_report(h_summary.get("handoff_summary", {}), handoff_df)
    with open(out_dir / "markdown" / "phase_114_handoff_report.md", "w", encoding="utf-8") as f:
        f.write(md_handoff)

    with open(out_dir / "txt" / "normalization_scoring_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Scored Datasets: {summary.get('score_summary', {}).get('total_scored_datasets', 0)}\n")
        f.write(f"Mean Normalization Score: {summary.get('score_summary', {}).get('mean_score', 1.0)}\n")
        f.write(f"Phase 114 Handoff Items: {h_summary.get('handoff_summary', {}).get('total_handoff_items', 0)}\n")

    print(f"Normalization score report and Phase 114 handoff generated successfully. Mean score: {summary.get('score_summary', {}).get('mean_score', 1.0)}")


if __name__ == "__main__":
    main()
