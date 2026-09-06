"""Tests for Phase 132 Macro/Event/News Timestamp Policies."""

import pandas as pd
from advanced_macro_event_news_regime.macro_event_news_timestamp_policies import (
    build_macro_event_news_timestamp_policy_registry,
    validate_macro_event_news_context_timestamp_not_future,
    summarize_macro_event_news_timestamp_policies,
)


def test_build_macro_event_news_timestamp_policies():
    df, summary = build_macro_event_news_timestamp_policy_registry()
    assert not df.empty
    assert len(df) >= 3
    assert "policy_id" in df.columns
    assert "direction" in df.columns
    assert summary["all_backward_only"] is True
    assert summary["all_non_signal"] is True


def test_validate_macro_event_news_context_timestamp_not_future():
    valid_df = pd.DataFrame({
        "base_ts": ["2026-01-02 12:00:00", "2026-01-03 12:00:00"],
        "context_ts": ["2026-01-02 10:00:00", "2026-01-03 11:30:00"],
    })
    res_valid = validate_macro_event_news_context_timestamp_not_future(valid_df, "base_ts", "context_ts")
    assert res_valid["valid"] is True
    assert res_valid["future_leakage_detected"] is False

    invalid_df = pd.DataFrame({
        "base_ts": ["2026-01-02 12:00:00"],
        "context_ts": ["2026-01-02 13:00:00"],  # Future relative to base
    })
    res_invalid = validate_macro_event_news_context_timestamp_not_future(invalid_df, "base_ts", "context_ts")
    assert res_invalid["valid"] is False
    assert res_invalid["future_leakage_detected"] is True


def test_summarize_macro_event_news_timestamp_policies():
    df, _ = build_macro_event_news_timestamp_policy_registry()
    summary = summarize_macro_event_news_timestamp_policies(df)
    assert summary["total_policies"] >= 3
    assert summary["all_backward"] is True
    assert summary["all_non_signal"] is True
