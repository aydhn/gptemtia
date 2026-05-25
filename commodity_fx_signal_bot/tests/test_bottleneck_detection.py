import pytest
import pandas as pd
from performance.performance_config import get_default_performance_profile
from performance.bottleneck_detection import (
    detect_runtime_bottlenecks,
    detect_memory_bottlenecks,
    detect_cache_bottlenecks,
    build_bottleneck_report
)

def test_detect_runtime_bottlenecks():
    profile = get_default_performance_profile()
    df = pd.DataFrame([
        {"module_name": "m1", "duration_seconds": profile.max_runtime_seconds_per_script * 0.95},
        {"module_name": "m2", "duration_seconds": profile.max_runtime_seconds_per_script * 0.1}
    ])

    res = detect_runtime_bottlenecks(df, profile)
    assert len(res) == 1
    assert res.iloc[0]["severity"] == "high"

def test_detect_memory_bottlenecks():
    profile = get_default_performance_profile()
    df = pd.DataFrame([
        {"module_name": "m1", "peak_memory_mb": profile.max_memory_mb_per_script * 0.6},
        {"module_name": "m2", "peak_memory_mb": profile.max_memory_mb_per_script * 0.1}
    ])

    res = detect_memory_bottlenecks(df, profile)
    assert len(res) == 1
    assert res.iloc[0]["severity"] == "medium"

def test_detect_cache_bottlenecks():
    df = pd.DataFrame([
        {"status": "invalid"}, {"status": "invalid"}, {"status": "invalid"},
        {"status": "invalid"}, {"status": "invalid"}, {"status": "valid"}
    ])

    res = detect_cache_bottlenecks(df)
    assert len(res) == 1
    assert res.iloc[0]["bottleneck_type"] == "cache_bottleneck"

def test_build_bottleneck_report():
    profile = get_default_performance_profile()
    r_df = pd.DataFrame([{"module_name": "m1", "duration_seconds": profile.max_runtime_seconds_per_script * 0.95}])

    df, summary = build_bottleneck_report(r_df, None, None, profile)
    assert len(df) == 1
    assert summary["total_bottlenecks"] == 1
    assert summary["high_severity"] == 1

    # Test bottleneck does not automatically change code
    # This is a conceptual test, verified by lack of file operations
    assert "auto_patch" not in df.columns
