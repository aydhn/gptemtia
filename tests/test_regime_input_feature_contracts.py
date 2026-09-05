from advanced_regime_foundation.regime_input_feature_contracts import (
    build_regime_input_feature_contract_registry,
    validate_regime_input_feature_contract,
    summarize_regime_input_feature_contracts,
)


def test_regime_input_feature_contracts():
    df, summary = build_regime_input_feature_contract_registry()
    assert not df.empty
    assert summary["all_validation_required"] is True
    assert summary["all_quality_required"] is True
    assert summary["all_no_lookahead_required"] is True
    assert summary["all_non_signal_required"] is True

    valid_contract = {
        "contract_name": "test_contract",
        "regime_family": "regime_family_volatility",
        "required_feature_families": "atr_features",
        "required_factor_families": "factor_volatility",
        "source_phase_refs": [117, 122],
        "no_lookahead_required": True,
        "non_signal_required": True,
    }
    assert validate_regime_input_feature_contract(valid_contract)["is_valid"] is True

    invalid_contract = {
        "contract_name": "test_contract",
        # missing fields
    }
    assert validate_regime_input_feature_contract(invalid_contract)["is_valid"] is False

    summ = summarize_regime_input_feature_contracts(df)
    assert summ["total_contracts"] == len(df)
    assert summ["all_non_signal"] is True
