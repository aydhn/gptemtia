"""
Script to test data download for the enabled universe symbols.
"""
import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from core.logger import get_logger
from config.settings import settings
from config.paths import CACHE_DIR, ensure_project_directories
from config.symbols import get_enabled_symbols
from data.storage.cache_manager import CacheManager
from data.data_pipeline import DataPipeline

def main():
    parser = argparse.ArgumentParser(description="Bulk download data to check universe stability.")
    parser.add_argument("--limit", type=int, help="Limit number of symbols to check")
    parser.add_argument("--interval", default=settings.default_interval, help="Data interval (e.g. 1d, 1h)")
    parser.add_argument("--period", default=settings.default_period, help="Data period (e.g. 6mo, 1y)")
    parser.add_argument("--refresh", action="store_true", help="Force refresh, ignoring cache")
    args = parser.parse_args()

    logger = get_logger("run_bulk_data_check")
    ensure_project_directories()

    specs = get_enabled_symbols()
    if args.limit:
        specs = specs[:args.limit]

    logger.info(f"Starting bulk data check for {len(specs)} symbols (interval: {args.interval}, period: {args.period})")

    cache_manager = CacheManager(CACHE_DIR)

    # We temporarily disable fail fast for bulk operations
    original_fail_fast = settings.fail_fast_data_downloads
    settings.fail_fast_data_downloads = False

    pipeline = DataPipeline(settings, cache_manager)

    try:
        results = pipeline.fetch_many(
            specs=specs,
            interval=args.interval,
            period=args.period
        )

        # Build Summary Report
        logger.info("====================================")
        logger.info("      BULK DATA CHECK SUMMARY       ")
        logger.info("====================================")

        total = len(specs)
        success = len(results)
        failed = total - success

        logger.info(f"Total symbols checked: {total}")
        logger.info(f"Successful: {success}")
        logger.info(f"Failed: {failed}")

        # Asset class success rates
        asset_class_stats = {}
        for spec in specs:
            ac = spec.asset_class
            if ac not in asset_class_stats:
                asset_class_stats[ac] = {"total": 0, "success": 0}
            asset_class_stats[ac]["total"] += 1
            if spec.symbol in results:
                asset_class_stats[ac]["success"] += 1

        logger.info("\nAsset Class Success Rates:")
        for ac, stats in asset_class_stats.items():
            rate = (stats["success"] / stats["total"]) * 100 if stats["total"] > 0 else 0
            logger.info(f"  {ac}: {stats['success']}/{stats['total']} ({rate:.1f}%)")

        if failed > 0:
            failed_symbols = [s.symbol for s in specs if s.symbol not in results]
            logger.warning(f"\nFailed symbols: {failed_symbols}")

    finally:
        # Restore setting
        settings.fail_fast_data_downloads = original_fail_fast

if __name__ == "__main__":
    main()
