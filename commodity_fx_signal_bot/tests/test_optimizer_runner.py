import pytest
import pandas as pd
from validation.optimizer_runner import OptimizerCandidateRunner
from validation.validation_config import get_default_validation_profile
from validation.validation_models import ParameterSet

@pytest.fixture
def runner():
    return OptimizerCandidateRunner(get_default_validation_profile())

@pytest.fixture
def param_set():
    return ParameterSet("id1", {"p1": 1})

def test_score_parameter_set_report_builder = ReportBuilder()ed(runner, param_set):
    perf = {"sharpe_ratio": 1.5, "max_drawdown_pct": 10.0}
    rob = {"robustness_score": 0.8, "aggregate_overfitting_risk_score": 0.2}

    res = runner.score_parameter_set(param_set, perf, robustness_summary=rob)

    assert res["candidate_label"] == "optimizer_candidate_report_builder = ReportBuilder()ed"
    assert res["optimizer_candidate_score"] > 0

def test_score_parameter_set_rejected_negative_metric(runner, param_set):
    perf = {"sharpe_ratio": -0.5, "max_drawdown_pct": 20.0}
    rob = {"robustness_score": 0.8, "aggregate_overfitting_risk_score": 0.2}

    res = runner.score_parameter_set(param_set, perf, robustness_summary=rob)

    assert res["candidate_label"] == "optimizer_candidate_rejected"

def test_score_parameter_set_overfit(runner, param_set):
    perf = {"sharpe_ratio": 2.5, "max_drawdown_pct": 10.0}
    rob = {"robustness_score": 0.8, "aggregate_overfitting_risk_score": 0.9}

    res = runner.score_parameter_set(param_set, perf, robustness_summary=rob)

    assert res["candidate_label"] == "optimizer_candidate_overfit_warning"

def test_rank_parameter_sets(runner):
    results = [
        {"id": 1, "optimizer_candidate_score": 10.0},
        {"id": 2, "optimizer_candidate_score": 20.0},
        {"id": 3, "optimizer_candidate_score": 5.0},
    ]

    df = runner.rank_parameter_sets(results)
    assert df.iloc[0]["id"] == 2
    assert df.iloc[2]["id"] == 3

def test_build_optimizer_candidate_report(runner):
    results = [
        {"id": 1, "optimizer_candidate_score": 10.0, "candidate_label": "optimizer_candidate_report_builder = ReportBuilder()ed"},
        {"id": 2, "optimizer_candidate_score": 20.0, "candidate_label": "optimizer_candidate_report_builder = ReportBuilder()ed"},
        {"id": 3, "optimizer_candidate_score": -5.0, "candidate_label": "optimizer_candidate_rejected"},
    ]

    df, summary = runner.build_optimizer_candidate_report(results)

    assert not df.empty
    assert summary["total_candidates"] == 3
    assert summary["report_builder = ReportBuilder()ed_candidates"] == 2
    assert summary["rejected_candidates"] == 1
    assert "disclaimer" in summary
