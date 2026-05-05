import argparse
import logging

from config.paths import LAKE_DIR, REPORTS_DIR
from config.settings import settings
from config.symbols import (
    get_enabled_symbols,
    get_symbol_spec,
    get_symbols_by_asset_class,
)
from data.storage.data_lake import DataLake
from reports.report_builder import build_strategy_batch_report
from strategies.strategy_config import get_strategy_selection_profile
from strategies.strategy_pipeline import StrategyPipeline

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Batch build strategy candidates")
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, help="Single symbol to process")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe")
    parser.add_argument(
        "--profile",
        type=str,
        default="balanced_strategy_selection",
        help="Strategy profile",
    )
    parser.add_argument("--save", action="store_true", default=True, help="Save output")
    args = parser.parse_args()

    specs = []
    if args.symbol:
        spec = get_symbol_spec(args.symbol)
        if spec:
            specs = [spec]
    elif args.asset_class:
        specs = get_symbols_by_asset_class(args.asset_class)
    else:
        specs = get_enabled_symbols()

    data_lake = DataLake(LAKE_DIR)

    try:
        profile = get_strategy_selection_profile(args.profile)
    except Exception as e:
        logger.error(f"Error loading profile: {e}")
        return

    pipeline = StrategyPipeline(data_lake, settings, profile)

    summary = pipeline.build_for_universe(
        specs, args.timeframe, profile, limit=args.limit, save=args.save
    )

    report = build_strategy_batch_report(summary)
    print("\n" + report + "\n")

    out_dir = REPORTS_DIR / "strategy_reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "strategy_batch_summary.txt"
    out_file.write_text(report, encoding="utf-8")
    logger.info(f"Report saved to {out_file}")


if __name__ == "__main__":
    main()
