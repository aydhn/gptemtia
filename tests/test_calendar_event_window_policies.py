"""Tests for Calendar Event Window Policies."""

import pandas as pd
from advanced_feature_fusion.calendar_event_window_policies import (
    build_calendar_event_window_policy_registry,
    get_calendar_event_window_policies,
    build_event_window_flags,
)


def test_calendar_event_window_policies():
    df, summary = build_calendar_event_window_policy_registry()
    assert len(df) == 3
    assert summary["total_policies"] == 3
    assert summary["non_signal_guaranteed"] is True


def test_build_event_window_flags():
    times = pd.date_range("2025-01-01 10:00:00", periods=5, freq="h", tz="UTC")
    df = pd.DataFrame({
        "timestamp": times,
        "scheduled_time": [pd.Timestamp("2025-01-01 12:00:00", tz="UTC")] * 5,
    })
    flagged = build_event_window_flags(df, pre_windows=[1, 4], post_windows=[1, 4])
    assert "is_pre_event_1h" in flagged.columns
    assert "is_pre_event_4h" in flagged.columns
    assert "is_post_event_1h" in flagged.columns
    assert "is_post_event_4h" in flagged.columns
    # Check that input df was not mutated
    assert "is_pre_event_1h" not in df.columns
