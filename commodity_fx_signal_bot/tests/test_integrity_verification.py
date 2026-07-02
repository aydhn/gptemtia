import pytest
import pandas as pd
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.integrity_verification import build_archive_integrity_verification_plan

def test_integrity_verification_plan():
    profile = get_default_local_archive_profile()
    item_df = pd.DataFrame([
        {"item_id": "1", "item_status": "archive_candidate", "relative_path": "test.txt", "integrity_status": "integrity_hash_available"},
        {"item_id": "2", "item_status": "archive_candidate", "relative_path": "big.bin", "integrity_status": "integrity_hash_skipped_large_file"}
    ])

    df, summary = build_archive_integrity_verification_plan(item_df, profile)

    assert not df.empty

    i1 = df[df["item_id"] == "1"]
    assert i1.iloc[0]["verification_method"] == "sha256_manifest_check"

    i2 = df[df["item_id"] == "2"]
    assert i2.iloc[0]["verification_method"] == "skipped_large_file_manual_check"
