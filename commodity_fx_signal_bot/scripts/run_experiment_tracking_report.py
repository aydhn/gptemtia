import argparse
import sys
import logging
from config.settings import settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from experiments.experiment_config import get_experiment_profile
from experiments.experiment_pipeline import ExperimentTrackingPipeline
from experiments.experiment_report_builder import build_experiment_tracking_markdown_report


logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Run Experiment Tracking Report")
    parser.add_argument("--experiment-name", type=str, default="auto_existing_research_run")
    parser.add_argument("--experiment-type", type=str, default="candidate_experiment")
    parser.add_argument("--hypothesis-id", type=str)
    parser.add_argument("--module-scope", nargs="+", default=["meta_research", "factor_research", "synthetic_indices", "portfolio_research"])
    parser.add_argument("--symbol", type=str)
    parser.add_argument("--timeframe", type=str, default="1d")
    parser.add_argument("--profile", type=str, default=settings.default_experiment_profile)
    args = parser.parse_args()

    paths = ProjectPaths()
    data_lake = DataLake(paths)
    profile = get_experiment_profile(args.profile)

    pipeline = ExperimentTrackingPipeline(data_lake, settings, paths.project_root, profile)

    symbols = [args.symbol] if args.symbol else ["*"]

    logger.info("Tracking experiment run...")
    run_manifest, summary = pipeline.track_existing_research_run(
        experiment_name=args.experiment_name,
        module_scope=args.module_scope,
        symbols=symbols,
        timeframe=args.timeframe,
        hypothesis_id=args.hypothesis_id,
        experiment_type=args.experiment_type,
        save=True
    )

    md_content = build_experiment_tracking_markdown_report(summary)


    import reports.report_builder as rb
    txt_content = rb.build_experiment_tracking_text_report(summary)

    md_path = paths.experiments_reports_markdown / "experiment_tracking_report.md"
    txt_path = paths.experiments_reports_txt / "experiment_tracking_report.txt"
    json_path = paths.experiments_reports_json / f"experiment_run_manifest_{run_manifest.get('run_id', 'unknown')}.json"

    md_path.parent.mkdir(parents=True, exist_ok=True)
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    with open(md_path, "w") as f:
        f.write(md_content)

    with open(txt_path, "w") as f:
        f.write(txt_content)

    import json
    with open(json_path, "w") as f:
        f.write(json.dumps(run_manifest))

    logger.info("Report generated successfully.")

if __name__ == "__main__":
    main()
