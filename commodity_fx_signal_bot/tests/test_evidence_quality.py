import pytest
import pandas as pd
from evidence_governance.evidence_config import get_default_evidence_governance_profile
from evidence_governance.evidence_quality import (
    check_artifact_inventory_quality,
    check_for_forbidden_terms_in_evidence,
    build_evidence_quality_report
)

def test_evidence_quality():
    profile = get_default_evidence_governance_profile()

    res = check_artifact_inventory_quality(pd.DataFrame([1]), profile)
    assert res["passed"] is True

    res = check_for_forbidden_terms_in_evidence("investment advice")
    assert res["passed"] is False

    res = check_for_forbidden_terms_in_evidence("yatırım tavsiyesi değildir")
    # depending on implementation detail this might hit as "yatırım tavsiyesidir" is the forbidden one, let's check exact matches
    assert res["passed"] is True # 'yatırım tavsiyesidir' != 'yatırım tavsiyesi değildir'

    report = build_evidence_quality_report({"dummy": "summary"}, pd.DataFrame([1]), pd.DataFrame([1]), pd.DataFrame([1]))
    assert "passed" in report
