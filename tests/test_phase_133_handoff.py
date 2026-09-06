"""Tests for Phase 132 -> Phase 133 Handoff."""

from advanced_macro_event_news_regime.phase_133_handoff import (
    build_phase_133_regime_validation_no_lookahead_acceptance_handoff_report,
    summarize_phase_133_handoff,
)


def test_build_phase_133_handoff():
    df, summary = build_phase_133_regime_validation_no_lookahead_acceptance_handoff_report()
    assert not df.empty
    assert len(df) >= 13
    assert summary["handoff_status"] == "READY"
    assert summary["current_phase"] == 132
    assert summary["next_phase"] == 133
    assert summary["target_final_phase"] == 160
    assert summary["all_ready"] is True
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_phase_133_handoff():
    df, _ = build_phase_133_regime_validation_no_lookahead_acceptance_handoff_report()
    summary = summarize_phase_133_handoff(df)
    assert summary["total_items"] >= 13
    assert summary["all_ready"] is True
    assert summary["all_non_signal"] is True
