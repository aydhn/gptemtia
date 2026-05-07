import pytest
import pandas as pd
from validation.overfitting_checks import (
    calculate_overfitting_risk_from_train_test,
    calculate_overfitting_risk_from_walk_forward,
    calculate_overfitting_risk_from_parameter_sensitivity,
    aggregate_overfitting_risk,
    build_overfitting_report
)

def test_calculate_overfitting_risk_from_train_test():
    good = calculate_overfitting_risk_from_train_test(
        {"sharpe_ratio": 1.5, "trade_count": 50, "win_rate": 0.5, "profit_factor": 1.5},
        {"sharpe_ratio": 1.2, "trade_count": 20}
    )
    assert good["risk_score"] < 0.5

    bad = calculate_overfitting_risk_from_train_test(
        {"sharpe_ratio": 3.0, "trade_count": 10, "win_rate": 0.9, "profit_factor": 1.1},
        {"sharpe_ratio": -0.5, "trade_count": 5}
    )
    assert bad["risk_score"] > good["risk_score"]

def test_calculate_overfitting_risk_from_walk_forward():
    df_stable = pd.DataFrame({
        "train_sharpe_ratio": [1.5, 1.5, 1.4],
        "test_sharpe_ratio": [1.2, 1.3, 1.1]
    })
    res_stable = calculate_overfitting_risk_from_walk_forward(df_stable)

    df_unstable = pd.DataFrame({
        "train_sharpe_ratio": [3.0, 3.1, 2.9],
        "test_sharpe_ratio": [1.0, -2.0, 2.5]
    })
    res_unstable = calculate_overfitting_risk_from_walk_forward(df_unstable)

    assert res_stable["risk_score"] < res_unstable["risk_score"]

def test_calculate_overfitting_risk_from_parameter_sensitivity():
    df_robust = pd.DataFrame({"fragility_warning": ["", "", ""]})
    res_robust = calculate_overfitting_risk_from_parameter_sensitivity(df_robust)
    assert res_robust["risk_score"] == 0.0

    df_fragile = pd.DataFrame({"fragility_warning": ["High variance", "", "High variance"]})
    res_fragile = calculate_overfitting_risk_from_parameter_sensitivity(df_fragile)
    assert res_fragile["risk_score"] == 1.0

def test_aggregate_overfitting_risk():
    res = aggregate_overfitting_risk([
        {"risk_score": 0.2},
        {"risk_score": 0.8},
        {"risk_score": 0.5}
    ])
    assert abs(res["aggregate_overfitting_risk_score"] - 0.71) < 0.01

def test_build_overfitting_report():
    train = {"sharpe_ratio": 2.0, "trade_count": 50}
    test = {"sharpe_ratio": -1.0, "trade_count": 20}

    report = build_overfitting_report(train_summary=train, test_summary=test)
    assert "aggregate_overfitting_risk_score" in report
    assert "overfitting_risk_label" in report
    assert report["overfitting_risk_label"] in ["moderate", "elevated", "high", "extreme"]
