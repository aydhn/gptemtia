"""Tests for Phase 134 Regime FeatureStore Contracts."""

from advanced_regime_featurestore_integration.regime_featurestore_contracts import (
    build_regime_featurestore_contract_registry,
    validate_regime_featurestore_contract,
    summarize_regime_featurestore_contracts,
)


def test_contracts_output():
    df, summary = build_regime_featurestore_contract_registry()
    assert not df.empty
    assert len(df) >= 10
    assert (df["non_signal_required"] == True).all()
    assert (df["source_preservation_required"] == True).all()
    assert (df["production_ready"] == False).all()

    s_res = summarize_regime_featurestore_contracts(df)
    assert s_res["all_non_signal"] is True
    assert s_res["all_production_false"] is True


def test_validate_contract():
    valid_contract = {
        "contract_name": "valid_test_contract",
        "non_signal_required": True,
        "source_preservation_required": True,
        "no_lookahead_acceptance_required": True,
        "production_ready": False,
        "broker_ready": False,
    }
    assert validate_regime_featurestore_contract(valid_contract)["is_valid"] is True

    invalid_contract = {
        "contract_name": "invalid_test_contract",
        "non_signal_required": False,
        "production_ready": True,
    }
    res = validate_regime_featurestore_contract(invalid_contract)
    assert res["is_valid"] is False
    assert len(res["errors"]) >= 2
