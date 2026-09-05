from advanced_regime_rule_free.regime_candidate_state_integrity_contracts import (
    build_regime_candidate_state_integrity_contract_registry,
    validate_candidate_state_integrity_contract,
    summarize_candidate_state_integrity_contracts,
)


def test_build_regime_candidate_state_integrity_contract_registry():
    df, summary = build_regime_candidate_state_integrity_contract_registry()
    assert len(df) == 8
    assert summary["all_mandatory"] is True
    assert summary["all_non_signal"] is True
    assert summary["integrity_status"] == "VALID"


def test_validate_candidate_state_integrity_contract():
    valid_c = {"contract_rule_id": "test_rule", "is_mandatory": True, "non_signal": True}
    res = validate_candidate_state_integrity_contract(valid_c)
    assert res["is_valid"] is True

    invalid_c = {"contract_rule_id": "test_bad", "is_mandatory": False, "non_signal": False}
    res_bad = validate_candidate_state_integrity_contract(invalid_c)
    assert res_bad["is_valid"] is False
    assert len(res_bad["violations"]) == 2
