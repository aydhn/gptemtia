from advanced_regime_matrix.regime_matrix_quality_inputs import (
    build_regime_matrix_quality_input_registry,
    build_regime_matrix_quality_inputs_registry,
    QUALITY_INPUTS_CATALOG,
)


def test_build_regime_matrix_quality_inputs_registry():
    df, s = build_regime_matrix_quality_input_registry()
    assert len(df) >= 5
    assert s["total_quality_inputs"] >= 5
    assert s["all_non_signal"] is True
    assert "qual_validation_status" in df["metric_id"].values
    assert "qual_missingness_score" in df["metric_id"].values


def test_quality_inputs_alias():
    df, s = build_regime_matrix_quality_inputs_registry()
    assert len(df) >= 5
    assert s["status"] == "matrix_ready"
