import pandas as pd
from quality_gates.quality_report_builder import (
    build_local_ci_markdown_report,
    build_test_health_markdown_report,
    build_import_graph_markdown_report,
    build_repo_hygiene_markdown_report,
    build_dependency_audit_markdown_report,
    build_static_safety_markdown_report,
    build_release_candidate_markdown_report,
    build_quality_gate_disclaimer
)

def test_build_local_ci_markdown_report():
    md = build_local_ci_markdown_report({}, pd.DataFrame())
    assert isinstance(md, str)

def test_build_test_health_markdown_report():
    md = build_test_health_markdown_report({}, pd.DataFrame())
    assert isinstance(md, str)

def test_build_import_graph_markdown_report():
    md = build_import_graph_markdown_report({}, pd.DataFrame(), pd.DataFrame())
    assert isinstance(md, str)

def test_build_repo_hygiene_markdown_report():
    md = build_repo_hygiene_markdown_report({}, pd.DataFrame())
    assert isinstance(md, str)

def test_build_dependency_audit_markdown_report():
    md = build_dependency_audit_markdown_report({}, {"test": pd.DataFrame()})
    assert isinstance(md, str)

def test_build_static_safety_markdown_report():
    md = build_static_safety_markdown_report({}, pd.DataFrame())
    assert isinstance(md, str)

def test_build_release_candidate_markdown_report():
    md = build_release_candidate_markdown_report({}, pd.DataFrame())
    assert isinstance(md, str)

def test_build_quality_gate_disclaimer():
    disclaimer = build_quality_gate_disclaimer()
    assert isinstance(disclaimer, str)
    assert "yatırım tavsiyesi değildir" in disclaimer
