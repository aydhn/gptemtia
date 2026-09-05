"""Tests for Macro-News Cross Fusion."""

import pandas as pd
from advanced_feature_fusion.macro_news_fusion import (
    fuse_macro_with_news_metadata,
    get_macro_news_fusion_summary,
)


def test_summary():
    summary = get_macro_news_fusion_summary()
    assert summary["join_direction"] == "backward"
    assert summary["strictly_metadata_only"] is True


def test_fuse_macro_with_news_metadata():
    times = pd.date_range("2025-01-01 10:00:00", periods=5, freq="1h", tz="UTC")
    macro_df = pd.DataFrame({
        "timestamp": times,
        "macro_tag": ["inflation"] * 5,
        "macro_val": [3.1, 3.1, 3.1, 3.2, 3.2],
    })

    news_df = pd.DataFrame({
        "published_timestamp": [times[1]],
        "macro_tag": ["inflation"],
        "news_topic": ["cpi_release"],
    })

    fused = fuse_macro_with_news_metadata(
        macro_df=macro_df,
        news_metadata_df=news_df,
        macro_timestamp_col="timestamp",
        news_published_col="published_timestamp",
        by="macro_tag",
        news_by="macro_tag",
    )
    assert len(fused) == len(macro_df)
    assert "news_topic" in fused.columns
    # Check backward only
    valid = fused.dropna(subset=["published_timestamp"])
    assert (valid["published_timestamp"] <= valid["timestamp"]).all()
