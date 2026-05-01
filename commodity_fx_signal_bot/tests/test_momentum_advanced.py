import numpy as np
import pandas as pd
import pytest

from indicators.momentum_advanced import (
    calculate_momentum_acceleration,
    calculate_momentum_slope,
    calculate_multi_cci,
    calculate_multi_momentum,
    calculate_multi_roc,
    calculate_multi_rsi,
    calculate_multi_stochastic,
    calculate_multi_williams_r,
    calculate_relative_momentum_rank,
)


@pytest.fixture
def sample_ohlcv():
    dates = pd.date_range("2023-01-01", periods=100, freq="D")
    df = pd.DataFrame(
        {
            "open": np.random.uniform(100, 200, 100),
            "high": np.random.uniform(150, 250, 100),
            "low": np.random.uniform(50, 150, 100),
            "close": np.random.uniform(100, 200, 100),
            "volume": np.random.uniform(1000, 5000, 100),
        },
        index=dates,
    )
    df["high"] = df[["open", "close", "high"]].max(axis=1)
    df["low"] = df[["open", "close", "low"]].min(axis=1)
    return df


def test_calculate_multi_rsi(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_rsi(df, windows=(7, 14))
    assert "rsi_7" in res.columns
    assert "rsi_14" in res.columns
    assert len(res) == len(df)
    assert df.equals(sample_ohlcv)


def test_calculate_multi_roc(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_roc(df, windows=(5, 10))
    assert "roc_5" in res.columns
    assert "roc_10" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_momentum(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_momentum(df, windows=(5, 10))
    assert "momentum_5" in res.columns
    assert "momentum_10" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_stochastic(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_stochastic(df, windows=(14,), smooth_window=3)
    assert "stoch_k_14_3" in res.columns
    assert "stoch_d_14_3" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_williams_r(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_williams_r(df, windows=(14, 21))
    assert "williams_r_14" in res.columns
    assert "williams_r_21" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_cci(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_cci(df, windows=(14, 20))
    assert "cci_14" in res.columns
    assert "cci_20" in res.columns
    assert len(res) == len(df)


def test_calculate_momentum_slope(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_momentum_slope(df, source_col="close", window=5)
    assert "slope_close_5" in res.columns
    assert len(res) == len(df)


def test_calculate_momentum_acceleration(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_momentum_acceleration(df, source_col="close", window=5)
    assert "accel_close_5" in res.columns
    assert len(res) == len(df)


def test_calculate_relative_momentum_rank(sample_ohlcv):
    df = sample_ohlcv.copy()
    features = calculate_multi_rsi(df, windows=(7, 14, 21))
    res = calculate_relative_momentum_rank(
        features, columns=["rsi_7", "rsi_14", "rsi_21"]
    )
    assert "rel_rank_rsi_7" in res.columns
    assert "rel_rank_rsi_21" in res.columns
    assert len(res) == len(df)
