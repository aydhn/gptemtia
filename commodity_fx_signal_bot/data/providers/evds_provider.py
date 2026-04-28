"""
EVDS Data Provider Skeleton.
"""

from typing import Optional
import pandas as pd
from data.providers.base_provider import BaseDataProvider
from config.settings import settings
from core.exceptions import DataProviderError


class EVDSProvider(BaseDataProvider):
    """
    EVDS (Central Bank of Turkey) data provider.
    Used for retrieving Turkish macroeconomic data.
    """

    def is_available(self) -> bool:
        """Check if EVDS API key is configured."""
        return settings.evds_api_key and settings.evds_api_key != "replace_me"

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
        EVDS primarily provides series data, so OHLCV might not make sense directly.
        """
        raise NotImplementedError(
            "EVDSProvider does not support fetching OHLCV data directly yet."
        )

    def fetch_series(
        self, series_code: str, start_date: str, end_date: str
    ) -> pd.DataFrame:
        """
        Fetch a specific series from EVDS.
        """
        if not self.is_available():
            raise DataProviderError("EVDS API key is not configured.")

        # Skeleton implementation
        # TODO: Implement actual EVDS API calls
        return pd.DataFrame()
