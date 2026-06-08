#!/usr/bin/env python3
import argparse
import sys
import pandas as pd
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from secrets_hygiene.secrets_config import get_secrets_hygiene_profile
from secrets_hygiene.secrets_pipeline import SecretsHygienePipeline
from secrets_hygiene.secrets_report_builder import build_credential_boundary_markdown_report
from secrets_hygiene.backup_packaging_boundary import audit_backup_recovery_secret_boundary, audit_portable_packaging_secret_boundary, audit_manifest_secret_exclusion
import reports.report_builder as ReportBuilder
from config.paths import ProjectPaths

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_secrets_hygiene")
    parser.add_argument("--save", type=str, default="true")
    args = parser.parse_args()
    settings = Settings()
    if not settings.secrets_hygiene_enabled: sys.exit(0)
    profile = get_secrets_hygiene_profile(args.profile)
    save = args.save.lower() == "true"
    project_root = Path(__file__).resolve().parent.parent
    paths = ProjectPaths()
    paths.ensure_project_directories()
    dl = DataLake(project_root)
    pipeline = SecretsHygienePipeline(dl, settings, project_root, profile)
    df, summary = pipeline.build_credential_boundary_report(save=save)
    b1, _ = audit_backup_recovery_secret_boundary(project_root)
    b2, _ = audit_portable_packaging_secret_boundary(project_root)
    b3, _ = audit_manifest_secret_exclusion(project_root)
    backup_df = pd.concat([b1, b2, b3], ignore_index=True) if not b1.empty or not b2.empty or not b3.empty else pd.DataFrame()
    if save:
        if df is not None and not df.empty: df.to_csv(paths.output_secrets_hygiene_csv_dir / "credential_boundary_report.csv", index=False)
        if backup_df is not None and not backup_df.empty: backup_df.to_csv(paths.output_secrets_hygiene_csv_dir / "backup_packaging_secret_boundary_report.csv", index=False)
        md = build_credential_boundary_markdown_report(summary, df)
        with open(paths.output_secrets_hygiene_markdown_dir / "credential_boundary_report.md", "w") as f: f.write(md)
        txt = ReportBuilder.ReportBuilder.build_credential_boundary_text_report(summary, df)
        with open(paths.output_secrets_hygiene_txt_dir / "credential_boundary_report.txt", "w") as f: f.write(txt)
    print("Done")
if __name__ == "__main__": main()
