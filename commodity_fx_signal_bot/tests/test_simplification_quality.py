from local_simplification.simplification_quality import check_for_forbidden_terms_in_simplification, build_simplification_quality_report

def test_quality():
    res = check_for_forbidden_terms_in_simplification("some text")
    assert res["forbidden_terms_found"] is False
    rep = build_simplification_quality_report({})
    assert rep["passed"] is True
