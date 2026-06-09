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
    parser = argparse.ArgumentParser(description="Build governance evidence export")
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

    res, summary = pipeline.build_governance_evidence_export(save=True)

    if "error" in summary:
        logger.error(f"Error: {summary['error']}")
        return

    export_index_df = res.get("export_index", pd.DataFrame())
    manifest = res.get("export_manifest", pd.DataFrame())
    if not manifest.empty:
        manifest_dict = manifest.iloc[0].to_dict()
    else:
        manifest_dict = summary.get("manifest", {})

    report_text = report_builder.build_governance_evidence_export_text_report(summary, export_index_df)

    csv_dir = paths.REPORTS_EVIDENCE_GOVERNANCE_CSV_DIR
    json_dir = paths.REPORTS_EVIDENCE_GOVERNANCE_JSON_DIR

    with open(json_dir / "governance_evidence_export_manifest.json", "w") as f:
        json.dump(manifest_dict, f, indent=4)

    export_index_df.to_csv(csv_dir / "local_evidence_export_index.csv", index=False)

    pack_names = [
        "safety", "secrets_hygiene", "backup_recovery", "packaging",
        "quality", "scenario_regression", "final_review", "documentation", "master_orchestration"
    ]
    for p in pack_names:
        df = res.get(p, pd.DataFrame())
        df.to_csv(csv_dir / f"{p}_evidence_pack.csv", index=False)

    if not res.get("packaging", pd.DataFrame()).empty:
        res.get("packaging").to_csv(csv_dir / "portable_packaging_evidence_pack.csv", index=False)
    if not res.get("quality", pd.DataFrame()).empty:
        res.get("quality").to_csv(csv_dir / "quality_gate_evidence_pack.csv", index=False)

    md_path = paths.REPORTS_EVIDENCE_GOVERNANCE_MARKDOWN_DIR / "governance_evidence_export_report.md"
    txt_path = paths.REPORTS_EVIDENCE_GOVERNANCE_TXT_DIR / "governance_evidence_export_report.txt"

    with open(md_path, "w") as f:
        f.write(report_text)
    with open(txt_path, "w") as f:
        f.write(report_text)

    logger.info("Governance evidence export generated.")

if __name__ == "__main__":
    main()
