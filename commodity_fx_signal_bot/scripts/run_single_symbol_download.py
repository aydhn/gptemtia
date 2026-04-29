"""
Script to download data for a single symbol using DataPipeline.
"""

import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from config.paths import CACHE_DIR, ensure_project_directories
from config.settings import settings
from config.symbols import get_symbol_spec
from core.logger import get_logger
from data.data_pipeline import DataPipeline
from data.data_quality import build_data_quality_report
from data.storage.cache_manager import CacheManager


def main():
    parser = argparse.ArgumentParser(
        description="Download OHLCV data for a single symbol."
    )
    parser.add_argument(
        "--symbol", required=True, help="Symbol to download (e.g. GC=F)"
    )
    parser.add_argument(
        "--interval",
        default=settings.default_interval,
        help="Data interval (e.g. 1d, 1h)",
    )
    parser.add_argument(
        "--period", default=settings.default_period, help="Data period (e.g. 1y, 6mo)"
    )
    parser.add_argument(
        "--refresh", action="store_true", help="Force refresh, ignoring cache"
    )
    args = parser.parse_args()

    logger = get_logger("run_single_symbol_download")
    ensure_project_directories()

    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol '{args.symbol}' not found in universe.")
        sys.exit(1)

    cache_manager = CacheManager(CACHE_DIR)
    pipeline = DataPipeline(settings, cache_manager)

    logger.info(
        f"Downloading data for {args.symbol} (interval: {args.interval}, period: {args.period})"
    )

    try:
        df = pipeline.fetch_symbol_data(
            spec=spec,
            interval=args.interval,
            period=args.period,
            use_cache=settings.data_cache_enabled,
            refresh=args.refresh,
        )

        report = build_data_quality_report(df)
        logger.info("Data Quality Report:")
        for k, v in report.items():
            logger.info(f"  {k}: {v}")

        logger.info("\nLast 5 rows:")
        print(df.tail(5))

    except Exception as e:
        logger.error(f"Failed to fetch data for {args.symbol}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
