from advanced_market_behavior_diagnostics.phase_130_handoff import (
    build_phase_130_regime_transition_stability_handoff_report,
    summarize_phase_130_handoff,
    CORE_PHASE_130_HANDOFF_ITEMS,
)


def test_phase_130_handoff():
    df, summary = build_phase_130_regime_transition_stability_handoff_report()

    assert not df.empty
    assert len(df) == len(CORE_PHASE_130_HANDOFF_ITEMS)
    assert summary["handoff_status"] == "READY"
    assert summary["source_phase"] == 129
    assert summary["next_phase"] == 130
    assert summary["target_final_phase"] == 160
    assert summary["all_ready"] is True
    assert summary["non_signal"] is True
