"""
Run ML Integration Status

Check the status of the data lake regarding ML integration files.
"""

import logging
from config.settings import Settings
from config.paths import ensure_project_directories
from data.storage.data_lake import DataLake
from reports.report_builder import build_ml_integration_status_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    ensure_project_directories()
    settings = Settings()
    from config.paths import PROJECT_ROOT
    data_lake = DataLake(PROJECT_ROOT / 'data' / 'lake')

    logger.info("Checking ML Integration Status in Data Lake")

    try:
        status_df = data_lake.list_ml_integration_reports()
    except Exception as e:
        logger.error(f"Error listing ML integration reports: {e}")
        status_df = None

    summary = {"total_files": len(status_df) if status_df is not None else 0}

    report_str = build_ml_integration_status_report(status_df, summary)
    print("\n" + report_str)

    from config.paths import REPORTS_ML_INTEGRATION_REPORTS_DIR
    out_txt = REPORTS_ML_INTEGRATION_REPORTS_DIR / "ml_integration_status_report.txt"
    with open(out_txt, "w") as f:
        f.write(report_str)

    if status_df is not None and not status_df.empty:
        out_csv = REPORTS_ML_INTEGRATION_REPORTS_DIR / "ml_integration_status.csv"
        status_df.to_csv(out_csv, index=False)

    logger.info("Status check complete.")


if __name__ == "__main__":
    main()
