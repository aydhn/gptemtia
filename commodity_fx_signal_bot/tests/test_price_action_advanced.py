import numpy as np
import pandas as pd
import pytest

from indicators.price_action_advanced import (
    calculate_body_features,
    calculate_breakout_distance,
    calculate_breakout_levels,
    calculate_candle_anatomy,
    calculate_candle_percentiles,
    calculate_candle_ratios,
    calculate_close_location_features,
    calculate_consecutive_candle_features,
    calculate_false_breakout_features,
    calculate_gap_features,
    calculate_inside_outside_bars,
    calculate_price_action_context,
    calculate_range_compression_expansion,
    calculate_range_features,
    calculate_wick_features,
)


@pytest.fixture
def sample_df():
    data = {
        "open": [100, 105, 110, 108, 102],
        "high": [110, 115, 112, 109, 105],
        "low": [90, 100, 105, 100, 95],
        "close": [105, 110, 108, 102, 100],
        "volume": [1000, 1500, 1200, 800, 900],
    }
    # Add a lot of rows to test rolling features
    for _ in range(50):
        data["open"].append(100)
        data["high"].append(110)
        data["low"].append(90)
        data["close"].append(105)
        data["volume"].append(1000)

    df = pd.DataFrame(data)
    df.index = pd.date_range(start="2023-01-01", periods=len(df), freq="D")
    return df


def test_calculate_candle_anatomy(sample_df):
    res = calculate_candle_anatomy(sample_df)
    assert "candle_body" in res.columns
    assert "candle_range" in res.columns
    assert "upper_wick" in res.columns
    assert "lower_wick" in res.columns


def test_calculate_candle_ratios(sample_df):
    res = calculate_candle_ratios(sample_df)
    assert "body_to_range_ratio" in res.columns
    assert "upper_wick_to_range_ratio" in res.columns
    assert "lower_wick_to_range_ratio" in res.columns


def test_calculate_close_location_features(sample_df):
    res = calculate_close_location_features(sample_df)
    assert "close_pos_range" in res.columns
    assert "open_pos_range" in res.columns
    assert "close_above_open" in res.columns
    assert "close_below_open" in res.columns


def test_calculate_range_features(sample_df):
    res = calculate_range_features(sample_df, windows=(5, 10))
    assert "range_sma_5" in res.columns
    assert "range_sma_10" in res.columns


def test_calculate_body_features(sample_df):
    res = calculate_body_features(sample_df, windows=(5, 10))
    assert "body_sma_5" in res.columns
    assert "body_sma_10" in res.columns


def test_calculate_wick_features(sample_df):
    res = calculate_wick_features(sample_df)
    assert "wick_imbalance" in res.columns


def test_calculate_gap_features(sample_df):
    res = calculate_gap_features(sample_df)
    assert "gap_pct" in res.columns
    assert "abs_gap_pct" in res.columns
    assert "gap_direction" in res.columns


def test_calculate_inside_outside_bars(sample_df):
    res = calculate_inside_outside_bars(sample_df)
    assert "inside_bar" in res.columns
    assert "outside_bar" in res.columns


def test_calculate_breakout_levels(sample_df):
    res = calculate_breakout_levels(sample_df, windows=(10,))
    assert "breakout_high_10" in res.columns
    assert "breakout_low_10" in res.columns


def test_calculate_breakout_distance(sample_df):
    res = calculate_breakout_distance(sample_df, windows=(10,))
    assert "dist_to_breakout_high_10" in res.columns
    assert "dist_to_breakout_low_10" in res.columns


def test_calculate_false_breakout_features(sample_df):
    res = calculate_false_breakout_features(sample_df, windows=(10,))
    assert "false_breakout_upper_10" in res.columns
    assert "false_breakout_lower_10" in res.columns


def test_calculate_range_compression_expansion(sample_df):
    res = calculate_range_compression_expansion(sample_df, window=10)
    assert "range_compression_10" in res.columns
    assert "range_expansion_10" in res.columns


def test_calculate_candle_percentiles(sample_df):
    res = calculate_candle_percentiles(sample_df, percentile_window=20)
    assert "candle_range_percentile_20" in res.columns
    assert "candle_body_percentile_20" in res.columns


def test_calculate_consecutive_candle_features(sample_df):
    res = calculate_consecutive_candle_features(sample_df)
    assert "consecutive_up_closes" in res.columns
    assert "consecutive_down_closes" in res.columns
    assert "consecutive_higher_highs" in res.columns
    assert "consecutive_lower_lows" in res.columns


def test_calculate_price_action_context(sample_df):
    res = calculate_price_action_context(sample_df, windows=(10,))
    assert "pa_context_range_position_10" in res.columns


def test_input_dataframe_not_mutated(sample_df):
    original_cols = list(sample_df.columns)
    calculate_candle_anatomy(sample_df)
    assert list(sample_df.columns) == original_cols
