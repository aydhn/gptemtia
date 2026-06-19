import argparse
from config.settings import Settings
from config.paths import PROJECT_ROOT
from data.storage.data_lake import DataLake
from local_readiness.readiness_config import get_local_readiness_profile
from local_readiness.readiness_pipeline import LocalReadinessPipeline
from local_readiness.operator_checklist import build_operator_first_run_checklist
from local_readiness.stabilization_checklist import build_pre_handoff_stabilization_checklist
from local_readiness.dry_run_commands import build_dry_run_command_checklist
from local_readiness.command_coverage import build_safe_command_coverage_report
from reports.report_builder import build_final_operator_checklist_text_report

def main():
    parser = argparse.ArgumentParser(description="Run final operator checklist.")
    parser.add_argument("--profile", type=str, default="balanced_local_readiness")
    parser.add_argument("--save", type=str, default="true")
    args = parser.parse_args()

    settings = Settings()
    data_lake = DataLake(PROJECT_ROOT / "data")
    profile = get_local_readiness_profile(args.profile)
    save = args.save.lower() == "true"

    pipeline = LocalReadinessPipeline(data_lake, settings, PROJECT_ROOT, profile)
    out, summary = pipeline.build_final_operator_checklist(save=save)
    df = out["operator_checklist"]

    first_run_df, _ = build_operator_first_run_checklist(profile)
    stab_df, _ = build_pre_handoff_stabilization_checklist(profile)
    dry_df, _ = build_dry_run_command_checklist(profile)
    cov_df, _ = build_safe_command_coverage_report(PROJECT_ROOT, dry_df, profile)

    if save:
        from config.paths import REPORTS_LOCAL_READINESS_CSV_DIR, REPORTS_LOCAL_READINESS_MD_DIR, REPORTS_LOCAL_READINESS_TXT_DIR
        REPORTS_LOCAL_READINESS_CSV_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_LOCAL_READINESS_MD_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_LOCAL_READINESS_TXT_DIR.mkdir(parents=True, exist_ok=True)

        df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "final_operator_checklist.csv", index=False)
        first_run_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "operator_first_run_checklist.csv", index=False)
        stab_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "pre_handoff_stabilization_checklist.csv", index=False)
        dry_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "dry_run_command_checklist.csv", index=False)
        cov_df.to_csv(REPORTS_LOCAL_READINESS_CSV_DIR / "safe_command_coverage_report.csv", index=False)

        from local_readiness.readiness_report_builder import build_final_operator_checklist_markdown_report
        md = build_final_operator_checklist_markdown_report(summary, df)
        with open(REPORTS_LOCAL_READINESS_MD_DIR / "final_operator_checklist_report.md", "w") as f:
            f.write(md)

        txt = build_final_operator_checklist_text_report(summary, df)
        with open(REPORTS_LOCAL_READINESS_TXT_DIR / "final_operator_checklist_report.txt", "w") as f:
            f.write(txt)

if __name__ == "__main__":
    main()
