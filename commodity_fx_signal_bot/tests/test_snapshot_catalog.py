import pytest
import pandas as pd
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.snapshot_catalog import build_project_snapshot_catalog

def test_snapshot_catalog():
    profile = get_default_local_archive_profile()
    item_df = pd.DataFrame([
        {"item_id": "1", "domain_label": "documentation_archive", "item_status": "archive_candidate"}
    ])

    df, summary = build_project_snapshot_catalog(item_df, profile)

    assert not df.empty
    assert "snapshot_id" in df.columns
    assert "snapshot_name" in df.columns

    # Verify local_only is True
    assert all(df['local_only'] == True)
