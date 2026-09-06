"""Tests for Phase 132 Macro/Event/News Regime Health."""

from pathlib import Path
from advanced_macro_event_news_regime.macro_event_news_regime_health import (
    build_macro_event_news_regime_health_check,
    summarize_macro_event_news_regime_health,
)


def test_build_health_check():
    project_root = Path(__file__).resolve().parent.parent
    df, summary = build_macro_event_news_regime_health_check(project_root)
    assert not df.empty
    assert len(df) >= 10
    assert "check_name" in df.columns
    assert summary["overall_status"] == "HEALTHY"
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_health_check():
    project_root = Path(__file__).resolve().parent.parent
    df, _ = build_macro_event_news_regime_health_check(project_root)
    summary = summarize_macro_event_news_regime_health(df)
    assert summary["total_checks"] >= 10
    assert summary["failed"] == 0
    assert summary["all_non_signal"] is True
