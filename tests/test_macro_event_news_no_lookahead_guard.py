"""Tests for Phase 132 Macro/Event/News No-Lookahead Guard."""

import pandas as pd
from advanced_macro_event_news_regime.macro_event_news_no_lookahead_guard import (
    build_macro_event_news_no_lookahead_guard_registry,
    validate_no_future_macro_event_news_join,
    validate_no_forbidden_macro_event_news_columns,
    validate_no_negative_shift_usage,
    summarize_macro_event_news_no_lookahead_guard,
)


def test_build_macro_event_news_no_lookahead_guard():
    df, summary = build_macro_event_news_no_lookahead_guard_registry()
    assert not df.empty
    assert len(df) >= 4
    assert "guard_id" in df.columns
    assert summary["all_enforced"] is True
    assert summary["all_non_signal"] is True


def test_validate_no_future_macro_event_news_join():
    left = pd.DataFrame({"time": ["2026-01-01 12:00:00", "2026-01-02 12:00:00"]})
    right_ok = pd.DataFrame({"time": ["2026-01-01 10:00:00"]})
    res_ok = validate_no_future_macro_event_news_join(left, right_ok, "time", "time")
    assert res_ok["valid"] is True

    right_future = pd.DataFrame({"time": ["2026-01-03 10:00:00"]})
    res_future = validate_no_future_macro_event_news_join(left, right_future, "time", "time")
    assert res_future["valid"] is False


def test_validate_no_forbidden_macro_event_news_columns():
    clean_df = pd.DataFrame({"macro_id": [1], "release_date": ["2026-01-01"]})
    res_clean = validate_no_forbidden_macro_event_news_columns(clean_df)
    assert res_clean["valid"] is True

    dirty_df = pd.DataFrame({"buy_signal": [1], "future_return": [0.05], "article_body": ["text"]})
    res_dirty = validate_no_forbidden_macro_event_news_columns(dirty_df)
    assert res_dirty["valid"] is False
    assert res_dirty["violation_count"] >= 3


def test_validate_no_negative_shift_usage():
    clean_code = "df['prior_val'] = df['val'].shift(1)"
    res_clean = validate_no_negative_shift_usage(clean_code)
    assert res_clean["valid"] is True

    leaky_code = "df['future_val'] = df['val'].shift(-1)"
    res_leaky = validate_no_negative_shift_usage(leaky_code)
    assert res_leaky["valid"] is False


def test_summarize_macro_event_news_no_lookahead_guard():
    df, _ = build_macro_event_news_no_lookahead_guard_registry()
    summary = summarize_macro_event_news_no_lookahead_guard(df)
    assert summary["total_guards"] >= 4
    assert summary["all_enforced"] is True
    assert summary["all_non_signal"] is True
