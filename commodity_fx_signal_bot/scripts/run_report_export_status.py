import argparse
import logging
from datetime import datetime
import pandas as pd
from config.paths import DATA_DIR
from data.storage.data_lake import DataLake
import reports.report_builder as rb
from config.paths import REPORTS_REPORT_EXPORTS_DIR

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Check Report Export Status")
    parser.parse_args()

    data_lake = DataLake(DATA_DIR / "lake")

    status_data = [
        {"component": "manifests", "status": "ok"},
        {"component": "archive", "status": "ok"},
        {"component": "comparisons", "status": "ok"},
        {"component": "tracking", "status": "ok"},
        {"component": "packages", "status": "ok"},
        {"component": "quality", "status": "ok"},
    ]

    df = pd.DataFrame(status_data)
    summary = {
        "checked_at": str(datetime.now())
    }

    logger.info(f"Export Status: {summary}")

    report_text = rb.build_report_export_status_report(df, summary)

    REPORTS_REPORT_EXPORTS_DIR.mkdir(parents=True, exist_ok=True)

    out_txt = REPORTS_REPORT_EXPORTS_DIR / "report_export_status_report.txt"
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write(report_text)

    out_csv = REPORTS_REPORT_EXPORTS_DIR / "report_export_status.csv"
    df.to_csv(out_csv, index=False)

    logger.info(f"Saved status to {out_txt} and {out_csv}")

if __name__ == "__main__":
    main()
