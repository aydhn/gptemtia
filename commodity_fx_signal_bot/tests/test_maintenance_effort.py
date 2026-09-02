from local_performance.maintenance_effort import build_maintenance_effort_matrix, classify_maintenance_effort
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_maintenance_effort():
    p = get_default_local_performance_profile()
    df, s = build_maintenance_effort_matrix(Path("."), p)
    assert not df.empty
