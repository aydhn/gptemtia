import argparse
import logging
from pathlib import Path

from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from evidence_governance.evidence_config import get_evidence_governance_profile
from evidence_governance.evidence_pipeline import EvidenceGovernancePipeline
import reports.report_builder as report_builder

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Build evidence artifact inventory")
    parser.add_argument("--profile", type=str, default="balanced_local_evidence", help="Evidence governance profile")
    parser.add_argument("--save", action="store_true", default=True, help="Save outputs")
    parser.add_argument("--no-save", dest="save", action="store_false", help="Do not save outputs")
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

    logger.info(f"Starting evidence artifact inventory with profile: {profile.name}")

    pipeline = EvidenceGovernancePipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=paths.PROJECT_ROOT,
        profile=profile
    )

    df, summary = pipeline.build_evidence_artifact_inventory(save=args.save)

    if df.empty:
        logger.warning("No artifacts found or error occurred.")
        return

    logger.info(f"Inventory complete. Total artifacts: {summary.get('total_artifacts', 0)}")

    if args.save:
        report_text = report_builder.build_evidence_artifact_inventory_text_report(summary, df)

        csv_path = paths.REPORTS_EVIDENCE_GOVERNANCE_CSV_DIR / "evidence_artifact_inventory.csv"
        md_path = paths.REPORTS_EVIDENCE_GOVERNANCE_MARKDOWN_DIR / "evidence_artifact_inventory_report.md"
        txt_path = paths.REPORTS_EVIDENCE_GOVERNANCE_TXT_DIR / "evidence_artifact_inventory_report.txt"

        df.to_csv(csv_path, index=False)
        with open(md_path, "w") as f:
            f.write(report_text)
        with open(txt_path, "w") as f:
            f.write(report_text)

        logger.info(f"Reports saved to {paths.REPORTS_EVIDENCE_GOVERNANCE_DIR}")

if __name__ == "__main__":
    main()
