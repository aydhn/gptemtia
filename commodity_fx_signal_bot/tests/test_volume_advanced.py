import pandas as pd
import numpy as np
import pytest
from indicators.volume_advanced import (
    detect_volume_usability,
    calculate_multi_volume_sma,
    calculate_multi_volume_zscore,
    calculate_relative_volume,
    calculate_obv_advanced,
    calculate_obv_slope,
    calculate_mfi_multi,
    calculate_cmf_multi,
    calculate_accumulation_distribution,
    calculate_chaikin_oscillator,
    calculate_price_volume_trend,
    calculate_volume_price_confirmation,
    calculate_dollar_volume_proxy,
    calculate_liquidity_proxy,
    calculate_volume_percentile,
)


@pytest.fixture
def sample_ohlcv():
    dates = pd.date_range("2020-01-01", periods=100)
    np.random.seed(42)
    return pd.DataFrame(
        {
            "open": np.random.uniform(100, 110, 100),
            "high": np.random.uniform(110, 120, 100),
            "low": np.random.uniform(90, 100, 100),
            "close": np.random.uniform(95, 115, 100),
            "volume": np.random.uniform(1000, 5000, 100),
        },
        index=dates,
    )


@pytest.fixture
def sample_ohlcv_unusable():
    dates = pd.date_range("2020-01-01", periods=100)
    np.random.seed(42)
    return pd.DataFrame(
        {
            "open": np.random.uniform(100, 110, 100),
            "high": np.random.uniform(110, 120, 100),
            "low": np.random.uniform(90, 100, 100),
            "close": np.random.uniform(95, 115, 100),
            "volume": np.zeros(100),
        },
        index=dates,
    )


def test_detect_volume_usability(sample_ohlcv):
    res = detect_volume_usability(sample_ohlcv)
    assert "volume_is_usable" in res.columns
    assert res["volume_is_usable"].iloc[-1] == True


def test_detect_volume_usability_unusable(sample_ohlcv_unusable):
    res = detect_volume_usability(sample_ohlcv_unusable)
    assert res["volume_is_usable"].iloc[-1] == False


def test_calculate_multi_volume_sma(sample_ohlcv):
    res = calculate_multi_volume_sma(sample_ohlcv, windows=(10, 20))
    assert "volume_sma_10" in res.columns
    assert "volume_sma_20" in res.columns


def test_calculate_multi_volume_zscore(sample_ohlcv):
    res = calculate_multi_volume_zscore(sample_ohlcv, windows=(20,))
    assert "volume_zscore_20" in res.columns


def test_calculate_relative_volume(sample_ohlcv):
    res = calculate_relative_volume(sample_ohlcv, windows=(20,))
    assert "relative_volume_20" in res.columns


def test_calculate_obv_advanced(sample_ohlcv):
    res = calculate_obv_advanced(sample_ohlcv)
    assert "obv" in res.columns


def test_calculate_obv_slope(sample_ohlcv):
    res = calculate_obv_slope(sample_ohlcv, window=10)
    assert "obv_slope_10" in res.columns


def test_calculate_mfi_multi(sample_ohlcv):
    res = calculate_mfi_multi(sample_ohlcv, windows=(14,))
    assert "mfi_14" in res.columns


def test_calculate_cmf_multi(sample_ohlcv):
    res = calculate_cmf_multi(sample_ohlcv, windows=(20,))
    assert "cmf_20" in res.columns


def test_calculate_accumulation_distribution(sample_ohlcv):
    res = calculate_accumulation_distribution(sample_ohlcv)
    assert "accumulation_distribution" in res.columns


def test_calculate_chaikin_oscillator(sample_ohlcv):
    res = calculate_chaikin_oscillator(sample_ohlcv)
    assert "chaikin_osc_3_10" in res.columns


def test_calculate_price_volume_trend(sample_ohlcv):
    res = calculate_price_volume_trend(sample_ohlcv)
    assert "pvt" in res.columns


def test_calculate_volume_price_confirmation(sample_ohlcv):
    res = calculate_volume_price_confirmation(sample_ohlcv, 10, 20)
    assert "price_volume_confirm_10_20" in res.columns


def test_calculate_dollar_volume_proxy(sample_ohlcv):
    res = calculate_dollar_volume_proxy(sample_ohlcv, windows=(20,))
    assert "dollar_volume_proxy" in res.columns


def test_calculate_liquidity_proxy(sample_ohlcv):
    res = calculate_liquidity_proxy(sample_ohlcv, windows=(20,))
    assert "liquidity_proxy_20" in res.columns


def test_calculate_volume_percentile(sample_ohlcv):
    res = calculate_volume_percentile(sample_ohlcv, window=120)
    assert "volume_percentile_120" in res.columns
