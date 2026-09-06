"""Tests for Phase 132 Macro/Event/News Context Scoring."""

import pandas as pd
from advanced_macro_event_news_regime.macro_event_news_context_scoring import (
    classify_macro_event_news_context_score,
    calculate_macro_event_news_context_score,
    build_macro_event_news_context_score_report,
    summarize_macro_event_news_context_scores,
)


def test_classify_macro_event_news_context_score():
    assert classify_macro_event_news_context_score(0.95) == "high_context_integrity"
    assert classify_macro_event_news_context_score(0.65) == "acceptable_context_integrity"
    assert classify_macro_event_news_context_score(0.35) == "marginal_context_integrity"
    assert classify_macro_event_news_context_score(0.10) == "critical_context_flaw"


def test_calculate_macro_event_news_context_score():
    empty_df = pd.DataFrame()
    score_clean = calculate_macro_event_news_context_score(empty_df)
    assert score_clean.context_score == 1.0
    assert score_clean.classification == "high_context_integrity"
    assert score_clean.non_signal is True

    findings_df = pd.DataFrame([
        {"severity_label": "blocker", "manual_review_required": True},
        {"severity_label": "warning", "manual_review_required": False},
    ])
    score_penalized = calculate_macro_event_news_context_score(findings_df)
    assert score_penalized.context_score < 1.0
    assert score_penalized.blocker_count == 1
    assert score_penalized.warning_count == 1


def test_build_macro_event_news_context_score_report():
    df, summary = build_macro_event_news_context_score_report()
    assert not df.empty
    assert "context_score" in df.columns
    assert summary["meets_threshold"] is True
    assert summary["all_non_signal"] is True


def test_summarize_macro_event_news_context_scores():
    df, _ = build_macro_event_news_context_score_report()
    summary = summarize_macro_event_news_context_scores(df)
    assert summary["total_scores"] == 1
    assert summary["mean_score"] > 0.5
    assert summary["all_non_signal"] is True
