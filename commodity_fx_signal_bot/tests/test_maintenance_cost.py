from local_performance.maintenance_cost import build_maintenance_cost_estimate
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_maintenance_cost():
    p = get_default_local_performance_profile()
    df, s = build_maintenance_cost_estimate(Path("."), p)
    assert not df.empty
