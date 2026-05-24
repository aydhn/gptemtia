import argparse
import sys
import logging
import pandas as pd
from config.settings import settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from experiments.experiment_config import get_experiment_profile
from experiments.experiment_pipeline import ExperimentTrackingPipeline


logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Run Experiment Status Check")
    args = parser.parse_args()

    paths = ProjectPaths()
    data_lake = DataLake(paths)
    profile = get_experiment_profile(settings.default_experiment_profile)

    pipeline = ExperimentTrackingPipeline(data_lake, settings, paths.project_root, profile)

    logger.info("Checking experiment status...")

    status_data = []

    dirs_to_check = [
        ("Hypotheses", paths.experiments_hypotheses),
        ("Definitions", paths.experiments_definitions),
        ("Runs", paths.experiments_runs),
        ("Artifacts", paths.experiments_artifacts),
        ("Reproducibility", paths.experiments_reproducibility),
        ("Versions", paths.experiments_versions),
        ("Ablation", paths.experiments_ablation),
        ("Comparisons", paths.experiments_comparisons),
        ("Leaderboards", paths.experiments_leaderboards),
        ("Quality", paths.experiments_quality)
    ]

    for name, path in dirs_to_check:
        try:
            if path.exists():
                files = list(path.glob("*"))
                status_data.append({"Category": name, "Path": str(path), "File_Count": len(files)})
            else:
                status_data.append({"Category": name, "Path": str(path), "File_Count": 0})
        except Exception as e:
            status_data.append({"Category": name, "Path": str(path), "File_Count": -1})

    df = pd.DataFrame(status_data)
    summary = {"total_directories_checked": len(dirs_to_check)}


    import reports.report_builder as rb
    txt_content = rb.build_experiment_status_report(df, summary)

    csv_path = paths.experiments_reports_csv / "experiment_status.csv"
    txt_path = paths.experiments_reports_txt / "experiment_status_report.txt"

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    txt_path.parent.mkdir(parents=True, exist_ok=True)

    with open(txt_path, "w") as f:
        f.write(txt_content)

    if not df.empty:
        df.to_csv(csv_path, index=False)

    logger.info(f"Status check generated. {df['File_Count'].sum()} total files found.")

if __name__ == "__main__":
    main()
