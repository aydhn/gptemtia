"""Tests for Phase 134 Handoff Report."""

from advanced_regime_validation_acceptance.phase_134_handoff import (
    build_phase_134_regime_featurestore_integration_handoff_report,
    summarize_phase_134_handoff,
    HANDOFF_ITEMS,
)


def test_phase_134_handoff():
    assert len(HANDOFF_ITEMS) >= 12

    df, summary = build_phase_134_regime_featurestore_integration_handoff_report()
    assert len(df) >= 12
    assert summary["all_ready"] is True
    assert summary["handoff_status"] == "READY"
    assert summary["source_phase"] == 133
    assert summary["next_phase"] == 134
    assert summary["target_final_phase"] == 160
    assert summary["non_signal"] is True
    assert summary["source_preserved"] is True

    s_df = summarize_phase_134_handoff(df)
    assert s_df["all_ready"] is True
    assert s_df["handoff_status"] == "READY"
