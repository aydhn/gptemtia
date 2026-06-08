
import pytest
from secrets_hygiene.secrets_models import (
    build_sensitive_file_id,
    build_secret_finding_id,
    build_credential_boundary_id,
    SensitiveFileRecord,
    SecretFinding,
    sensitive_file_record_to_dict,
    secret_finding_to_dict
)

def test_build_sensitive_file_id():
    id1 = build_sensitive_file_id("test/file.py")
    id2 = build_sensitive_file_id("test/file.py")
    assert id1 == id2
    assert id1.startswith("sf_")

def test_build_secret_finding_id():
    id1 = build_secret_finding_id("test.py", 1, "test_pattern", "****")
    id2 = build_secret_finding_id("test.py", 1, "test_pattern", "****")
    assert id1 == id2
    assert id1.startswith("sec_")

def test_build_credential_boundary_id():
    id1 = build_credential_boundary_id("test_boundary")
    id2 = build_credential_boundary_id("test_boundary")
    assert id1 == id2
    assert id1.startswith("cb_")

def test_to_dict_contains_keys():
    rec = SensitiveFileRecord(
        file_id="1", relative_path="path", file_type="py", size_bytes=100,
        scan_allowed=True, scan_reason="test", sensitive_path_hint=False, warnings=[]
    )
    d = sensitive_file_record_to_dict(rec)
    assert "file_id" in d
    assert "warnings" in d

def test_secret_finding_raw_secret():
    finding = SecretFinding(
        finding_id="1", finding_type="test", severity="low", relative_path="test",
        line_number=1, column_start=0, masked_value="****", pattern_name="test",
        confidence=1.0, redaction_status="ok", warnings=[]
    )
    d = secret_finding_to_dict(finding)
    assert "masked_value" in d
    assert "raw_value" not in d
