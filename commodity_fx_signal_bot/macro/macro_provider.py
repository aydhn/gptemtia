import datetime
import logging
from typing import Optional

import pandas as pd

from config.settings import Settings
from core.exceptions import DataProviderError
from data.providers.evds_provider import EVDSProvider
from data.providers.fred_provider import FREDProvider
from data.providers.yahoo_provider import YahooProvider
from macro.macro_series import MacroSeriesSpec

logger = logging.getLogger(__name__)


class MacroProvider:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.evds = EVDSProvider(api_key=settings.evds_api_key)
        self.fred = FREDProvider(api_key=settings.fred_api_key)
        self.yahoo = YahooProvider()

    def fetch_macro_series(
        self,
        spec: MacroSeriesSpec,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> pd.DataFrame:
        if not start_date:
            try:
                start_date = self.settings.default_macro_start_date
            except AttributeError:
                start_date = "2010-01-01"

        try:
            if spec.source == "evds":
                df = self.evds.fetch_series(
                    spec.code, start_date=start_date, end_date=end_date
                )
            elif spec.source == "fred":
                # For FRED, we can use aliases if code fails, or just use code directly
                fred_code = spec.aliases[0] if spec.aliases else spec.code
                df = self.fred.fetch_series(
                    fred_code, start_date=start_date, end_date=end_date
                )
            elif spec.source == "yahoo":
                # For Yahoo, we use the OHLCV method and extract the close price
                yahoo_symbol = spec.aliases[0] if spec.aliases else spec.code
                ohlcv_df = self.yahoo.fetch_ohlcv(
                    symbol=yahoo_symbol, interval="1d", start=start_date, end=end_date
                )
                if ohlcv_df.empty:
                    df = pd.DataFrame()
                else:
                    df = ohlcv_df[["close"]].rename(columns={"close": "value"})
            elif spec.source == "synthetic":
                logger.info("Skipping synthetic macro series fetch for %s", spec.code)
                return pd.DataFrame()
            else:
                raise DataProviderError(
                    f"Unsupported macro source: {spec.source} for {spec.code}"
                )

            # Add metadata
            if not df.empty:
                df.attrs["macro_code"] = spec.code
                df.attrs["source"] = spec.source
                df.attrs["frequency"] = spec.frequency
                df.attrs["downloaded_at_utc"] = datetime.datetime.now(
                    datetime.timezone.utc
                ).isoformat()

            return df

        except DataProviderError as e:
            logger.error("Data provider error for %s: %s", spec.code, str(e))
            return pd.DataFrame()
        except Exception as e:
            logger.error(
                "Unexpected error fetching macro series %s: %s", spec.code, str(e)
            )
            return pd.DataFrame()

    def fetch_many(
        self,
        specs: list[MacroSeriesSpec],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> dict[str, pd.DataFrame]:
        results = {}
        for spec in specs:
            if not spec.enabled:
                continue

            df = self.fetch_macro_series(spec, start_date=start_date, end_date=end_date)
            if not df.empty:
                results[spec.code] = df
            else:
                logger.warning("Failed to fetch or no data returned for %s", spec.code)

        return results
