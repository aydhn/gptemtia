import argparse
import sys
import logging
import pandas as pd
from pathlib import Path

from config.settings import settings
from config.paths import REPORTS_SIZING_REPORTS_DIR
from config.symbols import get_enabled_symbols
from data.storage.data_lake import DataLake
from sizing.sizing_pipeline import SizingPipeline
from sizing.sizing_config import get_sizing_profile
from reports.report_builder import build_sizing_batch_report

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Batch Build Sizing Candidates")
    parser.add_argument("--limit", type=int, help="Limit number of symbols to process")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class (e.g. metals)")
    parser.add_argument("--symbol", type=str, help="Process a single symbol")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g. 1d)")
    parser.add_argument("--profile", type=str, default="balanced_theoretical_sizing", help="Sizing profile name")
    parser.add_argument("--save", action="store_true", default=True, help="Save the generated candidates")

    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)

    try:
        profile = get_sizing_profile(args.profile)
    except Exception as e:
        logger.error(f"Error loading profile: {e}")
        sys.exit(1)

    all_specs = get_enabled_symbols()

    if args.symbol:
        specs = [s for s in all_specs if s.symbol == args.symbol]
    elif args.asset_class:
        specs = [s for s in all_specs if s.asset_class == args.asset_class]
    else:
        specs = all_specs

    if not specs:
        logger.error("No symbols matched criteria.")
        sys.exit(1)

    data_lake = DataLake()
    pipeline = SizingPipeline(data_lake, settings, profile)

    logger.info(f"Running sizing batch build for {len(specs)} symbols ({args.timeframe}) with profile {args.profile}")

    res = pipeline.build_for_universe(specs, args.timeframe, profile, args.limit, args.save)

    report_text = build_sizing_batch_report(res)
    print(report_text)

    REPORTS_SIZING_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS_SIZING_REPORTS_DIR / "sizing_batch_summary.txt"
    with open(report_path, "w") as f:
        f.write(report_text)

    csv_path = REPORTS_SIZING_REPORTS_DIR / "sizing_batch_summary.csv"
    summary_data = res.get("summary", {})
    if summary_data:
        df = pd.DataFrame([summary_data])
        # dicts inside df will be stringified in csv but that's fine for simple summary
        df.to_csv(csv_path, index=False)

    logger.info(f"Saved batch report to {report_path} and {csv_path}")

if __name__ == "__main__":
    main()
