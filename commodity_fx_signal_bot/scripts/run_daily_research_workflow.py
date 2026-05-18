#!/usr/bin/env python3
"""
Run daily research workflow.
"""
import argparse
import logging
import sys
import pandas as pd
from pathlib import Path

# Add project root to path
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.storage.data_lake import DataLake
from config.settings import settings
from config.symbols import group_symbols_by_asset_class, get_symbols_by_asset_class
from orchestration.orchestration_config import get_orchestration_profile
from orchestration.pipeline_orchestrator import PipelineOrchestrator
from reports.report_builder import build_daily_research_workflow_report

def main():
    parser = argparse.ArgumentParser(description="Run daily research workflow.")
    parser.add_argument("--symbol", type=str, help="Specific symbol to process")
    parser.add_argument("--asset-class", type=str, choices=list(group_symbols_by_asset_class().keys()), help="Asset class to process")
    parser.add_argument("--limit", type=int, help="Limit number of symbols to process")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g., 1d, 1h)")
    parser.add_argument("--run", action="store_true", default=False, help="Actually run jobs (disable dry-run)")
    parser.add_argument("--save", action="store_true", default=True, help="Save report")

    args = parser.parse_args()

    logging.basicConfig(level=getattr(logging, settings.log_level))
    logger = logging.getLogger(__name__)

    try:
        symbols = []
        if args.symbol:
            symbols = [args.symbol]
        elif args.asset_class:
            symbols = get_symbols_by_asset_class(args.asset_class)

        if args.limit and len(symbols) > args.limit:
            symbols = symbols[:args.limit]

        from config.paths import DATA_DIR
        dl = DataLake(DATA_DIR)
        profile = get_orchestration_profile("balanced_research_orchestration")
        orchestrator = PipelineOrchestrator(dl, settings, profile)

        dry_run = not args.run
        if args.run:
             print("WARNING: Running in actual mode (dry_run=False).")

        manifest, summary = orchestrator.run_workflow("daily_research_workflow", symbols, args.timeframe, dry_run=dry_run, save=args.save)

        df = pd.DataFrame(manifest.results) if manifest.results else None

        report_text = build_daily_research_workflow_report(summary, df)

        if args.save:
            from config.paths import ORCHESTRATION_REPORT_OUTPUT_DIR
            ORCHESTRATION_REPORT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            txt_path = ORCHESTRATION_REPORT_OUTPUT_DIR / "daily_research_workflow_report.txt"
            with open(txt_path, "w") as f:
                f.write(report_text)
            print(f"\nReport generated successfully: {txt_path}")

        print(report_text)

    except Exception as e:
        logger.error(f"Error running daily research workflow: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
