import pytest
import pandas as pd
from advanced_technical_indicators.range_indicators import (
    add_rolling_high_low_range,
    add_rolling_range_pct,
    add_average_range,
    add_range_zscore,
    build_range_indicator_registry,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


@pytest.fixture
def sample_ohlcv():
    n = 30
    return pd.DataFrame({
        "high": [105.0 + i for i in range(n)],
        "low": [95.0 + i for i in range(n)],
        "close": [100.0 + i for i in range(n)],
    })


def test_range_indicators(sample_ohlcv):
    orig = sample_ohlcv.copy()

    df1 = add_rolling_high_low_range(sample_ohlcv, window=10)
    assert "rolling_hl_range_10" in df1.columns
    assert sample_ohlcv.equals(orig)

    df2 = add_rolling_range_pct(sample_ohlcv, window=10)
    assert "rolling_range_pct_10" in df2.columns

    df3 = add_average_range(sample_ohlcv, window=10)
    assert "average_range_10" in df3.columns

    df4 = add_range_zscore(sample_ohlcv, window=10)
    assert "range_zscore_10" in df4.columns


def test_range_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_range_indicator_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
