import pytest
import pandas as pd
from advanced_technical_indicators.trend_indicators import (
    add_macd,
    add_ppo,
    add_donchian_channel,
    add_aroon,
    add_adx_dmi_placeholder,
    add_ichimoku_placeholder,
    build_trend_indicator_expansion_registry,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


@pytest.fixture
def sample_ohlcv():
    n = 60
    return pd.DataFrame({
        "open": [100.0 + i for i in range(n)],
        "high": [102.0 + i for i in range(n)],
        "low": [98.0 + i for i in range(n)],
        "close": [101.0 + i for i in range(n)],
    })


def test_trend_indicators(sample_ohlcv):
    orig = sample_ohlcv.copy()

    # MACD: test that smooth line is macd_smooth, NOT macd_signal
    df1 = add_macd(sample_ohlcv)
    assert "macd_line" in df1.columns
    assert "macd_smooth" in df1.columns
    assert "macd_hist" in df1.columns
    assert "macd_signal" not in df1.columns
    assert sample_ohlcv.equals(orig)

    df2 = add_ppo(sample_ohlcv)
    assert "ppo_line" in df2.columns
    assert "ppo_smooth" in df2.columns
    assert "ppo_hist" in df2.columns

    df3 = add_donchian_channel(sample_ohlcv, window=20)
    assert "donchian_upper_20" in df3.columns
    assert "donchian_lower_20" in df3.columns

    df4 = add_aroon(sample_ohlcv, window=20)
    assert "aroon_up_20" in df4.columns
    assert "aroon_down_20" in df4.columns

    df5 = add_adx_dmi_placeholder(sample_ohlcv, window=14)
    assert "adx_plus_di_14" in df5.columns
    assert "adx_minus_di_14" in df5.columns

    df6 = add_ichimoku_placeholder(sample_ohlcv)
    assert "ichimoku_tenkan" in df6.columns
    assert "ichimoku_kijun" in df6.columns


def test_trend_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_trend_indicator_expansion_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
