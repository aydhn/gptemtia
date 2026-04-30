import numpy as np
import pandas as pd
import pytest

from indicators.trend_events import (
    TrendEventConfig,
    build_trend_event_frame,
    detect_adx_strength_events,
    detect_aroon_trend_events,
    detect_dmi_direction_events,
    detect_ma_cross_events,
    detect_ma_stack_events,
    detect_macd_trend_events,
    detect_price_ma_position_events,
)


@pytest.fixture
def sample_features():
    dates = pd.date_range("2023-01-01", periods=100, freq="D")
    df = pd.DataFrame(index=dates)
    df["close"] = np.random.uniform(100, 200, 100)
    df["ema_20"] = np.random.uniform(100, 200, 100)
    df["ema_50"] = np.random.uniform(100, 200, 100)
    df["ema_200"] = np.random.uniform(100, 200, 100)
    df["sma_200"] = np.random.uniform(100, 200, 100)

    df["macd_12_26_9"] = np.random.uniform(-5, 5, 100)
    df["macd_signal_12_26_9"] = np.random.uniform(-5, 5, 100)
    df["macd_hist_12_26_9"] = np.random.uniform(-2, 2, 100)

    df["adx_14"] = np.random.uniform(10, 50, 100)
    df["plus_di_14"] = np.random.uniform(10, 50, 100)
    df["minus_di_14"] = np.random.uniform(10, 50, 100)

    df["aroon_up_25"] = np.random.uniform(0, 100, 100)
    df["aroon_down_25"] = np.random.uniform(0, 100, 100)

    df["slope_ema_20"] = np.random.uniform(-0.1, 0.1, 100)

    return df


def test_detect_price_ma_position_events(sample_features):
    config = TrendEventConfig()
    res = detect_price_ma_position_events(sample_features, config)
    assert "event_price_above_ema_20" in res.columns
    assert "event_price_below_ema_20" in res.columns
    assert set(res["event_price_above_ema_20"].unique()).issubset({0, 1})
    assert len(res) == len(sample_features)


def test_detect_ma_cross_events(sample_features):
    config = TrendEventConfig()
    res = detect_ma_cross_events(sample_features, config)
    assert "event_ema_20_cross_above_ema_50" in res.columns
    assert set(res["event_ema_20_cross_above_ema_50"].unique()).issubset({0, 1})
    assert len(res) == len(sample_features)


def test_detect_ma_stack_events(sample_features):
    config = TrendEventConfig()
    res = detect_ma_stack_events(sample_features, config)
    assert "event_ma_stack_bullish" in res.columns
    assert set(res["event_ma_stack_bullish"].unique()).issubset({0, 1})
    assert len(res) == len(sample_features)


def test_detect_macd_trend_events(sample_features):
    config = TrendEventConfig()
    res = detect_macd_trend_events(sample_features, config)
    assert "event_macd_hist_positive_shift" in res.columns
    assert "event_macd_line_above_signal" in res.columns
    assert set(res["event_macd_hist_positive_shift"].unique()).issubset({0, 1})
    assert len(res) == len(sample_features)


def test_detect_adx_strength_events(sample_features):
    config = TrendEventConfig()
    res = detect_adx_strength_events(sample_features, config)
    assert "event_adx_14_trend_strength" in res.columns
    assert "event_adx_14_rising" in res.columns
    assert set(res["event_adx_14_trend_strength"].unique()).issubset({0, 1})
    assert len(res) == len(sample_features)


def test_detect_dmi_direction_events(sample_features):
    config = TrendEventConfig()
    res = detect_dmi_direction_events(sample_features, config)
    assert "event_dmi_bullish_direction_14" in res.columns
    assert set(res["event_dmi_bullish_direction_14"].unique()).issubset({0, 1})
    assert len(res) == len(sample_features)


def test_detect_aroon_trend_events(sample_features):
    config = TrendEventConfig()
    res = detect_aroon_trend_events(sample_features, config)
    assert "event_aroon_bullish_25" in res.columns
    assert set(res["event_aroon_bullish_25"].unique()).issubset({0, 1})
    assert len(res) == len(sample_features)


def test_build_trend_event_frame(sample_features):
    config = TrendEventConfig()
    res, summary = build_trend_event_frame(sample_features, config)

    # Check it returned a dataframe
    assert isinstance(res, pd.DataFrame)

    # Check it contains expected event columns
    assert "event_price_above_ema_20" in res.columns
    assert "event_ma_stack_bullish" in res.columns

    # Check values are 0/1
    assert set(res["event_ma_stack_bullish"].unique()).issubset({0, 1})

    # Check summary contains expected keys
    assert "input_rows" in summary
    assert "event_columns" in summary
    assert "total_event_count" in summary
    assert "active_last_row_events" in summary

    # Verify no buy/sell terms
    for col in summary["event_columns"]:
        assert "buy" not in col.lower()
        assert "sell" not in col.lower()
