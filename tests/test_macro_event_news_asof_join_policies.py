"""Tests for Phase 132 Macro/Event/News Asof Join Policies."""

import pandas as pd
from advanced_macro_event_news_regime.macro_event_news_asof_join_policies import (
    build_macro_event_news_asof_join_policy_registry,
    safe_macro_event_news_asof_join_backward,
    summarize_macro_event_news_asof_join_policies,
)


def test_build_macro_event_news_asof_join_policies():
    df, summary = build_macro_event_news_asof_join_policy_registry()
    assert not df.empty
    assert len(df) >= 1
    assert "asof_policy_id" in df.columns
    assert "direction" in df.columns
    assert summary["direction"] == "backward"
    assert summary["all_non_signal"] is True


def test_safe_macro_event_news_asof_join_backward():
    left = pd.DataFrame({
        "time": pd.to_datetime(["2026-01-01 10:00:00", "2026-01-01 11:00:00", "2026-01-01 12:00:00"]),
        "price": [100.0, 101.0, 102.0],
    })
    right = pd.DataFrame({
        "pub_time": pd.to_datetime(["2026-01-01 09:30:00", "2026-01-01 10:30:00"]),
        "macro_val": [50.0, 52.0],
    })
    merged = safe_macro_event_news_asof_join_backward(
        left_df=left,
        right_df=right,
        left_on="time",
        right_on="pub_time",
    )
    assert len(merged) == 3
    assert merged.loc[merged["time"] == "2026-01-01 10:00:00", "macro_val"].values[0] == 50.0
    assert merged.loc[merged["time"] == "2026-01-01 11:00:00", "macro_val"].values[0] == 52.0
    assert merged.loc[merged["time"] == "2026-01-01 12:00:00", "macro_val"].values[0] == 52.0


def test_summarize_macro_event_news_asof_join_policies():
    df, _ = build_macro_event_news_asof_join_policy_registry()
    summary = summarize_macro_event_news_asof_join_policies(df)
    assert summary["total_policies"] >= 1
    assert summary["direction"] == "backward"
    assert summary["allow_forward"] is False
    assert summary["all_non_signal"] is True
