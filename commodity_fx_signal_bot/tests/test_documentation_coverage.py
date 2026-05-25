import pandas as pd
from pathlib import Path
from quality_gates.documentation_coverage import (
    check_readme_sections,
    check_architecture_sections,
    check_phase_log_coverage,
    check_script_documentation_coverage,
    build_documentation_coverage_report
)

def test_check_readme_sections():
    df = check_readme_sections(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_check_architecture_sections():
    df = check_architecture_sections(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_check_phase_log_coverage():
    df = check_phase_log_coverage(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_check_script_documentation_coverage():
    df = check_script_documentation_coverage(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_build_documentation_coverage_report():
    df, summary = build_documentation_coverage_report(Path("."))
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
