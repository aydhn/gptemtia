import argparse
import sys
import os
from pathlib import Path

# Fix python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import Settings
from config.paths import ProjectPaths, ensure_project_directories
from data.storage.data_lake import DataLake
from governance.governance_pipeline import GovernancePipeline
from governance.governance_config import get_governance_profile
import reports.report_builder as rb

def parse_args():
    parser = argparse.ArgumentParser(description="Run Artifact Inventory Report")
    parser.add_argument("--profile", type=str, default="balanced_research_governance", help="Governance profile to use")
    parser.add_argument("--save", type=bool, default=True, help="Whether to save the outputs")
    return parser.parse_args()

def main():
    args = parse_args()

    settings = Settings()
    if not getattr(settings, "governance_enabled", True):
        print("Governance is disabled in settings.")
        return

    paths = ProjectPaths()
    ensure_project_directories()

    data_lake = DataLake(paths)
    profile = get_governance_profile(args.profile)

    pipeline = GovernancePipeline(data_lake=data_lake, settings=settings, project_root=paths.project_root, profile=profile)

    df, summary = pipeline.build_artifact_inventory_report(save=args.save)


    txt_report = rb.build_artifact_inventory_text_report(summary, df)

    if args.save:
        txt_path = paths.REPORTS_GOVERNANCE_TXT_DIR / "artifact_inventory_report.txt"
        txt_path.parent.mkdir(parents=True, exist_ok=True)
        with open(txt_path, "w") as f:
            f.write(txt_report)

        csv_path = paths.REPORTS_GOVERNANCE_CSV_DIR / "artifact_inventory.csv"
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(csv_path, index=False)

        print(f"Artifact inventory report generated at {txt_path}")
    else:
        print(txt_report)

if __name__ == "__main__":
    main()
