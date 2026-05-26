"""Generate retention policy report."""
import argparse
from pathlib import Path
from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from maintenance.maintenance_config import get_maintenance_profile
from maintenance.maintenance_pipeline import MaintenancePipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_maintenance")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()

    settings = Settings()
    paths = ProjectPaths()
    data_lake = DataLake(paths)
    profile = get_maintenance_profile(args.profile)

    pipeline = MaintenancePipeline(data_lake, settings, paths.PROJECT_ROOT, profile)
    df, summary = pipeline.build_retention_policy_report(save=args.save)

    if args.save:
        data_lake.save_retention_policies(df, summary)

        from reports.report_builder import ReportBuilder
        from maintenance.maintenance_report_builder import build_retention_policy_markdown_report

        rb = ReportBuilder(paths)
        txt = rb.build_retention_policy_text_report(summary, df)
        md = build_retention_policy_markdown_report(summary, df)

        csv_dir = getattr(paths, "REPORTS_MAINTENANCE_CSV_DIR", paths.REPORTS_OUTPUT_DIR / "maintenance" / "csv")
        csv_dir.mkdir(parents=True, exist_ok=True)
        df.to_csv(csv_dir / "retention_policies.csv", index=False)

        md_dir = getattr(paths, "REPORTS_MAINTENANCE_MARKDOWN_DIR", paths.REPORTS_OUTPUT_DIR / "maintenance" / "markdown")
        md_dir.mkdir(parents=True, exist_ok=True)
        with open(md_dir / "retention_policy_report.md", "w") as f:
            f.write(md)

        txt_dir = getattr(paths, "REPORTS_MAINTENANCE_TXT_DIR", paths.REPORTS_OUTPUT_DIR / "maintenance" / "txt")
        txt_dir.mkdir(parents=True, exist_ok=True)
        with open(txt_dir / "retention_policy_report.txt", "w") as f:
            f.write(txt)

    print(f"Generated retention policy report with {summary.get('total_policies', 0)} policies.")

if __name__ == "__main__":
    main()
