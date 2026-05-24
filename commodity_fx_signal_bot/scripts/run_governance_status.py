import argparse
import sys
import os
import pandas as pd
from pathlib import Path

# Fix python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import Settings
from config.paths import ProjectPaths, ensure_project_directories
from data.storage.data_lake import DataLake
import reports.report_builder as rb

def parse_args():
    parser = argparse.ArgumentParser(description="Check Governance Status")
    return parser.parse_args()

def main():
    args = parse_args()

    paths = ProjectPaths()
    ensure_project_directories()

    data_lake = DataLake(paths)

    files = []

    gov_dirs = [
        paths.DATA_LAKE_GOVERNANCE_INVENTORY_DIR,
        paths.DATA_LAKE_GOVERNANCE_FINGERPRINTS_DIR,
        paths.DATA_LAKE_GOVERNANCE_PROVENANCE_DIR,
        paths.DATA_LAKE_GOVERNANCE_LINEAGE_DIR,
        paths.DATA_LAKE_GOVERNANCE_DEPENDENCIES_DIR,
        paths.DATA_LAKE_GOVERNANCE_AUDIT_DIR,
        paths.DATA_LAKE_GOVERNANCE_SOURCE_ATTRIBUTION_DIR,
        paths.DATA_LAKE_GOVERNANCE_CHECKLISTS_DIR,
        paths.DATA_LAKE_GOVERNANCE_QUALITY_DIR,
        paths.REPORTS_GOVERNANCE_CSV_DIR,
        paths.REPORTS_GOVERNANCE_MARKDOWN_DIR,
        paths.REPORTS_GOVERNANCE_TXT_DIR,
        paths.REPORTS_GOVERNANCE_JSON_DIR
    ]

    for d in gov_dirs:
        if d.exists():
            for f in d.glob("*.*"):
                files.append({
                    "report_name": f.name,
                    "path": str(f.relative_to(paths.project_root))
                })

    df = pd.DataFrame(files)


    txt_report = rb.build_governance_status_report(df, {})

    txt_path = paths.REPORTS_GOVERNANCE_TXT_DIR / "governance_status_report.txt"
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    with open(txt_path, "w") as f:
        f.write(txt_report)

    csv_path = paths.REPORTS_GOVERNANCE_CSV_DIR / "governance_status.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(csv_path, index=False)

    print(txt_report)
    print(f"\nStatus report saved to {txt_path}")

if __name__ == "__main__":
    main()
