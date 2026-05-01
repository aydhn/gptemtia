import numpy as np
import pandas as pd
import pytest

from config.settings import settings
from indicators.price_action_events import (
    PriceActionEventConfig,
    build_price_action_event_frame,
    detect_breakout_setup_events,
    detect_candle_body_events,
    detect_close_location_events,
    detect_consecutive_candle_events,
    detect_false_breakout_events,
    detect_gap_events,
    detect_inside_outside_bar_events,
    detect_range_expansion_compression_events,
    detect_wick_rejection_events,
)


@pytest.fixture
def sample_features():
    window = settings.default_large_body_percentile_window
    data = {
        f"candle_body_percentile_{window}": [0.95, 0.5, 0.05],
        f"candle_range_percentile_{window}": [0.95, 0.5, 0.05],
        "upper_wick_to_range_ratio": [0.7, 0.2, 0.1],
        "lower_wick_to_range_ratio": [0.1, 0.2, 0.7],
        "close_pos_range": [0.9, 0.5, 0.1],
        "range_compression_20": [0, 0, 1],
        "range_expansion_20": [1, 0, 0],
        "inside_bar": [0, 1, 0],
        "outside_bar": [1, 0, 0],
        "gap_pct": [0.02, 0.0, -0.02],
        "abs_gap_pct": [0.02, 0.0, 0.02],
        "dist_to_breakout_high_20": [0.001, 0.05, -0.01],  # near, far, broken
        "dist_to_breakout_low_20": [0.05, 0.001, -0.01],
        "false_breakout_upper_20": [1, 0, 0],
        "false_breakout_lower_20": [0, 0, 1],
        "consecutive_up_closes": [3, 0, 0],
        "consecutive_down_closes": [0, 0, 3],
        "consecutive_higher_highs": [3, 0, 0],
        "consecutive_lower_lows": [0, 0, 3],
    }
    df = pd.DataFrame(data)
    df.index = pd.date_range(start="2023-01-01", periods=len(df), freq="D")
    return df


def test_detect_candle_body_events(sample_features):
    events = detect_candle_body_events(sample_features)
    assert "event_large_body_candle" in events.columns
    assert "event_small_body_candle" in events.columns
    assert "event_large_range_candle" in events.columns


def test_detect_wick_rejection_events(sample_features):
    events = detect_wick_rejection_events(sample_features)
    assert "event_upper_wick_rejection_candidate" in events.columns
    assert "event_lower_wick_rejection_candidate" in events.columns


def test_detect_close_location_events(sample_features):
    events = detect_close_location_events(sample_features)
    assert "event_strong_close_upper" in events.columns
    assert "event_strong_close_lower" in events.columns


def test_detect_range_expansion_compression_events(sample_features):
    events = detect_range_expansion_compression_events(sample_features)
    assert "event_small_range_compression_20" in events.columns
    assert "event_range_expansion_20" in events.columns


def test_detect_inside_outside_bar_events(sample_features):
    events = detect_inside_outside_bar_events(sample_features)
    assert "event_inside_bar_compression" in events.columns
    assert "event_outside_bar_expansion" in events.columns


def test_detect_gap_events(sample_features):
    events = detect_gap_events(sample_features)
    assert "event_gap_up" in events.columns
    assert "event_gap_down" in events.columns
    assert "event_large_gap" in events.columns


def test_detect_breakout_setup_events(sample_features):
    events = detect_breakout_setup_events(sample_features)
    assert "event_near_breakout_high_20" in events.columns
    assert "event_breakout_high_20_candidate" in events.columns


def test_detect_false_breakout_events(sample_features):
    events = detect_false_breakout_events(sample_features)
    assert "event_false_breakout_upper_20_candidate" in events.columns
    assert "event_false_breakout_lower_20_candidate" in events.columns


def test_detect_consecutive_candle_events(sample_features):
    events = detect_consecutive_candle_events(sample_features)
    assert "event_consecutive_up_closes" in events.columns
    assert "event_consecutive_down_closes" in events.columns


def test_build_price_action_event_frame(sample_features):
    event_df, summary = build_price_action_event_frame(sample_features)
    assert not event_df.empty
    assert "event_columns" in summary

    # Check values are 0 or 1
    for col in event_df.columns:
        assert set(event_df[col].unique()).issubset({0, 1})

    # Check no 'buy' or 'sell' signal naming
    for col in event_df.columns:
        assert "buy" not in col.lower()
        assert "sell" not in col.lower()
        assert "signal" not in col.lower()
