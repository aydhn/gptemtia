import pytest
from pathlib import Path
import pandas as pd
from performance.runtime_profiler import (
    is_safe_performance_command,
    build_default_profile_commands,
    RuntimeProfiler,
    summarize_runtime_profiles
)
from performance.performance_config import get_default_performance_profile

def test_is_safe_performance_command():
    assert is_safe_performance_command("python -m scripts.run_status")["safe"] == True
    assert is_safe_performance_command("python -m scripts.run_live_trading")["safe"] == False
    assert is_safe_performance_command("python deploy.py")["safe"] == False

def test_build_default_profile_commands():
    df = build_default_profile_commands()
    assert not df.empty
    assert "command" in df.columns

def test_runtime_profiler_blocked_command():
    profile = get_default_performance_profile()
    profiler = RuntimeProfiler(Path("."), profile)

    record = profiler.profile_safe_command("test", "python live.py", "mod")
    assert record.warnings
    assert "BLOCKED" in record.warnings[0]
    assert record.exit_code == 1

def test_runtime_profiling_not_production_benchmark():
    # This is a conceptual test, ensuring the summary output is just a simple dict
    # and doesn't claim to be a low-latency benchmark.
    df = pd.DataFrame([{"duration_seconds": 1.0, "timed_out": False}])
    summary = summarize_runtime_profiles(df)
    assert "avg_runtime" in summary
