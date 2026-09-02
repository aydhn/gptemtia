from local_performance.cpu_estimates import build_cpu_usage_estimate_registry, estimate_cpu_pressure_for_file
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_cpu_estimates():
    p = get_default_local_performance_profile()
    df, s = build_cpu_usage_estimate_registry(Path("."), p)
    assert not df.empty
    est = estimate_cpu_pressure_for_file(Path("."), Path("."), p)
    assert isinstance(est, dict)
