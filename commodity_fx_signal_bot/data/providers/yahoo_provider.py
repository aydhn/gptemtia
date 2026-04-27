"""
Yahoo Finance data provider.
"""
import yfinance as yf
import pandas as pd
from typing import Optional

from core.logger import get_logger
from core.exceptions import DataProviderError
from data.providers.base_provider import BaseDataProvider

logger = get_logger(__name__)

class YahooProvider(BaseDataProvider):
    """Data provider using the yfinance library."""

    def fetch_ohlcv(
        self,
        symbol: str,
        interval: str,
        start: Optional[str] = None,
        end: Optional[str] = None
    ) -> pd.DataFrame:

        logger.info(f"Fetching data from Yahoo for {symbol} ({interval})")

        try:
            ticker = yf.Ticker(symbol)
            # Fetch data
            if start and end:
                df = ticker.history(interval=interval, start=start, end=end, auto_adjust=False)
            else:
                # If no start/end provided, fetch max available history based on interval
                period = "730d" if interval in ["1h", "60m"] else "max"
                df = ticker.history(interval=interval, period=period, auto_adjust=False)

            if df is None or df.empty:
                raise DataProviderError(f"No data returned for {symbol} from Yahoo Finance.")

            # Normalize column names to lowercase
            df.columns = [c.lower() for c in df.columns]

            # Ensure required columns exist
            # yfinance returns 'adj close' with space if auto_adjust=False
            if "adj close" in df.columns:
                df.rename(columns={"adj close": "adj_close"}, inplace=True)
            elif "close" in df.columns and "adj_close" not in df.columns:
                df["adj_close"] = df["close"]

            required_cols = ["open", "high", "low", "close", "adj_close", "volume"]
            for col in required_cols:
                if col not in df.columns:
                    if col == "volume":
                         df["volume"] = 0 # Default volume if missing
                    else:
                         raise DataProviderError(f"Missing required column {col} in data for {symbol}")

            # Keep only required columns
            df = df[required_cols]

            # Ensure index is timezone-aware datetime
            if df.index.tz is None:
                df.index = df.index.tz_localize('UTC')
            else:
                df.index = df.index.tz_convert('UTC')

            return df

        except Exception as e:
            error_msg = f"Failed to fetch data from Yahoo Finance for {symbol}: {str(e)}"
            logger.error(error_msg)
            raise DataProviderError(error_msg) from e
