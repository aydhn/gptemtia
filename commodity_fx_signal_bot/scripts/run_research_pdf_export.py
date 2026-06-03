import argparse
import sys
import logging
from config.settings import settings
from config.paths import DATA_DIR
from data.storage.data_lake import DataLake
from report_exports.export_pipeline import ReportExportPipeline
from report_exports.export_config import get_report_export_profile
import reports.report_builder as rb
from config.paths import REPORTS_REPORT_EXPORTS_DIR

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Export research report to PDF.")
    parser.add_argument("--symbol", type=str, help="Symbol to export")
    parser.add_argument("--report-type", type=str, choices=["symbol", "universe", "daily_digest"], default="symbol")
    parser.add_argument("--timeframe", type=str, default="1d")
    parser.add_argument("--research-profile", type=str, default="balanced_research_report")
    parser.add_argument("--export-profile", type=str, default="pdf_focused_report_export")
    parser.add_argument("--no-save", action="store_true", help="Do not save output")

    args = parser.parse_args()

    data_lake = DataLake(DATA_DIR / "lake")
    try:
        profile = get_report_export_profile(args.export_profile)
    except Exception as e:
        logger.error(f"Invalid export profile: {e}")
        sys.exit(1)

    pipeline = ReportExportPipeline(data_lake, settings, profile)
    save = not args.no_save

    if args.report_type == "symbol":
        if not args.symbol:
            logger.error("Symbol is required for symbol report type.")
            sys.exit(1)
        _, summary = pipeline.export_symbol_report(args.symbol, args.timeframe, args.research_profile, profile, save)
    elif args.report_type == "universe":
        _, summary = pipeline.export_universe_report(args.timeframe, args.research_profile, profile, save)
    elif args.report_type == "daily_digest":
        _, summary = pipeline.export_daily_digest(args.timeframe, args.research_profile, profile, save)

    if summary.get("status") == "missing_report":
        logger.warning(f"No existing research report found for export: {summary}")
    else:
        logger.info(f"Export summary: {summary}")
        if save:
            report_text = rb.build_pdf_export_report(summary)
            out_path = REPORTS_REPORT_EXPORTS_DIR / "pdf_export_report.txt"
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(report_text)
            logger.info(f"Saved pdf_export_report.txt to {out_path}")

if __name__ == "__main__":
    main()
