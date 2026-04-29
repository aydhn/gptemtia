"""
Yahoo Finance data provider.
"""

from typing import Optional

import pandas as pd
import yfinance as yf

from core.exceptions import DataProviderError
from core.logger import get_logger
from data.data_quality import validate_ohlcv_dataframe
from data.providers.base_provider import BaseDataProvider

logger = get_logger(__name__)


class YahooProvider(BaseDataProvider):
    """Data provider using the yfinance library."""

    def fetch_ohlcv(
        self,
        symbol: str,
        interval: str,
        start: Optional[str] = None,
        end: Optional[str] = None,
        period: Optional[str] = None,
    ) -> pd.DataFrame:

        self.validate_symbol(symbol)

        logger.info(f"Fetching data from Yahoo for {symbol} ({interval})")

        try:
            ticker = yf.Ticker(symbol)
            # Fetch data
            if start and end:
                df = ticker.history(
                    interval=interval, start=start, end=end, auto_adjust=False
                )
            elif period:
                df = ticker.history(interval=interval, period=period, auto_adjust=False)
            else:
                # If no start/end/period provided, default to a sensible value like 2y
                period = "2y"
                df = ticker.history(interval=interval, period=period, auto_adjust=False)

            if df is None or df.empty:
                raise DataProviderError(
                    f"No data returned for {symbol} from Yahoo Finance."
                )

            # MultiIndex columns handler
            if isinstance(df.columns, pd.MultiIndex):
                # Flatten MultiIndex, keeping only the first level (Price type)
                df.columns = [col[0] for col in df.columns]

            # Use base class to normalize columns and index
            df = self.normalize_ohlcv(df)

            # Validate the normalized data using data quality module
            validate_ohlcv_dataframe(df)

            return df

        except Exception as e:
            error_msg = (
                f"Failed to fetch data from Yahoo Finance for {symbol}: {str(e)}"
            )
            logger.error(error_msg)
            raise DataProviderError(error_msg) from e
