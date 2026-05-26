"""Generate cleanup dry-run report."""
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
    df, summary = pipeline.build_cleanup_dry_run_report(save=args.save)

    if args.save:
        data_lake.save_cleanup_dry_run_plan(df, summary)

        from reports.report_builder import ReportBuilder
        from maintenance.maintenance_report_builder import build_cleanup_dry_run_markdown_report

        rb = ReportBuilder(paths)
        txt = rb.build_cleanup_dry_run_text_report(summary, df)
        md = build_cleanup_dry_run_markdown_report(summary, df)

        csv_dir = getattr(paths, "REPORTS_MAINTENANCE_CSV_DIR", paths.REPORTS_OUTPUT_DIR / "maintenance" / "csv")
        csv_dir.mkdir(parents=True, exist_ok=True)
        df.to_csv(csv_dir / "cleanup_dry_run_plan.csv", index=False)
        df.to_csv(csv_dir / "cleanup_candidates.csv", index=False) # duplicate for simplicity in phase 53

        md_dir = getattr(paths, "REPORTS_MAINTENANCE_MARKDOWN_DIR", paths.REPORTS_OUTPUT_DIR / "maintenance" / "markdown")
        md_dir.mkdir(parents=True, exist_ok=True)
        with open(md_dir / "cleanup_dry_run_report.md", "w") as f:
            f.write(md)

        txt_dir = getattr(paths, "REPORTS_MAINTENANCE_TXT_DIR", paths.REPORTS_OUTPUT_DIR / "maintenance" / "txt")
        txt_dir.mkdir(parents=True, exist_ok=True)
        with open(txt_dir / "cleanup_dry_run_report.txt", "w") as f:
            f.write(txt)

    print(f"Generated cleanup dry run report with {summary.get('candidate_count', 0)} candidates.")

if __name__ == "__main__":
    main()
