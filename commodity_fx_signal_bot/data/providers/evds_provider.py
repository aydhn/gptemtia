import logging
from typing import Optional
import datetime
import requests
import pandas as pd

from config.settings import settings
from core.exceptions import DataProviderError
from data.providers.base_provider import BaseDataProvider

logger = logging.getLogger(__name__)


class EVDSProvider(BaseDataProvider):
    """
    EVDS (Central Bank of Turkey) data provider.
    Used for retrieving Turkish macroeconomic data.
    """

    def __init__(self, api_key: Optional[str] = None):
        super().__init__()
        self.api_key = api_key or settings.evds_api_key
        self.base_url = "https://evds2.tcmb.gov.tr/service/evds/"

    def is_available(self) -> bool:
        """Check if EVDS API key is configured."""
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
        EVDS primarily provides series data, so OHLCV might not make sense directly.
        """
        raise NotImplementedError(
            "EVDSProvider does not support fetching OHLCV data directly."
        )

    def fetch_series(
        self, series_code: str, start_date: str, end_date: Optional[str] = None
    ) -> pd.DataFrame:
        """
        Fetch a specific series from EVDS.
        """
        if not self.is_available():
            logger.warning(
                "EVDS API key is not configured. Cannot fetch series %s", series_code
            )
            raise DataProviderError("EVDS API key is not configured.")

        if not end_date:
            end_date = datetime.datetime.now().strftime("%d-%m-%Y")

        # EVDS dates are usually DD-MM-YYYY
        try:
            # Parse YYYY-MM-DD and convert to DD-MM-YYYY if needed
            if "-" in start_date and len(start_date.split("-")[0]) == 4:
                start_dt = pd.to_datetime(start_date)
                start_date = start_dt.strftime("%d-%m-%Y")

            if "-" in end_date and len(end_date.split("-")[0]) == 4:
                end_dt = pd.to_datetime(end_date)
                end_date = end_dt.strftime("%d-%m-%Y")
        except Exception:
            pass

        url = f"{self.base_url}series={series_code}&startDate={start_date}&endDate={end_date}&type=json&key={self.api_key}"

        try:
            logger.info(
                "Fetching EVDS series %s from %s to %s",
                series_code,
                start_date,
                end_date,
            )
            response = requests.get(url, timeout=15)
            response.raise_for_status()

            data = response.json()
            if "items" not in data:
                raise DataProviderError(f"Unexpected EVDS response format: {data}")

            items = data["items"]
            if not items:
                logger.warning("No data found for EVDS series %s", series_code)
                return pd.DataFrame()

            df = pd.DataFrame(items)

            # Series column usually replaces '.' with '_' in the response
            col_name = series_code.replace(".", "_")
            if col_name not in df.columns:
                # Sometimes it returns a slightly different name or the original name
                if series_code in df.columns:
                    col_name = series_code
                else:
                    # Find a column that looks like data
                    possible_cols = [
                        c for c in df.columns if c not in ("Tarih", "UNIXTIME")
                    ]
                    if possible_cols:
                        col_name = possible_cols[0]
                    else:
                        raise DataProviderError(
                            f"Cannot find data column in EVDS response: {df.columns}"
                        )

            # Clean and format
            df = df.rename(columns={"Tarih": "date", col_name: "value"})

            # Convert date
            df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y", errors="coerce")

            # Convert value to numeric, handling missing
            df["value"] = pd.to_numeric(df["value"], errors="coerce")

            # Drop nulls and duplicates
            df = df.dropna(subset=["date", "value"])
            df = df.drop_duplicates(subset=["date"])

            df = df.set_index("date").sort_index()

            # Select only value column
            df = df[["value"]]

            # Add metadata
            df.attrs["source"] = "evds"
            df.attrs["series_code"] = series_code

            return df

        except requests.RequestException as e:
            logger.error("Failed to fetch EVDS series %s: %s", series_code, str(e))
            raise DataProviderError(f"EVDS API request failed: {str(e)}")
        except Exception as e:
            logger.error("Error processing EVDS series %s: %s", series_code, str(e))
            raise DataProviderError(f"Error processing EVDS data: {str(e)}")

    def normalize_series(
        self, df: pd.DataFrame, value_col: Optional[str] = None
    ) -> pd.DataFrame:
        """Normalize series data frame to standard format."""
        if df.empty:
            return df

        result = df.copy()

        if value_col and value_col in result.columns and value_col != "value":
            result = result.rename(columns={value_col: "value"})

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
