#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from secrets_hygiene.secrets_config import get_secrets_hygiene_profile
from secrets_hygiene.secrets_pipeline import SecretsHygienePipeline
from secrets_hygiene.secrets_report_builder import build_secrets_hygiene_status_markdown_report
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
    df, summary = pipeline.build_secrets_hygiene_status(save=save)
    if save:
        if df is not None and not df.empty: df.to_csv(paths.output_secrets_hygiene_csv_dir / "secrets_hygiene_status.csv", index=False)
        txt = ReportBuilder.ReportBuilder.build_secrets_hygiene_status_report(df, summary)
        with open(paths.output_secrets_hygiene_txt_dir / "secrets_hygiene_status_report.txt", "w") as f: f.write(txt)
    print("Done")
if __name__ == "__main__": main()
