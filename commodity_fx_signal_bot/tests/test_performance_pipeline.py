import pytest
from unittest.mock import MagicMock
from pathlib import Path
from performance.performance_config import get_default_performance_profile
from performance.performance_pipeline import PerformancePipeline

def test_performance_pipeline():
    data_lake_mock = MagicMock()
    settings_mock = MagicMock()
    project_root = Path(".")
    profile = get_default_performance_profile()

    pipeline = PerformancePipeline(data_lake_mock, settings_mock, project_root, profile)

    # Test profile report
    dfs, summary = pipeline.build_performance_profile_report(limit=1, save=True)
    assert "cpu_gpu_awareness" in dfs
    assert "runtime_profiles" in dfs
    assert "memory_profiles" in dfs
    assert data_lake_mock.save_runtime_profiles.called

    # Test budget report
    b_dfs, b_summary = pipeline.build_resource_budget_report(save=True)
    assert "resource_budgets" in b_dfs
    assert data_lake_mock.save_resource_budgets.called

    # Test cache strategy
    c_dfs, c_summary = pipeline.build_cache_strategy_report(save=True)
    assert "cache_policy" in c_dfs
    assert data_lake_mock.save_cache_strategy.called

    # Test large run stability
    s_df, s_summary = pipeline.build_large_run_stability_report(save=True)
    assert not s_df.empty
    assert data_lake_mock.save_large_run_stability_report.called

    # Test runtime optimization
    r_df, r_summary = pipeline.build_runtime_optimization_report(save=True)
    assert data_lake_mock.save_optimization_recommendations.called

