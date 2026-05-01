import numpy as np
import pandas as pd
import pytest

from indicators.trend_advanced import (
    calculate_dmi_adx,
    calculate_hma,
    calculate_ichimoku_full,
    calculate_ma_slopes,
    calculate_ma_stack_state,
    calculate_multi_adx,
    calculate_multi_aroon,
    calculate_multi_ema,
    calculate_multi_hma,
    calculate_multi_macd,
    calculate_multi_sma,
    calculate_multi_wma,
    calculate_price_ma_distances,
    calculate_trend_persistence,
    calculate_wma,
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


def test_calculate_multi_sma(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_sma(df, windows=(10, 20))
    assert "sma_10" in res.columns
    assert "sma_20" in res.columns
    assert len(res) == len(df)
    assert df.equals(sample_ohlcv)  # Does not mutate


def test_calculate_multi_ema(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_ema(df, windows=(10, 20))
    assert "ema_10" in res.columns
    assert "ema_20" in res.columns
    assert len(res) == len(df)


def test_calculate_wma(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_wma(df, window=20)
    assert "wma_20" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_wma(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_wma(df, windows=(20, 50))
    assert "wma_20" in res.columns
    assert "wma_50" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_hma(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_hma(df, windows=(20, 50))
    assert "hma_20" in res.columns
    assert "hma_50" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_macd(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_macd(df, configs=((12, 26, 9),))
    assert "macd_12_26_9" in res.columns
    assert "macd_signal_12_26_9" in res.columns
    assert "macd_hist_12_26_9" in res.columns
    assert len(res) == len(df)


def test_calculate_dmi_adx(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_dmi_adx(df, window=14)
    assert "adx_14" in res.columns
    assert "plus_di_14" in res.columns
    assert "minus_di_14" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_adx(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_adx(df, windows=(14, 21))
    assert "adx_14" in res.columns
    assert "adx_21" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_aroon(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_aroon(df, windows=(14, 25))
    assert "aroon_up_14" in res.columns
    assert "aroon_down_25" in res.columns
    assert len(res) == len(df)


def test_calculate_ichimoku_full(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_ichimoku_full(df)
    assert "ichimoku_tenkan" in res.columns
    assert "ichimoku_chikou" in res.columns
    assert len(res) == len(df)


def test_calculate_price_ma_distances(sample_ohlcv):
    df = sample_ohlcv.copy()
    df["sma_20"] = df["close"].rolling(20).mean()
    res = calculate_price_ma_distances(df, ["sma_20"])
    assert "dist_close_sma_20" in res.columns
    assert len(res) == len(df)


def test_calculate_ma_slopes(sample_ohlcv):
    df = sample_ohlcv.copy()
    df["sma_20"] = df["close"].rolling(20).mean()
    res = calculate_ma_slopes(df, ["sma_20"], slope_window=5)
    assert "slope_sma_20_5" in res.columns
    assert len(res) == len(df)


def test_calculate_ma_stack_state(sample_ohlcv):
    df = sample_ohlcv.copy()
    df["ema_20"] = df["close"].rolling(20).mean()
    df["ema_50"] = df["close"].rolling(50).mean()
    df["ema_200"] = df["close"].rolling(200).mean()
    res = calculate_ma_stack_state(df, "ema_20", "ema_50", "ema_200")
    assert "ma_stack_bullish_20_50_200" in res.columns
    assert "ma_stack_bearish_20_50_200" in res.columns
    assert len(res) == len(df)


def test_calculate_trend_persistence(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_trend_persistence(df["close"], window=10)
    assert res.name == "trend_persistence_close_10"
    assert len(res) == len(df)
