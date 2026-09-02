from local_performance.lightweight_mode import build_lightweight_mode_recommendation_registry
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_lightweight_mode():
    p = get_default_local_performance_profile()
    df, s = build_lightweight_mode_recommendation_registry(Path("."), p)
    assert not df.empty
