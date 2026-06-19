import argparse
import pandas as pd
from config.settings import Settings
from config.paths import PROJECT_ROOT
from data.storage.data_lake import DataLake
from local_readiness.readiness_config import get_local_readiness_profile
from local_readiness.readiness_pipeline import LocalReadinessPipeline
from reports.report_builder import build_readiness_reports_text_report
from local_readiness.tests_readiness import build_test_readiness_report
from local_readiness.datalake_readiness import build_datalake_readiness_report
from local_readiness.reports_readiness import build_report_output_readiness_report
from local_readiness.security_boundary_readiness import build_security_boundary_readiness_report
from local_readiness.backup_packaging_readiness import build_backup_packaging_readiness_report
from local_readiness.cross_layer_readiness import build_metadata_evidence_graph_timeline_consistency_readiness_report
from local_readiness.limitations_register import build_known_limitations_register
from local_readiness.gaps_register import build_known_gaps_register
from local_readiness.manual_review_register import build_manual_review_register

def main():
    parser = argparse.ArgumentParser(description="Run readiness reports.")
    parser.add_argument("--profile", type=str, default="balanced_local_readiness")
    parser.add_argument("--save", type=str, default="true")
    args = parser.parse_args()

    settings = Settings()
    data_lake = DataLake(PROJECT_ROOT / "data")
    profile = get_local_readiness_profile(args.profile)
    save = args.save.lower() == "true"

    pipeline = LocalReadinessPipeline(data_lake, settings, PROJECT_ROOT, profile)
    out, summary = pipeline.build_readiness_reports(save=save)
    docs_df = out["docs_readiness"]

    tests_df, _ = build_test_readiness_report(PROJECT_ROOT, profile)
    datalake_df, _ = build_datalake_readiness_report(PROJECT_ROOT, profile)
    rep_out_df, _ = build_report_output_readiness_report(PROJECT_ROOT, profile)
    sec_df, _ = build_security_boundary_readiness_report(PROJECT_ROOT, profile)
    back_df, _ = build_backup_packaging_readiness_report(PROJECT_ROOT, profile)
    cross_df, _ = build_metadata_evidence_graph_timeline_consistency_readiness_report(PROJECT_ROOT, profile)

    lim_df, _ = build_known_limitations_register(PROJECT_ROOT, profile)
    gap_df, _ = build_known_gaps_register(PROJECT_ROOT, profile)
    man_df, _ = build_manual_review_register(PROJECT_ROOT, gap_df, lim_df, profile)

    if save:
        from config.paths import REPORTS_LOCAL_READINESS_CSV_DIR, REPORTS_LOCAL_READINESS_MD_DIR, REPORTS_LOCAL_READINESS_TXT_DIR
        REPORTS_LOCAL_READINESS_CSV_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_LOCAL_READINESS_MD_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_LOCAL_READINESS_TXT_DIR.mkdir(parents=True, exist_ok=True)

        docs_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "documentation_readiness_report.csv", index=False)
        tests_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "test_readiness_report.csv", index=False)
        datalake_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "datalake_readiness_report.csv", index=False)
        rep_out_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "report_output_readiness_report.csv", index=False)
        sec_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "security_boundary_readiness_report.csv", index=False)
        back_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "backup_packaging_readiness_report.csv", index=False)
        cross_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "cross_layer_readiness_report.csv", index=False)

        lim_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "known_limitations_register.csv", index=False)
        gap_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "known_gaps_register.csv", index=False)
        man_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "manual_review_register.csv", index=False)

        combined = pd.concat([docs_df, sec_df], ignore_index=True)

        from local_readiness.readiness_report_builder import build_readiness_reports_markdown_report
        md = build_readiness_reports_markdown_report(summary, combined)
        with open(REPORTS_LOCAL_READINESS_MD_DIR / "readiness_reports.md", "w") as f:
            f.write(md)

        txt = build_readiness_reports_text_report(summary, combined)
        with open(REPORTS_LOCAL_READINESS_TXT_DIR / "readiness_reports.txt", "w") as f:
            f.write(txt)

if __name__ == "__main__":
    main()
