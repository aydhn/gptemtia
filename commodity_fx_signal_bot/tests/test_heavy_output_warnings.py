from local_performance.heavy_output_warnings import build_heavy_output_warning_registry
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_heavy_output_warnings():
    p = get_default_local_performance_profile()
    df, s = build_heavy_output_warning_registry(Path("."), p)
    assert not df.empty
