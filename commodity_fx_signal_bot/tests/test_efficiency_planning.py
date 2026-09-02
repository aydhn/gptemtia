from local_performance.efficiency_planning import build_offline_efficiency_planning_guide
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_efficiency_planning():
    p = get_default_local_performance_profile()
    text, s = build_offline_efficiency_planning_guide(Path("."), p)
    assert isinstance(text, str)
    assert len(text) > 0
