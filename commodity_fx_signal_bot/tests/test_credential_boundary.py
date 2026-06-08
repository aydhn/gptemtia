
import pytest
from pathlib import Path
import pandas as pd
from secrets_hygiene.credential_boundary import (
    build_credential_boundary_policy,
    check_credentials_only_in_templates_or_local_env,
    check_no_credentials_in_reports,
    check_no_credentials_in_docs,
    check_no_credentials_in_tests,
    check_no_credentials_in_backup_packaging_manifests
)

def test_boundary_policy():
    df = build_credential_boundary_policy()
    assert not df.empty

def test_credentials_only_in_templates():
    res = check_credentials_only_in_templates_or_local_env(Path("."))
    assert res.status == "boundary_ok"

def test_no_credentials_in_reports():
    findings = pd.DataFrame([{"relative_path": "reports/output/test.txt", "severity": "high_secret_risk"}])
    res = check_no_credentials_in_reports(Path("."), findings)
    assert res.status == "boundary_failed"

def test_no_credentials_in_docs():
    findings = pd.DataFrame([{"relative_path": "docs/test.md", "severity": "high_secret_risk"}])
    res = check_no_credentials_in_docs(Path("."), findings)
    assert res.status == "boundary_failed"

def test_no_credentials_in_tests():
    findings = pd.DataFrame([{"relative_path": "tests/test.py", "severity": "high_secret_risk"}])
    res = check_no_credentials_in_tests(Path("."), findings)
    assert res.status == "boundary_failed"

def test_no_credentials_in_backup_packaging():
    findings = pd.DataFrame([{"relative_path": "manifests/backup.json", "severity": "high_secret_risk"}])
    res = check_no_credentials_in_backup_packaging_manifests(Path("."), findings)
    assert res.status == "boundary_failed"
