import argparse
from pathlib import Path
from config.settings import settings
from config.paths import PROJECT_ROOT
from data.storage.data_lake import DataLake
from local_maintenance.maintenance_config import get_local_maintenance_profile
from local_maintenance.maintenance_pipeline import LocalMaintenancePipeline


def main():
    parser = argparse.ArgumentParser(description="Run Refresh Cadence Report")
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

    tables, summary = pipeline.build_refresh_cadence_report(save=args.save)

    if args.save:

        from local_maintenance.maintenance_report_builder import build_refresh_cadence_markdown_report

        md = build_refresh_cadence_markdown_report(summary, tables["report_cadence"])
        from reports.report_builder import build_refresh_cadence_text_report
        txt = build_refresh_cadence_text_report(summary, tables["report_cadence"])

        out_dir = PROJECT_ROOT / "reports" / "output" / "local_maintenance"
        out_dir.joinpath("csv").mkdir(parents=True, exist_ok=True)
        out_dir.joinpath("markdown").mkdir(parents=True, exist_ok=True)
        out_dir.joinpath("txt").mkdir(parents=True, exist_ok=True)

        tables["report_cadence"].to_csv(out_dir / "csv" / "report_refresh_cadence_registry.csv", index=False)
        tables["datalake_cadence"].to_csv(out_dir / "csv" / "datalake_refresh_cadence_registry.csv", index=False)
        tables["documentation_cadence"].to_csv(out_dir / "csv" / "documentation_refresh_cadence_registry.csv", index=False)
        tables["test_cadence"].to_csv(out_dir / "csv" / "test_refresh_cadence_registry.csv", index=False)
        tables["safety_cadence"].to_csv(out_dir / "csv" / "safety_security_refresh_cadence_registry.csv", index=False)
        tables["backup_cadence"].to_csv(out_dir / "csv" / "backup_packaging_refresh_cadence_registry.csv", index=False)
        tables["cross_layer_cadence"].to_csv(out_dir / "csv" / "cross_layer_refresh_cadence_registry.csv", index=False)
        tables["command_plan"].to_csv(out_dir / "csv" / "refresh_command_plan.csv", index=False)

        with open(out_dir / "markdown" / "refresh_cadence_report.md", "w") as f:
            f.write(md)

        with open(out_dir / "txt" / "refresh_cadence_report.txt", "w") as f:
            f.write(txt)

    print("Refresh Cadence Report complete.")

if __name__ == "__main__":
    main()
