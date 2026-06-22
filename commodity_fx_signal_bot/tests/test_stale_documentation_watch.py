import pytest
from pathlib import Path
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.stale_documentation_watch import build_stale_documentation_watch_report

def test_stale_documentation_watch_report(tmp_path):
    profile = get_default_local_maintenance_profile()
    d = tmp_path / "docs"
    d.mkdir()
    f = d / "ARCHITECTURE.md"
    f.write_text("This is an old doc without phase ref.")

    df, summary = build_stale_documentation_watch_report(tmp_path, profile)
    assert not df.empty
    assert "ARCHITECTURE.md" in str(df["file_path"].values)
    assert "heuristic" in summary["disclaimer"].lower()
