"""
Script to generate the Long-Horizon Preservation Binder.
"""

import argparse
from pathlib import Path

from config.paths import ProjectPaths, ensure_project_directories, LAKE_DIR
get_paths = lambda: ProjectPaths()
from config.settings import settings
from data.storage.data_lake import DataLake
from core.logger import get_logger
from local_archive.archive_config import get_local_archive_profile
from local_archive.archive_pipeline import LocalArchivePipeline

logger = get_logger("run_preservation_binder")

def main():
    parser = argparse.ArgumentParser(description="Generate Long-Horizon Preservation Binder")
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

    logger.info(f"Generating preservation binder using profile: {args.profile}")

    binder_text, summary = pipeline.build_preservation_binder(save=args.save)

    if args.save:
        from reports.report_builder import ReportBuilder
        builder = ReportBuilder(paths)

        # Save CSVs
        if pipeline.gap_df is not None and not pipeline.gap_df.empty:
            pipeline.gap_df.to_csv(paths.reports_local_archive_csv / "archive_gap_register.csv", index=False)
        if pipeline.risk_df is not None and not pipeline.risk_df.empty:
            pipeline.risk_df.to_csv(paths.reports_local_archive_csv / "archive_risk_summary.csv", index=False)

        # Save markdown/text reports
        md_report = builder.build_preservation_binder_text_report(summary, binder_text)

        md_path = paths.reports_local_archive_markdown / "long_horizon_preservation_binder.md"
        md_path.write_text(md_report, encoding="utf-8")

        txt_path = paths.reports_local_archive_txt / "long_horizon_preservation_binder.txt"
        txt_path.write_text(md_report, encoding="utf-8")

        # Also copy to docs/generated
        docs_path = paths.docs_generated_local_archive / "LONG_HORIZON_PRESERVATION_BINDER.md"
        docs_path.write_text(md_report, encoding="utf-8")

        logger.info(f"Reports saved to {paths.reports_local_archive_markdown} and {paths.docs_generated_local_archive}")

    logger.info("Done.")

if __name__ == "__main__":
    main()
