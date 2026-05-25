import pytest
import pandas as pd
from datetime import datetime, timezone, timedelta
from performance.performance_config import get_default_performance_profile
from performance.cache_strategy import (
    should_use_cache,
    is_cache_stale,
    build_cache_policy_table,
    build_cache_invalidation_plan,
    summarize_cache_strategy
)

def test_is_cache_stale():
    now = datetime.now(timezone.utc)
    old = (now - timedelta(hours=25)).isoformat()
    recent = (now - timedelta(hours=1)).isoformat()

    assert is_cache_stale({"created_at_utc": old}, 24) == True
    assert is_cache_stale({"created_at_utc": recent}, 24) == False

def test_should_use_cache():
    profile = get_default_performance_profile()

    # Missing record
    res, info = should_use_cache(None, profile)
    assert not res

    # Good record
    now = datetime.now(timezone.utc).isoformat()
    record = {"status": "valid", "created_at_utc": now, "size_bytes": 1024}
    res, info = should_use_cache(record, profile)
    assert res

    # Over size limits
    large_record = {"status": "valid", "created_at_utc": now, "size_bytes": profile.cache_max_size_mb * 1024 * 1024 + 10}
    res, info = should_use_cache(large_record, profile)
    assert not res

def test_build_cache_policy_table():
    profile = get_default_performance_profile()
    df = build_cache_policy_table(profile)
    assert not df.empty
    assert "module_name" in df.columns

def test_build_cache_invalidation_plan():
    profile = get_default_performance_profile()
    old = (datetime.now(timezone.utc) - timedelta(hours=25)).isoformat()

    cache_df = pd.DataFrame([
        {"cache_id": "1", "created_at_utc": old, "status": "valid"},
        {"cache_id": "2", "created_at_utc": datetime.now(timezone.utc).isoformat(), "status": "invalid"}
    ])

    plan, summary = build_cache_invalidation_plan(cache_df, profile)
    assert not plan.empty
    assert len(plan) == 2
    assert summary["total_to_invalidate"] == 2

def test_summarize_cache_strategy():
    profile = get_default_performance_profile()
    df = build_cache_policy_table(profile)
    summary = summarize_cache_strategy(df)
    assert "total_policies" in summary
