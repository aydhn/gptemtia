import pandas as pd

from strategies.strategy_quality import (
    check_for_forbidden_order_terms,
    check_strategy_duplicates,
    check_strategy_score_ranges,
)


def test_check_strategy_score_ranges():
    df = pd.DataFrame({"strategy_selection_score": [1.5, 0.5]})
    res = check_strategy_score_ranges(df)
    assert res["invalid_score_count"] == 1


def test_check_strategy_duplicates():
    df = pd.DataFrame({"strategy_id": ["1", "1", "2"]})
    res = check_strategy_duplicates(df)
    assert res["duplicate_strategy_count"] == 1


def test_check_for_forbidden_order_terms():
    df = pd.DataFrame({"directional_bias": ["neutral", "BUY", "long_bias"]})
    res = check_for_forbidden_order_terms(df)
    assert res["forbidden_order_terms_found"] is True
    assert "buy" in res["terms_found"]
