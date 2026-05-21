import argparse
import sys
import logging
import pandas as pd
from config.settings import settings
from data.storage.data_lake import DataLake
from report_exports.export_pipeline import ReportExportPipeline
from report_exports.export_config import get_report_export_profile
import reports.report_builder as rb
from config.paths import REPORTS_REPORT_EXPORTS_DIR

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Batch Export Research Reports")
    parser.add_argument("--symbol", type=str, help="Symbol to export")
    parser.add_argument("--asset-class", type=str, help="Asset class (unused placeholder)")
    parser.add_argument("--limit", type=int, help="Limit", default=10)
    parser.add_argument("--timeframe", type=str, default="1d")
    parser.add_argument("--research-profile", type=str, default="balanced_research_report")
    parser.add_argument("--export-profile", type=str, default="balanced_report_export")
    parser.add_argument("--include-pdf", action="store_true", help="Include PDF")
    parser.add_argument("--no-save", action="store_true", help="Do not save output")

    args = parser.parse_args()

    data_lake = DataLake()
    profile = get_report_export_profile(args.export_profile)

    if args.include_pdf:
        pass

    pipeline = ReportExportPipeline(data_lake, settings, profile)
    save = not args.no_save

    batch_results = []

    symbols_to_run = [args.symbol] if args.symbol else ["GC=F", "EURUSD=X"]
    symbols_to_run = symbols_to_run[:args.limit]

    for sym in symbols_to_run:
        logger.info(f"Exporting symbol report for {sym}")
        _, s = pipeline.export_symbol_report(sym, args.timeframe, args.research_profile, profile, save)
        batch_results.append({
            "report_id": s.get("report_id"),
            "symbol": sym,
            "html_status": s.get("html_status"),
            "pdf_status": s.get("pdf_status"),
            "archive_status": "success" if s.get("archive_id") else "missing",
            "quality_passed": s.get("quality_passed"),
            "warnings": s.get("warnings", [])
        })

    logger.info("Exporting universe report")
    _, s = pipeline.export_universe_report(args.timeframe, args.research_profile, profile, save)
    batch_results.append({
            "report_id": s.get("report_id"),
            "symbol": "UNIVERSE",
            "html_status": s.get("html_status"),
            "pdf_status": s.get("pdf_status"),
            "archive_status": "success" if s.get("archive_id") else "missing",
            "quality_passed": s.get("quality_passed"),
            "warnings": s.get("warnings", [])
    })

    logger.info("Exporting daily digest")
    _, s = pipeline.export_daily_digest(args.timeframe, args.research_profile, profile, save)
    batch_results.append({
            "report_id": s.get("report_id"),
            "symbol": "DIGEST",
            "html_status": s.get("html_status"),
            "pdf_status": s.get("pdf_status"),
            "archive_status": "success" if s.get("archive_id") else "missing",
            "quality_passed": s.get("quality_passed"),
            "warnings": s.get("warnings", [])
    })

    df = pd.DataFrame(batch_results)
    summary = {
        "total_exports": len(df),
        "success_count": len(df[df["quality_passed"] == True]) if "quality_passed" in df.columns else 0
    }

    if save:
        report_text = rb.build_report_export_batch_report(summary, df)

        REPORTS_REPORT_EXPORTS_DIR.mkdir(parents=True, exist_ok=True)

        out_txt = REPORTS_REPORT_EXPORTS_DIR / "report_export_batch_report.txt"
        with open(out_txt, "w", encoding="utf-8") as f:
            f.write(report_text)

        out_csv = REPORTS_REPORT_EXPORTS_DIR / "report_export_batch_summary.csv"
        df.to_csv(out_csv, index=False)

        logger.info(f"Saved batch summary to {out_txt} and {out_csv}")

if __name__ == "__main__":
    main()
