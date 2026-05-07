#!/usr/bin/env python
"""
Script to run an optimizer candidate preview for a specific symbol.
"""

import argparse
import logging
import sys
from pathlib import Path

import os
project_root = str(Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config.settings import settings
from config.paths import ensure_project_directories, REPORTS_VALIDATION_DIR
from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from validation.validation_pipeline import ValidationPipeline
from validation.validation_config import get_validation_profile
from reports.report_builder import build_optimizer_candidate_preview_report

logging.basicConfig(level=getattr(logging, settings.log_level), format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Run optimizer candidate preview.")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to analyze")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe")
    parser.add_argument("--profile", type=str, default="balanced_walk_forward_validation", help="Validation profile name")
    parser.add_argument("--backtest-profile", type=str, default="balanced_candidate_backtest", help="Backtest profile name")
    parser.add_argument("--top", type=int, default=20, help="Number of top candidates to display")
    parser.add_argument("--save", action="store_true", help="Save the validation outputs")

    args = parser.parse_args()
    ensure_project_directories()

    try:
        spec = get_symbol_spec(args.symbol)
        profile = get_validation_profile(args.profile)
    except Exception as e:
        logger.error(f"Error: {e}")
        return

    data_lake = DataLake(settings)
    pipeline = ValidationPipeline(data_lake, settings, profile)

    df, summary = pipeline.run_optimizer_candidate_analysis(spec, args.timeframe, args.backtest_profile, profile, args.save)

    if df.empty:
         logger.warning("Validation returned empty result.")

    report_text = build_optimizer_candidate_preview_report(args.symbol, args.timeframe, args.profile, summary, df)
    print("\n" + report_text)

    report_path = REPORTS_VALIDATION_DIR / f"optimizer_candidate_preview_{args.symbol}_{args.timeframe}_{args.profile}.txt"
    report_path.write_text(report_text, encoding="utf-8")
    logger.info(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
