"""
Script to report the status of the local archive data lake.
"""

import argparse
from pathlib import Path

from config.paths import ProjectPaths
get_paths = lambda: ProjectPaths()
from config.settings import settings
from data.storage.data_lake import DataLake
from core.logger import get_logger
from local_archive.archive_config import get_local_archive_profile
from local_archive.archive_pipeline import LocalArchivePipeline

logger = get_logger("run_archive_status")

def main():
    parser = argparse.ArgumentParser(description="Check Local Archive Status")
    parser.add_argument("--profile", type=str, default="balanced_local_archive")
    parser.add_argument("--save", action="store_true", default=True)
    parser.add_argument("--no-save", dest="save", action="store_false")
    args = parser.parse_args()

    profile = get_local_archive_profile(args.profile)
    paths = get_paths()
    data_lake = DataLake(paths)
    project_root = Path(__file__).parent.parent

    pipeline = LocalArchivePipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=project_root,
        profile=profile
    )

    # Try loading some data
    if hasattr(data_lake, 'load_archive_domain_registry'):
        pipeline.domain_df = data_lake.load_archive_domain_registry()
    if hasattr(data_lake, 'load_archive_item_registry'):
        pipeline.item_df = data_lake.load_archive_item_registry()
    if hasattr(data_lake, 'load_cold_storage_manifest'):
        pipeline.manifest = data_lake.load_cold_storage_manifest()

    logger.info(f"Checking archive status...")

    status_df, summary = pipeline.build_archive_status(save=False) # Doesn't save to datalake

    if args.save:
        from reports.report_builder import ReportBuilder
        builder = ReportBuilder(paths)

        # Save CSV
        if status_df is not None and not status_df.empty:
            status_df.to_csv(paths.reports_local_archive_csv / "archive_status.csv", index=False)

        # Save markdown/text reports
        md_report = builder.build_archive_status_report(status_df, summary)

        md_path = paths.reports_local_archive_markdown / "archive_status_report.md"
        md_path.write_text(md_report, encoding="utf-8")

        txt_path = paths.reports_local_archive_txt / "archive_status_report.txt"
        txt_path.write_text(md_report, encoding="utf-8")

        logger.info(f"Reports saved to {paths.reports_local_archive_txt}")

    logger.info("Done.")

if __name__ == "__main__":
    main()
