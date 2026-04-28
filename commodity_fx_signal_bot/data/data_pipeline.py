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
from config.timeframes import is_derived_timeframe, get_provider_interval_for_timeframe

logger = get_logger(__name__)


def resample_ohlcv(df: pd.DataFrame, target_timeframe: str) -> pd.DataFrame:
    """
    Resample an OHLCV DataFrame to a target timeframe.
    """
    if df is None or df.empty:
        return df

    # Pandas offset aliases: '4h' -> '4H'
    pandas_tf = target_timeframe.upper()
    if pandas_tf == "1D":
        pandas_tf = "D"
    elif pandas_tf == "1WK":
        pandas_tf = "W"
    elif pandas_tf == "1MO":
        pandas_tf = "M"

    agg_dict = {}
    if "open" in df.columns:
        agg_dict["open"] = "first"
    if "high" in df.columns:
        agg_dict["high"] = "max"
    if "low" in df.columns:
        agg_dict["low"] = "min"
    if "close" in df.columns:
        agg_dict["close"] = "last"
    if "adj_close" in df.columns:
        agg_dict["adj_close"] = "last"
    if "volume" in df.columns:
        agg_dict["volume"] = "sum"

    resampled_df = df.resample(pandas_tf).agg(agg_dict)
    resampled_df = resampled_df.dropna(how="all")

    # Restore attrs if possible
    resampled_df.attrs = df.attrs.copy()

    return resampled_df


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
        # Timeframe awareness
        is_derived = False
        try:
            if is_derived_timeframe(interval):
                is_derived = True
                provider_interval = get_provider_interval_for_timeframe(interval)
            else:
                provider_interval = interval
        except Exception:
            # Fallback if timeframe not found in registry
            provider_interval = interval

        candidate_symbols = get_all_candidate_symbols(spec)
        provider = get_provider(spec.data_source)

        for attempt_symbol in candidate_symbols:
            cache_path = self.cache_manager.build_cache_path(
                attempt_symbol, interval, period, start, end, self.settings.cache_format
            )

            # 1. Try Cache
            if use_cache and not refresh and self.cache_manager.exists(cache_path):
                logger.debug(f"Cache hit for {attempt_symbol} at {interval}")
                try:
                    df = self.cache_manager.load_dataframe(cache_path)
                    if is_dataframe_usable(df, self.settings.min_ohlcv_rows):
                        logger.info(f"Loaded {attempt_symbol} from cache successfully.")
                        df.attrs["requested_symbol"] = spec.symbol
                        df.attrs["resolved_symbol"] = attempt_symbol
                        df.attrs["used_alias"] = attempt_symbol != spec.symbol
                        df.attrs["data_source"] = spec.data_source
                        return df
                except Exception as e:
                    logger.warning(
                        f"Failed to load/validate cache for {attempt_symbol}: {e}"
                    )

            # 2. Try Provider
            if self.settings.allow_network_calls:
                try:
                    # Fetch using provider interval
                    df = provider.fetch_ohlcv(
                        attempt_symbol, provider_interval, start, end, period
                    )

                    # Resample if derived
                    if is_derived and not df.empty:
                        logger.debug(
                            f"Resampling {attempt_symbol} from {provider_interval} to {interval}"
                        )
                        df = resample_ohlcv(df, interval)

                    if is_dataframe_usable(df, self.settings.min_ohlcv_rows):
                        logger.info(
                            f"Fetched {attempt_symbol} via provider successfully."
                        )
                        if use_cache:
                            self.cache_manager.save_dataframe(df, cache_path)
                        df.attrs["requested_symbol"] = spec.symbol
                        df.attrs["resolved_symbol"] = attempt_symbol
                        df.attrs["used_alias"] = attempt_symbol != spec.symbol
                        df.attrs["data_source"] = spec.data_source
                        return df
                    else:
                        logger.warning(
                            f"Data for {attempt_symbol} fetched but not usable."
                        )
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
            logger.warning(
                f"Failed to fetch {len(failed_symbols)} symbols: {failed_symbols}"
            )

        return results
