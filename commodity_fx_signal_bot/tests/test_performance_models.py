import pytest
from performance.performance_models import (
    RuntimeProfileRecord,
    MemoryProfileRecord,
    ResourceBudget,
    CacheRecord,
    BatchPlan,
    build_runtime_profile_id,
    build_resource_budget_id,
    build_cache_id,
    build_batch_plan_id,
    runtime_profile_record_to_dict,
    memory_profile_record_to_dict,
    resource_budget_to_dict,
    cache_record_to_dict,
    batch_plan_to_dict,
    sanitize_command_for_profile
)

def test_id_builders_deterministic():
    assert build_runtime_profile_id("test", "2023-01-01") == build_runtime_profile_id("test", "2023-01-01")
    assert build_resource_budget_id("mod", "prof") == build_resource_budget_id("mod", "prof")
    assert build_cache_id("key", "type") == build_cache_id("key", "type")
    assert build_batch_plan_id("plan", "mod") == build_batch_plan_id("plan", "mod")

def test_dataclass_to_dict():
    budget = ResourceBudget(
        budget_id="b1",
        module_name="mod",
        max_runtime_seconds=100,
        max_memory_mb=1024,
        max_batch_symbols=10,
        max_parallel_workers=1,
        cache_enabled=True,
        checkpointing_enabled=True,
        warnings=[]
    )
    d = resource_budget_to_dict(budget)
    assert d["budget_id"] == "b1"
    assert "max_runtime_seconds" in d

def test_sanitize_command():
    cmd = "python   -m   scripts.test   "
    assert sanitize_command_for_profile(cmd) == "python -m scripts.test"
