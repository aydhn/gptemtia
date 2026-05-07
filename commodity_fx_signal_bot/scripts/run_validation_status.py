#!/usr/bin/env python
"""
Script to check the status of validation results in the data lake.
"""

import argparse
import logging
import sys
from pathlib import Path
import pandas as pd

import os
project_root = str(Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config.settings import settings
from config.paths import ensure_project_directories, REPORTS_VALIDATION_DIR
from data.storage.data_lake import DataLake
from reports.report_builder import build_validation_status_report

logging.basicConfig(level=getattr(logging, settings.log_level), format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Check validation status.")
    parser.parse_args()
    ensure_project_directories()

    data_lake = DataLake(settings)

    try:
        df = data_lake.list_validation_runs()

        summary = {
             "total_reports": len(df),
             "unique_symbols": df['symbol'].nunique() if not df.empty else 0
        }

        report_text = build_validation_status_report(df, summary)
        print("\n" + report_text)

        txt_path = REPORTS_VALIDATION_DIR / "validation_status_report.txt"
        csv_path = REPORTS_VALIDATION_DIR / "validation_status.csv"

        txt_path.write_text(report_text, encoding="utf-8")
        if not df.empty:
            df.to_csv(csv_path, index=False)

        logger.info(f"Reports saved to {txt_path} and {csv_path}")

    except Exception as e:
        logger.error(f"Error checking validation status: {e}")

if __name__ == "__main__":
    main()
