"""Generate maintenance status report."""
import argparse
import pandas as pd
from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from maintenance.maintenance_config import get_maintenance_profile
from maintenance.maintenance_pipeline import MaintenancePipeline

def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    settings = Settings()
    paths = ProjectPaths()
    data_lake = DataLake(paths)
    profile = get_maintenance_profile("balanced_local_maintenance")

    pipeline = MaintenancePipeline(data_lake, settings, paths.PROJECT_ROOT, profile)
    df, summary = pipeline.build_maintenance_status(save=True)

    from reports.report_builder import ReportBuilder
    from maintenance.maintenance_report_builder import build_maintenance_status_markdown_report

    rb = ReportBuilder(paths)
    txt = rb.build_maintenance_status_report(df, summary)

    csv_dir = getattr(paths, "REPORTS_MAINTENANCE_CSV_DIR", paths.REPORTS_OUTPUT_DIR / "maintenance" / "csv")
    csv_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(csv_dir / "maintenance_status.csv", index=False)

    txt_dir = getattr(paths, "REPORTS_MAINTENANCE_TXT_DIR", paths.REPORTS_OUTPUT_DIR / "maintenance" / "txt")
    txt_dir.mkdir(parents=True, exist_ok=True)
    with open(txt_dir / "maintenance_status_report.txt", "w") as f:
        f.write(txt)

    print(f"Generated maintenance status report: {summary.get('status')}")

if __name__ == "__main__":
    main()
