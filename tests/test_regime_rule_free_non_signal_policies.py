from advanced_regime_rule_free.regime_rule_free_non_signal_policies import (
    validate_regime_rule_free_non_signal_text,
    build_regime_rule_free_non_signal_policy_registry,
    summarize_regime_rule_free_non_signal_policies,
)


def test_validate_regime_rule_free_non_signal_text():
    clean_text = "This report analyzes volatility distributions across commodity assets."
    assert validate_regime_rule_free_non_signal_text(clean_text)["is_valid"] is True

    bad_text = "Bu analiz brent için kesin al sinyali üretmektedir."
    res = validate_regime_rule_free_non_signal_text(bad_text)
    assert res["is_valid"] is False
    assert len(res["detected_signal_terms"]) > 0


def test_build_regime_rule_free_non_signal_policy_registry():
    df, summary = build_regime_rule_free_non_signal_policy_registry()
    assert len(df) == 5
    assert summary["all_enforced"] is True
    assert summary["policy_status"] == "ACTIVE_SECURE"
