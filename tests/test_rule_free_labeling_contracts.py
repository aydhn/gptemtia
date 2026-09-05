from advanced_regime_rule_free.rule_free_labeling_contracts import (
    build_rule_free_labeling_contract_registry,
    validate_rule_free_labeling_contract,
)


def test_build_rule_free_labeling_contract_registry():
    df, summary = build_rule_free_labeling_contract_registry()
    assert len(df) == 8
    assert summary["all_non_signal"] is True
    assert summary["all_target_forbidden"] is True
    assert summary["all_prediction_forbidden"] is True
    assert summary["all_clustering_forbidden"] is True
    assert summary["all_training_forbidden"] is True
    assert summary["contracts_status"] == "VALID"

    contracts = df["contract_name"].tolist()
    assert "volatility_candidate_state_contract" in contracts
    assert "trend_candidate_state_contract" in contracts
    assert "range_candidate_state_contract" in contracts
    assert "macro_event_candidate_state_contract" in contracts
    assert "news_attention_candidate_state_contract" in contracts
    assert "cross_asset_candidate_state_contract" in contracts
    assert "transition_candidate_state_contract" in contracts
    assert "uncertain_candidate_state_contract" in contracts


def test_validate_rule_free_labeling_contract():
    valid_c = {
        "contract_name": "volatility_candidate_state_contract",
        "candidate_state_family": "volatility",
        "non_signal_required": True,
        "target_label_forbidden": True,
        "prediction_forbidden": True,
        "model_training_allowed": False,
        "clustering_allowed": False,
    }
    assert validate_rule_free_labeling_contract(valid_c)["is_valid"] is True

    invalid_c = {
        "contract_name": "buy_signal_contract",
        "candidate_state_family": "buy",
        "non_signal_required": False,
        "target_label_forbidden": False,
        "prediction_forbidden": False,
        "model_training_allowed": True,
        "clustering_allowed": True,
    }
    res = validate_rule_free_labeling_contract(invalid_c)
    assert res["is_valid"] is False
    assert len(res["violations"]) >= 5
