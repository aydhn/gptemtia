import logging
from typing import Optional
import datetime
import requests
import pandas as pd

from config.settings import settings
from core.exceptions import DataProviderError
from data.providers.base_provider import BaseDataProvider

logger = logging.getLogger(__name__)


class FREDProvider(BaseDataProvider):
    """
    FRED (Federal Reserve Economic Data) data provider.
    Used for retrieving US macroeconomic data.
    """

    def __init__(self, api_key: Optional[str] = None):
        super().__init__()
        self.api_key = api_key or settings.fred_api_key
        self.base_url = "https://api.stlouisfed.org/fred/"

    def is_available(self) -> bool:
        """Check if FRED API key is configured."""
        return bool(self.api_key) and self.api_key != "replace_me"

    def fetch_ohlcv(
        self,
        symbol: str,
        interval: str,
        start: Optional[str] = None,
        end: Optional[str] = None,
        period: Optional[str] = None,
    ) -> pd.DataFrame:
        """
        FRED primarily provides series data, so OHLCV might not make sense directly.
        """
        raise NotImplementedError(
            "FREDProvider does not support fetching OHLCV data directly."
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
            logger.warning(
                "FRED API key is not configured. Cannot fetch series %s", series_id
            )
            raise DataProviderError("FRED API key is not configured.")

        url = f"{self.base_url}series/observations?series_id={series_id}&api_key={self.api_key}&file_type=json"

        if start_date:
            try:
                start_dt = pd.to_datetime(start_date)
                url += f"&observation_start={start_dt.strftime('%Y-%m-%d')}"
            except Exception:
                pass

        if end_date:
            try:
                end_dt = pd.to_datetime(end_date)
                url += f"&observation_end={end_dt.strftime('%Y-%m-%d')}"
            except Exception:
                pass

        try:
            logger.info(
                "Fetching FRED series %s from %s to %s", series_id, start_date, end_date
            )
            response = requests.get(url, timeout=15)
            response.raise_for_status()

            data = response.json()
            if "observations" not in data:
                raise DataProviderError(f"Unexpected FRED response format: {data}")

            observations = data["observations"]
            if not observations:
                logger.warning("No data found for FRED series %s", series_id)
                return pd.DataFrame()

            df = pd.DataFrame(observations)

            # Clean and format
            df = df[["date", "value"]]

            # Convert date
            df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d", errors="coerce")

            # Convert value to numeric, handling missing (FRED uses '.' for missing)
            df["value"] = pd.to_numeric(
                df["value"].replace(".", float("nan")), errors="coerce"
            )

            # Drop nulls and duplicates
            df = df.dropna(subset=["date", "value"])
            df = df.drop_duplicates(subset=["date"])

            df = df.set_index("date").sort_index()

            # Add metadata
            df.attrs["source"] = "fred"
            df.attrs["series_id"] = series_id

            return df

        except requests.RequestException as e:
            logger.error("Failed to fetch FRED series %s: %s", series_id, str(e))
            raise DataProviderError(f"FRED API request failed: {str(e)}")
        except Exception as e:
            logger.error("Error processing FRED series %s: %s", series_id, str(e))
            raise DataProviderError(f"Error processing FRED data: {str(e)}")

    def normalize_series(self, df: pd.DataFrame) -> pd.DataFrame:
        """Normalize series data frame to standard format."""
        if df.empty:
            return df

        result = df.copy()

        if "value" not in result.columns:
            if len(result.columns) == 1:
                result.columns = ["value"]
            else:
                raise DataProviderError(
                    "Cannot identify value column for normalization"
                )

        # Ensure index is datetime
        if not isinstance(result.index, pd.DatetimeIndex):
            result.index = pd.to_datetime(result.index)

        result = result[["value"]].sort_index()
        return result
