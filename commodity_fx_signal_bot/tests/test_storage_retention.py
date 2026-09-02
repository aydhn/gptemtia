from local_performance.storage_retention import build_storage_retention_rehearsal_plan
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_storage_retention():
    p = get_default_local_performance_profile()
    df, s = build_storage_retention_rehearsal_plan(Path("."), p)
    assert not df.empty
