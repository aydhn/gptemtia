
import pytest
from secrets_hygiene.redaction import (
    mask_secret_value,
    safe_preview_line,
    redact_mapping_values,
    assert_no_unmasked_secret
)

def test_mask_secret_value():
    assert mask_secret_value("1234567890123456", 4, 4) == "1234********3456"

def test_mask_secret_value_short():
    assert mask_secret_value("short", 4, 4) == "*****"

def test_safe_preview_line():
    long_line = "a" * 300
    preview = safe_preview_line(long_line, 240)
    assert len(preview) == 243
    assert preview.endswith("...")

def test_redact_mapping_values():
    data = {"api_key": "mysecretkey123", "normal": "value"}
    redacted = redact_mapping_values(data)
    assert redacted["normal"] == "value"
    assert "*" in redacted["api_key"]

def test_assert_no_unmasked_secret():
    assert assert_no_unmasked_secret("my line with masked ****", "mysecret") == True
    assert assert_no_unmasked_secret("my line with mysecret", "mysecret") == False
