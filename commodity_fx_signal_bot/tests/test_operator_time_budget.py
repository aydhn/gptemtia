from local_performance.operator_time_budget import build_operator_time_budget_report
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_operator_time_budget():
    p = get_default_local_performance_profile()
    df, s = build_operator_time_budget_report(Path("."), p)
    assert not df.empty
