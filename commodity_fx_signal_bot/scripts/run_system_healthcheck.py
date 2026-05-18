#!/usr/bin/env python3
"""
Script to run the system healthcheck and generate observability reports.
"""

import argparse
import logging
from pathlib import Path

from config.settings import settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from observability.observability_config import get_observability_profile
from observability.observability_pipeline import ObservabilityPipeline
from reports.report_builder import build_system_healthcheck_report

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Run System Healthcheck.")
    parser.add_argument("--profile", type=str, default="balanced_system_observability", help="Observability profile to use.")
    parser.add_argument("--save", action="store_true", default=True, help="Save report to DataLake and output files.")
    parser.add_argument("--no-save", action="store_false", dest="save", help="Do not save reports.")
    args = parser.parse_args()

    logger.info("Initializing DataLake...")
    paths = ProjectPaths()
    data_lake = DataLake(paths)

    logger.info(f"Loading Observability Profile: {args.profile}...")
    profile = get_observability_profile(args.profile)

    pipeline = ObservabilityPipeline(data_lake, settings, profile)

    logger.info("Running System Healthcheck...")
    df, summary = pipeline.run_system_healthcheck(save=args.save)

    logger.info(f"Healthcheck Overall Status: {summary.get('overall_status', 'unknown')}")
    logger.info(f"Healthcheck Overall Score: {summary.get('overall_score', 0.0):.2f}")

    if args.save:
        report_text = build_system_healthcheck_report(df, summary)
        out_dir = paths.REPORTS_OBSERVABILITY_DIR
        out_dir.mkdir(parents=True, exist_ok=True)

        txt_path = out_dir / "system_healthcheck_report.txt"
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(report_text)

        csv_path = out_dir / "system_healthcheck.csv"
        df.to_csv(csv_path, index=False)

        logger.info(f"Saved text report to: {txt_path}")
        logger.info(f"Saved CSV report to: {csv_path}")

if __name__ == "__main__":
    main()
