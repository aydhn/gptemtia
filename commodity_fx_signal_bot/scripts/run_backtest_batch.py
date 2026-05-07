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
from reports.report_builder import build_backtest_batch_report

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Run Backtest Batch")
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, help="Single symbol to run")
    parser.add_argument(
        "--timeframe", type=str, default="1d", help="Timeframe (default: 1d)"
    )
    parser.add_argument(
        "--profile",
        type=str,
        default="balanced_candidate_backtest",
        help="Backtest profile name",
    )
    parser.add_argument("--no-save", action="store_true", help="Do not save outputs")

    args = parser.parse_args()

    paths = ProjectPaths()
    lake = DataLake(paths.lake_dir)

    try:
        profile = get_backtest_profile(args.profile)
    except Exception as e:
        logger.error(f"Failed to load profile: {e}")
        return

    specs = []
    if args.symbol:
        specs.append(
            SymbolSpec(
                args.symbol, "Mock", args.asset_class or "metals", "precious", "USD"
            )
        )
    else:
        # Dummy specs for now since we don't have universe loading here directly
        specs = [
            SymbolSpec("GC=F", "Gold", "metals", "precious", "USD"),
            SymbolSpec("SI=F", "Silver", "metals", "precious", "USD"),
        ]

    pipeline = BacktestPipeline(lake, settings, profile)

    logger.info(f"Running batch backtest for {len(specs)} symbols")

    summary = pipeline.build_for_universe(
        specs, args.timeframe, profile, limit=args.limit, save=not args.no_save
    )

    report = build_backtest_batch_report(summary)
    print(report)

    if not args.no_save:
        out_path = paths.backtest_reports / "backtest_batch_summary.txt"
        with open(out_path, "w") as f:
            f.write(report)
        logger.info(f"Report saved to {out_path}")


if __name__ == "__main__":
    main()
