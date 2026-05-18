#!/usr/bin/env python3
"""
Script to generate the standard error taxonomy report.
"""

import argparse
import logging

from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from observability.error_taxonomy import build_error_taxonomy_report
from reports.report_builder import build_error_taxonomy_report as build_text_report

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Run Error Taxonomy Report.")
    parser.add_argument("--save", action="store_true", default=True, help="Save report to DataLake and output files.")
    parser.add_argument("--no-save", action="store_false", dest="save", help="Do not save reports.")
    args = parser.parse_args()

    logger.info("Initializing DataLake...")
    paths = ProjectPaths()
    data_lake = DataLake(paths)

    logger.info("Generating Error Taxonomy Report...")
    df, summary = build_error_taxonomy_report()

    logger.info(f"Total Errors Defined: {summary.get('total_errors_defined', 0)}")

    if args.save:
        # Save to data lake
        if hasattr(data_lake, "save_error_taxonomy_report"):
            data_lake.save_error_taxonomy_report(df, summary)

        # Save readable text and CSV to output directory
        report_text = build_text_report(df, summary)
        out_dir = paths.REPORTS_OBSERVABILITY_DIR
        out_dir.mkdir(parents=True, exist_ok=True)

        txt_path = out_dir / "error_taxonomy_report.txt"
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(report_text)

        csv_path = out_dir / "error_taxonomy.csv"
        df.to_csv(csv_path, index=False)

        logger.info(f"Saved text report to: {txt_path}")
        logger.info(f"Saved CSV report to: {csv_path}")

if __name__ == "__main__":
    main()
