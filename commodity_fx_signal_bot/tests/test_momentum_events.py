import pytest
import numpy as np
import pandas as pd

from indicators.momentum_events import (
    detect_rsi_zone_events,
    detect_rsi_crossback_events,
    detect_stochastic_cross_events,
    detect_roc_shift_events,
    detect_cci_zone_events,
    detect_momentum_slope_events,
    build_momentum_event_frame,
)


@pytest.fixture
def sample_features():
    dates = pd.date_range("2023-01-01", periods=10)
    df = pd.DataFrame(
        {
            "rsi_14": [50, 40, 25, 35, 60, 75, 65, 50, 20, 40],
            "stoch_k_14_3": [50, 40, 30, 20, 40, 60, 80, 90, 80, 60],
            "stoch_d_14_3": [50, 45, 40, 30, 25, 40, 60, 70, 85, 75],
            "roc_10": [0, -2, -5, 1, 3, 5, 2, -1, -3, 1],
            "cci_20": [0, -50, -150, -50, 0, 150, 50, 0, -120, -80],
            "slope_rsi_14_5": [0, -1, -2, 1, 2, 3, -1, -2, -3, 1],
        },
        index=dates,
    )
    return df


def test_detect_rsi_zone_events(sample_features):
    events = detect_rsi_zone_events(sample_features)
    assert "event_rsi_14_oversold" in events.columns
    assert "event_rsi_14_overbought" in events.columns
    assert events["event_rsi_14_oversold"].iloc[2] == 1
    assert events["event_rsi_14_oversold"].iloc[8] == 1
    assert events["event_rsi_14_overbought"].iloc[5] == 1


def test_detect_rsi_crossback_events(sample_features):
    events = detect_rsi_crossback_events(sample_features)
    assert "event_rsi_14_recovery_cross" in events.columns
    assert "event_rsi_14_bearish_crossback" in events.columns
    assert events["event_rsi_14_recovery_cross"].iloc[3] == 1
    assert events["event_rsi_14_bearish_crossback"].iloc[6] == 1


def test_detect_stochastic_cross_events(sample_features):
    events = detect_stochastic_cross_events(sample_features)
    assert "event_stoch_14_bullish_cross" in events.columns
    assert "event_stoch_14_bearish_cross" in events.columns
    assert events["event_stoch_14_bullish_cross"].iloc[4] == 1
    assert events["event_stoch_14_bearish_cross"].iloc[8] == 1


def test_detect_roc_shift_events(sample_features):
    events = detect_roc_shift_events(sample_features)
    assert "event_roc_10_positive_shift" in events.columns
    assert "event_roc_10_negative_shift" in events.columns
    assert events["event_roc_10_positive_shift"].iloc[3] == 1
    assert events["event_roc_10_negative_shift"].iloc[7] == 1


def test_detect_cci_zone_events(sample_features):
    events = detect_cci_zone_events(sample_features)
    assert "event_cci_20_oversold" in events.columns
    assert "event_cci_20_overbought" in events.columns
    assert events["event_cci_20_oversold"].iloc[2] == 1
    assert events["event_cci_20_overbought"].iloc[5] == 1


def test_detect_momentum_slope_events(sample_features):
    events = detect_momentum_slope_events(sample_features)
    assert "event_momentum_slope_positive_rsi_14_5" in events.columns
    assert "event_momentum_slope_negative_rsi_14_5" in events.columns
    assert events["event_momentum_slope_positive_rsi_14_5"].iloc[3] == 1
    assert events["event_momentum_slope_negative_rsi_14_5"].iloc[1] == 1


def test_build_momentum_event_frame(sample_features):
    event_df, summary = build_momentum_event_frame(sample_features)
    assert len(event_df) == len(sample_features)
    assert "input_rows" in summary
    assert "event_columns" in summary
    assert "total_event_count" in summary
    assert event_df.dtypes.iloc[0] in [np.int64, np.int32, int]
    for col in event_df.columns:
        assert "buy" not in col.lower()
        assert "sell" not in col.lower()
