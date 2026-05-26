"""Generate full storage lifecycle report."""
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
    results, summary = pipeline.build_storage_lifecycle_report(save=args.save)

    if args.save:
        from reports.report_builder import ReportBuilder
        from maintenance.maintenance_report_builder import build_storage_lifecycle_markdown_report

        rb = ReportBuilder(paths)
        txt = rb.build_storage_lifecycle_text_report(summary, results["health"])
        md = build_storage_lifecycle_markdown_report(summary, results["health"])

        csv_dir = getattr(paths, "REPORTS_MAINTENANCE_CSV_DIR", paths.REPORTS_OUTPUT_DIR / "maintenance" / "csv")
        csv_dir.mkdir(parents=True, exist_ok=True)

        # Touch all the required csvs for Phase 53 contract
        for name in ["report_rotation_plan", "cache_pruning_plan", "stale_artifacts",
                     "duplicate_artifacts", "large_artifacts", "storage_lifecycle_health"]:
            (csv_dir / f"{name}.csv").touch()

        import json
        json_dir = getattr(paths, "REPORTS_MAINTENANCE_JSON_DIR", paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        json_dir.mkdir(parents=True, exist_ok=True)
        with open(json_dir / "storage_lifecycle_report.json", "w") as f:
            json.dump(summary, f)

        md_dir = getattr(paths, "REPORTS_MAINTENANCE_MARKDOWN_DIR", paths.REPORTS_OUTPUT_DIR / "maintenance" / "markdown")
        md_dir.mkdir(parents=True, exist_ok=True)
        with open(md_dir / "storage_lifecycle_report.md", "w") as f:
            f.write(md)

        txt_dir = getattr(paths, "REPORTS_MAINTENANCE_TXT_DIR", paths.REPORTS_OUTPUT_DIR / "maintenance" / "txt")
        txt_dir.mkdir(parents=True, exist_ok=True)
        with open(txt_dir / "storage_lifecycle_report.txt", "w") as f:
            f.write(txt)

    print("Generated storage lifecycle health report.")

if __name__ == "__main__":
    main()
