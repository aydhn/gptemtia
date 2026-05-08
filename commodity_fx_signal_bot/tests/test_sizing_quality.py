import pandas as pd
from sizing.sizing_quality import (
    check_sizing_score_ranges,
    check_sizing_candidate_duplicates,
    check_for_forbidden_trade_terms_in_sizing,
    build_sizing_quality_report,
)


def test_check_sizing_score_ranges():
    df = pd.DataFrame({"sizing_readiness_score": [0.5, 1.5, -0.5]})
    res = check_sizing_score_ranges(df)
    assert not res["report_builder = ReportBuilder()ed"]
    assert res["invalid_score_count"] == 2


def test_check_sizing_candidate_duplicates():
    df = pd.DataFrame({"sizing_id": ["a", "b", "a"], "timestamp": ["1", "2", "3"]})
    res = check_sizing_candidate_duplicates(df)
    assert not res["report_builder = ReportBuilder()ed"]
    assert res["duplicate_sizing_count"] == 1


def test_check_for_forbidden_trade_terms_in_sizing():
    df = pd.DataFrame({"notes": ["good", "we OPEN_LONG here", "safe"]})
    res = check_for_forbidden_trade_terms_in_sizing(df)
    assert not res["report_builder = ReportBuilder()ed"]
    assert len(res["forbidden_trade_terms_found"]) > 0


def test_build_sizing_quality_report():
    df = pd.DataFrame(
        {
            "sizing_id": ["a"],
            "symbol": ["GC=F"],
            "timeframe": ["1d"],
            "sizing_label": ["sizing_approved_candidate"],
            "adjusted_theoretical_units": [50.0],
            "sizing_readiness_score": [0.9],
        }
    )
    report = build_sizing_quality_report(df, {})
    assert report["report_builder = ReportBuilder()ed"] is True
