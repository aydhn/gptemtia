#!/usr/bin/env python3
"""
Orchestration workflow status report.
"""
import logging
import sys
from pathlib import Path

# Add project root to path
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.storage.data_lake import DataLake
from config.settings import settings
from orchestration.job_registry import list_registered_jobs, validate_registered_jobs
from orchestration.workflow_templates import list_workflow_templates, validate_workflow_templates
from reports.report_builder import build_workflow_status_report

def main():
    logging.basicConfig(level=getattr(logging, settings.log_level))
    logger = logging.getLogger(__name__)

    try:
        from config.paths import DATA_DIR
        dl = DataLake(DATA_DIR)

        jobs = list_registered_jobs()
        job_validation = validate_registered_jobs()

        templates = list_workflow_templates()
        template_validation = validate_workflow_templates(jobs)

        runs_df = dl.list_orchestration_runs()

        summary = {
            "registered_jobs_count": len(jobs),
            "job_registry_valid": job_validation["valid"],
            "templates_count": len(templates),
            "template_registry_valid": template_validation["valid"],
            "total_runs": len(runs_df) if not runs_df.empty else 0
        }


        report_text = build_workflow_status_report(runs_df, summary)

        from config.paths import ORCHESTRATION_REPORT_OUTPUT_DIR
        ORCHESTRATION_REPORT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        txt_path = ORCHESTRATION_REPORT_OUTPUT_DIR / "workflow_status_report.txt"
        with open(txt_path, "w") as f:
            f.write(report_text)

        if not runs_df.empty:
            csv_path = ORCHESTRATION_REPORT_OUTPUT_DIR / "workflow_status.csv"
            runs_df.to_csv(csv_path, index=False)

        print(f"\nReport generated successfully: {txt_path}")
        print(report_text)

    except Exception as e:
        logger.error(f"Error generating workflow status report: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
