"""Tests for Calendar-News Cross Fusion."""

import pandas as pd
from advanced_feature_fusion.calendar_news_fusion import (
    fuse_calendar_with_news_metadata,
    get_calendar_news_fusion_summary,
)


def test_summary():
    summary = get_calendar_news_fusion_summary()
    assert summary["join_direction"] == "backward"
    assert summary["strictly_metadata_only"] is True


def test_fuse_calendar_with_news_metadata():
    times = pd.date_range("2025-01-01 10:00:00", periods=5, freq="1h", tz="UTC")
    cal_df = pd.DataFrame({
        "release_timestamp": times,
        "event_id": ["EVT_FOMC"] * 5,
        "actual_value": [5.25, 5.25, 5.25, 5.25, 5.00],
    })

    news_df = pd.DataFrame({
        "published_timestamp": [times[2]],
        "event_linkage_id": ["EVT_FOMC"],
        "news_topic": ["rate_cut"],
    })

    fused = fuse_calendar_with_news_metadata(
        calendar_df=cal_df,
        news_metadata_df=news_df,
        calendar_timestamp_col="release_timestamp",
        news_published_col="published_timestamp",
        by="event_id",
        news_by="event_linkage_id",
    )
    assert len(fused) == len(cal_df)
    assert "news_topic" in fused.columns
    # Check backward only
    valid = fused.dropna(subset=["published_timestamp"])
    assert (valid["published_timestamp"] <= valid["release_timestamp"]).all()
