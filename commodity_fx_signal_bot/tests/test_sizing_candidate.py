from sizing.sizing_candidate import (
    build_sizing_id,
    build_sizing_candidate_from_evaluation,
    sizing_candidate_to_dict,
)
import pandas as pd


def test_build_sizing_id():
    id1 = build_sizing_id("GC=F", "1d", "2023-01-01", "risk_1")
    id2 = build_sizing_id("GC=F", "1d", "2023-01-01", "risk_1")
    id3 = build_sizing_id("GC=F", "1d", "2023-01-01", "risk_2")

    assert id1 == id2
    assert id1 != id3


def test_build_sizing_candidate_from_evaluation():
    risk_row = pd.Series(
        {"risk_id": "r1", "risk_readiness_score": 0.8}, name="2023-01-01"
    )
    eval_ctx = {
        "theoretical_account_equity": 10000.0,
        "capped_theoretical_risk_amount": 100.0,
        "sizing_label": "sizing_approved_candidate",
        "combined_adjustment_factor": 1.0,
        "adjusted_theoretical_notional": 1000.0,
    }

    candidate = build_sizing_candidate_from_evaluation(risk_row, eval_ctx, "GC=F", "1d")

    assert candidate.symbol == "GC=F"
    assert candidate.sizing_label == "sizing_approved_candidate"
    assert candidate.sizing_readiness_score == 0.8

    d = sizing_candidate_to_dict(candidate)
    assert "symbol" in d
