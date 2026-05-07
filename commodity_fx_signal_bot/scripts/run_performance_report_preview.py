import argparse
import sys
import logging
import json
from pathlib import Path

from config.settings import settings
from config.symbols import get_symbol_spec
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
        description="Run advanced performance analysis for a single symbol."
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
        f"Starting performance analysis preview for {args.symbol} ({args.timeframe})"
    )

    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found in universe.")
        sys.exit(1)

    p = ProjectPaths()
    data_lake = DataLake(str(p.lake_dir))
    pipeline = PerformanceAnalysisPipeline(data_lake, settings)

    summary, _ = pipeline.analyze_symbol_performance(
        spec, args.timeframe, args.backtest_profile, save=args.save
    )

    if not summary:
        logger.error(
            "Failed to generate performance summary. Check if backtest outputs exist."
        )
        sys.exit(1)

    if hasattr(builder, "build_performance_report_preview"):
        report = builder.build_performance_report_preview(
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
            / f"performance_report_preview_{args.symbol}_{args.timeframe}_{args.backtest_profile}.txt"
        )
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(report)
        logger.info(f"Report saved to {out_file}")


if __name__ == "__main__":
    main()
