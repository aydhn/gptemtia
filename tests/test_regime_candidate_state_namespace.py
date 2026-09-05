from advanced_regime_rule_free.regime_candidate_state_namespace import (
    build_candidate_state_key,
    validate_candidate_state_key,
    build_regime_candidate_state_namespace_registry,
    summarize_regime_candidate_state_namespace,
)


def test_build_candidate_state_key():
    key = build_candidate_state_key("COMMODITY", "BRENT", "volatility")
    assert key == "candidate_state_commodity_brent_volatility"


def test_validate_candidate_state_key_valid():
    res = validate_candidate_state_key("candidate_state_commodity_brent_volatility")
    assert res["is_valid"] is True
    assert len(res["violations"]) == 0


def test_validate_candidate_state_key_forbidden_and_format():
    res1 = validate_candidate_state_key("candidate_state_commodity_brent_buy")
    assert res1["is_valid"] is False
    assert any("Forbidden word 'buy'" in v for v in res1["violations"])

    res2 = validate_candidate_state_key("invalid_prefix_brent")
    assert res2["is_valid"] is False
    assert any("Key must start with" in v for v in res2["violations"])


def test_build_regime_candidate_state_namespace_registry():
    df, summary = build_regime_candidate_state_namespace_registry()
    assert len(df) == 4
    assert summary["all_rules_enforced"] is True
    assert summary["namespace_status"] == "VALID"
