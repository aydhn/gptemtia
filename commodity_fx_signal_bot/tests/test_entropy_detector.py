
import pytest
from secrets_hygiene.entropy_detector import (
    calculate_shannon_entropy,
    scan_text_for_high_entropy_tokens,
    filter_entropy_false_positives
)
from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile

def test_calculate_entropy():
    e1 = calculate_shannon_entropy("aaaaaaaa")
    e2 = calculate_shannon_entropy("aBcDeFgHiJkLmNoPqRsTuVwXyZ123456")
    assert e2 > e1

def test_high_entropy_token_finding():
    text = "my_token = 'aBcDeFgHiJkLmNoPqRsTuVwXyZ123456'"
    profile = get_default_secrets_hygiene_profile()
    findings = scan_text_for_high_entropy_tokens(text, "test.py", profile)
    assert len(findings) > 0

def test_short_token_ignore():
    text = "token = 'short'"
    profile = get_default_secrets_hygiene_profile()
    findings = scan_text_for_high_entropy_tokens(text, "test.py", profile)
    assert len(findings) == 0

def test_false_positive_filter():
    candidates = [{"raw_value": "123e4567-e89b-12d3-a456-426614174000", "line_number": 1, "column_start": 0}]
    filtered = filter_entropy_false_positives(candidates)
    assert filtered[0]["is_false_positive"]

def test_raw_token_not_reported():
    text = "my_token = 'aBcDeFgHiJkLmNoPqRsTuVwXyZ123456'"
    profile = get_default_secrets_hygiene_profile()
    findings = scan_text_for_high_entropy_tokens(text, "test.py", profile)
    d = findings[0].__dict__
    assert "raw_value" not in d
