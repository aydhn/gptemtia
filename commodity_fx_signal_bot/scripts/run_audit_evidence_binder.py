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
    parser = argparse.ArgumentParser(description="Build audit evidence binder")
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

    logger.info(f"Building audit evidence binder with profile: {profile.name}")

    pipeline = EvidenceGovernancePipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=paths.PROJECT_ROOT,
        profile=profile
    )

    binder_text, summary = pipeline.build_audit_evidence_binder(save=True)

    if "error" in summary:
        logger.error(f"Error building binder: {summary['error']}")
        return

    logger.info("Binder text generated.")

    docs_path = paths.DOCS_EVIDENCE_GOVERNANCE_DIR / "AUDIT_EVIDENCE_BINDER.md"
    with open(docs_path, "w") as f:
        f.write(binder_text)

    report_text = report_builder.build_audit_evidence_binder_text_report(summary, binder_text)

    md_path = paths.REPORTS_EVIDENCE_GOVERNANCE_MARKDOWN_DIR / "audit_evidence_binder_report.md"
    txt_path = paths.REPORTS_EVIDENCE_GOVERNANCE_TXT_DIR / "audit_evidence_binder_report.txt"

    with open(md_path, "w") as f:
        f.write(report_text)
    with open(txt_path, "w") as f:
        f.write(report_text)

    pd.DataFrame([{"info": "See datalake"}]).to_csv(paths.REPORTS_EVIDENCE_GOVERNANCE_CSV_DIR / "audit_evidence_binder_index.csv", index=False)
    pd.DataFrame([{"info": "See datalake"}]).to_csv(paths.REPORTS_EVIDENCE_GOVERNANCE_CSV_DIR / "evidence_gap_register.csv", index=False)

    logger.info("Audit evidence binder generated.")

if __name__ == "__main__":
    main()
