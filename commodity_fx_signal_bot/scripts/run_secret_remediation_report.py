#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from secrets_hygiene.secrets_config import get_secrets_hygiene_profile
from secrets_hygiene.secrets_pipeline import SecretsHygienePipeline
from secrets_hygiene.secrets_report_builder import build_secret_remediation_markdown_report
from secrets_hygiene.secrets_runbook import build_secret_hygiene_runbook
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
    dl = DataLake(project_root)
    pipeline = SecretsHygienePipeline(dl, settings, project_root, profile)
    df, summary = pipeline.build_secret_remediation_report(save=save)
    if save:
        runbook_text, _ = build_secret_hygiene_runbook(None, df, profile)
        with open(paths.docs_generated_secrets_hygiene_dir / "SECRET_HYGIENE_RUNBOOK.md", "w") as f: f.write(runbook_text)
        if df is not None and not df.empty: df.to_csv(paths.output_secrets_hygiene_csv_dir / "secret_remediation_recommendations.csv", index=False)
        md = build_secret_remediation_markdown_report(summary, df)
        with open(paths.output_secrets_hygiene_markdown_dir / "secret_remediation_report.md", "w") as f: f.write(md)
        txt = ReportBuilder.ReportBuilder.build_secret_remediation_text_report(summary, df)
        with open(paths.output_secrets_hygiene_txt_dir / "secret_remediation_report.txt", "w") as f: f.write(txt)
    print("Done")
if __name__ == "__main__": main()
