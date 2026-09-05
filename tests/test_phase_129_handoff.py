from advanced_regime_rule_free.phase_129_handoff import (
    build_phase_129_market_behavior_diagnostics_handoff_report,
    summarize_phase_129_handoff,
    PHASE_129_HANDOFF_ITEMS,
)


def test_build_phase_129_market_behavior_diagnostics_handoff_report():
    df, summary = build_phase_129_market_behavior_diagnostics_handoff_report()
    assert len(df) == 12
    assert summary["source_phase"] == 128
    assert summary["next_phase"] == 129
    assert summary["target_final_phase"] == 160
    assert summary["total_items"] == 12
    assert summary["verified_items"] == 12
    assert summary["all_ready"] is True
    assert summary["handoff_status"] == "READY"

    assert len(PHASE_129_HANDOFF_ITEMS) == 12
