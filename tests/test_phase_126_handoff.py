from advanced_feature_factor_acceptance.phase_126_handoff import (
    HANDOFF_ITEMS,
    build_phase_126_regime_classification_handoff_report,
    summarize_phase_126_handoff,
)

def test_phase_126_handoff():
    assert len(HANDOFF_ITEMS) >= 10
    df, s = build_phase_126_regime_classification_handoff_report()
    assert not df.empty
    assert s["handoff_status"] == "READY"
    assert s["source_phase"] == 125
    assert s["next_phase"] == 126
    assert s["target_final_phase"] == 160
    assert s["non_signal"] is True
    assert s["source_preserved"] is True
    assert s["ready_items"] == len(HANDOFF_ITEMS)

    summary = summarize_phase_126_handoff(df)
    assert summary["all_ready"] is True
    assert summary["non_signal"] is True
