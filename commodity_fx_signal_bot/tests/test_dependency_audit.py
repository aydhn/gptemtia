import pandas as pd
from pathlib import Path
from quality_gates.dependency_audit import (
    discover_requirement_files,
    parse_requirements_file,
    collect_imported_external_packages,
    compare_imports_to_requirements,
    build_optional_dependency_map,
    build_dependency_audit_report
)

def test_discover_requirement_files():
    df = discover_requirement_files(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_parse_requirements_file():
    df = parse_requirements_file(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_collect_imported_external_packages():
    df = collect_imported_external_packages(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_compare_imports_to_requirements():
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    df = compare_imports_to_requirements(df1, df2)
    assert isinstance(df, pd.DataFrame)

def test_build_optional_dependency_map():
    df = build_optional_dependency_map(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_build_dependency_audit_report():
    tables, summary = build_dependency_audit_report(Path("."))
    assert isinstance(tables, dict)
    assert isinstance(summary, dict)
