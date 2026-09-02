from local_performance.resource_footprint import build_resource_footprint_rehearsal_report, discover_resource_footprint_items
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_resource_footprint():
    p = get_default_local_performance_profile()
    df, s = build_resource_footprint_rehearsal_report(Path("."), p)
    assert not df.empty
