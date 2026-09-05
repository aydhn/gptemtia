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
    build_dataset_quality_score_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_quality_profile()
    lake = DataLake()
    pipeline = DataQualityPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    domain_tables, domain_sum = pipeline.run_domain_quality_contracts(save=True)
    scoring_tables, scoring_sum = pipeline.build_quality_scores(save=True)

    out_dir = root / "reports" / "output" / "advanced_data_quality"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    ds_score_df = scoring_tables.get("dataset_quality_scores")
    if ds_score_df is not None:
        ds_score_df.to_csv(out_dir / "csv" / "dataset_quality_scores.csv", index=False)
        md = build_dataset_quality_score_markdown_report(scoring_sum.get("dataset_score_summary", {}), ds_score_df)
        with open(out_dir / "markdown" / "dataset_quality_score_report.md", "w", encoding="utf-8") as f:
            f.write(md)

    with open(out_dir / "txt" / "asset_checks_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Asset Checks Evaluated: {len(domain_tables)}\n")
        f.write(f"Datasets Scored: {len(ds_score_df) if ds_score_df is not None else 0}\n")

    print(f"Asset checks evaluated successfully. Datasets scored: {len(ds_score_df) if ds_score_df is not None else 0}")


if __name__ == "__main__":
    main()
