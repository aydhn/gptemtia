import pandas as pd
from synthetic_indices.index_config import get_default_synthetic_index_profile
from synthetic_indices.index_models import SyntheticIndexDefinition
from synthetic_indices.index_quality import (
    check_index_definition_quality,
    check_for_forbidden_trade_terms_in_synthetic_indices,
    build_synthetic_index_quality_report
)

def test_index_quality():
    profile = get_default_synthetic_index_profile()

    # Valid definition
    def1 = SyntheticIndexDefinition(
        index_id="1", index_name="1", index_type="custom", timeframe="1d",
        symbols=["A", "B", "C", "D"], weights={"A": 0.25, "B": 0.25, "C": 0.25, "D": 0.25},
        weighting_scheme="equal", base_value=100.0, created_at_utc="", methodology="", warnings=[]
    )
    res = check_index_definition_quality(def1, profile)
    assert res["passed"]

    # Invalid definition (too few symbols)
    def2 = SyntheticIndexDefinition(
        index_id="2", index_name="2", index_type="custom", timeframe="1d",
        symbols=["A"], weights={"A": 1.0},
        weighting_scheme="equal", base_value=100.0, created_at_utc="", methodology="", warnings=[]
    )
    res2 = check_index_definition_quality(def2, profile)
    assert not res2["passed"]

def test_forbidden_terms():
    res = check_for_forbidden_trade_terms_in_synthetic_indices(text="We should BUY this asset.")
    assert not res["passed"]
    assert "BUY" in res["forbidden_trade_terms_found"]

    res2 = check_for_forbidden_trade_terms_in_synthetic_indices(text="This is a strong leader in relative strength.")
    assert res2["passed"]

def test_build_quality_report():
    summary = {"info": "Test BUY"} # contains forbidden term
    quality = build_synthetic_index_quality_report(summary=summary)
    assert not quality["passed"]
    assert "BUY" in quality["forbidden_trade_terms_found"]
