import pytest
from pathlib import Path
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.datalake_archive import build_datalake_archive_index

def test_datalake_archive_index(tmp_path):
    profile = get_default_local_archive_profile()

    lake_dir = tmp_path / "data" / "lake" / "local_archive"
    lake_dir.mkdir(parents=True)
    (lake_dir / "data.parquet").write_text("Data")

    df, summary = build_datalake_archive_index(tmp_path, profile)

    assert not df.empty
    assert df.iloc[0]["datalake_domain"] == "local_archive"
