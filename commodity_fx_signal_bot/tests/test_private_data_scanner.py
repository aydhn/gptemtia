
import pytest
from secrets_hygiene.private_data_scanner import (
    build_private_data_pattern_registry,
    scan_text_for_private_data,
    classify_private_data_severity
)
from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile

def test_private_data_pattern_registry():
    df = build_private_data_pattern_registry()
    assert not df.empty

def test_email_like_values():
    text = "Contact me at user@example.org"
    profile = get_default_secrets_hygiene_profile()
    findings = scan_text_for_private_data(text, "test.txt", profile)
    assert len(findings) > 0
    assert findings[0].finding_type == "personal_data_finding"

def test_dummy_examples_low_risk():
    text = "Contact me at dummy@example.com"
    profile = get_default_secrets_hygiene_profile()
    findings = scan_text_for_private_data(text, "test.txt", profile)
    assert len(findings) == 0 # Skipped due to example.com false positive logic

def test_raw_private_data_not_written():
    text = "Contact me at realuser@domain.com"
    profile = get_default_secrets_hygiene_profile()
    findings = scan_text_for_private_data(text, "test.txt", profile)
    assert len(findings) > 0
    assert "realuser" not in findings[0].masked_value
