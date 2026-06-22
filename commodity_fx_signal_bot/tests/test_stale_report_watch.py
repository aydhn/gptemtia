import pytest
from pathlib import Path
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.stale_report_watch import build_stale_report_watch_report
import time

def test_stale_report_watch_report(tmp_path):
    profile = get_default_local_maintenance_profile()
    d = tmp_path / "reports" / "output"
    d.mkdir(parents=True)
    f = d / "test.csv"
    f.touch()

    # Make it artificially old
    old_time = time.time() - (100 * 24 * 60 * 60)
    import os
    os.utime(str(f), (old_time, old_time))

    df, summary = build_stale_report_watch_report(tmp_path, profile)
    assert not df.empty
    assert "stale_report" in df["status"].values
    assert "manual" in summary["disclaimer"].lower()
