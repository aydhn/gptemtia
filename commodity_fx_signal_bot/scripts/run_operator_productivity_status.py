import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from config.settings import settings
from analyst_ux.ux_config import get_analyst_ux_profile
from data.storage.data_lake import DataLake
from analyst_ux.ux_pipeline import AnalystUXPipeline
from reports.report_builder import *

def main():
    parser = argparse.ArgumentParser(description="Check operator productivity layer status.")
    parser.add_argument("--profile", type=str, default="balanced_analyst_productivity", help="UX profile name")
    parser.add_argument("--save", type=str, default="true", help="Save reports to DataLake")
    args = parser.parse_args()

    save_flag = args.save.lower() == "true"
    try:
        profile = get_analyst_ux_profile(args.profile)
    except Exception as e:
        print(f"Failed to load profile: {e}")
        return

    dl = DataLake(project_root)
    pipeline = AnalystUXPipeline(dl, settings, project_root, profile)

    print(f"Checking operator productivity status using profile: {profile.name}...")
    df, summary = pipeline.build_operator_productivity_status(save=save_flag)

    print("\n--- Operator Productivity Status Report ---")
    print(build_operator_productivity_status_report(df, summary))
    print(f"\nDone. Status Passed: {summary.get('passed', False)}")

if __name__ == "__main__":
    main()
