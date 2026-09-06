"""Tests for Phase 132 Macro Surprise Placeholders."""

from advanced_macro_event_news_regime.macro_surprise_placeholders import (
    build_macro_surprise_placeholder_registry,
    summarize_macro_surprise_placeholders,
)


def test_build_macro_surprise_placeholders():
    df, summary = build_macro_surprise_placeholder_registry()
    assert not df.empty
    assert len(df) >= 3
    assert "surprise_id" in df.columns
    assert "contract_type" in df.columns
    assert summary["zero_signals"] is True
    assert summary["zero_predictions"] is True
    assert summary["all_non_signal"] is True


def test_summarize_macro_surprise_placeholders():
    df, _ = build_macro_surprise_placeholder_registry()
    summary = summarize_macro_surprise_placeholders(df)
    assert summary["total_placeholders"] >= 3
    assert summary["zero_signals"] is True
    assert summary["zero_predictions"] is True
    assert summary["all_non_signal"] is True
