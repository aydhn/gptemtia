import pytest
import pandas as pd
from final_review.final_review_quality import (
    check_final_audit_tables_quality, check_risk_register_quality,
    check_gap_register_quality, check_acceptance_quality,
    check_for_forbidden_terms_in_final_review, build_final_review_quality_report
)

def test_quality_checks():
    assert check_final_audit_tables_quality({"t": pd.DataFrame()})["valid"]
    assert check_risk_register_quality(pd.DataFrame())["valid"]
    assert check_gap_register_quality(pd.DataFrame())["valid"]
    assert check_acceptance_quality(pd.DataFrame())["valid"]

def test_forbidden_terms():
    res = check_for_forbidden_terms_in_final_review(text="This is a live order")
    assert res["found"]

    res2 = check_for_forbidden_terms_in_final_review(text="Canlı emir yoktur")
    assert not res2["found"]

def test_build_quality_report():
    report = build_final_review_quality_report({}, {"t": pd.DataFrame()})
    assert report["passed"]
