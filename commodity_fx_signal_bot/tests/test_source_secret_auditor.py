
import pytest
from pathlib import Path
from secrets_hygiene.source_secret_auditor import (
    audit_source_for_secret_references,
    audit_source_for_forbidden_credential_patterns,
    classify_source_secret_reference
)
from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile

def test_audit_source_references():
    profile = get_default_secrets_hygiene_profile()
    df, s = audit_source_for_secret_references(Path("."), profile)
    assert df.empty

def test_audit_source_forbidden():
    profile = get_default_secrets_hygiene_profile()
    df, s = audit_source_for_forbidden_credential_patterns(Path("."), profile)
    assert df.empty

def test_classify_source_reference():
    c = classify_source_secret_reference("os.environ.get('API_KEY')", "test.py")
    assert c["status"] == "info"

    c2 = classify_source_secret_reference("API_KEY='secret'", "test.py")
    assert c2["status"] == "warning"
