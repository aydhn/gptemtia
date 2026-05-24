import pytest
import pandas as pd
from experiments.experiment_comparison import (
    compare_experiment_metrics,
    infer_comparison_label,
    compare_experiment_runs,
    build_experiment_comparison_table,
    summarize_experiment_comparisons
)

def test_compare_experiment_metrics():
    b = {"quality_adjusted_score": 0.5, "warning_count": 5}
    c = {"quality_adjusted_score": 0.8, "warning_count": 2}

    res = compare_experiment_metrics(b, c)
    assert res["deltas"]["quality_adjusted_score"] > 0
    assert res["deltas"]["warning_count"] < 0
    assert "quality_adjusted_score" in res["improved"]
    assert "warning_count" in res["improved"]

def test_infer_comparison_label():
    res1 = {"improved": ["a"], "deteriorated": [], "deltas": {}}
    assert infer_comparison_label(res1) == "candidate_better"

    res2 = {"improved": ["a"], "deteriorated": ["b"], "deltas": {"quality_adjusted_score": 0.1}}
    assert infer_comparison_label(res2) == "candidate_better"

def test_compare_experiment_runs():
    b_man = {"run_id": "b1", "metrics": {"quality_adjusted_score": 0.5}}
    c_man = {"run_id": "c1", "metrics": {"quality_adjusted_score": 0.8}}

    cmp = compare_experiment_runs(b_man, c_man)
    assert cmp.comparison_label == "candidate_better"
    assert "candidate_better" not in ["live_selection", "buy_signal"]

def test_build_experiment_comparison_table():
    cmp = compare_experiment_runs({"run_id":"b1", "metrics":{}}, {"run_id":"c1", "metrics":{}})
    df = build_experiment_comparison_table([cmp])
    assert len(df) == 1
    assert "comparison_label" in df.columns

def test_summarize_experiment_comparisons():
    df = pd.DataFrame([{"comparison_label": "candidate_better"}])
    summary = summarize_experiment_comparisons(df)
    assert summary["by_label"]["candidate_better"] == 1
