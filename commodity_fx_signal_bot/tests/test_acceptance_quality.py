from local_acceptance.acceptance_quality import build_acceptance_quality_report

def test_build_acceptance_quality_report():
    res = build_acceptance_quality_report({})
    assert res["passed"] is True
