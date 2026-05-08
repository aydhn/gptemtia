import pandas as pd
from decisions.decision_quality import (
    check_decision_score_ranges,
    check_decision_duplicates,
    check_for_forbidden_trade_terms,
    build_decision_quality_report,
)


def test_check_score_ranges():
    df = pd.DataFrame({"decision_score": [0.5, 1.5, -0.1]})
    res = check_decision_score_ranges(df)
    assert res["invalid_score_count"] == 2


def test_check_duplicates():
    df = pd.DataFrame({"decision_id": ["A", "B", "A"]})
    res = check_decision_duplicates(df)
    assert res["duplicate_decision_count"] == 1


def test_forbidden_terms():
    df = pd.DataFrame({"notes": ["this is a BUY signal", "ok"]})
    res = check_for_forbidden_trade_terms(df)
    assert len(res["forbidden_trade_terms_found"]) > 0


def test_quality_report():
    df = pd.DataFrame(
        {
            "symbol": ["A"],
            "timeframe": ["1d"],
            "decision_id": ["1"],
            "decision_label": ["x"],
            "directional_bias": ["y"],
            "decision_score": [0.5],
            "decision_confidence": [0.5],
            "strategy_readiness_score": [0.5],
        }
    )
    rep = build_decision_quality_report(df, {"report_builder = ReportBuilder()ed_decisions": 1})
    assert rep["report_builder = ReportBuilder()ed"] is True
