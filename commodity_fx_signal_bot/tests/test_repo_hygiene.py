import pandas as pd
from pathlib import Path
from quality_gates.repo_hygiene import (
    check_required_directories,
    check_required_docs,
    check_python_file_hygiene,
    check_large_files,
    check_empty_or_placeholder_files,
    check_duplicate_script_names,
    build_repo_hygiene_report
)

def test_check_required_directories():
    df = check_required_directories(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_check_required_docs():
    df = check_required_docs(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_check_python_file_hygiene():
    df = check_python_file_hygiene(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_check_large_files():
    df = check_large_files(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_check_empty_or_placeholder_files():
    df = check_empty_or_placeholder_files(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_check_duplicate_script_names():
    df = check_duplicate_script_names(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_build_repo_hygiene_report():
    df, summary = build_repo_hygiene_report(Path("."))
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
