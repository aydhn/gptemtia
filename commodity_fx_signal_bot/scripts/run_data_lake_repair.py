import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from config.paths import LAKE_DIR, LAKE_JOURNALS_DIR, ensure_project_directories
from config.settings import settings
from config.symbols import get_allowed_timeframes_for_symbol, get_enabled_symbols
from core.logger import get_logger
from data.data_pipeline import DataPipeline
from data.download_manager import DownloadManager
from data.storage.cache_manager import CacheManager
from data.storage.data_lake import DataLake
from data.storage.download_journal import DownloadJournal


def main():
    parser = argparse.ArgumentParser(
        description="Repair missing or low-quality data in the Data Lake."
    )
    parser.add_argument("--limit", type=int, help="Limit number of symbols to check")
    parser.add_argument(
        "--asset-class", type=str, help="Filter by asset class (e.g., metals)"
    )
    parser.add_argument(
        "--period", type=str, default="2y", help="Data period for repair"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Only report what would be repaired"
    )
    args = parser.parse_args()

    logger = get_logger("run_data_lake_repair")
    ensure_project_directories()

    symbols = get_enabled_symbols()
    if args.asset_class:
        symbols = [s for s in symbols if s.asset_class == args.asset_class]

    timeframes_by_symbol = {
        s.symbol: get_allowed_timeframes_for_symbol(s) for s in symbols
    }

    data_lake = DataLake(LAKE_DIR)

    if args.dry_run:
        logger.info("Running in DRY-RUN mode. No data will be downloaded.")
        repair_candidates = []
        for spec in symbols[: args.limit] if args.limit else symbols:
            if spec.data_source == "synthetic" or spec.data_source in ("evds", "fred"):
                continue

            allowed_tfs = timeframes_by_symbol.get(spec.symbol, tuple())
            metadata = data_lake.load_metadata(spec)
            grades = metadata.get("quality_grades", {})

            for tf in allowed_tfs:
                exists = data_lake.has_ohlcv(spec, tf)
                grade = grades.get(tf, "N/A")

                if not exists or grade in ("D", "F", "N/A"):
                    repair_candidates.append(
                        f"{spec.symbol} ({tf}) - Grade: {grade}, Exists: {exists}"
                    )

        logger.info(f"Found {len(repair_candidates)} items needing repair:")
        for r in repair_candidates:
            logger.info(f"  - {r}")
        sys.exit(0)

    # Actual Repair
    cache_manager = CacheManager(LAKE_DIR.parent / "cache")
    pipeline = DataPipeline(settings, cache_manager)
    journal = DownloadJournal(LAKE_JOURNALS_DIR / "download_journal.csv")
    manager = DownloadManager(pipeline, data_lake, journal, settings)

    logger.info(f"Starting repair process for up to {args.limit or 'all'} symbols...")
    results = manager.repair_missing_data(
        specs=symbols,
        timeframes_by_symbol=timeframes_by_symbol,
        period=args.period,
        limit=args.limit,
    )

    logger.info("=== Repair Results ===")
    logger.info(f"Attempted: {results['attempted']}")
    logger.info(f"Success: {results['success']}")
    logger.info(f"Failed: {results['failed']}")
    logger.info("======================")


if __name__ == "__main__":
    main()
