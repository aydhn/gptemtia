import pytest
import pandas as pd
from experiments.experiment_metrics import (
    extract_metrics_from_meta_research,
    extract_metrics_from_factor_research,
    extract_metrics_from_portfolio_research,
    extract_metrics_from_validation,
    extract_metrics_from_paper,
    normalize_experiment_metrics,
    build_experiment_metric_table,
    summarize_experiment_metrics
)

def test_extract_meta_metrics():
    report = {"summary": {"mean_quality_score": 0.8, "warning_count": 2}}
    metrics = extract_metrics_from_meta_research(report)
    assert metrics["quality_adjusted_score"] == 0.8
    assert metrics["warning_count"] == 2

def test_extract_factor_metrics():
    metrics = extract_metrics_from_factor_research({"mean_ic": 0.1})
    assert metrics["factor_ic_proxy"] == 0.1

def test_extract_portfolio_paper_validation():
    p = extract_metrics_from_portfolio_research({"diversification_score": 0.5})
    assert p["portfolio_diversification_score"] == 0.5

    v = extract_metrics_from_validation({"mean_validation_score": 0.9})
    assert v["validation_score"] == 0.9

    pap = extract_metrics_from_paper({"virtual_return": 0.05})
    assert pap["paper_virtual_return"] == 0.05

def test_normalize_experiment_metrics():
    metrics = {"quality_adjusted_score": 0.8, "custom_metric": 10.0, "string_val": "hello"}
    norm = normalize_experiment_metrics(metrics)
    assert "quality_adjusted_score" in norm
    assert "custom_metric" in norm
    assert "string_val" not in norm

def test_build_experiment_metric_table():
    manifests = [
        {"run_id": "r1", "metrics": {"quality_adjusted_score": 0.8}},
        {"run_id": "r2", "metrics": {"quality_adjusted_score": 0.9}}
    ]
    df = build_experiment_metric_table(manifests)
    assert len(df) == 2
    assert "quality_adjusted_score" in df.columns

def test_summarize_experiment_metrics():
    df = pd.DataFrame([{"run_id": "r1", "score": 1.0}, {"run_id": "r2", "score": 2.0}])
    s = summarize_experiment_metrics(df)
    assert s["mean_score"] == 1.5
