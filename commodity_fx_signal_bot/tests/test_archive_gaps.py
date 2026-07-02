import pytest
import pandas as pd
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.archive_gaps import build_archive_gap_register

def test_archive_gaps():
    profile = get_default_local_archive_profile()
    item_df = pd.DataFrame([{"domain_label": "report_archive"}])
    snap_df = pd.DataFrame()
    man_df = pd.DataFrame()
    exc_df = pd.DataFrame()

    df, summary = build_archive_gap_register(item_df, snap_df, man_df, exc_df, profile)

    assert not df.empty
    gaps = df["gap_type"].tolist()
    assert "missing_domain" in gaps
    assert "missing_snapshot_catalog" in gaps
    assert "missing_cold_storage_manifest" in gaps
