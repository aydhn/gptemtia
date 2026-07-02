import pytest
from pathlib import Path
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.dependency_snapshot import build_archive_dependency_snapshot_summary

def test_dependency_snapshot(tmp_path):
    profile = get_default_local_archive_profile()

    (tmp_path / "requirements.txt").write_text("pytest")

    df, summary = build_archive_dependency_snapshot_summary(tmp_path, profile)

    assert not df.empty
    req = df[df["source_file"] == "requirements.txt"]
    assert req.iloc[0]["status"] == "found"

    req_dev = df[df["source_file"] == "requirements-dev.txt"]
    assert req_dev.iloc[0]["status"] == "missing"
