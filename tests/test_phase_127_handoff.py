from advanced_regime_foundation.phase_127_handoff import (
    build_phase_127_regime_feature_matrix_handoff_report,
    summarize_phase_127_handoff,
)


def test_phase_127_handoff():
    df, summary = build_phase_127_regime_feature_matrix_handoff_report()
    assert not df.empty
    assert summary["source_phase"] == 126
    assert summary["next_phase"] == 127
    assert summary["target_final_phase"] == 160
    assert summary["handoff_status"] == "READY"
    assert summary["ready_items"] == summary["total_handoff_items"]
    assert summary["non_signal"] is True
    assert summary["source_preserved"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False

    summ = summarize_phase_127_handoff(df)
    assert summ["all_ready"] is True
    assert summ["non_signal"] is True
