import argparse
import logging
import pandas as pd
import json

from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from evidence_governance.evidence_config import get_evidence_governance_profile
from evidence_governance.evidence_pipeline import EvidenceGovernancePipeline
import reports.report_builder as report_builder

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Build evidence quality report")
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

    report, summary = pipeline.build_evidence_quality_report(save=True)

    if "error" in summary:
        logger.error(f"Error: {summary['error']}")
        return

    report_text = report_builder.build_evidence_quality_text_report(summary, report)

    csv_dir = paths.REPORTS_EVIDENCE_GOVERNANCE_CSV_DIR
    json_dir = paths.REPORTS_EVIDENCE_GOVERNANCE_JSON_DIR

    pd.DataFrame([report]).to_csv(csv_dir / "evidence_validation_report.csv", index=False)
    with open(json_dir / "evidence_quality_report.json", "w") as f:
        json.dump(report, f, indent=4)

    md_path = paths.REPORTS_EVIDENCE_GOVERNANCE_MARKDOWN_DIR / "evidence_quality_report.md"
    txt_path = paths.REPORTS_EVIDENCE_GOVERNANCE_TXT_DIR / "evidence_quality_report.txt"

    with open(md_path, "w") as f:
        f.write(report_text)
    with open(txt_path, "w") as f:
        f.write(report_text)

    logger.info("Evidence quality report generated.")

if __name__ == "__main__":
    main()
