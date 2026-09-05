from advanced_fx_providers.fx_validation import validate_no_forbidden_fx_claims
def test_val():
    assert validate_no_forbidden_fx_claims("some text")["valid"] is True
    assert validate_no_forbidden_fx_claims("production deployed")["valid"] is False
