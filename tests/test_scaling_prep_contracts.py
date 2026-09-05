from advanced_regime_rule_free.scaling_prep_contracts import (
    build_scaling_prep_contract_registry,
    summarize_scaling_prep_contracts,
)


def test_build_scaling_prep_contract_registry():
    df, summary = build_scaling_prep_contract_registry()
    assert len(df) == 3
    assert summary["all_execution_forbidden"] is True
    assert summary["all_non_signal"] is True
    assert summary["status"] == "VALID"

    methods = df["scaling_method"].tolist()
    assert "standard_scaler_prep" in methods
    assert "max_abs_scaler_prep" in methods
    assert "unit_vector_scaler_prep" in methods
