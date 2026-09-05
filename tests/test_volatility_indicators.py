import pytest
import pandas as pd
from advanced_technical_indicators.volatility_indicators import (
    add_true_range,
    add_atr,
    add_rolling_std,
    add_realized_volatility,
    add_parkinson_volatility,
    add_garman_klass_volatility_placeholder,
    build_volatility_indicator_expansion_registry,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


@pytest.fixture
def sample_ohlcv():
    n = 40
    return pd.DataFrame({
        "open": [100.0 + i for i in range(n)],
        "high": [102.0 + i for i in range(n)],
        "low": [98.0 + i for i in range(n)],
        "close": [101.0 + i for i in range(n)],
    })


def test_volatility_indicators(sample_ohlcv):
    orig = sample_ohlcv.copy()

    df1 = add_true_range(sample_ohlcv)
    assert "true_range" in df1.columns
    assert sample_ohlcv.equals(orig)

    df2 = add_atr(sample_ohlcv, window=14)
    assert "atr_14" in df2.columns

    df3 = add_rolling_std(sample_ohlcv, window=20)
    assert "rolling_std_20" in df3.columns

    df4 = add_realized_volatility(sample_ohlcv, window=20)
    assert "realized_vol_20" in df4.columns

    df5 = add_parkinson_volatility(sample_ohlcv, window=20)
    assert "parkinson_vol_20" in df5.columns

    df6 = add_garman_klass_volatility_placeholder(sample_ohlcv, window=20)
    assert "garman_klass_vol_20" in df6.columns


def test_volatility_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_volatility_indicator_expansion_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
