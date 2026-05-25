import pandas as pd
from pathlib import Path
from quality_gates.test_discovery import (
    discover_test_files,
    discover_source_modules,
    map_tests_to_modules,
    summarize_test_discovery
)

def test_discover_test_files():
    root = Path(".")
    df = discover_test_files(root)
    assert isinstance(df, pd.DataFrame)
    assert "test_file" in df.columns

def test_discover_source_modules():
    root = Path(".")
    df = discover_source_modules(root)
    assert isinstance(df, pd.DataFrame)
    assert "module_name" in df.columns

def test_map_tests_to_modules():
    test_df = pd.DataFrame([{"test_file": "tests/test_mock.py"}])
    source_df = pd.DataFrame([{"module_name": "mock"}])
    df = map_tests_to_modules(test_df, source_df)
    assert isinstance(df, pd.DataFrame)
    assert "inferred_module" in df.columns
    assert "exists" in df.columns

def test_summarize_test_discovery():
    test_df = pd.DataFrame([{"test_file": "tests/test_mock.py"}])
    source_df = pd.DataFrame([{"module_name": "mock"}])
    summary = summarize_test_discovery(test_df, source_df)
    assert "total_tests" in summary
