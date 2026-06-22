import pytest
from pathlib import Path
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.stale_artifact_watch import build_deprecated_artifact_watch_report

def test_deprecated_artifact_watch_report(tmp_path):
    profile = get_default_local_maintenance_profile()
    d = tmp_path / "scripts"
    d.mkdir(parents=True)
    (d / "old_script.py").touch()

    df, summary = build_deprecated_artifact_watch_report(tmp_path, profile)
    assert not df.empty
    assert "old_script.py" in str(df["file_path"].values)
    assert "automatic file deletion" in summary["disclaimer"].lower()
