"""
Data Pipeline to handle symbol fetching, alias fallback, caching, and data quality.
"""
from typing import Optional, Dict, List
import pandas as pd

from core.logger import get_logger
from core.exceptions import DataProviderError
from config.settings import Settings
from config.symbols import SymbolSpec, get_all_candidate_symbols
from data.storage.cache_manager import CacheManager
from data.provider_registry import get_provider
from data.data_quality import validate_ohlcv_dataframe, is_dataframe_usable

logger = get_logger(__name__)

class DataPipeline:
    """Orchestrates data fetching, caching, and validation."""

    def __init__(self, settings: Settings, cache_manager: CacheManager):
        self.settings = settings
        self.cache_manager = cache_manager

    def fetch_symbol_data(
        self,
        spec: SymbolSpec,
        interval: str,
        period: Optional[str] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        use_cache: bool = True,
        refresh: bool = False,
    ) -> pd.DataFrame:
        """
        Fetch data for a symbol, trying aliases if primary fails.
        """
        candidate_symbols = get_all_candidate_symbols(spec)
        provider = get_provider(spec.data_source)

        for attempt_symbol in candidate_symbols:
            cache_path = self.cache_manager.build_cache_path(
                attempt_symbol, interval, period, start, end, self.settings.cache_format
            )

            # 1. Try Cache
            if use_cache and not refresh and self.cache_manager.exists(cache_path):
                logger.debug(f"Cache hit for {attempt_symbol}")
                try:
                    df = self.cache_manager.load_dataframe(cache_path)
                    if is_dataframe_usable(df, self.settings.min_ohlcv_rows):
                        logger.info(f"Loaded {attempt_symbol} from cache successfully.")
                        return df
                except Exception as e:
                    logger.warning(f"Failed to load/validate cache for {attempt_symbol}: {e}")

            # 2. Try Provider
            if self.settings.allow_network_calls:
                try:
                    df = provider.fetch_ohlcv(attempt_symbol, interval, start, end, period)

                    if is_dataframe_usable(df, self.settings.min_ohlcv_rows):
                        logger.info(f"Fetched {attempt_symbol} via provider successfully.")
                        if use_cache:
                            self.cache_manager.save_dataframe(df, cache_path)
                        return df
                    else:
                        logger.warning(f"Data for {attempt_symbol} fetched but not usable.")
                except Exception as e:
                    logger.debug(f"Failed to fetch {attempt_symbol} via provider: {e}")

        # If all candidates fail
        raise DataProviderError(
            f"Failed to fetch usable data for {spec.symbol} and its aliases {spec.aliases} using {spec.data_source}"
        )

    def fetch_many(
        self,
        specs: List[SymbolSpec],
        interval: str,
        period: Optional[str] = None,
        max_symbols: Optional[int] = None,
    ) -> Dict[str, pd.DataFrame]:
        """
        Fetch data for multiple symbols.
        Returns a dictionary mapping primary symbol to its DataFrame.
        """
        results = {}
        failed_symbols = []

        limit = max_symbols if max_symbols else len(specs)
        for spec in specs[:limit]:
            try:
                df = self.fetch_symbol_data(spec, interval, period=period)
                results[spec.symbol] = df
            except Exception as e:
                logger.error(f"Error fetching data for {spec.symbol}: {e}")
                failed_symbols.append(spec.symbol)
                if self.settings.fail_fast_data_downloads:
                    raise

        if failed_symbols:
            logger.warning(f"Failed to fetch {len(failed_symbols)} symbols: {failed_symbols}")

        return results
