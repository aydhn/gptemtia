import pytest
from pathlib import Path
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.stale_test_watch import build_stale_test_watch_report

def test_stale_test_watch_report(tmp_path):
    profile = get_default_local_maintenance_profile()
    d = tmp_path / "tests"
    d.mkdir()
    f = d / "test_old.py"
    f.touch()

    df, summary = build_stale_test_watch_report(tmp_path, profile)
    assert not df.empty
    assert "test_old.py" in str(df["file_path"].values)
    assert "not executed" in summary["disclaimer"].lower()
