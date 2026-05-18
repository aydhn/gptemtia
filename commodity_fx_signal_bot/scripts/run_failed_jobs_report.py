#!/usr/bin/env python3
"""
Orchestration failed jobs report.
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
from orchestration.orchestration_config import get_default_orchestration_profile
from orchestration.retry_policy import build_retry_policy, summarize_retry_plan
from orchestration.orchestration_quality import check_failed_jobs
from reports.report_builder import build_failed_jobs_report

def main():
    parser = argparse.ArgumentParser(description="Report failed orchestration jobs.")
    parser.add_argument("--last", type=int, default=1, help="Number of last runs to check")

    args = parser.parse_args()

    logging.basicConfig(level=getattr(logging, settings.log_level))
    logger = logging.getLogger(__name__)

    try:
        from config.paths import DATA_DIR
        dl = DataLake(DATA_DIR)

        runs_df = dl.list_orchestration_runs()

        if runs_df.empty:
             print("No orchestration runs found.")
             sys.exit(0)

        runs_to_check = runs_df.head(args.last).to_dict('records')

        all_failed = []
        for run in runs_to_check:
             try:
                 manifest = dl.load_orchestration_run_manifest(run["run_id"])
                 results = manifest.get("results", [])
                 for r in results:
                     if r.get("status") in ["job_failed", "job_blocked"]:
                          r["run_id"] = run["run_id"]
                          all_failed.append(r)
             except Exception as e:
                 logger.warning(f"Could not load manifest for {run['run_id']}: {e}")

        if not all_failed:
             df = pd.DataFrame(columns=["run_id", "job_id", "symbol", "status", "error_message"])
             summary = {"failed_count": 0, "blocked_count": 0, "retry_plan": {}}
        else:
             df = pd.DataFrame(all_failed)
             # Convert dicts back to simple mock objects for the retry planner
             class MockResult:
                 def __init__(self, d):
                     self.job_id = d.get("job_id")
                     self.symbol = d.get("symbol")
                     self.status = d.get("status")
                     self.attempts = d.get("attempts", 1)

             mock_results = [MockResult(d) for d in all_failed]
             failed_summary = check_failed_jobs(mock_results)

             profile = get_default_orchestration_profile()
             policy = build_retry_policy(profile)
             retry_plan = summarize_retry_plan(mock_results, policy)

             summary = {
                 "failed_count": failed_summary["failed_count"],
                 "blocked_count": failed_summary["blocked_count"],
                 "retry_plan": retry_plan
             }


        report_text = build_failed_jobs_report(summary, df)

        from config.paths import ORCHESTRATION_REPORT_OUTPUT_DIR
        ORCHESTRATION_REPORT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        txt_path = ORCHESTRATION_REPORT_OUTPUT_DIR / "failed_jobs_report.txt"
        with open(txt_path, "w") as f:
            f.write(report_text)

        csv_path = ORCHESTRATION_REPORT_OUTPUT_DIR / "failed_jobs.csv"
        df.to_csv(csv_path, index=False)

        print(f"\nReport generated successfully: {txt_path}")
        print(report_text)

    except Exception as e:
        logger.error(f"Error generating failed jobs report: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
