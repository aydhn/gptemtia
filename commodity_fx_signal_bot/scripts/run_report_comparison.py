import argparse
import sys
import logging
from config.settings import settings
from config.paths import DATA_DIR
from data.storage.data_lake import DataLake
from report_exports.export_pipeline import ReportExportPipeline
from report_exports.export_config import get_default_report_export_profile
import reports.report_builder as rb
from config.paths import REPORTS_REPORT_EXPORTS_COMPARISONS_DIR
from report_exports.report_comparison import summarize_report_comparisons

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Run Report Comparison")
    parser.add_argument("--symbol", type=str, help="Symbol to compare")
    parser.add_argument("--report-type", type=str, choices=["symbol", "universe", "daily_digest"], default="symbol")
    parser.add_argument("--timeframe", type=str, default="1d")
    parser.add_argument("--profile", type=str, default="balanced_research_report")
    parser.add_argument("--no-save", action="store_true", help="Do not save output")

    args = parser.parse_args()

    data_lake = DataLake(DATA_DIR / "lake")
    profile = get_default_report_export_profile()
    pipeline = ReportExportPipeline(data_lake, settings, profile)
    save = not args.no_save

    df, summary = pipeline.build_report_comparison(
        args.report_type, args.symbol, args.timeframe, args.profile, save
    )

    logger.info(f"Comparison Summary: {summary}")

    if save and not df.empty:
        comp_summary = summarize_report_comparisons(df)
        report_text = rb.build_report_comparison_text_report(df, comp_summary)

        REPORTS_REPORT_EXPORTS_COMPARISONS_DIR.mkdir(parents=True, exist_ok=True)

        out_txt = REPORTS_REPORT_EXPORTS_COMPARISONS_DIR / "report_comparison_report.txt"
        with open(out_txt, "w", encoding="utf-8") as f:
            f.write(report_text)

        out_csv = REPORTS_REPORT_EXPORTS_COMPARISONS_DIR / f"report_comparison_{args.report_type}_{args.timeframe}_{args.profile}.csv"
        df.to_csv(out_csv, index=False)

        logger.info(f"Saved comparison to {out_txt} and {out_csv}")
    elif df.empty:
        logger.info("No comparisons were generated (possibly insufficient history).")

if __name__ == "__main__":
    main()
