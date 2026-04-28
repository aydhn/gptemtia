import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from core.logger import get_logger
from config.settings import settings
from config.paths import (
    LAKE_DIR,
    LAKE_MANIFESTS_DIR,
    LAKE_JOURNALS_DIR,
    REPORTS_DIR,
    ensure_project_directories,
)
from config.symbols import get_enabled_symbols, get_allowed_timeframes_for_symbol
from data.storage.cache_manager import CacheManager
from data.data_pipeline import DataPipeline
from data.storage.data_lake import DataLake
from data.storage.download_journal import DownloadJournal
from data.storage.manifest import (
    build_manifest,
    save_manifest_csv,
    save_manifest_json,
    summarize_manifest,
)
from data.download_manager import DownloadManager
from reports.report_builder import build_data_lake_update_report, save_text_report


def main():
    parser = argparse.ArgumentParser(
        description="Update the local Data Lake with latest OHLCV data."
    )
    parser.add_argument("--limit", type=int, help="Limit number of symbols to update")
    parser.add_argument(
        "--asset-class",
        type=str,
        help="Filter by asset class (e.g., metals, forex_try)",
    )
    parser.add_argument(
        "--symbol", type=str, help="Specific symbol to update (e.g., GC=F)"
    )
    parser.add_argument(
        "--timeframe", type=str, help="Specific timeframe to update (e.g., 1d, 4h)"
    )
    parser.add_argument(
        "--profile",
        type=str,
        default=settings.default_scan_profile,
        help="Scan profile to use",
    )
    parser.add_argument(
        "--period",
        type=str,
        default=settings.default_download_period,
        help="Data period (e.g., 2y)",
    )
    parser.add_argument(
        "--refresh", action="store_true", help="Force refresh, ignoring cache"
    )
    args = parser.parse_args()

    logger = get_logger("run_data_lake_update")

    if not settings.data_lake_enabled:
        logger.error("Data Lake is not enabled in settings (DATA_LAKE_ENABLED).")
        sys.exit(1)

    ensure_project_directories()

    # Determine symbols to process
    symbols = get_enabled_symbols()

    if args.symbol:
        symbols = [s for s in symbols if s.symbol == args.symbol]
        if not symbols:
            logger.error(f"Symbol '{args.symbol}' not found in enabled universe.")
            sys.exit(1)
    elif args.asset_class:
        symbols = [s for s in symbols if s.asset_class == args.asset_class]

    # Initialize components
    cache_manager = CacheManager(LAKE_DIR.parent / "cache")
    pipeline = DataPipeline(settings, cache_manager)
    data_lake = DataLake(LAKE_DIR)

    journal_path = LAKE_JOURNALS_DIR / "download_journal.csv"
    journal = DownloadJournal(journal_path)

    manager = DownloadManager(pipeline, data_lake, journal, settings)

    # Prepare timeframes map
    timeframes_by_symbol = {}
    for spec in symbols:
        if args.timeframe:
            timeframes_by_symbol[spec.symbol] = (args.timeframe,)
        else:
            timeframes_by_symbol[spec.symbol] = get_allowed_timeframes_for_symbol(spec)

    logger.info(
        f"Starting Data Lake update for {len(symbols)} symbols. Period: {args.period}, Refresh: {args.refresh}"
    )

    # Run update
    summary = manager.download_universe(
        specs=symbols,
        timeframes_by_symbol=timeframes_by_symbol,
        period=args.period,
        limit=args.limit,
        refresh=args.refresh,
    )

    # Generate Report
    report_text = build_data_lake_update_report(summary)
    logger.info(f"\n{report_text}")

    report_path = REPORTS_DIR / "data_lake_update_report.txt"
    save_text_report(report_text, report_path)
    logger.info(f"Report saved to {report_path}")

    # Generate Manifest
    if settings.manifest_enabled:
        logger.info("Building updated Data Lake manifest...")
        all_symbols = get_enabled_symbols()
        all_tfs = {s.symbol: get_allowed_timeframes_for_symbol(s) for s in all_symbols}

        manifest_entries = build_manifest(data_lake, all_symbols, all_tfs)

        save_manifest_csv(manifest_entries, REPORTS_DIR / "data_lake_manifest.csv")
        save_manifest_csv(manifest_entries, LAKE_MANIFESTS_DIR / "latest_manifest.csv")
        save_manifest_json(
            manifest_entries, LAKE_MANIFESTS_DIR / "latest_manifest.json"
        )
        logger.info("Manifests updated.")


if __name__ == "__main__":
    main()
