#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from secrets_hygiene.secrets_config import get_secrets_hygiene_profile, get_default_secrets_hygiene_profile
from secrets_hygiene.secrets_pipeline import SecretsHygienePipeline
from secrets_hygiene.secrets_report_builder import build_sensitive_file_scan_markdown_report
import reports.report_builder as ReportBuilder
from config.paths import ProjectPaths

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_secrets_hygiene")
    parser.add_argument("--save", type=str, default="true")
    args = parser.parse_args()

    settings = Settings()
    if not settings.secrets_hygiene_enabled: sys.exit(0)

    try: profile = get_secrets_hygiene_profile(args.profile)
    except: profile = get_default_secrets_hygiene_profile()

    save = args.save.lower() == "true"
    project_root = Path(__file__).resolve().parent.parent
    paths = ProjectPaths()
    paths.ensure_project_directories()
    dl = DataLake(project_root)

    pipeline = SecretsHygienePipeline(dl, settings, project_root, profile)
    tables, summary = pipeline.build_sensitive_file_scan_report(save=save)

    if save:
        inv, pat, ent = tables.get("inventory"), tables.get("patterns"), tables.get("entropy")
        if inv is not None and not inv.empty: inv.to_csv(paths.output_secrets_hygiene_csv_dir / "sensitive_file_inventory.csv", index=False)
        if pat is not None and not pat.empty: pat.to_csv(paths.output_secrets_hygiene_csv_dir / "secret_pattern_findings.csv", index=False)
        if ent is not None and not ent.empty: ent.to_csv(paths.output_secrets_hygiene_csv_dir / "high_entropy_findings.csv", index=False)
        md = build_sensitive_file_scan_markdown_report(summary, inv, pat)
        with open(paths.output_secrets_hygiene_markdown_dir / "sensitive_file_scan_report.md", "w") as f: f.write(md)
        txt = ReportBuilder.ReportBuilder.build_sensitive_file_scan_text_report(summary, pat)
        with open(paths.output_secrets_hygiene_txt_dir / "sensitive_file_scan_report.txt", "w") as f: f.write(txt)
    print("Done")

if __name__ == "__main__": main()
