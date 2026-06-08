
import pytest
import pandas as pd
from secrets_hygiene.secrets_quality import (
    check_sensitive_file_inventory_quality,
    check_secret_findings_quality,
    check_env_template_audit_quality,
    check_credential_boundary_quality,
    check_remediation_quality,
    check_for_forbidden_terms_in_secrets,
    build_secrets_quality_report
)
from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile

def test_inventory_quality():
    profile = get_default_secrets_hygiene_profile()
    res = check_sensitive_file_inventory_quality(pd.DataFrame([{"file_id": "1"}]), profile)
    assert res["inventory_valid"]

def test_findings_quality():
    profile = get_default_secrets_hygiene_profile()
    res = check_secret_findings_quality(pd.DataFrame([{"masked_value": "****"}]), profile)
    assert res["findings_redacted"]

def test_remediation_quality():
    profile = get_default_secrets_hygiene_profile()
    res = check_remediation_quality(pd.DataFrame([{"destructive": False}]), profile)
    assert res["remediation_safe"]

def test_forbidden_terms():
    res = check_for_forbidden_terms_in_secrets(text="print secret")
    assert res["forbidden_terms_found"]

def test_build_quality_report():
    q = build_secrets_quality_report(
        {},
        pd.DataFrame([{"f": 1}]),
        pd.DataFrame([{"masked_value": "1"}]),
        pd.DataFrame([{"status": "ok"}]),
        pd.DataFrame([{"destructive": False}])
    )
    assert q["passed"]
