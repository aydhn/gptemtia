import pytest
from pathlib import Path
import pandas as pd
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.hash_manifest import build_archive_hash_manifest

def test_hash_manifest(tmp_path):
    profile = get_default_local_archive_profile()

    f1 = tmp_path / "test.txt"
    f1.write_text("hello world")

    item_df = pd.DataFrame([
        {"item_id": "1", "item_status": "archive_candidate", "relative_path": "test.txt"}
    ])

    df, summary = build_archive_hash_manifest(item_df, tmp_path, profile)

    assert not df.empty
    assert "sha256" in df.columns
    assert df.iloc[0]["sha256"] is not None
    assert df.iloc[0]["integrity_status"] == "integrity_hash_available"
