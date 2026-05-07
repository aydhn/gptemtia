import argparse
import sys
import logging
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from config.symbols import SymbolSpec
from config.settings import settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from backtesting.backtest_pipeline import BacktestPipeline
from backtesting.backtest_config import get_backtest_profile
from reports.report_builder import build_backtest_preview_report

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Run Backtest Preview")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to backtest")
    parser.add_argument(
        "--timeframe", type=str, default="1d", help="Timeframe (default: 1d)"
    )
    parser.add_argument(
        "--profile",
        type=str,
        default="balanced_candidate_backtest",
        help="Backtest profile name",
    )
    parser.add_argument(
        "--last", type=int, default=20, help="Number of last trades to show"
    )
    parser.add_argument("--save", action="store_true", help="Save outputs")

    args = parser.parse_args()

    paths = ProjectPaths()
    lake = DataLake(paths.lake_dir)

    try:
        profile = get_backtest_profile(args.profile)
    except Exception as e:
        logger.error(f"Failed to load profile: {e}")
        return

    pipeline = BacktestPipeline(lake, settings, profile)
    spec = SymbolSpec(args.symbol, "Mock", "metals", "precious", "USD")

    logger.info(
        f"Running backtest for {args.symbol} {args.timeframe} with profile {args.profile}"
    )

    trades_df, summary = pipeline.build_for_symbol_timeframe(
        spec, args.timeframe, profile, save=args.save
    )

    if trades_df.empty:
        logger.warning("No trades simulated.")
        return

    tail_df = trades_df.tail(args.last)
    report = build_backtest_preview_report(
        args.symbol, args.timeframe, args.profile, summary, tail_df
    )

    print(report)

    if args.save:
        out_path = (
            paths.backtest_reports
            / f"backtest_preview_{args.symbol}_{args.timeframe}_{args.profile}.txt"
        )
        with open(out_path, "w") as f:
            f.write(report)
        logger.info(f"Report saved to {out_path}")


if __name__ == "__main__":
    main()
