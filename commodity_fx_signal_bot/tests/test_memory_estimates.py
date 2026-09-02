from local_performance.memory_estimates import build_memory_usage_estimate_registry, estimate_memory_pressure_for_layer
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_memory_estimates():
    p = get_default_local_performance_profile()
    df, s = build_memory_usage_estimate_registry(Path("."), p)
    assert not df.empty
    est = estimate_memory_pressure_for_layer("l", 1, p)
    assert isinstance(est, dict)
