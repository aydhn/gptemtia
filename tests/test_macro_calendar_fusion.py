"""Tests for Macro-Calendar Cross Fusion."""

import pandas as pd
from advanced_feature_fusion.macro_calendar_fusion import (
    fuse_macro_with_calendar,
    get_macro_calendar_fusion_summary,
)


def test_summary():
    summary = get_macro_calendar_fusion_summary()
    assert summary["join_direction"] == "backward"
    assert summary["no_lookahead_guaranteed"] is True


def test_fuse_macro_with_calendar():
    times = pd.date_range("2025-01-01 10:00:00", periods=5, freq="1h", tz="UTC")
    macro_df = pd.DataFrame({
        "timestamp": times,
        "indicator_id": ["CPI"] * 5,
        "macro_value": [3.1, 3.1, 3.1, 3.2, 3.2],
    })

    cal_df = pd.DataFrame({
        "event_macro_indicator_id": ["CPI"] * 2,
        "release_timestamp": [times[0], times[3]],
        "actual_value": [3.1, 3.2],
    })

    fused = fuse_macro_with_calendar(
        macro_df=macro_df,
        calendar_df=cal_df,
        macro_timestamp_col="timestamp",
        calendar_release_col="release_timestamp",
        by="indicator_id",
        calendar_by="event_macro_indicator_id",
    )
    assert len(fused) == len(macro_df)
    assert "actual_value" in fused.columns
    # Backward only
    valid = fused.dropna(subset=["release_timestamp"])
    assert (valid["release_timestamp"] <= valid["timestamp"]).all()
