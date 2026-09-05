from advanced_regime_matrix.regime_matrix_validation import (
    run_regime_matrix_validation,
    check_forbidden_claims_in_text,
)


def test_run_regime_matrix_validation():
    df, s = run_regime_matrix_validation()
    assert s["validation_status"] == "VALIDATION_PASS"
    assert s["total_rules"] == s["passed_rules"]
    assert s["failed_rules"] == 0
    assert s["forbidden_claims_clean"] is True


def test_check_forbidden_claims_in_text():
    clean_text = "Analysis of historical regime features and contracts."
    dirty_text = "This algorithm delivers guaranteed profitable buy signals and broker ready execution."
    assert len(check_forbidden_claims_in_text(clean_text)) == 0
    assert len(check_forbidden_claims_in_text(dirty_text)) > 0
