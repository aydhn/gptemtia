from advanced_regime_matrix.regime_matrix_input_features import (
    build_regime_matrix_input_feature_registry,
    build_regime_matrix_input_features_registry,
    INPUT_FEATURES_CATALOG,
)


def test_build_regime_matrix_input_features_registry():
    df, s = build_regime_matrix_input_feature_registry()
    assert len(df) >= 10
    assert s["total_input_features"] >= 10
    assert s["all_non_signal"] is True
    assert s["all_source_preserved"] is True
    assert "regime_matrix__tech__sma_ratio" in df["feature_key"].values


def test_input_features_alias():
    df, s = build_regime_matrix_input_features_registry()
    assert len(df) >= 10
    assert s["status"] == "matrix_ready"
