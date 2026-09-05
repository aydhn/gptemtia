"""Tests for Phase 132 Handoff."""

from advanced_cross_asset_regime_context.phase_132_handoff import (
    HANDOFF_ITEMS,
    build_phase_132_macro_event_news_regime_context_handoff_report,
)


def test_phase_132_handoff():
    assert len(HANDOFF_ITEMS) == 10
    df, summary = build_phase_132_macro_event_news_regime_context_handoff_report()
    assert len(df) == 10
    assert summary["total_items"] == 10
    assert summary["ready_items"] == 10
    assert summary["all_ready"] is True
    assert summary["handoff_status"] == "READY"
    assert summary["source_phase"] == 131
    assert summary["next_phase"] == 132
    assert summary["target_final_phase"] == 160
    assert summary["non_signal"] is True
    assert summary["source_preserved"] is True
