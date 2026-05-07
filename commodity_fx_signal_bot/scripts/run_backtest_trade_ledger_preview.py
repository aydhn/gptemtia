import argparse
import sys
import logging
from pathlib import Path
import pandas as pd

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from config.symbols import SymbolSpec
from config.settings import settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from backtesting.backtest_pipeline import BacktestPipeline
from backtesting.backtest_config import get_backtest_profile
from backtesting.trade_ledger import TradeLedger
from reports.report_builder import build_backtest_trade_ledger_report

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Run Backtest Trade Ledger Preview")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol")
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
        "--last", type=int, default=50, help="Number of last trades to show"
    )
    parser.add_argument("--rebuild", action="store_true", help="Force rebuild")

    args = parser.parse_args()

    paths = ProjectPaths()
    lake = DataLake(paths.lake_dir)

    try:
        profile = get_backtest_profile(args.profile)
    except Exception as e:
        logger.error(f"Failed to load profile: {e}")
        return

    trades_df = pd.DataFrame()
    summary = {}

    if not args.rebuild and hasattr(lake, "load_backtest_trades"):
        trades_df = lake.load_backtest_trades(args.symbol, args.timeframe, args.profile)
        if hasattr(lake, "load_backtest_summary"):
            s = lake.load_backtest_summary(args.symbol, args.timeframe, args.profile)
            if s and "run_summary" in s:
                summary = s["run_summary"]

    if trades_df.empty or args.rebuild:
        logger.info("Rebuilding backtest...")
        pipeline = BacktestPipeline(lake, settings, profile)
        spec = SymbolSpec(args.symbol, "Mock", "metals", "precious", "USD")
        trades_df, full_summary = pipeline.build_for_symbol_timeframe(
            spec, args.timeframe, profile, save=True
        )
        if "run_summary" in full_summary:
            summary = full_summary["run_summary"]

    if trades_df.empty:
        logger.warning("No trades found or generated.")
        return

    ledger = TradeLedger.from_dataframe(trades_df)
    ledger_summary = ledger.summarize()

    report = build_backtest_trade_ledger_report(
        args.symbol,
        args.timeframe,
        args.profile,
        ledger_summary,
        trades_df.tail(args.last),
    )

    print(report)

    out_path = (
        paths.backtest_reports
        / f"backtest_trade_ledger_preview_{args.symbol}_{args.timeframe}_{args.profile}.txt"
    )
    with open(out_path, "w") as f:
        f.write(report)
    logger.info(f"Report saved to {out_path}")


if __name__ == "__main__":
    main()
