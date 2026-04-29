"""
FRED Data Provider Skeleton.
"""

from typing import Optional

import pandas as pd

from config.settings import settings
from core.exceptions import DataProviderError
from data.providers.base_provider import BaseDataProvider


class FREDProvider(BaseDataProvider):
    """
    FRED (Federal Reserve Economic Data) provider.
    Used for retrieving US macroeconomic data.
    """

    def is_available(self) -> bool:
        """Check if FRED API key is configured."""
        return settings.fred_api_key and settings.fred_api_key != "replace_me"

    def fetch_ohlcv(
        self,
        symbol: str,
        interval: str,
        start: Optional[str] = None,
        end: Optional[str] = None,
        period: Optional[str] = None,
    ) -> pd.DataFrame:
        """
        Skeleton method to align with BaseDataProvider.
        FRED provides series data, not OHLCV.
        """
        raise NotImplementedError(
            "FREDProvider does not support fetching OHLCV data directly yet."
        )

    def fetch_series(
        self,
        series_id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> pd.DataFrame:
        """
        Fetch a specific series from FRED.
        """
        if not self.is_available():
            raise DataProviderError("FRED API key is not configured.")

        # Skeleton implementation
        # TODO: Implement actual FRED API calls
        return pd.DataFrame()
