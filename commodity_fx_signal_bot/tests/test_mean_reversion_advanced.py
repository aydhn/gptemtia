import pytest
import numpy as np
import pandas as pd

from indicators.mean_reversion_advanced import (
    calculate_multi_zscore_close,
    calculate_multi_rolling_mean_distance,
    calculate_multi_sma_distance,
    calculate_multi_ema_distance,
    calculate_rolling_percentile_rank,
    calculate_multi_percentile_rank,
    calculate_rolling_minmax_position,
    calculate_bollinger_reversion_features,
    calculate_channel_deviation_features,
    calculate_overextension_score,
    calculate_snapback_pressure,
    calculate_reversion_half_life_proxy,
    calculate_range_position_features,
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


def test_calculate_multi_zscore_close(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_zscore_close(df, windows=(20, 50))
    assert "zscore_close_20" in res.columns
    assert "zscore_close_50" in res.columns
    assert len(res) == len(df)
    assert df.equals(sample_ohlcv)  # Should not mutate input


def test_calculate_multi_rolling_mean_distance(sample_ohlcv):
    res = calculate_multi_rolling_mean_distance(sample_ohlcv, windows=(20, 50))
    assert "rolling_mean_dist_20" in res.columns
    assert "rolling_mean_dist_50" in res.columns
    assert len(res) == len(sample_ohlcv)


def test_calculate_multi_sma_distance(sample_ohlcv):
    res = calculate_multi_sma_distance(sample_ohlcv, windows=(20, 50))
    assert "dist_sma_20" in res.columns
    assert "dist_sma_50" in res.columns
    assert len(res) == len(sample_ohlcv)


def test_calculate_multi_ema_distance(sample_ohlcv):
    res = calculate_multi_ema_distance(sample_ohlcv, windows=(20, 50))
    assert "dist_ema_20" in res.columns
    assert "dist_ema_50" in res.columns
    assert len(res) == len(sample_ohlcv)


def test_calculate_rolling_percentile_rank(sample_ohlcv):
    res = calculate_rolling_percentile_rank(sample_ohlcv, window=60)
    assert "percentile_close_60" in res.columns
    assert len(res) == len(sample_ohlcv)


def test_calculate_multi_percentile_rank(sample_ohlcv):
    res = calculate_multi_percentile_rank(sample_ohlcv, windows=(60, 120))
    assert "percentile_close_60" in res.columns
    assert "percentile_close_120" in res.columns
    assert len(res) == len(sample_ohlcv)


def test_calculate_rolling_minmax_position(sample_ohlcv):
    res = calculate_rolling_minmax_position(sample_ohlcv, windows=(20, 50))
    assert "minmax_pos_20" in res.columns
    assert "minmax_pos_50" in res.columns
    assert len(res) == len(sample_ohlcv)


def test_calculate_bollinger_reversion_features(sample_ohlcv):
    res = calculate_bollinger_reversion_features(
        sample_ohlcv, windows=(20,), num_std=2.0
    )
    assert "bb_reversion_z_20_2" in res.columns
    assert "bb_percent_b_20_2" in res.columns
    assert "bb_lower_extension_20_2" in res.columns
    assert "bb_upper_extension_20_2" in res.columns
    assert "bb_reentry_pressure_20_2" in res.columns
    assert len(res) == len(sample_ohlcv)


def test_calculate_channel_deviation_features(sample_ohlcv):
    res = calculate_channel_deviation_features(sample_ohlcv, windows=(20,))
    assert "channel_dev_20" in res.columns
    assert len(res) == len(sample_ohlcv)


def test_calculate_overextension_score(sample_ohlcv):
    res = calculate_overextension_score(sample_ohlcv, window=20)
    assert "overextension_score_20" in res.columns
    assert len(res) == len(sample_ohlcv)


def test_calculate_snapback_pressure(sample_ohlcv):
    res = calculate_snapback_pressure(sample_ohlcv, zscore_col="zscore_close_20")
    assert "snapback_pressure_zscore_close_20" in res.columns
    assert len(res) == len(sample_ohlcv)


def test_calculate_reversion_half_life_proxy(sample_ohlcv):
    res = calculate_reversion_half_life_proxy(sample_ohlcv, window=50)
    assert "half_life_proxy_50" in res.columns
    assert len(res) == len(sample_ohlcv)


def test_calculate_range_position_features(sample_ohlcv):
    res = calculate_range_position_features(sample_ohlcv, windows=(20,))
    assert "range_pos_20" in res.columns
    assert len(res) == len(sample_ohlcv)
