import pytest
import pandas as pd
from datetime import datetime, timezone
from data.data_pipeline import resample_ohlcv, DataPipeline
from config.settings import Settings


@pytest.fixture
def hourly_df():
    dates = pd.date_range("2023-01-01 00:00:00", periods=5, freq="1h", tz="UTC")
    df = pd.DataFrame(
        {
            "open": [10.0, 11.0, 12.0, 11.5, 12.5],
            "high": [10.5, 11.5, 12.5, 12.0, 13.0],
            "low": [9.5, 10.5, 11.5, 11.0, 12.0],
            "close": [10.2, 11.2, 12.2, 11.8, 12.8],
            "adj_close": [10.2, 11.2, 12.2, 11.8, 12.8],
            "volume": [100, 200, 150, 300, 250],
        },
        index=dates,
    )
    return df


def test_resample_ohlcv_1h_to_4h(hourly_df):
    # This will take 5 hourly rows and group them by 4 hours
    resampled = resample_ohlcv(hourly_df, "4h")

    # 2023-01-01 00:00:00 to 03:00:00 (4 rows) -> 1 row
    # 2023-01-01 04:00:00 (1 row) -> 1 row
    assert len(resampled) == 2

    first_row = resampled.iloc[0]
    assert first_row["open"] == 10.0
    assert first_row["high"] == 12.5  # max of 10.5, 11.5, 12.5, 12.0
    assert first_row["low"] == 9.5  # min of 9.5, 10.5, 11.5, 11.0
    assert first_row["close"] == 11.8  # last close
    assert first_row["volume"] == 750  # sum of 100+200+150+300
