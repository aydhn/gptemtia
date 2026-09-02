import pytest
from local_performance.performance_config import validate_local_performance_profiles, get_default_local_performance_profile, get_local_performance_profile, ConfigError

def test_validate_local_performance_profiles():
    validate_local_performance_profiles()

def test_get_default_local_performance_profile():
    p = get_default_local_performance_profile()
    assert p.name == "balanced_local_performance"
    assert p.language != ""
    assert p.default_memory_budget_mb > 0
    assert p.default_disk_budget_mb > 0
    assert p.default_runtime_budget_minutes > 0
    assert p.max_items > 0
    assert 0 <= p.min_readiness_score <= 1
    assert p.dry_run_default is True
    assert p.allow_real_benchmark is False
    assert p.allow_production_capacity_claim is False

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_local_performance_profile("unknown")
