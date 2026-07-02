import pytest
from pathlib import Path
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.cross_layer_archive import build_cross_layer_archive_index

def test_cross_layer_archive_index(tmp_path):
    profile = get_default_local_archive_profile()

    # Needs to match cross_layer_archive domain logic
    # "consistency" in rel_path or "evidence" in rel_path
    c_dir = tmp_path / "reports" / "consistency"
    c_dir.mkdir(parents=True)
    (c_dir / "check.json").write_text("{}")

    df, summary = build_cross_layer_archive_index(tmp_path, profile)

    if not df.empty:
        pass
