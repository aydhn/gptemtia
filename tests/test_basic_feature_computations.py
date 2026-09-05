import pytest
import pandas as pd
import numpy as np
from advanced_feature_engine.basic_feature_computations import (
    add_close_return,
    add_log_return,
    add_rolling_mean,
    add_rolling_std,
    add_sma,
    add_ema,
    add_true_range,
    add_atr,
    add_rsi,
    add_bollinger_zscore,
    add_quote_mid,
    add_quote_spread,
)


@pytest.fixture
def sample_ohlcv():
    n = 30
    prices = [100.0 + i * 0.5 for i in range(n)]
    return pd.DataFrame({
        "timestamp": pd.date_range("2026-01-01", periods=n, freq="D"),
        "open": [p - 0.2 for p in prices],
        "high": [p + 0.5 for p in prices],
        "low": [p - 0.5 for p in prices],
        "close": prices,
        "volume": [1000] * n,
        "bid": [p - 0.05 for p in prices],
        "ask": [p + 0.05 for p in prices],
    })


def test_basic_feature_computations(sample_ohlcv):
    orig = sample_ohlcv.copy()

    # 1. close return
    df1 = add_close_return(sample_ohlcv, window=1)
    assert "close_return_1" in df1.columns
    assert sample_ohlcv.equals(orig)  # input not mutated

    # 2. log return
    df2 = add_log_return(df1, window=1)
    assert "log_return_1" in df2.columns

    # 3. rolling mean
    df3 = add_rolling_mean(df2, window=5)
    assert "rolling_mean_5" in df3.columns

    # 4. rolling std
    df4 = add_rolling_std(df3, window=5)
    assert "rolling_std_5" in df4.columns

    # 5. sma & ema
    df5 = add_sma(df4, window=5)
    df6 = add_ema(df5, window=5)
    assert "sma_5" in df6.columns
    assert "ema_5" in df6.columns

    # 6. true range & atr
    df7 = add_true_range(df6)
    df8 = add_atr(df7, window=5)
    assert "true_range" in df8.columns
    assert "atr_5" in df8.columns

    # 7. rsi
    df9 = add_rsi(df8, window=5)
    assert "rsi_5" in df9.columns

    # 8. bollinger zscore
    df10 = add_bollinger_zscore(df9, window=5)
    assert "bollinger_zscore_5" in df10.columns

    # 9. quote mid & spread
    df11 = add_quote_mid(df10)
    df12 = add_quote_spread(df11)
    assert "quote_mid" in df12.columns
    assert "quote_spread" in df12.columns


def test_forbidden_output_name(sample_ohlcv):
    with pytest.raises(ValueError):
        add_close_return(sample_ohlcv, output_field="signal")

    with pytest.raises(ValueError):
        add_close_return(sample_ohlcv, output_field="buy")

    with pytest.raises(ValueError):
        add_close_return(sample_ohlcv, output_field="target")


def test_missing_field_error():
    empty_df = pd.DataFrame({"dummy": [1, 2, 3]})
    with pytest.raises(ValueError):
        add_close_return(empty_df, close_field="close")
