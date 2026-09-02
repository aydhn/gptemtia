from local_performance.performance_budget import build_final_local_performance_budget, build_default_performance_budget_items, classify_budget_pressure
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_performance_budget():
    p = get_default_local_performance_profile()
    df, s = build_final_local_performance_budget(Path("."), p)
    assert not df.empty
    items = build_default_performance_budget_items(p)
    assert not items.empty
    assert classify_budget_pressure(None, p) == "normal"
