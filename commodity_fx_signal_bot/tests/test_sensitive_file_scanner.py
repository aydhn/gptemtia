
import pytest
from pathlib import Path
from secrets_hygiene.sensitive_file_scanner import (
    discover_sensitive_scan_files,
    should_scan_file,
    scan_file_for_secrets
)
from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile

def test_scan_file_inventory():
    project_root = Path(__file__).parent.parent
    profile = get_default_secrets_hygiene_profile()
    df = discover_sensitive_scan_files(project_root, profile)
    assert not df.empty

def test_large_binary_skip():
    profile = get_default_secrets_hygiene_profile()
    path = Path("fake_large.bin")
    scan_info = should_scan_file(path, Path("."), profile)
    assert not scan_info["scan_allowed"]

def test_env_content_not_read():
    profile = get_default_secrets_hygiene_profile()
    path = Path(".env")
    scan_info = should_scan_file(path, Path("."), profile)
    assert not scan_info["scan_allowed"]
    assert scan_info["sensitive_hint"]

def test_scan_file_for_secrets(tmp_path):
    f = tmp_path / "test.py"
    f.write_text("api_key = 'AKIAIOSFODNN7EXAMPLE'")
    profile = get_default_secrets_hygiene_profile()
    findings, summary = scan_file_for_secrets(f, tmp_path, profile)
    assert summary["scanned"]
    assert len(findings) > 0
