from advanced_regime_matrix.phase_128_handoff import (
    build_phase_128_handoff_registry,
    validate_phase_128_handoff_ready,
)


def test_build_phase_128_handoff_registry():
    df, s = build_phase_128_handoff_registry()
    assert len(df) == 12
    assert s["total_handoff_items"] == 12
    assert s["ready_items"] == 12
    assert s["handoff_status"] == "READY"
    assert s["source_phase"] == 127
    assert s["next_phase"] == 128
    assert s["target_final_phase"] == 160
    assert s["all_non_signal"] is True
    assert validate_phase_128_handoff_ready() is True
