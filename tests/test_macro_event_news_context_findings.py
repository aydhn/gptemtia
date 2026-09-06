"""Tests for Phase 132 Macro/Event/News Context Findings."""

from advanced_macro_event_news_regime.macro_event_news_context_findings import (
    create_macro_event_news_context_finding,
    build_macro_event_news_context_findings_registry,
    summarize_macro_event_news_context_findings,
)


def test_create_macro_event_news_context_finding():
    finding = create_macro_event_news_context_finding(
        finding_type="test_finding",
        context_type="macro_indicator_context",
        severity_label="info",
        message="Test message",
        recommendation="Test recommendation",
    )
    assert finding.finding_id.startswith("find_")
    assert finding.destructive_action_allowed is False
    assert finding.auto_fix_allowed is False


def test_build_macro_event_news_context_findings():
    df, summary = build_macro_event_news_context_findings_registry()
    assert not df.empty
    assert len(df) >= 3
    assert "finding_id" in df.columns
    assert summary["destructive_action_allowed"] is False
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_macro_event_news_context_findings():
    df, _ = build_macro_event_news_context_findings_registry()
    summary = summarize_macro_event_news_context_findings(df)
    assert summary["total_findings"] >= 3
    assert summary["all_non_signal"] is True
