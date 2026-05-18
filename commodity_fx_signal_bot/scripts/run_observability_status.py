#!/usr/bin/env python3
"""
Script to check the overall status of observability data in the data lake.
"""

import argparse
import logging
from datetime import datetime

from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from ml.feature_store import FeatureStore
from reports.report_builder import build_observability_status_report

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Check Observability Status.")
    parser.add_argument("--save", action="store_true", default=True, help="Save report to DataLake and output files.")
    parser.add_argument("--no-save", action="store_false", dest="save", help="Do not save reports.")
    args = parser.parse_args()

    logger.info("Initializing DataLake & FeatureStore...")
    paths = ProjectPaths()
    data_lake = DataLake(paths)
    feature_store = FeatureStore(data_lake)

    logger.info("Gathering observability status...")

    # We can use list_observability_reports to see what's available
    df = pd.DataFrame()
    if hasattr(data_lake, "list_observability_reports"):
        df = data_lake.list_observability_reports()

    summary = {
        "timestamp": datetime.now().isoformat(),
        "reports_found": len(df),
        "report_types": df['report_type'].unique().tolist() if not df.empty else []
    }

    logger.info(f"Found {summary['reports_found']} observability reports.")

    if args.save:
        import pandas as pd
        report_text = build_observability_status_report(df, summary)
        out_dir = paths.REPORTS_OBSERVABILITY_DIR
        out_dir.mkdir(parents=True, exist_ok=True)

        txt_path = out_dir / "observability_status_report.txt"
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(report_text)

        csv_path = out_dir / "observability_status.csv"
        if not df.empty:
            df.to_csv(csv_path, index=False)

        logger.info(f"Saved text report to: {txt_path}")
        if not df.empty:
            logger.info(f"Saved CSV report to: {csv_path}")

if __name__ == "__main__":
    main()
