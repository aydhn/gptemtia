
import pytest
from pathlib import Path
from secrets_hygiene.documentation_secret_scanner import (
    scan_docs_for_secret_like_values,
    audit_docs_for_secret_handling_guidance
)
from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile

def test_scan_docs_for_secret_like():
    profile = get_default_secrets_hygiene_profile()
    df, s = scan_docs_for_secret_like_values(Path("."), profile)
    assert df.empty

def test_audit_docs_guidance():
    df, s = audit_docs_for_secret_handling_guidance(Path("."))
    assert not df.empty
