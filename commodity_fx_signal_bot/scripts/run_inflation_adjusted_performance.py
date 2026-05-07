import argparse
import sys
import logging
import json
import pandas as pd

from config.settings import settings
from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from backtesting.inflation_adjusted import build_inflation_adjusted_performance
from config.paths import ProjectPaths
import reports.report_builder as builder

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Run inflation adjusted performance for a single symbol."
    )
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to analyze")
    parser.add_argument(
        "--timeframe", type=str, default="1d", help="Timeframe (default: 1d)"
    )
    parser.add_argument(
        "--backtest-profile",
        type=str,
        default="balanced_candidate_backtest",
        help="Backtest profile name",
    )
    parser.add_argument(
        "--save", action="store_true", help="Save the resulting report to disk"
    )

    args = parser.parse_args()

    logger.info(
        f"Starting inflation adjusted performance preview for {args.symbol} ({args.timeframe})"
    )

    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found in universe.")
        sys.exit(1)

    p = ProjectPaths()
    data_lake = DataLake(str(p.lake_dir))

    equity_curve = data_lake.load_backtest_equity_curve(
        args.symbol, args.timeframe, args.backtest_profile
    )
    if equity_curve.empty:
        logger.error(f"Empty equity curve for {args.symbol}. Run backtest first.")
        sys.exit(1)

    if hasattr(data_lake, "load_macro_features"):
        macro_df = data_lake.load_macro_features(args.timeframe)
    else:
        macro_df = pd.DataFrame()

    aligned_df, summary = build_inflation_adjusted_performance(equity_curve, macro_df)

    if not summary:
        logger.warning("No inflation data available or unable to align.")

    if hasattr(builder, "build_inflation_adjusted_performance_report"):
        report = builder.build_inflation_adjusted_performance_report(
            args.symbol, args.timeframe, args.backtest_profile, summary
        )
    else:
        report = json.dumps(summary, indent=4)

    print(report)

    if args.save:
        out_dir = (
            p.performance_reports
            if hasattr(p, "performance_reports")
            else p.reports_dir / "performance_reports"
        )
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = (
            out_dir
            / f"inflation_adjusted_performance_{args.symbol}_{args.timeframe}_{args.backtest_profile}.txt"
        )
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(report)
        logger.info(f"Report saved to {out_file}")


if __name__ == "__main__":
    main()
