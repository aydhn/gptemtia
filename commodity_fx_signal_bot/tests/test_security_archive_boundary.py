import pytest
from pathlib import Path
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.security_archive_boundary import build_security_sensitive_archive_boundary_report

def test_security_sensitive_archive_boundary(tmp_path):
    profile = get_default_local_archive_profile()

    (tmp_path / ".env.production").write_text("secret")
    (tmp_path / "app.key").write_text("key")

    df, summary = build_security_sensitive_archive_boundary_report(tmp_path, profile)

    assert not df.empty
    paths = df["relative_path"].tolist()
    assert ".env.production" in paths
    assert "app.key" in paths
    assert all(df["boundary_status"] == "out_of_bounds_sensitive")
