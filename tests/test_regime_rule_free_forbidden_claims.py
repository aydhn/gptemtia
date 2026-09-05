from advanced_regime_rule_free.regime_rule_free_forbidden_claims import (
    validate_regime_rule_free_forbidden_claims,
    build_regime_rule_free_forbidden_claim_registry,
    summarize_regime_rule_free_forbidden_claims,
    FORBIDDEN_CLAIMS_CATALOG,
)


def test_validate_regime_rule_free_forbidden_claims():
    clean_text = "System operates without trade signals and does not generate target labels."
    res_clean = validate_regime_rule_free_forbidden_claims(clean_text)
    assert res_clean["is_clean"] is True

    bad_text = "The pipeline is now production ready for live market execution."
    res_bad = validate_regime_rule_free_forbidden_claims(bad_text)
    assert res_bad["is_clean"] is False
    assert "production ready" in res_bad["detected_forbidden_claims"]


def test_build_regime_rule_free_forbidden_claim_registry():
    df, summary = build_regime_rule_free_forbidden_claim_registry()
    assert len(df) == 15
    assert summary["total_forbidden_claims"] == 15
    assert summary["critical_risk_claims"] > 0
    assert summary["status"] == "CATALOG_ACTIVE"
