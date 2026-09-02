from local_performance.performance_no_go_safe_go import build_performance_no_go_safe_go_summary
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_performance_no_go_safe_go():
    p = get_default_local_performance_profile()
    df, s = build_performance_no_go_safe_go_summary(p)
    assert not df.empty
