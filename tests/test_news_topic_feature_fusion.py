"""Tests for News Topic Feature Fusion."""

import pandas as pd
from advanced_feature_fusion.news_topic_feature_fusion import (
    build_news_topic_feature_fusion_registry,
    summarize_news_topic_feature_fusion,
    add_news_topic_flag_placeholder,
    add_news_topic_count_placeholder,
)


def test_news_topic_registry():
    df, summary = build_news_topic_feature_fusion_registry()
    assert len(df) == 2
    assert summary["total_features"] == 2
    assert summary["non_signal_guaranteed"] is True


def test_news_topic_features():
    df = pd.DataFrame({
        "topic": ["rates,inflation", "energy", None],
    })
    flagged = add_news_topic_flag_placeholder(df, topic_field="topic", topic_value="rates", output_field="has_rates")
    assert "has_rates" in flagged.columns
    assert bool(flagged["has_rates"].iloc[0]) is True
    assert bool(flagged["has_rates"].iloc[1]) is False

    counted = add_news_topic_count_placeholder(df, topic_field="topic")
    assert "news_topic_count_placeholder" in counted.columns
    assert counted["news_topic_count_placeholder"].iloc[0] == 2
    assert counted["news_topic_count_placeholder"].iloc[1] == 1
    assert counted["news_topic_count_placeholder"].iloc[2] == 0
