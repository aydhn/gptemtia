"""Test suite for Phase 136 ML/GPU Handoff."""

from advanced_regime_acceptance.phase_136_handoff import (
    build_phase_136_advanced_ml_gpu_handoff_report,
    summarize_phase_136_handoff,
)


def test_phase_136_handoff():
    df, summary = build_phase_136_advanced_ml_gpu_handoff_report()
    assert not df.empty
    assert summary["source_phase"] == 135
    assert summary["next_phase"] == 136
    assert summary["target_final_phase"] == 160
    assert summary["total_prerequisites"] >= 14
    assert summary["all_satisfied"] is True
    assert summary["non_signal"] is True

    s2 = summarize_phase_136_handoff(df)
    assert s2["all_satisfied"] is True
    assert s2["non_signal"] is True
