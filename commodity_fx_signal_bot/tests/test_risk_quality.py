import pandas as pd
from risk.risk_quality import (
    check_risk_score_ranges,
    check_risk_candidate_duplicates,
    check_for_forbidden_order_terms_in_risk,
    build_risk_quality_report,
)


def test_check_risk_score_ranges():
    df = pd.DataFrame([{"total_pretrade_risk_score": 1.5}])
    res = check_risk_score_ranges(df)
    assert res["invalid_score_count"] == 1


def test_check_risk_candidate_duplicates():
    df = pd.DataFrame([{"risk_id": "1"}, {"risk_id": "1"}])
    res = check_risk_candidate_duplicates(df)
    assert res["duplicate_risk_count"] == 1


def test_check_forbidden_terms():
    df = pd.DataFrame([{"notes": "We should BUY this immediately."}])
    res = check_for_forbidden_order_terms_in_risk(df)
    assert res["forbidden_order_terms_found"]
    assert "BUY" in res["found_terms"]


def test_build_risk_quality_report():
    df = pd.DataFrame(
        [
            {
                "symbol": "AAPL",
                "timeframe": "1d",
                "risk_id": "1",
                "risk_label": "approval",
                "total_pretrade_risk_score": 0.5,
                "warnings": [],
            }
        ]
    )
    res = build_risk_quality_report(df, {"report_builder = ReportBuilder()ed_risk_candidates": 1})
    assert res["report_builder = ReportBuilder()ed"]
