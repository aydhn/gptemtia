
import pytest
from secrets_hygiene.secret_patterns import (
    build_secret_pattern_registry,
    scan_text_for_secret_patterns,
    _is_false_positive
)
from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile

def test_pattern_registry_not_empty():
    df = build_secret_pattern_registry()
    assert not df.empty

def test_api_key_finding():
    text = "API_KEY = 'AKIAIOSFODNN7EXAMPLE'"
    profile = get_default_secrets_hygiene_profile()
    findings = scan_text_for_secret_patterns(text, "config.py", profile)
    assert len(findings) > 0
    assert findings[0].finding_type == "api_key_finding"

def test_placeholder_false_positive():
    text = "API_KEY = 'YOUR_API_KEY_HERE_123456'"
    profile = get_default_secrets_hygiene_profile()
    findings = scan_text_for_secret_patterns(text, "config.py", profile)
    assert len(findings) > 0
    assert findings[0].severity == "low_secret_warning"

def test_finding_masked_value():
    text = "API_KEY = 'AKIAIOSFODNN7EXAMPLE'"
    profile = get_default_secrets_hygiene_profile()
    findings = scan_text_for_secret_patterns(text, "config.py", profile)
    assert "AKIA" in findings[0].masked_value
    assert "MPLE" in findings[0].masked_value
    assert "*" in findings[0].masked_value

def test_raw_value_not_in_dict():
    text = "API_KEY = 'AKIAIOSFODNN7EXAMPLE'"
    profile = get_default_secrets_hygiene_profile()
    findings = scan_text_for_secret_patterns(text, "config.py", profile)
    d = findings[0].__dict__
    assert "raw_value" not in d
