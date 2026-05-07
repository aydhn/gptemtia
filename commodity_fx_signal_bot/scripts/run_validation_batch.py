#!/usr/bin/env python
"""
Script to run validation across multiple symbols.
"""

import argparse
import logging
import sys
import pandas as pd
from pathlib import Path

import os
project_root = str(Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config.settings import settings
from config.paths import ensure_project_directories, REPORTS_VALIDATION_DIR
from config.symbols import get_symbol_spec, get_enabled_symbols
from data.storage.data_lake import DataLake
from validation.validation_pipeline import ValidationPipeline
from validation.validation_config import get_validation_profile
from reports.report_builder import build_validation_batch_report

logging.basicConfig(level=getattr(logging, settings.log_level), format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Run validation batch.")
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, help="Specific symbol")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe")
    parser.add_argument("--profile", type=str, default="balanced_walk_forward_validation", help="Validation profile")
    parser.add_argument("--backtest-profile", type=str, default="balanced_candidate_backtest", help="Backtest profile")
    parser.add_argument("--no-save", action="store_true", help="Do not save outputs")

    args = parser.parse_args()
    ensure_project_directories()

    try:
        profile = get_validation_profile(args.profile)
    except Exception as e:
        logger.error(f"Error: {e}")
        return

    specs = []
    if args.symbol:
         specs = [get_symbol_spec(args.symbol)]
    elif args.asset_class:
         universe = get_enabled_symbols()
         specs = [s for s in universe if s.asset_class == args.asset_class]
    else:
         specs = get_enabled_symbols()

    data_lake = DataLake(settings)
    pipeline = ValidationPipeline(data_lake, settings, profile)

    res = pipeline.run_universe_validation(specs, args.timeframe, args.backtest_profile, profile, limit=args.limit, save=not args.no_save)

    ranking_df = pd.DataFrame(res["ranking"])
    report_text = build_validation_batch_report(res, ranking_df)

    print("\n" + report_text)

    txt_path = REPORTS_VALIDATION_DIR / "validation_batch_summary.txt"
    csv_path = REPORTS_VALIDATION_DIR / "validation_batch_summary.csv"

    txt_path.write_text(report_text, encoding="utf-8")
    if not ranking_df.empty:
        ranking_df.to_csv(csv_path, index=False)

    logger.info(f"Reports saved to {txt_path} and {csv_path}")

if __name__ == "__main__":
    main()
