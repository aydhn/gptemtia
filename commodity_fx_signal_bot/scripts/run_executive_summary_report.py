import argparse
import sys
import logging
from pathlib import Path

from config.settings import settings
from config.paths import PROJECT_ROOT
from data.storage.data_lake import DataLake
from report_summarization.summary_config import get_report_summary_profile, get_default_report_summary_profile
from report_summarization.summary_pipeline import ReportSummarizationPipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Run Executive Summary Report")
    parser.add_argument("--profile", type=str, default="executive_brief_summaries", help="Report summary profile name")
    parser.add_argument("--save", action="store_true", default=True, help="Save outputs")
    return parser.parse_args([])

def main():
    args = parse_args()
    try:
        profile = get_report_summary_profile(args.profile)
    except Exception:
        profile = get_default_report_summary_profile()

    data_lake = DataLake(root_dir=Path('/tmp'))
    pipeline = ReportSummarizationPipeline(data_lake, settings, PROJECT_ROOT, profile)

    text, meta = pipeline.build_executive_summary_report(save=args.save)
    logger.info("Executive Summary Report generated successfully.")

if __name__ == "__main__":
    main()
