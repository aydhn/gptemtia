"""Tests for Phase 132 Macro/Event/News Manual Review."""

from advanced_macro_event_news_regime.macro_event_news_manual_review import (
    build_macro_event_news_manual_review_queue,
    summarize_macro_event_news_manual_review_queue,
)


def test_build_macro_event_news_manual_review_queue():
    df, summary = build_macro_event_news_manual_review_queue()
    assert not df.empty
    assert len(df) >= 8
    assert "review_id" in df.columns
    assert "safe_recommendation" in df.columns
    assert summary["prohibited_actions_enforced"] is True
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_macro_event_news_manual_review_queue():
    df, _ = build_macro_event_news_manual_review_queue()
    summary = summarize_macro_event_news_manual_review_queue(df)
    assert summary["total_reviews"] >= 8
    assert summary["prohibited_actions_count"] >= 10
    assert summary["all_non_signal"] is True
