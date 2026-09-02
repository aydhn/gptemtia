from local_performance.efficiency_candidates import build_efficiency_candidate_registry
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_efficiency_candidates():
    p = get_default_local_performance_profile()
    df, s = build_efficiency_candidate_registry(Path("."), p)
    assert not df.empty
