import pytest
import pandas as pd
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.cold_storage_manifest import build_cold_storage_manifest

def test_cold_storage_manifest():
    profile = get_default_local_archive_profile()
    item_df = pd.DataFrame([
        {"item_id": "1", "domain_label": "documentation_archive", "item_status": "archive_candidate"}
    ])
    snap_df = pd.DataFrame([{"snapshot_id": "1"}])

    manifest, summary = build_cold_storage_manifest(item_df, snap_df, profile)

    assert "statements" in manifest
    assert manifest["statements"]["local_only"] is True
    assert manifest["statements"]["no_cloud_upload"] is True
    assert summary["is_safe"] is True
