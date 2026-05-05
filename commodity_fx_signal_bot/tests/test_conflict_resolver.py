import pandas as pd
from decisions.conflict_resolver import (
    detect_signal_direction_conflict,
    aggregate_decision_conflicts,
)


def test_signal_direction_conflict():
    df = pd.DataFrame({"signal_direction": ["bullish", "bearish"]})
    res = detect_signal_direction_conflict(df)
    assert res["blocking_conflict"] == False


def test_aggregate_decision_conflicts():
    c1 = {
        "conflict_score": 0.5,
        "conflict_reasons": ["A"],
        "blocking_conflict": False,
        "warnings": [],
    }
    c2 = {
        "conflict_score": 0.8,
        "conflict_reasons": ["B"],
        "blocking_conflict": True,
        "warnings": [],
    }
    res = aggregate_decision_conflicts([c1, c2])
    assert res["conflict_score"] == 0.8
    assert res["blocking_conflict"] == True
    assert set(res["conflict_reasons"]) == {"A", "B"}
