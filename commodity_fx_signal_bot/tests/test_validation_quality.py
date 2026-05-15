import pytest
import pandas as pd
from validation.validation_quality import (
    check_validation_input_integrity,
    check_split_coverage,
    check_walk_forward_result_quality,
    check_parameter_result_quality,
    check_for_forbidden_live_terms_in_validation,
    build_validation_quality_report
)
from validation.validation_models import TimeSplit

def test_check_validation_input_integrity():
    res_empty = check_validation_input_integrity(None, None, None)
    assert res_empty["passed"] is False
    assert len(res_empty["warnings"]) >= 3

    idx = pd.date_range("2020-01-01", periods=5)
    df = pd.DataFrame({"close": [1,2,3,4,5]}, index=idx)
    res_valid = check_validation_input_integrity(df, df, df)
    assert res_valid["passed"] is True

def test_check_split_coverage():
    res_empty = check_split_coverage([])
    assert res_empty["passed"] is False

    split = TimeSplit("1", "start", "end", "tstart", "tend", 10, 10, 0)
    res_one = check_split_coverage([split])
    assert res_one["passed"] is True
    assert len(res_one["warnings"]) == 1 # only 1 split

def test_check_walk_forward_result_quality():
    res_empty = check_walk_forward_result_quality(pd.DataFrame())
    assert res_empty["passed"] is False

    df_valid = pd.DataFrame({"split_id": [1], "train_sharpe_ratio": [1], "test_sharpe_ratio": [1]})
    res_valid = check_walk_forward_result_quality(df_valid)
    assert res_valid["passed"] is True

def test_check_for_forbidden_live_terms():
    df_clean = pd.DataFrame({"col1": ["safe", "text"]})
    res_clean = check_for_forbidden_live_terms_in_validation(df=df_clean)
    assert res_clean["passed"] is True

    df_dirty = pd.DataFrame({"col1": ["some", "REAL_POSITION", "text"]})
    res_dirty = check_for_forbidden_live_terms_in_validation(df=df_dirty)
    assert res_dirty["passed"] is False
    assert len(res_dirty["warnings"]) > 0

    summary_dirty = {"msg": "EXECUTE_TRADE now"}
    res_sum = check_for_forbidden_live_terms_in_validation(summary=summary_dirty)
    assert res_sum["passed"] is False

def test_build_validation_quality_report():
    summary = {
        "input": {"passed": True, "warnings": []},
        "walk_forward": {"passed": False, "warnings": ["missing column"]},
        "forbidden_terms": {"passed": True, "warnings": []}
    }

    report = build_validation_quality_report(summary)
    assert report["passed"] is False
    assert report["walk_forward_quality_passed"] is False
    assert report["forbidden_live_terms_found"] is False # passed = True means not found
    assert report["warning_count"] == 1
