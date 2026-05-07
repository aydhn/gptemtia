import argparse
import sys
import logging
import pandas as pd

from config.settings import settings
from config.symbols import get_symbol_spec, get_enabled_symbols
from data.storage.data_lake import DataLake
from backtesting.performance_pipeline import PerformanceAnalysisPipeline
from config.paths import ProjectPaths
import reports.report_builder as builder

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Run performance analysis for multiple symbols."
    )
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, help="Run for specific symbol")
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
        "--save",
        action="store_true",
        default=True,
        help="Save the resulting report to disk",
    )

    args = parser.parse_args()

    logger.info(f"Starting performance batch analysis ({args.timeframe})")

    universe = get_enabled_symbols()
    specs = universe

    if args.symbol:
        specs = [s for s in universe if s.symbol == args.symbol]
    elif args.asset_class:
        specs = [s for s in universe if s.asset_class == args.asset_class]

    if args.limit:
        specs = specs[: args.limit]

    if not specs:
        logger.error("No symbols selected.")
        sys.exit(1)

    p = ProjectPaths()
    data_lake = DataLake(str(p.lake_dir))
    pipeline = PerformanceAnalysisPipeline(data_lake, settings)

    batch_result = pipeline.analyze_universe_performance(
        specs, args.timeframe, args.backtest_profile, args.limit, args.save
    )

    ranking_df = pd.DataFrame(batch_result["ranking"])

    if hasattr(builder, "build_performance_batch_report"):
        report = builder.build_performance_batch_report(batch_result, ranking_df)
    else:
        report = (
            "Batch analysis completed. Missing ReportBuilder support.\n"
            + ranking_df.to_string()
            if not ranking_df.empty
            else "No results."
        )

    print(report)

    if args.save and not ranking_df.empty:
        out_dir = (
            p.performance_reports
            if hasattr(p, "performance_reports")
            else p.reports_dir / "performance_reports"
        )
        out_dir.mkdir(parents=True, exist_ok=True)

        txt_file = out_dir / "performance_batch_summary.txt"
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(report)

        csv_file = out_dir / "performance_batch_summary.csv"
        ranking_df.to_csv(csv_file, index=False)

        logger.info(f"Saved batch summary to {out_dir}")


if __name__ == "__main__":
    main()
