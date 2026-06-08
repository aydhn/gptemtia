
import pytest
from pathlib import Path
from secrets_hygiene.backup_packaging_boundary import (
    audit_backup_recovery_secret_boundary,
    audit_portable_packaging_secret_boundary,
    audit_manifest_secret_exclusion
)

def test_backup_recovery_boundary():
    df, s = audit_backup_recovery_secret_boundary(Path("."))
    assert df.empty

def test_portable_packaging_boundary():
    df, s = audit_portable_packaging_secret_boundary(Path("."))
    assert df.empty

def test_manifest_secret_exclusion():
    df, s = audit_manifest_secret_exclusion(Path("."))
    assert not df.empty
