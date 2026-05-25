import pytest
import pandas as pd
from performance.memory_profiler import (
    get_current_process_memory_mb,
    estimate_dataframe_memory_mb,
    build_memory_profile_table,
    classify_memory_budget_status,
    summarize_memory_profiles,
    profile_function_memory
)

def test_get_current_process_memory():
    mem = get_current_process_memory_mb()
    if mem is not None:
        assert mem > 0

def test_estimate_dataframe_memory():
    df = pd.DataFrame({"A": range(1000), "B": ["test"] * 1000})
    mem = estimate_dataframe_memory_mb(df)
    assert mem > 0

def test_build_memory_profile_table():
    df = pd.DataFrame({"A": range(100)})
    table = build_memory_profile_table({"test_df": df})
    assert not table.empty
    assert "estimated_memory_mb" in table.columns

def test_classify_memory_budget_status():
    assert classify_memory_budget_status(1500, 2048) == "within_budget"
    assert classify_memory_budget_status(1800, 2048) == "near_budget_limit"
    assert classify_memory_budget_status(2500, 2048) == "over_budget"
    assert classify_memory_budget_status(None, 2048) == "budget_unknown"

def dummy_func():
    return sum(range(1000))

def test_profile_function_memory():
    # Mock datetime to avoid import issues inside the function for this test
    import builtins
    from datetime import datetime, timezone
    setattr(builtins, 'datetime', datetime)
    setattr(builtins, 'timezone', timezone)

    result, record = profile_function_memory(dummy_func, "dummy", "mod", 1024)
    assert result == sum(range(1000))
    assert record.peak_memory_mb is not None
    assert record.budget_status == "within_budget"
