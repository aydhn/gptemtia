import argparse
import sys
import logging
from config.settings import settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from experiments.experiment_config import get_experiment_profile
from experiments.experiment_pipeline import ExperimentTrackingPipeline
from experiments.experiment_report_builder import build_ablation_study_markdown_report


logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Run Ablation Study Report")
    parser.add_argument("--profile", type=str, default=settings.default_experiment_profile)
    args = parser.parse_args()

    paths = ProjectPaths()
    data_lake = DataLake(paths)
    profile = get_experiment_profile(args.profile)

    pipeline = ExperimentTrackingPipeline(data_lake, settings, paths.project_root, profile)

    logger.info("Building ablation study report...")
    df, summary = pipeline.build_ablation_study_report(save=True)

    md_content = build_ablation_study_markdown_report(summary, df)

    import reports.report_builder as rb
    txt_content = rb.build_ablation_study_text_report(summary, df)

    md_path = paths.experiments_reports_markdown / "ablation_study_report.md"
    txt_path = paths.experiments_reports_txt / "ablation_study_report.txt"
    csv_path = paths.experiments_reports_csv / "ablation_study_results.csv"

    md_path.parent.mkdir(parents=True, exist_ok=True)
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    with open(md_path, "w") as f:
        f.write(md_content)

    with open(txt_path, "w") as f:
        f.write(txt_content)

    if not df.empty:
        df.to_csv(csv_path, index=False)

    logger.info("Report generated successfully.")

if __name__ == "__main__":
    main()
