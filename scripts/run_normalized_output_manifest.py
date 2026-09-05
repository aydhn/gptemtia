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
    build_normalized_output_manifest_markdown_report,
    build_manual_review_normalization_markdown_report,
    build_normalization_findings_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_normalization_profile()
    lake = DataLake()
    pipeline = DataNormalizationPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    tables, summary = pipeline.build_normalized_views_and_findings(save=True)
    view_df = tables.get("normalized_views")
    find_df = tables.get("findings_registry")
    dec_df = tables.get("decision_registry")
    queue_df = tables.get("manual_review_queue")
    man_df = tables.get("output_manifest")

    out_dir = root / "reports" / "output" / "advanced_data_normalization"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    if view_df is not None:
        view_df.to_csv(out_dir / "csv" / "normalized_view_registry.csv", index=False)
    if find_df is not None:
        find_df.to_csv(out_dir / "csv" / "normalization_finding_registry.csv", index=False)
    if dec_df is not None:
        dec_df.to_csv(out_dir / "csv" / "normalization_decision_registry.csv", index=False)
    if queue_df is not None:
        queue_df.to_csv(out_dir / "csv" / "manual_review_normalization_queue.csv", index=False)
    if man_df is not None:
        man_df.to_csv(out_dir / "csv" / "normalized_output_manifest.csv", index=False)

    md_man = build_normalized_output_manifest_markdown_report(summary.get("output_manifest_summary", {}), man_df)
    with open(out_dir / "markdown" / "normalized_output_manifest_report.md", "w", encoding="utf-8") as f:
        f.write(md_man)

    md_queue = build_manual_review_normalization_markdown_report(summary.get("manual_review_summary", {}), queue_df)
    with open(out_dir / "markdown" / "manual_review_normalization_queue_report.md", "w", encoding="utf-8") as f:
        f.write(md_queue)

    with open(out_dir / "txt" / "normalized_views_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Normalized Views: {summary.get('view_summary', {}).get('total_normalized_views', 0)}\n")
        f.write(f"Findings: {summary.get('finding_summary', {}).get('total_findings', 0)}\n")
        f.write(f"Manual Review Queue: {summary.get('manual_review_summary', {}).get('total_queued_items', 0)}\n")

    print(f"Normalized output manifest and review queue generated successfully. Views: {len(view_df) if view_df is not None else 0}")


if __name__ == "__main__":
    main()
