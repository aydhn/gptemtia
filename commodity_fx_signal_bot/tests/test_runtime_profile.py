from local_performance.runtime_profile import build_lightweight_runtime_profile, build_runtime_profile_items, classify_runtime_mode
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path
import pandas as pd

def test_runtime_profile():
    p = get_default_local_performance_profile()
    df, s = build_lightweight_runtime_profile(Path("."), p)
    assert not df.empty
    items = build_runtime_profile_items(p)
    assert not items.empty
    assert classify_runtime_mode(pd.Series({"mode_name": "test"}), p) == "test"
