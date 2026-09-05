"""Tests for Cross-Domain Context Fusion."""

import pandas as pd
from advanced_feature_fusion.cross_domain_context_fusion import (
    fuse_cross_domain_context,
    get_cross_domain_context_fusion_summary,
)


def test_summary():
    summary = get_cross_domain_context_fusion_summary()
    assert summary["engine"] == "cross_domain_context_fusion"
    assert summary["join_policy"] == "backward_only_asof"
    assert summary["is_signal"] is False


def test_fuse_cross_domain_context():
    times = pd.date_range("2025-01-01 10:00:00", periods=5, freq="1h", tz="UTC")
    base_df = pd.DataFrame({
        "timestamp": times,
        "asset": ["XAUUSD"] * 5,
        "close": [2600.0, 2605.0, 2602.0, 2610.0, 2608.0],
    })

    macro_df = pd.DataFrame({
        "macro_release_timestamp": times,
        "cpi": [3.1, 3.1, 3.1, 3.2, 3.2],
    })

    calendar_df = pd.DataFrame({
        "calendar_release_timestamp": times,
        "fomc_actual": [5.25, 5.25, 5.25, 5.25, 5.00],
    })

    news_df = pd.DataFrame({
        "news_published_timestamp": times,
        "news_topic": ["fed"] * 5,
    })

    fused = fuse_cross_domain_context(
        base_df=base_df,
        macro_df=macro_df,
        calendar_df=calendar_df,
        news_metadata_df=news_df,
        timestamp_col="timestamp",
    )
    assert len(fused) == 5
    assert "cpi" in fused.columns
    assert "fomc_actual" in fused.columns
    assert "news_topic" in fused.columns
    # Check input immutability
    assert "cpi" not in base_df.columns
