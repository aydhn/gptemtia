from local_performance.test_runtime_estimates import build_test_runtime_estimate_registry, estimate_test_runtime_from_static_features
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_test_runtime_estimates():
    p = get_default_local_performance_profile()
    df, s = build_test_runtime_estimate_registry(Path("."), p)
    assert not df.empty
    est = estimate_test_runtime_from_static_features(Path("."), Path("."), p)
    assert isinstance(est, dict)
