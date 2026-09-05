"""Tests for Release Event Features."""

import pandas as pd
from advanced_feature_fusion.release_event_features import (
    build_release_event_feature_registry,
    summarize_release_event_features,
    add_release_delay_placeholder,
    add_release_has_actual_flag,
    add_release_revised_previous_flag,
)


def test_release_features_registry():
    df, summary = build_release_event_feature_registry()
    assert len(df) == 3
    assert summary["total_features"] == 3
    assert summary["non_signal_guaranteed"] is True


def test_release_event_calculations():
    df = pd.DataFrame({
        "scheduled_time": pd.to_datetime(["2025-01-01 10:00:00", "2025-01-01 12:00:00"], utc=True),
        "actual_release_time": pd.to_datetime(["2025-01-01 10:05:00", "2025-01-01 12:00:00"], utc=True),
        "actual": [10.0, None],
        "revised_previous": [5.0, None],
    })

    delayed = add_release_delay_placeholder(df)
    assert "release_delay_placeholder" in delayed.columns
    assert delayed["release_delay_placeholder"].iloc[0] == 5.0
    assert delayed["release_delay_placeholder"].iloc[1] == 0.0

    actual_flagged = add_release_has_actual_flag(df, actual_field="actual")
    assert "release_has_actual_flag" in actual_flagged.columns
    assert bool(actual_flagged["release_has_actual_flag"].iloc[0]) is True
    assert bool(actual_flagged["release_has_actual_flag"].iloc[1]) is False

    revised_flagged = add_release_revised_previous_flag(df, revised_field="revised_previous")
    assert "release_revised_previous_flag" in revised_flagged.columns
    assert bool(revised_flagged["release_revised_previous_flag"].iloc[0]) is True
    assert bool(revised_flagged["release_revised_previous_flag"].iloc[1]) is False
