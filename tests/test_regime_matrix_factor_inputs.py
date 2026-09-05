from advanced_regime_matrix.regime_matrix_factor_inputs import (
    build_regime_matrix_factor_input_registry,
    build_regime_matrix_factor_inputs_registry,
    FACTOR_INPUTS_CATALOG,
)


def test_build_regime_matrix_factor_inputs_registry():
    df, s = build_regime_matrix_factor_input_registry()
    assert len(df) >= 7
    assert s["total_factor_inputs"] >= 7
    assert s["all_non_signal"] is True
    assert s["all_source_preserved"] is True
    assert "trend_factor_family" in df["factor_family"].values


def test_factor_inputs_alias():
    df, s = build_regime_matrix_factor_inputs_registry()
    assert len(df) >= 7
    assert s["status"] == "matrix_ready"
