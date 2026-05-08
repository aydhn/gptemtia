import pandas as pd
import pytest

from core.exceptions import DataProviderError
from data.providers.yahoo_provider import YahooProvider


@pytest.fixture
def provider():
    return YahooProvider()


def test_normalize_ohlcv_basic(provider):
    # Mock dataframe with spaces and weird capitalization
    dates = pd.date_range("2023-01-01", periods=3)
    df = pd.DataFrame(
        {
            "Open": [10.0, 11.0, 12.0],
            "High": [10.5, 11.5, 12.5],
            "Low": [9.5, 10.5, 11.5],
            "Close": [10.2, 11.2, 12.2],
            "Adj Close": [10.2, 11.2, 12.2],
            "Volume": [100, 200, 150],
        },
        index=dates,
    )

    norm_df = provider.normalize_ohlcv(df)

    # Check column names
    assert list(norm_df.columns) == [
        "open",
        "high",
        "low",
        "close",
        "adj_close",
        "volume",
    ]

    # Check index timezone
    assert norm_df.index.tz is not None
    assert str(norm_df.index.tz) == "UTC"


def test_normalize_ohlcv_missing_adj_close(provider):
    # Missing adj_close should fall back to close
    dates = pd.date_range("2023-01-01", periods=3)
    df = pd.DataFrame(
        {
            "Open": [10.0, 11.0, 12.0],
            "High": [10.5, 11.5, 12.5],
            "Low": [9.5, 10.5, 11.5],
            "Close": [10.2, 11.2, 12.2],
            "Volume": [100, 200, 150],
        },
        index=dates,
    )

    norm_df = provider.normalize_ohlcv(df)
    assert "adj_close" in norm_df.columns
    pd.testing.assert_series_equal(
        norm_df["close"], norm_df["adj_close"], check_names=False
    )


def test_normalize_ohlcv_missing_volume(provider):
    # Missing volume (common in FX) should be set to 0
    dates = pd.date_range("2023-01-01", periods=3)
    df = pd.DataFrame(
        {
            "Open": [10.0, 11.0, 12.0],
            "High": [10.5, 11.5, 12.5],
            "Low": [9.5, 10.5, 11.5],
            "Close": [10.2, 11.2, 12.2],
            "Adj Close": [10.2, 11.2, 12.2],
        },
        index=dates,
    )

    norm_df = provider.normalize_ohlcv(df)
    assert "volume" in norm_df.columns
    assert (norm_df["volume"] == 0).all()


def test_normalize_ohlcv_missing_required_column(provider):
    # Missing something critical like open
    dates = pd.date_range("2023-01-01", periods=3)
    df = pd.DataFrame(
        {
            "High": [10.5, 11.5, 12.5],
            "Low": [9.5, 10.5, 11.5],
            "Close": [10.2, 11.2, 12.2],
        },
        index=dates,
    )

    with pytest.raises(
        DataProviderError, match="Missing required columns after normalization"
    ):
        provider.normalize_ohlcv(df)


@pytest.mark.network
def test_fetch_ohlcv_network(provider):
    """
    Optional network test. Only run if --run-network is report_builder = ReportBuilder()ed or similar.
    We just use a very safe symbol and period.
    """
    df = provider.fetch_ohlcv("GC=F", interval="1d", period="1mo")
    assert not df.empty
    assert list(df.columns) == ["open", "high", "low", "close", "adj_close", "volume"]
