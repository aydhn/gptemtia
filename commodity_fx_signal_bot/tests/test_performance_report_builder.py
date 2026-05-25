import pytest
import pandas as pd
from performance.performance_report_builder import (
    build_performance_disclaimer,
    build_performance_profile_markdown_report,
    build_resource_budget_markdown_report,
    build_cache_strategy_markdown_report,
    build_large_run_stability_markdown_report,
    build_runtime_optimization_markdown_report
)

def test_build_performance_disclaimer():
    disc = build_performance_disclaimer()
    assert "offline performance profiling/resource budgeting raporudur" in disc
    assert "yatırım tavsiyesi değildir" in disc

def test_build_performance_profile_markdown_report():
    summary = {"test": 1}
    df = pd.DataFrame([{"a": 1}])
    md = build_performance_profile_markdown_report(summary, df, df)
    assert "test" in md
    assert "Runtime Profiles" in md
    assert "Memory Profiles" in md

def test_build_resource_budget_markdown_report():
    summary = {"test": 1}
    df = pd.DataFrame([{"a": 1}])
    md = build_resource_budget_markdown_report(summary, df, df)
    assert "test" in md
    assert "Defined Budgets" in md
    assert "Budget Violations" in md

def test_build_cache_strategy_markdown_report():
    summary = {"test": 1}
    df = pd.DataFrame([{"a": 1}])
    md = build_cache_strategy_markdown_report(summary, df, df)
    assert "Cache Policies" in md
    assert "Tracked Caches" in md

def test_build_large_run_stability_markdown_report():
    summary = {"test": 1}
    df = pd.DataFrame([{"a": 1}])
    md = build_large_run_stability_markdown_report(summary, df)
    assert "Stability Checklist" in md

def test_build_runtime_optimization_markdown_report():
    summary = {"test": 1}
    df = pd.DataFrame([{"a": 1}])
    md = build_runtime_optimization_markdown_report(summary, df)
    assert "Safe Optimization Recommendations" in md
