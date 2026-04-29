import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from config.paths import (
    LAKE_DIR,
    LAKE_MANIFESTS_DIR,
    REPORTS_DIR,
    ensure_project_directories,
)
from config.symbols import get_allowed_timeframes_for_symbol, get_enabled_symbols
from core.logger import get_logger
from data.storage.data_lake import DataLake
from data.storage.manifest import (
    build_manifest,
    manifest_to_dataframe,
    save_manifest_csv,
    save_manifest_json,
    summarize_manifest,
)
from reports.report_builder import build_data_lake_status_report, save_text_report


def main():
    parser = argparse.ArgumentParser(
        description="Check status of the local Data Lake and generate a manifest."
    )
    args = parser.parse_args()

    logger = get_logger("run_data_lake_status")
    ensure_project_directories()

    data_lake = DataLake(LAKE_DIR)

    symbols = get_enabled_symbols()
    timeframes_by_symbol = {
        s.symbol: get_allowed_timeframes_for_symbol(s) for s in symbols
    }

    logger.info("Scanning Data Lake...")
    manifest_entries = build_manifest(data_lake, symbols, timeframes_by_symbol)

    # Save Manifests
    save_manifest_csv(manifest_entries, REPORTS_DIR / "data_lake_manifest.csv")
    save_manifest_csv(manifest_entries, LAKE_MANIFESTS_DIR / "latest_manifest.csv")
    save_manifest_json(manifest_entries, LAKE_MANIFESTS_DIR / "latest_manifest.json")

    # Summarize and Report
    manifest_summary = summarize_manifest(manifest_entries)
    manifest_df = manifest_to_dataframe(manifest_entries)

    report_text = build_data_lake_status_report(manifest_summary, manifest_df)

    logger.info(f"\n{report_text}")

    report_path = REPORTS_DIR / "data_lake_status_report.txt"
    save_text_report(report_text, report_path)
    logger.info(f"Status report saved to {report_path}")


if __name__ == "__main__":
    main()
