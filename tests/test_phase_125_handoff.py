from advanced_feature_store_integration.phase_125_handoff import (
    HANDOFF_ITEMS,
    build_phase_125_feature_factor_engine_acceptance_handoff_report,
    summarize_phase_125_handoff,
)

def test_phase_125_handoff():
    assert len(HANDOFF_ITEMS) >= 10
    df, s = build_phase_125_feature_factor_engine_acceptance_handoff_report()
    assert not df.empty
    assert s["handoff_status"] == "READY"
    assert s["source_phase"] == 124
    assert s["next_phase"] == 125
    assert s["target_final_phase"] == 160
    assert s["non_signal"] is True
    assert s["source_preserved"] is True
    assert s["ready_items"] == len(HANDOFF_ITEMS)
    summary = summarize_phase_125_handoff(df)
    assert summary["handoff_status"] == "READY"
