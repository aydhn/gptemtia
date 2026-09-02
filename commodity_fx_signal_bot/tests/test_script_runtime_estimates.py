from local_performance.script_runtime_estimates import build_script_runtime_estimate_registry, estimate_script_runtime_from_static_features
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_script_runtime_estimates():
    p = get_default_local_performance_profile()
    df, s = build_script_runtime_estimate_registry(Path("."), p)
    assert not df.empty
    est = estimate_script_runtime_from_static_features(Path("."), Path("."), p)
    assert isinstance(est, dict)
