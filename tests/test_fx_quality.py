from advanced_fx_providers.fx_quality import check_for_forbidden_terms_in_fx_layer
def test_qual():
    assert check_for_forbidden_terms_in_fx_layer("some text")["score"] == 1.0
    assert check_for_forbidden_terms_in_fx_layer("API key printed")["score"] == 0.0
