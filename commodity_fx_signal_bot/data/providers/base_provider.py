"""
Base Data Provider definition.
"""

from abc import ABC, abstractmethod
from typing import Optional

import pandas as pd

from core.exceptions import DataProviderError


class BaseDataProvider(ABC):
    """
    Abstract base class for all data providers.
    Defines the standard interface for fetching OHLCV data.
    """

    def __init__(self):
        self.name = self.__class__.__name__

    @abstractmethod
    def fetch_ohlcv(
        self,
        symbol: str,
        interval: str,
        start: Optional[str] = None,
        end: Optional[str] = None,
        period: Optional[str] = None,
    ) -> pd.DataFrame:
        """
        Fetch OHLCV data for a given symbol and interval.

        Args:
            symbol: The symbol to fetch (e.g., 'GC=F', 'EURUSD=X')
            interval: The timeframe interval (e.g., '1h', '1d')
            start: Start date string 'YYYY-MM-DD'
            end: End date string 'YYYY-MM-DD'
            period: Time period to fetch (e.g., '1y', '60d')

        Returns:
            pd.DataFrame: DataFrame containing standardized OHLCV data.
                          Expected columns: open, high, low, close, adj_close, volume
                          Expected index: DatetimeIndex

        Raises:
            DataProviderError: If data cannot be fetched or processed.
        """

    def is_available(self) -> bool:
        """
        Check if the data provider is available for use.
        Override this for providers requiring API keys.
        """
        return True

    def validate_symbol(self, symbol: str) -> None:
        """
        Validate a symbol before fetching. Override to implement custom validation.
        """
        if not symbol or not isinstance(symbol, str):
            raise ValueError(f"Invalid symbol: {symbol}")

    def normalize_ohlcv(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Normalize OHLCV DataFrame to ensure standard columns and formatting.

        Args:
            df: Raw DataFrame from provider

        Returns:
            pd.DataFrame: Normalized DataFrame
        """
        if df is None or df.empty:
            return df

        # 1. Lowercase column names
        df.columns = [str(c).lower().strip() for c in df.columns]

        # 2. Rename space 'adj close' if it exists (yfinance behavior)
        if "adj close" in df.columns:
            df.rename(columns={"adj close": "adj_close"}, inplace=True)

        # 3. Handle missing 'adj_close'
        if "close" in df.columns and "adj_close" not in df.columns:
            df["adj_close"] = df["close"]

        # 4. Handle missing 'volume' (especially for FX)
        if "volume" not in df.columns:
            df["volume"] = 0

        # 5. Check if we have all necessary columns
        required_cols = ["open", "high", "low", "close", "adj_close", "volume"]
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise DataProviderError(
                f"Missing required columns after normalization: {missing_cols}"
            )

        # 6. Reorder columns
        df = df[required_cols]

        # 7. Ensure DatetimeIndex
        if not isinstance(df.index, pd.DatetimeIndex):
            try:
                df.index = pd.to_datetime(df.index)
            except Exception as e:
                raise DataProviderError(
                    f"Failed to convert index to DatetimeIndex: {e}"
                )

        # 8. Timezone handling
        if df.index.tz is None:
            df.index = df.index.tz_localize("UTC")
        else:
            df.index = df.index.tz_convert("UTC")

        return df
