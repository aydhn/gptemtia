import pandas as pd
from pathlib import Path
from quality_gates.static_safety_scan import (
    scan_file_for_forbidden_terms,
    scan_project_for_forbidden_terms,
    scan_for_network_call_patterns,
    scan_for_background_loop_patterns,
    scan_for_broker_execution_patterns,
    build_static_safety_report
)

def test_scan_file_for_forbidden_terms():
    res = scan_file_for_forbidden_terms(Path("."))
    assert isinstance(res, dict)

def test_scan_project_for_forbidden_terms():
    df, summary = scan_project_for_forbidden_terms(Path("."))
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)

def test_scan_for_network_call_patterns():
    df, summary = scan_for_network_call_patterns(Path("."))
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)

def test_scan_for_background_loop_patterns():
    df, summary = scan_for_background_loop_patterns(Path("."))
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)

def test_scan_for_broker_execution_patterns():
    df, summary = scan_for_broker_execution_patterns(Path("."))
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)

def test_build_static_safety_report():
    df, summary = build_static_safety_report(Path("."))
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
