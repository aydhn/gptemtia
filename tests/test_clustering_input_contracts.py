from advanced_regime_rule_free.clustering_input_contracts import (
    build_clustering_input_contract_registry,
    validate_clustering_input_contract,
)


def test_build_clustering_input_contract_registry():
    df, summary = build_clustering_input_contract_registry()
    assert len(df) == 5
    assert summary["all_non_signal"] is True
    assert summary["all_no_clustering"] is True
    assert summary["all_no_training"] is True
    assert summary["contracts_status"] == "VALID"

    names = df["input_contract_name"].tolist()
    assert "technical_volatility_clustering_input_contract" in names
    assert "technical_trend_clustering_input_contract" in names
    assert "cross_asset_correlation_clustering_input_contract" in names


def test_validate_clustering_input_contract():
    valid = {
        "input_contract_name": "technical_volatility_clustering_input_contract",
        "model_training_allowed": False,
        "clustering_allowed": False,
        "non_signal": True,
        "no_lookahead_required": True,
    }
    assert validate_clustering_input_contract(valid)["is_valid"] is True

    invalid = {
        "input_contract_name": "clustering_exec_contract",
        "model_training_allowed": True,
        "clustering_allowed": True,
        "non_signal": False,
        "no_lookahead_required": False,
    }
    assert validate_clustering_input_contract(invalid)["is_valid"] is False
