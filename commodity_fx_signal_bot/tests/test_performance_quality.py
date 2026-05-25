import pytest
import pandas as pd
from performance.performance_config import get_default_performance_profile
from performance.performance_quality import (
    check_runtime_profile_quality,
    check_memory_profile_quality,
    check_resource_budget_quality,
    check_for_forbidden_terms_in_performance,
    build_performance_quality_report
)

def test_check_runtime_profile_quality():
    profile = get_default_performance_profile()
    df = pd.DataFrame([{"duration_seconds": 1.0, "exit_code": 0, "timed_out": False}])
    res = check_runtime_profile_quality(df, profile)
    assert res["passed"]

    df_fail = pd.DataFrame([{"duration_seconds": 1.0, "exit_code": 1, "timed_out": False}])
    res_fail = check_runtime_profile_quality(df_fail, profile)
    assert not res_fail["passed"]

def test_check_memory_profile_quality():
    profile = get_default_performance_profile()
    df = pd.DataFrame([{"peak_memory_mb": 100.0, "budget_status": "within_budget"}])
    res = check_memory_profile_quality(df, profile)
    assert res["passed"]

    df_fail = pd.DataFrame([{"peak_memory_mb": 100.0, "budget_status": "over_budget"}])
    res_fail = check_memory_profile_quality(df_fail, profile)
    assert not res_fail["passed"]

def test_check_resource_budget_quality():
    df = pd.DataFrame([{"max_parallel_workers": 1}])
    res = check_resource_budget_quality(df)
    assert res["passed"]

def test_check_for_forbidden_terms():
    res = check_for_forbidden_terms_in_performance(text="This has a live order.")
    assert not res["passed"]
    assert "live order" in res["warnings"][0]

    # Check negation
    res2 = check_for_forbidden_terms_in_performance(text="This system produces no live order.")
    assert res2["passed"]

def test_build_performance_quality_report():
    profile = get_default_performance_profile()
    r_df = pd.DataFrame([{"duration_seconds": 1.0, "exit_code": 0, "timed_out": False}])
    m_df = pd.DataFrame([{"peak_memory_mb": 100.0, "budget_status": "within_budget"}])
    b_df = pd.DataFrame([{"max_parallel_workers": 1}])

    report = build_performance_quality_report({"dummy": "ok"}, r_df, m_df, b_df, profile)
    assert report["passed"]
    assert report["runtime_profiles_valid"]
    assert report["memory_profiles_valid"]

