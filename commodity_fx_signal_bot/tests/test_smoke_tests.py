import pandas as pd
from pathlib import Path
from quality_gates.smoke_tests import (
    build_smoke_test_command_registry,
    run_safe_smoke_command,
    run_smoke_tests,
    summarize_smoke_tests
)
from quality_gates.quality_config import QualityGateProfile

def test_build_smoke_test_command_registry():
    df = build_smoke_test_command_registry()
    assert isinstance(df, pd.DataFrame)

def test_run_safe_smoke_command():
    res = run_safe_smoke_command("mock", Path("."))
    assert isinstance(res, dict)

def test_run_smoke_tests():
    profile = QualityGateProfile(name="mock", description="mock")
    df, summary = run_smoke_tests(Path("."), profile)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)

def test_summarize_smoke_tests():
    df = pd.DataFrame()
    summary = summarize_smoke_tests(df)
    assert isinstance(summary, dict)
