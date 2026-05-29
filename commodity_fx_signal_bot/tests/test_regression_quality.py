from scenario_regression.regression_quality import check_for_forbidden_terms_in_regression

def test_forbidden_terms():
    res = check_for_forbidden_terms_in_regression(text="Bu bir live order testidir")
    assert res["passed"] is False
    assert "live order" in res["forbidden_terms_found"]

    res2 = check_for_forbidden_terms_in_regression(text="Canlı emir yoktur.")
    assert res2["passed"] is True
