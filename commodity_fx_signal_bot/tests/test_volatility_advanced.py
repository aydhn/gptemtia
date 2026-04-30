import numpy as np
import pandas as pd
import pytest

from indicators.volatility_advanced import (
    calculate_multi_true_range,
    calculate_multi_atr,
    calculate_atr_percent,
    calculate_multi_bollinger_bands,
    calculate_multi_keltner_channels,
    calculate_multi_donchian_channels,
    calculate_historical_volatility_multi,
    calculate_parkinson_volatility,
    calculate_garman_klass_volatility,
    calculate_range_percent,
    calculate_gap_volatility,
    calculate_volatility_percentile,
    calculate_volatility_slope,
    calculate_channel_position,
)


@pytest.fixture
def sample_ohlcv():
    dates = pd.date_range("2023-01-01", periods=150, freq="D")
    df = pd.DataFrame(
        {
            "open": np.random.uniform(100, 200, 150),
            "high": np.random.uniform(150, 250, 150),
            "low": np.random.uniform(50, 150, 150),
            "close": np.random.uniform(100, 200, 150),
            "volume": np.random.uniform(1000, 5000, 150),
        },
        index=dates,
    )
    df["high"] = df[["open", "close", "high"]].max(axis=1)
    df["low"] = df[["open", "close", "low"]].min(axis=1)
    return df


def test_calculate_multi_true_range(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_true_range(df)
    assert "true_range" in res.columns
    assert len(res) == len(df)
    assert df.equals(sample_ohlcv)  # Does not mutate


def test_calculate_multi_atr(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_atr(df, windows=(7, 14))
    assert "atr_7" in res.columns
    assert "atr_14" in res.columns
    assert len(res) == len(df)


def test_calculate_atr_percent(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_atr_percent(df, windows=(14,))
    assert "atr_pct_14" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_bollinger_bands(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_bollinger_bands(df, windows=(20,), num_std=2.0)
    assert "bb_upper_20_2" in res.columns
    assert "bb_lower_20_2" in res.columns
    assert "bb_width_20_2" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_keltner_channels(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_keltner_channels(df, windows=(20,))
    assert "keltner_upper_20" in res.columns
    assert "keltner_width_20" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_donchian_channels(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_donchian_channels(df, windows=(20,))
    assert "donchian_high_20" in res.columns
    assert "donchian_width_20" in res.columns
    assert len(res) == len(df)


def test_calculate_historical_volatility_multi(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_historical_volatility_multi(df, windows=(20,))
    assert "hist_vol_20" in res.columns
    assert len(res) == len(df)


def test_calculate_parkinson_volatility(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_parkinson_volatility(df, window=20)
    assert "parkinson_vol_20" in res.columns
    assert len(res) == len(df)


def test_calculate_garman_klass_volatility(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_garman_klass_volatility(df, window=20)
    assert "garman_klass_vol_20" in res.columns
    assert len(res) == len(df)


def test_calculate_range_percent(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_range_percent(df)
    assert "range_pct" in res.columns
    assert len(res) == len(df)


def test_calculate_gap_volatility(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_gap_volatility(df)
    assert "gap_pct" in res.columns
    assert "abs_gap_pct" in res.columns
    assert len(res) == len(df)


def test_calculate_volatility_percentile(sample_ohlcv):
    df = sample_ohlcv.copy()
    df["dummy_vol"] = np.random.uniform(0.01, 0.05, len(df))
    res = calculate_volatility_percentile(df, source_col="dummy_vol", window=120)
    assert "percentile_dummy_vol_120" in res.columns
    assert len(res) == len(df)


def test_calculate_volatility_slope(sample_ohlcv):
    df = sample_ohlcv.copy()
    df["dummy_vol"] = np.linspace(0.01, 0.05, len(df))
    res = calculate_volatility_slope(df, source_col="dummy_vol", window=5)
    assert "slope_dummy_vol_5" in res.columns
    assert len(res) == len(df)


def test_calculate_channel_position(sample_ohlcv):
    df = sample_ohlcv.copy()
    df["upper"] = df["close"] + 5
    df["lower"] = df["close"] - 5
    res = calculate_channel_position(df, "upper", "lower", "test")
    assert "channel_pos_test" in res.columns
    assert len(res) == len(df)
