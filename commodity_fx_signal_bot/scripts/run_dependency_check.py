#!/usr/bin/env python3
"""
Orchestration dependency check.
"""
import argparse
import logging
import sys
from pathlib import Path

# Add project root to path
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.storage.data_lake import DataLake
from config.settings import settings
from config.symbols import group_symbols_by_asset_class, get_symbols_by_asset_class
from orchestration.orchestration_config import get_orchestration_profile, get_default_orchestration_profile
from orchestration.pipeline_orchestrator import PipelineOrchestrator
from reports.report_builder import build_dependency_check_report

def main():
    parser = argparse.ArgumentParser(description="Check pipeline dependencies.")
    parser.add_argument("--workflow", type=str, default="daily_research_workflow", help="Workflow template name")
    parser.add_argument("--symbol", type=str, help="Specific symbol to check")
    parser.add_argument("--asset-class", type=str, choices=list(group_symbols_by_asset_class().keys()), help="Asset class to check")
    parser.add_argument("--limit", type=int, help="Limit number of symbols to check")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g., 1d, 1h)")
    parser.add_argument("--profile", type=str, default="balanced_research_orchestration", help="Orchestration profile")
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

        try:
            profile = get_orchestration_profile(args.profile)
        except Exception:
            profile = get_default_orchestration_profile()

        orchestrator = PipelineOrchestrator(dl, settings, profile)

        jobs = orchestrator._resolve_workflow_jobs(args.workflow)
        df, summary = orchestrator.checker.check_workflow_dependencies(jobs, symbols, args.timeframe)


        report_text = build_dependency_check_report(summary, df)

        if args.save:
            from config.paths import ORCHESTRATION_REPORT_OUTPUT_DIR
            ORCHESTRATION_REPORT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            txt_path = ORCHESTRATION_REPORT_OUTPUT_DIR / "dependency_check_report.txt"
            with open(txt_path, "w") as f:
                f.write(report_text)

            csv_path = ORCHESTRATION_REPORT_OUTPUT_DIR / "dependency_check.csv"
            df.to_csv(csv_path, index=False)
            print(f"\nReport generated successfully: {txt_path}")

        print(report_text)

    except Exception as e:
        logger.error(f"Error checking dependencies: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
