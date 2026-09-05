from advanced_regime_matrix.regime_matrix_forbidden_column_policies import (
    is_forbidden_column_name,
    find_forbidden_columns,
    build_regime_matrix_forbidden_column_policies,
)


def test_is_forbidden_column_name():
    assert is_forbidden_column_name("target_return_5d") is True
    assert is_forbidden_column_name("future_price") is True
    assert is_forbidden_column_name("pred_label") is True
    assert is_forbidden_column_name("lead_close") is True
    assert is_forbidden_column_name("regime_matrix__volatility_atr_14") is False
    assert is_forbidden_column_name("canonical_symbol") is False


def test_find_forbidden_columns():
    cols = ["timestamp", "target_price", "regime_matrix__volatility_atr_14", "pred_cluster"]
    forbidden = find_forbidden_columns(cols)
    assert len(forbidden) == 2
    assert "target_price" in forbidden
    assert "pred_cluster" in forbidden


def test_build_regime_matrix_forbidden_column_policies():
    df, s = build_regime_matrix_forbidden_column_policies()
    assert len(df) == 6
    assert s["total_forbidden_column_types"] == 6
