"""
Smoke test script to verify data fetching for a few symbols.
"""
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from core.logger import get_logger
from config.symbols import get_enabled_symbols
from data.providers.yahoo_provider import YahooProvider
from data.data_quality import validate_ohlcv_dataframe

logger = get_logger("run_data_check")

def main():
    logger.info("Starting Data Check Smoke Test...")

    symbols = get_enabled_symbols()
    if not symbols:
        logger.warning("No enabled symbols found.")
        return

    # Test first 3 symbols
    test_symbols = symbols[:3]
    provider = YahooProvider()

    success_count = 0
    for spec in test_symbols:
        try:
            logger.info(f"Testing fetch for {spec.symbol}...")
            df = provider.fetch_ohlcv(spec.symbol, interval="1d", start=None, end=None)

            # Basic validation
            validate_ohlcv_dataframe(df)

            logger.info(f"Success! {spec.symbol} returned {len(df)} rows.")
            success_count += 1
        except Exception as e:
            logger.error(f"Failed for {spec.symbol}: {str(e)}")

    logger.info(f"Data Check completed. {success_count}/{len(test_symbols)} successful.")

if __name__ == "__main__":
    main()
