import numpy as np
import pandas as pd
import pytest

from indicators.mean_reversion_events import (
    MeanReversionEventConfig,
    build_mean_reversion_event_frame,
    detect_band_extension_events,
    detect_band_reentry_events,
    detect_distance_overextension_events,
    detect_minmax_position_events,
    detect_percentile_extreme_events,
    detect_snapback_pressure_events,
    detect_zscore_extreme_events,
    detect_zscore_snapback_events,
)


@pytest.fixture
def sample_features():
    dates = pd.date_range("2023-01-01", periods=10)
    df = pd.DataFrame(
        {
            "zscore_close_20": [0, 1, 2.5, 3.5, 1.5, -2.5, -3.5, -1.5, 0, 0],
            "percentile_close_120": [
                0.5,
                0.6,
                0.95,
                0.95,
                0.5,
                0.05,
                0.05,
                0.5,
                0.5,
                0.5,
            ],
            "minmax_pos_50": [0.5, 0.6, 0.95, 0.95, 0.5, 0.05, 0.05, 0.5, 0.5, 0.5],
            "bb_lower_extension_20_2": [0, 0, 0, 0, 0, 0.01, 0.02, 0, 0, 0],
            "bb_upper_extension_20_2": [0, 0, 0.01, 0.02, 0, 0, 0, 0, 0, 0],
            "bb_percent_b_20_2": [0.5, 0.8, 1.1, 1.2, 0.9, -0.1, -0.2, 0.1, 0.5, 0.5],
            "dist_sma_20": [0, 0.01, 0.06, 0.08, 0.02, -0.06, -0.08, -0.02, 0, 0],
            "snapback_pressure_zscore_close_20": [
                0,
                0,
                -0.5,
                -0.5,
                1.0,
                -0.5,
                -0.5,
                1.0,
                0,
                0,
            ],
        },
        index=dates,
    )
    return df


def test_detect_zscore_extreme_events(sample_features):
    events = detect_zscore_extreme_events(sample_features)
    assert "event_zscore_20_low_extreme" in events.columns
    assert "event_zscore_20_high_extreme" in events.columns
    assert events["event_zscore_20_high_extreme"].iloc[2] == 1
    assert events["event_zscore_20_major_high_extreme"].iloc[3] == 1
    assert events["event_zscore_20_low_extreme"].iloc[5] == 1
    assert events["event_zscore_20_major_low_extreme"].iloc[6] == 1


def test_detect_zscore_snapback_events(sample_features):
    events = detect_zscore_snapback_events(sample_features)
    assert "event_zscore_20_low_snapback_candidate" in events.columns
    assert "event_zscore_20_high_snapback_candidate" in events.columns
    assert events["event_zscore_20_high_snapback_candidate"].iloc[4] == 1
    assert events["event_zscore_20_low_snapback_candidate"].iloc[7] == 1


def test_detect_percentile_extreme_events(sample_features):
    events = detect_percentile_extreme_events(sample_features)
    assert "event_percentile_120_low_extreme" in events.columns
    assert "event_percentile_120_high_extreme" in events.columns
    assert events["event_percentile_120_high_extreme"].iloc[2] == 1
    assert events["event_percentile_120_low_extreme"].iloc[5] == 1


def test_detect_minmax_position_events(sample_features):
    events = detect_minmax_position_events(sample_features)
    assert "event_minmax_50_low_zone" in events.columns
    assert "event_minmax_50_high_zone" in events.columns
    assert events["event_minmax_50_high_zone"].iloc[2] == 1
    assert events["event_minmax_50_low_zone"].iloc[5] == 1


def test_detect_band_extension_events(sample_features):
    events = detect_band_extension_events(sample_features)
    assert "event_bb20_lower_extension" in events.columns
    assert "event_bb20_upper_extension" in events.columns
    assert events["event_bb20_upper_extension"].iloc[2] == 1
    assert events["event_bb20_lower_extension"].iloc[5] == 1


def test_detect_band_reentry_events(sample_features):
    events = detect_band_reentry_events(sample_features)
    assert "event_bb20_lower_reentry_candidate" in events.columns
    assert "event_bb20_upper_reentry_candidate" in events.columns
    assert events["event_bb20_upper_reentry_candidate"].iloc[4] == 1
    assert events["event_bb20_lower_reentry_candidate"].iloc[7] == 1


def test_detect_distance_overextension_events(sample_features):
    events = detect_distance_overextension_events(sample_features)
    assert "event_dist_sma_20_negative_overextension" in events.columns
    assert "event_dist_sma_20_positive_overextension" in events.columns
    assert events["event_dist_sma_20_positive_overextension"].iloc[2] == 1
    assert events["event_dist_sma_20_negative_overextension"].iloc[5] == 1


def test_detect_snapback_pressure_events(sample_features):
    events = detect_snapback_pressure_events(sample_features)
    assert "event_snapback_pressure_positive_20" in events.columns
    assert "event_snapback_pressure_negative_20" in events.columns
    assert events["event_snapback_pressure_positive_20"].iloc[4] == 1


def test_build_mean_reversion_event_frame(sample_features):
    event_df, summary = build_mean_reversion_event_frame(sample_features)
    assert len(event_df) == len(sample_features)
    assert "input_rows" in summary
    assert "event_columns" in summary
    assert "total_event_count" in summary
    assert event_df.dtypes.iloc[0] in [np.int64, np.int32, int]
    for col in event_df.columns:
        assert "buy" not in col.lower()
        assert "sell" not in col.lower()
