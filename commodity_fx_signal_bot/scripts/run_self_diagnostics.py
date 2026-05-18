#!/usr/bin/env python3
"""
Script to run full self-diagnostics and generate reports.
"""

import argparse
import logging
import json

from config.settings import settings
from config.paths import ProjectPaths
from config.symbols import DEFAULT_SYMBOL_UNIVERSE as ALL_SYMBOLS
from data.storage.data_lake import DataLake
from observability.observability_config import get_observability_profile
from observability.observability_pipeline import ObservabilityPipeline
from reports.report_builder import build_self_diagnostics_report

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Run Self Diagnostics.")
    parser.add_argument("--symbol", type=str, help="Specific symbol to check")
    parser.add_argument("--asset-class", type=str, help="Specific asset class to check")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe to check")
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    parser.add_argument("--profile", type=str, default="balanced_system_observability", help="Observability profile to use.")
    parser.add_argument("--save", action="store_true", default=True, help="Save report to DataLake and output files.")
    parser.add_argument("--no-save", action="store_false", dest="save", help="Do not save reports.")
    args = parser.parse_args()

    logger.info("Initializing DataLake...")
    paths = ProjectPaths()
    data_lake = DataLake(paths)

    logger.info(f"Loading Observability Profile: {args.profile}...")
    profile = get_observability_profile(args.profile)

    pipeline = ObservabilityPipeline(data_lake, settings, profile)

    # Filter symbols
    symbols = [s for s in ALL_SYMBOLS if s.enabled]
    if args.symbol:
        symbols = [s for s in symbols if s.symbol == args.symbol]
    elif args.asset_class:
        symbols = [s for s in symbols if s.asset_class == args.asset_class]

    if args.limit:
        symbols = symbols[:args.limit]

    logger.info(f"Running Self Diagnostics for {len(symbols)} symbols...")
    details, summary = pipeline.run_self_diagnostics(symbols=symbols, timeframe=args.timeframe, limit=args.limit, save=args.save)

    logger.info(f"Overall Health Status: {summary.get('overall_health_status', 'unknown')}")
    logger.info(f"Overall Health Score: {summary.get('overall_health_score', 0.0):.2f}")

    if args.save:
        report_text = build_self_diagnostics_report(summary)
        out_dir = paths.REPORTS_OBSERVABILITY_DIR
        out_dir.mkdir(parents=True, exist_ok=True)

        txt_path = out_dir / "self_diagnostics_report.txt"
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(report_text)

        json_path = out_dir / "self_diagnostics.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        logger.info(f"Saved text report to: {txt_path}")
        logger.info(f"Saved JSON report to: {json_path}")

if __name__ == "__main__":
    main()
