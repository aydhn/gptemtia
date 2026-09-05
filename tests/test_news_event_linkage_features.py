"""Tests for News Event Linkage Features."""

import pandas as pd
from advanced_feature_fusion.news_event_linkage_features import (
    build_news_event_linkage_feature_registry,
    summarize_news_event_linkage_features,
    add_news_event_linkage_flag_placeholder,
)


def test_linkage_registry():
    df, summary = build_news_event_linkage_feature_registry()
    assert len(df) == 1
    assert summary["total_features"] == 1
    assert summary["non_signal_guaranteed"] is True


def test_add_linkage_flag():
    df = pd.DataFrame({
        "event_reference": ["EVT_FOMC_01", "", None],
    })
    res = add_news_event_linkage_flag_placeholder(df, event_ref_field="event_reference")
    assert "news_event_linkage_flag_placeholder" in res.columns
    assert bool(res["news_event_linkage_flag_placeholder"].iloc[0]) is True
    assert bool(res["news_event_linkage_flag_placeholder"].iloc[1]) is False
    assert bool(res["news_event_linkage_flag_placeholder"].iloc[2]) is False
