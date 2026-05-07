import argparse
import sys
from pathlib import Path
import logging

from config.settings import settings
from config.paths import REPORTS_SIZING_REPORTS_DIR
from data.storage.data_lake import DataLake
from sizing.sizing_pipeline import SizingPipeline
from sizing.sizing_config import get_sizing_profile
from config.symbols import get_symbol_spec
from reports.report_builder import build_sizing_candidate_preview_report

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Preview Sizing Candidates for a Symbol")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol code (e.g. GC=F)")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g. 1d)")
    parser.add_argument("--profile", type=str, default="balanced_theoretical_sizing", help="Sizing profile name")
    parser.add_argument("--last", type=int, default=10, help="Number of recent candidates to show")
    parser.add_argument("--save", action="store_true", help="Save the generated candidates")

    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)

    try:
        profile = get_sizing_profile(args.profile)
    except Exception as e:
        logger.error(f"Error loading profile: {e}")
        sys.exit(1)

    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found in manager.")
        sys.exit(1)

    data_lake = DataLake()
    pipeline = SizingPipeline(data_lake, settings, profile)

    logger.info(f"Running sizing candidate build for {args.symbol} ({args.timeframe}) with profile {args.profile}")

    df, summary = pipeline.build_for_symbol_timeframe(spec, args.timeframe, save=args.save)

    if df.empty:
        logger.warning(f"No sizing candidates produced. Summary: {summary}")
        return

    tail_df = df.tail(args.last)
    report_text = build_sizing_candidate_preview_report(args.symbol, args.timeframe, args.profile, summary, tail_df)

    print(report_text)

    REPORTS_SIZING_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS_SIZING_REPORTS_DIR / f"sizing_candidate_preview_{args.symbol}_{args.timeframe}_{args.profile}.txt"
    with open(report_path, "w") as f:
        f.write(report_text)
    logger.info(f"Saved preview report to {report_path}")

if __name__ == "__main__":
    main()
