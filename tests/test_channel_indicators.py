import pytest
import pandas as pd
from advanced_technical_indicators.channel_indicators import (
    add_bollinger_bands,
    add_bollinger_bandwidth,
    add_bollinger_percent_b,
    add_keltner_channel_placeholder,
    add_donchian_position,
    build_channel_indicator_registry,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


@pytest.fixture
def sample_ohlcv():
    n = 40
    return pd.DataFrame({
        "open": [100.0 + i for i in range(n)],
        "high": [103.0 + i for i in range(n)],
        "low": [97.0 + i for i in range(n)],
        "close": [100.0 + i for i in range(n)],
    })


def test_channel_indicators(sample_ohlcv):
    orig = sample_ohlcv.copy()

    df1 = add_bollinger_bands(sample_ohlcv, window=20)
    assert "bb_upper_20" in df1.columns
    assert "bb_mid_20" in df1.columns
    assert "bb_lower_20" in df1.columns
    assert sample_ohlcv.equals(orig)

    df2 = add_bollinger_bandwidth(sample_ohlcv, window=20)
    assert "bb_bandwidth_20" in df2.columns

    df3 = add_bollinger_percent_b(sample_ohlcv, window=20)
    assert "bb_percent_b_20" in df3.columns

    df4 = add_keltner_channel_placeholder(sample_ohlcv, window=20)
    assert "keltner_upper_20" in df4.columns

    df5 = add_donchian_position(sample_ohlcv, window=20)
    assert "donchian_position_20" in df5.columns


def test_channel_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_channel_indicator_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
