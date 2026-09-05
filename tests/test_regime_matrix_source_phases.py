from advanced_regime_matrix.regime_matrix_source_phases import (
    build_regime_matrix_source_phases_registry,
    is_valid_regime_matrix_source_phase,
)


def test_build_regime_matrix_source_phases_registry():
    df, s = build_regime_matrix_source_phases_registry()
    assert len(df) == 10
    assert s["total_source_phases"] == 10
    assert s["all_non_signal"] is True
    assert s["all_source_preserved"] is True
    assert is_valid_regime_matrix_source_phase(117) is True
    assert is_valid_regime_matrix_source_phase(126) is True
    assert is_valid_regime_matrix_source_phase(128) is False
