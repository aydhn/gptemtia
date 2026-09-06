"""Tests for Macro/Event/News Validation Acceptance."""

from advanced_regime_validation_acceptance.macro_event_news_validation_acceptance import (
    build_macro_event_news_validation_acceptance_report,
    summarize_macro_event_news_validation_acceptance,
)


def test_macro_event_news_validation_acceptance():
    df, summary = build_macro_event_news_validation_acceptance_report()
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["component"] == "phase_132_macro_event_news"
    assert summary["non_signal"] is True

    s_df = summarize_macro_event_news_validation_acceptance(df)
    assert s_df["all_passed"] is True
