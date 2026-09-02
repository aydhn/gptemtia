"""
Script to generate the Archive Quality Report.
"""

import argparse
from pathlib import Path
import json

from config.paths import ProjectPaths, ensure_project_directories, LAKE_DIR
get_paths = lambda: ProjectPaths()
from config.settings import settings
from data.storage.data_lake import DataLake
from core.logger import get_logger
from local_archive.archive_config import get_local_archive_profile
from local_archive.archive_pipeline import LocalArchivePipeline

logger = get_logger("run_archive_quality_report")

def main():
    parser = argparse.ArgumentParser(description="Generate Archive Quality Report")
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

    # Needs some base data to build a good quality report
    pipeline._ensure_base_data()

    logger.info(f"Generating archive quality report using profile: {args.profile}")

    qual_report, summary = pipeline.build_archive_quality_report(save=args.save)

    if args.save:
        from reports.report_builder import ReportBuilder
        builder = ReportBuilder(paths)

        # Save JSON
        json_path = paths.reports_local_archive_json / "archive_quality_report.json"
        json_path.write_text(json.dumps(qual_report, indent=2), encoding="utf-8")

        # Load validation df if available
        val_df = pd.DataFrame()
        if hasattr(data_lake, 'load_archive_validation_report'):
            val_df = data_lake.load_archive_validation_report()
            if val_df is not None and not val_df.empty:
                val_df.to_csv(paths.reports_local_archive_csv / "archive_validation_report.csv", index=False)

        # Save markdown/text reports
        md_report = builder.build_archive_quality_text_report(summary, qual_report)

        md_path = paths.reports_local_archive_markdown / "archive_quality_report.md"
        md_path.write_text(md_report, encoding="utf-8")

        txt_path = paths.reports_local_archive_txt / "archive_quality_report.txt"
        txt_path.write_text(md_report, encoding="utf-8")

        logger.info(f"Reports saved to {paths.reports_local_archive_markdown}")

    logger.info("Done.")

if __name__ == "__main__":
    import pandas as pd
    main()
