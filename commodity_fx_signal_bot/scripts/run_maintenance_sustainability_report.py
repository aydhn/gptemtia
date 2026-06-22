import argparse
from pathlib import Path
from config.settings import settings
from config.paths import PROJECT_ROOT, DOCS_GENERATED_LOCAL_MAINTENANCE_DIR
from data.storage.data_lake import DataLake
from local_maintenance.maintenance_config import get_local_maintenance_profile
from local_maintenance.maintenance_pipeline import LocalMaintenancePipeline


def main():
    parser = argparse.ArgumentParser(description="Run Maintenance Sustainability Report")
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

    tables, summary = pipeline.build_maintenance_sustainability_report(save=args.save)

    if args.save:

        from local_maintenance.maintenance_report_builder import build_sustainability_markdown_report

        md = build_sustainability_markdown_report(summary, tables["score"], tables["risks"])
        from reports.report_builder import build_maintenance_sustainability_text_report
        txt = build_maintenance_sustainability_text_report(summary, tables["score"], tables["risks"])

        out_dir = PROJECT_ROOT / "reports" / "output" / "local_maintenance"
        out_dir.joinpath("csv").mkdir(parents=True, exist_ok=True)
        out_dir.joinpath("markdown").mkdir(parents=True, exist_ok=True)
        out_dir.joinpath("txt").mkdir(parents=True, exist_ok=True)

        tables["deprecated_artifacts"].to_csv(out_dir / "csv" / "deprecated_artifact_watch_report.csv", index=False)
        tables["stale_reports"].to_csv(out_dir / "csv" / "stale_report_watch_report.csv", index=False)
        tables["stale_docs"].to_csv(out_dir / "csv" / "stale_documentation_watch_report.csv", index=False)
        tables["stale_tests"].to_csv(out_dir / "csv" / "stale_test_watch_report.csv", index=False)
        tables["manual_review_queue"].to_csv(out_dir / "csv" / "manual_review_queue.csv", index=False)
        tables["gaps"].to_csv(out_dir / "csv" / "maintenance_gap_register.csv", index=False)
        tables["risks"].to_csv(out_dir / "csv" / "maintenance_risk_summary.csv", index=False)
        tables["score"].to_csv(out_dir / "csv" / "sustainability_score_report.csv", index=False)

        with open(out_dir / "markdown" / "maintenance_sustainability_report.md", "w") as f:
            f.write(md)

        with open(out_dir / "txt" / "maintenance_sustainability_report.txt", "w") as f:
            f.write(txt)

        # Write to DOCS_GENERATED
        DOCS_GENERATED_LOCAL_MAINTENANCE_DIR.mkdir(parents=True, exist_ok=True)

        runbook = data_lake.load_maintenance_runbook()
        with open(DOCS_GENERATED_LOCAL_MAINTENANCE_DIR / "MAINTENANCE_RUNBOOK.md", "w") as f:
            f.write(runbook)

        binder = data_lake.load_long_term_sustainability_binder()
        with open(DOCS_GENERATED_LOCAL_MAINTENANCE_DIR / "LONG_TERM_SUSTAINABILITY_BINDER.md", "w") as f:
            f.write(binder)

        m_temp = data_lake.load_monthly_review_template()
        with open(DOCS_GENERATED_LOCAL_MAINTENANCE_DIR / "MONTHLY_REVIEW_TEMPLATE.md", "w") as f:
            f.write(m_temp)

        q_temp = data_lake.load_quarterly_review_template()
        with open(DOCS_GENERATED_LOCAL_MAINTENANCE_DIR / "QUARTERLY_REVIEW_TEMPLATE.md", "w") as f:
            f.write(q_temp)

    print("Maintenance Sustainability Report complete.")

if __name__ == "__main__":
    main()
