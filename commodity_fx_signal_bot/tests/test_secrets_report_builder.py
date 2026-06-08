
import pytest
import pandas as pd
from secrets_hygiene.secrets_report_builder import (
    build_secrets_disclaimer,
    build_sensitive_file_scan_markdown_report,
    build_env_template_audit_markdown_report,
    build_credential_boundary_markdown_report,
    build_private_data_protection_markdown_report,
    build_secret_remediation_markdown_report,
    build_secrets_quality_markdown_report
)

def test_disclaimer():
    d = build_secrets_disclaimer()
    assert "yatırım tavsiyesi içermez" in d
    assert "offline/local secrets hygiene" in d

def test_sensitive_file_markdown():
    md = build_sensitive_file_scan_markdown_report({"inventory": {"total_files": 10}})
    assert "Total Files" in md

def test_env_template_markdown():
    md = build_env_template_audit_markdown_report({"total_variables": 5})
    assert "Total Variables" in md

def test_credential_boundary_markdown():
    md = build_credential_boundary_markdown_report({"failed_boundaries": 1})
    assert "Failed Boundaries" in md

def test_private_data_markdown():
    md = build_private_data_protection_markdown_report({"total_private_findings": 2})
    assert "Total Findings" in md

def test_quality_markdown():
    md = build_secrets_quality_markdown_report({}, {"passed": True})
    assert "Passed" in md
