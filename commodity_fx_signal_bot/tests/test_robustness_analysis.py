import pytest
import pandas as pd
from validation.robustness_analysis import (
    calculate_train_test_degradation,
    calculate_split_consistency,
    calculate_positive_split_ratio,
    calculate_metric_variability,
    calculate_robustness_score,
    build_robustness_report
)

def test_calculate_train_test_degradation():
    assert round(calculate_train_test_degradation(1.0, 0.8), 2) == 0.2
    assert round(calculate_train_test_degradation(1.0, 1.2), 2) == 0.0
    assert round(calculate_train_test_degradation(1.0, -0.5), 2) == 1.0
    assert round(calculate_train_test_degradation(-0.5, 0.5), 2) == 0.0
    assert round(calculate_train_test_degradation(-0.5, -0.8), 2) == 1.0

def test_calculate_split_consistency():
    df_consistent = pd.DataFrame({"test_sharpe_ratio": [1.0, 1.1, 0.9, 1.0]})
    score_c = calculate_split_consistency(df_consistent)
    assert score_c > 0.8

    df_inconsistent = pd.DataFrame({"test_sharpe_ratio": [2.0, -1.0, 3.0, -2.0]})
    score_i = calculate_split_consistency(df_inconsistent)
    assert score_i < score_c

def test_calculate_positive_split_ratio():
    df = pd.DataFrame({"test_total_return_pct": [1.0, -1.0, 2.0, 3.0]})
    assert calculate_positive_split_ratio(df) == 0.75

def test_calculate_robustness_score():
    df = pd.DataFrame({
        "train_sharpe_ratio": [1.5, 1.5, 1.5],
        "test_sharpe_ratio": [1.2, 1.0, 1.1],
        "test_total_return_pct": [5.0, 3.0, 4.0]
    })

    res = calculate_robustness_score(df)
    assert "robustness_score" in res
    assert 0.0 <= res["robustness_score"] <= 1.0
    assert res["components"]["positive_ratio"] == 1.0

def test_build_robustness_report():
    df = pd.DataFrame({
        "train_sharpe_ratio": [1.5, 1.5],
        "test_sharpe_ratio": [1.2, -1.0],
        "test_total_return_pct": [5.0, -3.0]
    })

    report = build_robustness_report(df)
    assert "warnings" in report
    assert len(report["warnings"]) > 0
