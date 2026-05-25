import pytest
import pandas as pd
from performance.performance_config import get_default_performance_profile
from performance.resource_budget import (
    build_default_resource_budgets,
    resource_budgets_to_dataframe,
    check_runtime_against_budget,
    check_memory_against_budget,
    build_resource_budget_violation_report,
    summarize_resource_budgets
)

def test_build_default_resource_budgets():
    profile = get_default_performance_profile()
    budgets = build_default_resource_budgets(profile)
    assert len(budgets) > 0
    assert budgets[0].max_parallel_workers == 1

def test_resource_budgets_to_dataframe():
    profile = get_default_performance_profile()
    budgets = build_default_resource_budgets(profile)
    df = resource_budgets_to_dataframe(budgets)
    assert not df.empty
    assert "module_name" in df.columns

def test_budget_checks():
    profile = get_default_performance_profile()
    budgets = build_default_resource_budgets(profile)
    b_df = resource_budgets_to_dataframe(budgets)

    r_df = pd.DataFrame([{"module_name": "performance", "duration_seconds": profile.max_runtime_seconds_per_script + 10}])
    v_df = check_runtime_against_budget(r_df, b_df)
    assert not v_df.empty

    m_df = pd.DataFrame([{"module_name": "performance", "peak_memory_mb": profile.max_memory_mb_per_script + 10}])
    m_v_df = check_memory_against_budget(m_df, b_df)
    assert not m_v_df.empty

def test_violation_report():
    profile = get_default_performance_profile()
    budgets = build_default_resource_budgets(profile)
    b_df = resource_budgets_to_dataframe(budgets)

    r_df = pd.DataFrame([{"module_name": "performance", "duration_seconds": profile.max_runtime_seconds_per_script + 10}])
    m_df = pd.DataFrame([{"module_name": "performance", "peak_memory_mb": profile.max_memory_mb_per_script + 10}])

    v_df, summary = build_resource_budget_violation_report(r_df, m_df, b_df)
    assert len(v_df) == 2
    assert summary["total_violations"] == 2
