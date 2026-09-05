from advanced_regime_rule_free.normalization_prep_contracts import (
    build_normalization_prep_contract_registry,
    summarize_normalization_prep_contracts,
)


def test_build_normalization_prep_contract_registry():
    df, summary = build_normalization_prep_contract_registry()
    assert len(df) == 4
    assert summary["all_non_mutating"] is True
    assert summary["all_non_signal"] is True
    assert summary["status"] == "VALID"

    methods = df["normalization_method"].tolist()
    assert "min_max_prep_contract" in methods
    assert "zscore_prep_contract" in methods
    assert "robust_median_iqr_prep_contract" in methods
    assert "quantile_prep_contract" in methods
