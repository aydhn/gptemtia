import argparse
from pathlib import Path
from config.settings import settings
from config.paths import PROJECT_ROOT
from data.storage.data_lake import DataLake
from local_maintenance.maintenance_config import get_local_maintenance_profile
from local_maintenance.maintenance_pipeline import LocalMaintenancePipeline


def main():
    parser = argparse.ArgumentParser(description="Run Periodic Review Calendar")
    parser.add_argument("--profile", type=str, default=settings.default_local_maintenance_profile, help="Maintenance profile name")
    parser.add_argument("--save", type=lambda x: (str(x).lower() == 'true'), default=True, help="Save to DataLake")
    args = parser.parse_args()

    if not settings.local_maintenance_enabled:
        print("Local maintenance is disabled.")
        return

    profile = get_local_maintenance_profile(args.profile)
    data_lake = DataLake() if args.save else None

    pipeline = LocalMaintenancePipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=PROJECT_ROOT,
        profile=profile
    )

    tables, summary = pipeline.build_periodic_review_calendar(save=args.save)

    if args.save:

        from local_maintenance.maintenance_report_builder import build_periodic_review_calendar_markdown_report

        md = build_periodic_review_calendar_markdown_report(summary, tables["calendar"])
        from reports.report_builder import build_periodic_review_calendar_text_report
        txt = build_periodic_review_calendar_text_report(summary, tables["calendar"])

        out_dir = PROJECT_ROOT / "reports" / "output" / "local_maintenance"
        out_dir.joinpath("csv").mkdir(parents=True, exist_ok=True)
        out_dir.joinpath("markdown").mkdir(parents=True, exist_ok=True)
        out_dir.joinpath("txt").mkdir(parents=True, exist_ok=True)

        tables["calendar"].to_csv(out_dir / "csv" / "periodic_review_calendar.csv", index=False)
        tables["monthly_calendar"].to_csv(out_dir / "csv" / "monthly_review_calendar.csv", index=False)
        tables["quarterly_calendar"].to_csv(out_dir / "csv" / "quarterly_review_calendar.csv", index=False)
        tables["operator_checklist"].to_csv(out_dir / "csv" / "operator_periodic_review_checklist.csv", index=False)

        with open(out_dir / "markdown" / "periodic_review_calendar_report.md", "w") as f:
            f.write(md)

        with open(out_dir / "txt" / "periodic_review_calendar_report.txt", "w") as f:
            f.write(txt)

    print(f"Periodic Review Calendar complete. Found {summary['calendar']['total_items']} scheduled items.")

if __name__ == "__main__":
    main()
