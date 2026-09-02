from local_performance.disk_estimates import build_disk_usage_estimate_registry, estimate_disk_usage_by_layer
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_disk_estimates():
    p = get_default_local_performance_profile()
    df, s = build_disk_usage_estimate_registry(Path("."), p)
    assert not df.empty
