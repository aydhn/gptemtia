import pandas as pd
from pathlib import Path
from quality_gates.test_health import (
    run_pytest_collect_only,
    run_pytest_suite,
    parse_pytest_output,
    build_test_health_table,
    summarize_test_health
)

def test_run_pytest_collect_only():
    df, summary = run_pytest_collect_only(Path("."))
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)

def test_run_pytest_suite():
    df, summary = run_pytest_suite(Path("."))
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)

def test_parse_pytest_output():
    summary = parse_pytest_output("Mock output")
    assert isinstance(summary, dict)

def test_build_test_health_table():
    df = pd.DataFrame()
    table = build_test_health_table(df)
    assert isinstance(table, pd.DataFrame)

def test_summarize_test_health():
    df = pd.DataFrame()
    summary = summarize_test_health(df)
    assert isinstance(summary, dict)
