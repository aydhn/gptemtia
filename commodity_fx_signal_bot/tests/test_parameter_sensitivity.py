import pytest
import pandas as pd
from validation.parameter_sensitivity import (
    build_parameter_result_table,
    calculate_parameter_sensitivity,
    calculate_metric_stability_across_parameters,
    identify_fragile_parameters,
    build_parameter_sensitivity_report
)

@pytest.fixture
def sample_results():
    return [
        {"parameters": {"p1": 1, "p2": "a"}, "test_summary": {"sharpe_ratio": 1.5, "total_return_pct": 10.0}},
        {"parameters": {"p1": 1, "p2": "b"}, "test_summary": {"sharpe_ratio": 1.2, "total_return_pct": 8.0}},
        {"parameters": {"p1": 2, "p2": "a"}, "test_summary": {"sharpe_ratio": -0.5, "total_return_pct": -2.0}},
        {"parameters": {"p1": 2, "p2": "b"}, "test_summary": {"sharpe_ratio": -1.0, "total_return_pct": -5.0}},
    ]

def test_build_parameter_result_table(sample_results):
    df = build_parameter_result_table(sample_results)
    assert not df.empty
    assert len(df) == 4
    assert "param_p1" in df.columns
    assert "test_sharpe_ratio" in df.columns

def test_calculate_parameter_sensitivity(sample_results):
    df = build_parameter_result_table(sample_results)
    sens_df = calculate_parameter_sensitivity(df, metric="test_sharpe_ratio")

    assert not sens_df.empty
    assert "parameter_name" in sens_df.columns
    assert "metric_mean" in sens_df.columns
    assert len(sens_df) == 4 # 2 for p1, 2 for p2

def test_calculate_metric_stability(sample_results):
    df = build_parameter_result_table(sample_results)
    stability = calculate_metric_stability_across_parameters(df, metric="test_sharpe_ratio")

    assert "stability_score" in stability
    assert "is_stable" in stability
    assert stability["positive_ratio"] == 0.5

def test_identify_fragile_parameters(sample_results):
    df = build_parameter_result_table(sample_results)
    fragile = identify_fragile_parameters(df, metric="test_sharpe_ratio")
    assert fragile.empty

def test_build_parameter_sensitivity_report(sample_results):
    df = build_parameter_result_table(sample_results)
    sens_df, summary = build_parameter_sensitivity_report(df, primary_metric="test_sharpe_ratio")

    assert not sens_df.empty
    assert "combinations_tested" in summary
    assert summary["combinations_tested"] == 4
