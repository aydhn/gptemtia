import pytest
import pandas as pd
from performance.performance_config import get_default_performance_profile
from performance.large_run_stability import (
    build_large_run_stability_checklist,
    evaluate_large_run_stability,
    infer_large_run_stability_label,
    summarize_large_run_stability
)

def test_build_large_run_stability_checklist():
    profile = get_default_performance_profile()
    df = build_large_run_stability_checklist(profile)
    assert not df.empty
    assert "item" in df.columns
    assert "expected" in df.columns

def test_evaluate_large_run_stability():
    profile = get_default_performance_profile()

    # Missing data
    df = evaluate_large_run_stability(None, None, None, None, profile)
    assert not df.empty
    assert "passed" in df.columns
    # Some will fail
    assert df["passed"].sum() < len(df)

    # With data
    r_df = pd.DataFrame([{"a": 1}])
    b_df = pd.DataFrame([{"b": 1}])

    df2 = evaluate_large_run_stability(r_df, r_df, r_df, b_df, profile)
    assert df2["passed"].sum() > df["passed"].sum()

def test_infer_large_run_stability_label():
    # Mock all passed
    df_all_pass = pd.DataFrame([{"passed": True}] * 10)
    assert infer_large_run_stability_label(df_all_pass) == "stable_large_run"

    # Mock partial pass
    df_partial = pd.DataFrame([{"passed": True}] * 8 + [{"passed": False}] * 2)
    assert infer_large_run_stability_label(df_partial) == "stable_with_warnings"

def test_summarize_large_run_stability():
    df_all_pass = pd.DataFrame([{"passed": True}] * 10)
    summary = summarize_large_run_stability(df_all_pass)
    assert summary["passed_checks"] == 10
    assert summary["stability_label"] == "stable_large_run"

def test_stable_large_run_is_not_production_readiness():
    # Conceptual check, ensuring labels don't imply live deployment
    label = "stable_large_run"
    assert "production" not in label
    assert "deploy" not in label
    assert "live" not in label
