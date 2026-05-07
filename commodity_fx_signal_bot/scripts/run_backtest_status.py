import argparse
import sys
import logging
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from reports.report_builder import build_backtest_status_report

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Run Backtest Status")
    args = parser.parse_args()

    paths = ProjectPaths()
    lake = DataLake(paths.lake_dir)

    if not hasattr(lake, "list_backtest_runs"):
        logger.error("list_backtest_runs not available in DataLake")
        return

    status_df = lake.list_backtest_runs()

    report = build_backtest_status_report(status_df, {})
    print(report)

    out_path = paths.backtest_reports / "backtest_status_report.txt"
    with open(out_path, "w") as f:
        f.write(report)
    logger.info(f"Report saved to {out_path}")


if __name__ == "__main__":
    main()
