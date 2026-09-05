"""Tests for News Freshness Feature Placeholders."""

import pandas as pd
from advanced_feature_fusion.news_freshness_feature_placeholders import (
    get_news_freshness_features_registry,
    get_news_freshness_features_summary,
    add_news_freshness_placeholder,
)


def test_freshness_registry():
    features = get_news_freshness_features_registry()
    assert len(features) >= 2
    summary = get_news_freshness_features_summary()
    assert summary["count"] == len(features)
    assert summary["strictly_metadata_only"] is True


def test_add_news_freshness_placeholder():
    df = pd.DataFrame({
        "timestamp": pd.to_datetime(["2025-01-01 12:00:00", "2025-01-01 15:00:00"], utc=True),
        "news_published_timestamp": pd.to_datetime(["2025-01-01 10:00:00", "2025-01-01 10:00:00"], utc=True),
    })
    res = add_news_freshness_placeholder(df)
    assert "news_freshness_hours" in res.columns
    assert res["news_freshness_hours"].iloc[0] == 2.0
    assert res["news_freshness_hours"].iloc[1] == 5.0
