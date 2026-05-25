import pytest
import pandas as pd
from performance.performance_config import get_default_performance_profile
from performance.batch_planner import (
    calculate_safe_batch_size,
    build_symbol_batch_plan,
    build_module_batch_plans,
    estimate_batch_runtime_seconds
)

def test_calculate_safe_batch_size():
    profile = get_default_performance_profile()

    # Normal case
    size = calculate_safe_batch_size(100, profile)
    assert size > 0
    assert size <= profile.max_batch_symbols

    # Memory constrained case
    size_mem = calculate_safe_batch_size(100, profile, item_cost_estimate_mb=1024) # 1 item = 1GB, limit is 2GB
    assert size_mem == 2

def test_build_symbol_batch_plan():
    profile = get_default_performance_profile()
    symbols = ["AAPL", "MSFT", "GOOG"]
    plan = build_symbol_batch_plan(symbols, "test_mod", profile)

    assert plan.total_items == 3
    assert plan.batch_count == 1
    assert plan.max_parallel_workers == 1

def test_build_module_batch_plans():
    profile = get_default_performance_profile()
    modules = {
        "mod1": ["A", "B"],
        "mod2": ["C"] * 100
    }

    df, summary = build_module_batch_plans(modules, profile)
    assert len(df) == 2
    assert summary["total_plans"] == 2
    assert summary["total_batches"] > 1

def test_estimate_batch_runtime():
    assert estimate_batch_runtime_seconds(5, 10.0) == 50.0
    assert estimate_batch_runtime_seconds(5, None) is None
