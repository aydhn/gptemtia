"""Tests for Calendar Event Window Features."""

import pandas as pd
from advanced_feature_fusion.calendar_event_window_features import (
    build_calendar_event_window_feature_registry,
    summarize_calendar_event_window_features,
    add_pre_event_window_placeholder,
    add_post_event_window_placeholder,
)


def test_window_features_registry():
    df, summary = build_calendar_event_window_feature_registry()
    assert len(df) == 2
    assert summary["total_features"] == 2
    assert summary["non_signal_guaranteed"] is True


def test_pre_post_event_placeholders():
    df = pd.DataFrame({
        "timestamp": pd.to_datetime(["2025-01-01 10:00:00", "2025-01-01 14:00:00"], utc=True),
        "scheduled_time": pd.to_datetime(["2025-01-01 12:00:00", "2025-01-01 12:00:00"], utc=True),
        "actual_release_time": pd.to_datetime(["2025-01-01 12:00:00", "2025-01-01 12:00:00"], utc=True),
    })

    pre_df = add_pre_event_window_placeholder(df, window_hours=4)
    assert "is_pre_event_4h" in pre_df.columns
    assert bool(pre_df["is_pre_event_4h"].iloc[0]) is True
    assert bool(pre_df["is_pre_event_4h"].iloc[1]) is False

    post_df = add_post_event_window_placeholder(df, window_hours=4)
    assert "is_post_event_4h" in post_df.columns
    assert bool(post_df["is_post_event_4h"].iloc[0]) is False
    assert bool(post_df["is_post_event_4h"].iloc[1]) is True
