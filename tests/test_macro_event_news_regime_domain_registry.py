"""Tests for Phase 132 Domain Registry."""

from advanced_macro_event_news_regime.macro_event_news_regime_domain_registry import (
    build_macro_event_news_regime_domain_registry,
    summarize_macro_event_news_regime_domains,
)


def test_build_domain_registry():
    df, summary = build_macro_event_news_regime_domain_registry()
    assert not df.empty
    assert len(df) >= 35
    assert "domain_label" in df.columns
    assert "category" in df.columns
    assert summary["all_non_signal"] is True


def test_summarize_domain_registry():
    df, _ = build_macro_event_news_regime_domain_registry()
    summary = summarize_macro_event_news_regime_domains(df)
    assert summary["total_domains"] >= 35
    assert summary["categories"] >= 5
    assert summary["all_non_signal"] is True
