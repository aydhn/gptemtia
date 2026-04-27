"""
Base Data Provider definition.
"""
from abc import ABC, abstractmethod
from typing import Optional
import pandas as pd

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
        end: Optional[str] = None
    ) -> pd.DataFrame:
        """
        Fetch OHLCV data for a given symbol and interval.

        Args:
            symbol: The symbol to fetch (e.g., 'GC=F', 'EURUSD=X')
            interval: The timeframe interval (e.g., '1h', '1d')
            start: Start date string 'YYYY-MM-DD'
            end: End date string 'YYYY-MM-DD'

        Returns:
            pd.DataFrame: DataFrame containing standardized OHLCV data.
                          Expected columns: open, high, low, close, adj_close, volume
                          Expected index: DatetimeIndex

        Raises:
            DataProviderError: If data cannot be fetched or processed.
        """
        pass
