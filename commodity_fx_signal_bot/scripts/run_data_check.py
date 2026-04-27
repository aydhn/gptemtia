"""
Smoke test script to verify data fetching for a few symbols using DataPipeline.
"""
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
    logger = get_logger("run_data_check")
    ensure_project_directories()

    logger.info("Starting Data Check Smoke Test...")

    symbols = get_enabled_symbols()
    if not symbols:
        logger.warning("No enabled symbols found.")
        return

    # Test first 3 symbols
    test_symbols = symbols[:3]

    cache_manager = CacheManager(CACHE_DIR)

    # Force settings so smoke tests don't fail due to small data request sizes
    original_min_rows = settings.min_ohlcv_rows
    settings.min_ohlcv_rows = 10

    pipeline = DataPipeline(settings, cache_manager)

    try:
        results = pipeline.fetch_many(
            specs=test_symbols,
            interval="1d",
            period="1mo",
            max_symbols=3
        )

        success_count = len(results)

        for symbol, df in results.items():
            logger.info(f"Success! {symbol} returned {len(df)} rows.")

        logger.info(f"Data Check completed. {success_count}/{len(test_symbols)} successful.")

    except Exception as e:
        logger.error(f"Smoke test failed: {e}")
    finally:
        settings.min_ohlcv_rows = original_min_rows

if __name__ == "__main__":
    main()
