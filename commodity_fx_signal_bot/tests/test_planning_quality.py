import pandas as pd
from research_planning.planning_quality import check_for_forbidden_trade_terms_in_planning, build_planning_quality_report
from research_planning.planning_config import get_default_research_planning_profile

def test_forbidden_terms():
    df = pd.DataFrame([{"text": "we should OPEN_LONG here"}])
    res = check_for_forbidden_trade_terms_in_planning(df=df)

    assert not res["passed"]
    assert "OPEN_LONG" in res["forbidden_terms_found"]

def test_no_forbidden_terms():
    df = pd.DataFrame([{"text": "we should run this experiment offline"}])
    res = check_for_forbidden_trade_terms_in_planning(df=df)

    assert res["passed"]
    assert len(res["forbidden_terms_found"]) == 0

def test_build_quality_report():
    df = pd.DataFrame([{"text": "safe"}])
    report = build_planning_quality_report({"key": "val"}, None, df, None)

    assert report["passed"]
    assert report["warning_count"] == 0
