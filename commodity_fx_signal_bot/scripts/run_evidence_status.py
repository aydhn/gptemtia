import argparse
import logging
import pandas as pd

from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from evidence_governance.evidence_config import get_evidence_governance_profile
from evidence_governance.evidence_pipeline import EvidenceGovernancePipeline
import reports.report_builder as report_builder

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Check evidence status")
    parser.add_argument("--profile", type=str, default="balanced_local_evidence", help="Profile")
    args = parser.parse_args()

    settings = Settings()
    paths = ProjectPaths()
    data_lake = DataLake(paths, settings)


    try:
        profile = get_evidence_governance_profile(args.profile)
    except ValueError as e:
        logger.error(str(e))
        return

    pipeline = EvidenceGovernancePipeline(data_lake, settings, paths.PROJECT_ROOT, profile)

    status_df, summary = pipeline.build_evidence_status(save=False)

    if "error" in summary:
        logger.error(f"Error: {summary['error']}")
        return

    report_text = report_builder.build_evidence_status_report(status_df, summary)

    csv_dir = paths.REPORTS_EVIDENCE_GOVERNANCE_CSV_DIR
    status_df.to_csv(csv_dir / "evidence_status.csv", index=False)

    txt_path = paths.REPORTS_EVIDENCE_GOVERNANCE_TXT_DIR / "evidence_status_report.txt"
    with open(txt_path, "w") as f:
        f.write(report_text)

    logger.info("Evidence status checked.")

if __name__ == "__main__":
    main()
