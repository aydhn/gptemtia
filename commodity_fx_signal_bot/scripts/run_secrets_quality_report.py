#!/usr/bin/env python3
import argparse
import sys
import json
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from secrets_hygiene.secrets_config import get_secrets_hygiene_profile
from secrets_hygiene.secrets_pipeline import SecretsHygienePipeline
from secrets_hygiene.secrets_report_builder import build_secrets_quality_markdown_report
from secrets_hygiene.secrets_safety import build_secrets_safety_report
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
    quality, summary = pipeline.build_secrets_quality_report(save=save)
    safety_df, safety_summary = build_secrets_safety_report({}, profile)
    if save:
        if safety_df is not None and not safety_df.empty: safety_df.to_csv(paths.output_secrets_hygiene_csv_dir / "secrets_safety_report.csv", index=False)
        with open(paths.output_secrets_hygiene_json_dir / "secrets_quality_report.json", "w") as f: json.dump(quality, f, indent=2)
        md = build_secrets_quality_markdown_report(summary, quality)
        with open(paths.output_secrets_hygiene_markdown_dir / "secrets_quality_report.md", "w") as f: f.write(md)
        txt = ReportBuilder.ReportBuilder.build_secrets_quality_text_report(summary, quality)
        with open(paths.output_secrets_hygiene_txt_dir / "secrets_quality_report.txt", "w") as f: f.write(txt)
    print("Done")
if __name__ == "__main__": main()
