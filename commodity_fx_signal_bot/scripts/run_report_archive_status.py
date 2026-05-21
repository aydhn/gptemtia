import argparse
import sys
import logging
from config.settings import settings
from data.storage.data_lake import DataLake
from report_exports.report_archive import ReportArchive
import reports.report_builder as rb
from config.paths import REPORTS_REPORT_EXPORTS_DIR, LAKE_REPORT_EXPORTS_ARCHIVE_DIR

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Check Report Archive Status")
    parser.parse_args()

    archive = ReportArchive(LAKE_REPORT_EXPORTS_ARCHIVE_DIR)
    df = archive.load_records()
    summary = archive.summarize()

    logger.info(f"Archive summary: {summary}")

    report_text = rb.build_report_archive_status_report(df, summary)

    out_dir = REPORTS_REPORT_EXPORTS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    out_txt = out_dir / "report_archive_status_report.txt"
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write(report_text)

    out_csv = out_dir / "report_archive_status.csv"
    df.to_csv(out_csv, index=False)

    logger.info(f"Saved status to {out_txt} and {out_csv}")

if __name__ == "__main__":
    main()
