import argparse
import logging
from pathlib import Path

from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from evidence_governance.evidence_config import get_evidence_governance_profile
from evidence_governance.evidence_pipeline import EvidenceGovernancePipeline
import reports.report_builder as report_builder
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Build policy and control mapping")
    parser.add_argument("--profile", type=str, default="balanced_local_evidence", help="Evidence governance profile")
    args = parser.parse_args()

    settings = Settings()
    paths = ProjectPaths()
    paths.ensure_project_directories()

    data_lake = DataLake(paths, settings)


    try:
        profile = get_evidence_governance_profile(args.profile)
    except ValueError as e:
        logger.error(str(e))
        return

    logger.info(f"Starting policy and control mapping with profile: {profile.name}")

    pipeline = EvidenceGovernancePipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=paths.PROJECT_ROOT,
        profile=profile
    )

    res, summary = pipeline.build_policy_control_mapping(save=True)

    if "error" in summary:
        logger.error(f"Error mapping: {summary['error']}")
        return

    logger.info(f"Mapping complete. Total mappings: {summary.get('total_mappings', 0)}")

    report_text = report_builder.build_policy_control_mapping_text_report(summary, res.get("control_to_evidence_mapping"))

    csv_dir = paths.REPORTS_EVIDENCE_GOVERNANCE_CSV_DIR
    res.get("policy_registry", pd.DataFrame()).to_csv(csv_dir / "policy_registry.csv", index=False)
    res.get("control_registry", pd.DataFrame()).to_csv(csv_dir / "control_registry.csv", index=False)
    res.get("policy_to_control_mapping", pd.DataFrame()).to_csv(csv_dir / "policy_to_control_mapping.csv", index=False)
    res.get("control_to_evidence_mapping", pd.DataFrame()).to_csv(csv_dir / "control_to_evidence_mapping.csv", index=False)
    res.get("control_status_table", pd.DataFrame()).to_csv(csv_dir / "control_status_table.csv", index=False)

    md_path = paths.REPORTS_EVIDENCE_GOVERNANCE_MARKDOWN_DIR / "policy_control_mapping_report.md"
    txt_path = paths.REPORTS_EVIDENCE_GOVERNANCE_TXT_DIR / "policy_control_mapping_report.txt"

    with open(md_path, "w") as f:
        f.write(report_text)
    with open(txt_path, "w") as f:
        f.write(report_text)

    logger.info("Reports saved.")

if __name__ == "__main__":
    main()
