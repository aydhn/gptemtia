from advanced_regime_matrix.regime_matrix_context_inputs import (
    build_regime_matrix_context_input_registry,
    build_regime_matrix_context_inputs_registry,
    CONTEXT_INPUTS_CATALOG,
)


def test_build_regime_matrix_context_inputs_registry():
    df, s = build_regime_matrix_context_input_registry()
    assert len(df) >= 6
    assert s["total_context_inputs"] >= 6
    assert s["all_non_signal"] is True
    assert s["all_metadata_only"] is True
    assert "context_macro_regime" in df["context_id"].values
    assert "context_news_metadata_regime" in df["context_id"].values


def test_context_inputs_alias():
    df, s = build_regime_matrix_context_inputs_registry()
    assert len(df) >= 6
    assert s["status"] == "matrix_ready"
