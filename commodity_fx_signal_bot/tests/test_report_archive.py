import pytest
from pathlib import Path
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.report_archive import build_report_archive_index

def test_report_archive_index(tmp_path):
    profile = get_default_local_archive_profile()

    rep_dir = tmp_path / "reports" / "output" / "local_archive"
    rep_dir.mkdir(parents=True)
    (rep_dir / "report.md").write_text("Report")

    df, summary = build_report_archive_index(tmp_path, profile)

    assert not df.empty
    assert df.iloc[0]["report_domain"] == "local_archive"


def test_dummy(): pass
