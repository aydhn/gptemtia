import argparse
import sys
import logging
from config.settings import settings
from data.storage.data_lake import DataLake
from report_exports.export_pipeline import ReportExportPipeline
from report_exports.export_config import get_default_report_export_profile
import reports.report_builder as rb
from config.paths import REPORTS_REPORT_EXPORTS_TRACKING_DIR

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Run Periodic Tracking Report")
    parser.add_argument("--symbol", type=str, help="Symbol to track")
    parser.add_argument("--asset-class", type=str, help="Asset class (unused placeholder)")
    parser.add_argument("--limit", type=int, help="Limit (unused placeholder)")
    parser.add_argument("--timeframe", type=str, default="1d")
    parser.add_argument("--profile", type=str, default="balanced_research_report")
    parser.add_argument("--no-save", action="store_true", help="Do not save output")

    args = parser.parse_args()

    data_lake = DataLake()
    profile = get_default_report_export_profile()
    pipeline = ReportExportPipeline(data_lake, settings, profile)
    save = not args.no_save

    symbols = [args.symbol] if args.symbol else None

    df, summary = pipeline.build_periodic_tracking(
        symbols, args.timeframe, save
    )

    logger.info(f"Tracking Summary: {summary}")

    if save and not df.empty:
        report_text = rb.build_periodic_tracking_text_report(df, summary)

        REPORTS_REPORT_EXPORTS_TRACKING_DIR.mkdir(parents=True, exist_ok=True)

        out_txt = REPORTS_REPORT_EXPORTS_TRACKING_DIR / "periodic_tracking_report.txt"
        with open(out_txt, "w", encoding="utf-8") as f:
            f.write(report_text)

        out_csv = REPORTS_REPORT_EXPORTS_TRACKING_DIR / f"periodic_tracking_{args.timeframe}_{args.profile}.csv"
        df.to_csv(out_csv, index=False)

        logger.info(f"Saved tracking to {out_txt} and {out_csv}")
    elif df.empty:
        logger.info("No tracking records were generated.")

if __name__ == "__main__":
    main()
