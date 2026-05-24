import argparse
import sys
import os
from pathlib import Path
import pandas as pd

# Fix python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import Settings
from config.paths import ProjectPaths, ensure_project_directories
from data.storage.data_lake import DataLake
from governance.governance_pipeline import GovernancePipeline
from governance.governance_config import get_governance_profile
import reports.report_builder as rb

def parse_args():
    parser = argparse.ArgumentParser(description="Run Full Research Governance Report")
    parser.add_argument("--profile", type=str, default="balanced_research_governance")
    parser.add_argument("--save", type=bool, default=True)
    return parser.parse_args()

def main():
    args = parse_args()

    settings = Settings()
    paths = ProjectPaths()
    ensure_project_directories()

    data_lake = DataLake(paths)
    profile = get_governance_profile(args.profile)

    pipeline = GovernancePipeline(data_lake=data_lake, settings=settings, project_root=paths.project_root, profile=profile)

    res, summary = pipeline.build_research_governance_report(save=args.save)


    # Check if checklist exists in summary to pass checklist_df optionally
    checklist_df = pd.DataFrame() # would need to construct it, but text builder just uses summary for basic status
    txt_report = rb.build_research_governance_text_report(summary, checklist_df)

    if args.save:
        txt_path = paths.REPORTS_GOVERNANCE_TXT_DIR / "research_governance_report.txt"
        txt_path.parent.mkdir(parents=True, exist_ok=True)
        with open(txt_path, "w") as f:
            f.write(txt_report)

        print(f"Research governance report generated at {txt_path}")
    else:
        print(txt_report)

if __name__ == "__main__":
    main()
