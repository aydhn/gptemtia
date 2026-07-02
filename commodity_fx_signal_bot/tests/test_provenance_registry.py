import pytest
import pandas as pd
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.provenance_registry import build_archive_provenance_registry

def test_provenance_registry():
    profile = get_default_local_archive_profile()
    item_df = pd.DataFrame([
        {"item_id": "1", "item_status": "archive_candidate", "relative_path": "data/lake/test.parquet", "domain_label": "datalake_archive"},
        {"item_id": "2", "item_status": "archive_candidate", "relative_path": "reports/output/test.pdf", "domain_label": "report_archive"}
    ])

    df, summary = build_archive_provenance_registry(item_df, profile)

    assert not df.empty

    i1 = df[df["item_id"] == "1"]
    assert i1.iloc[0]["source_layer"] == "storage"

    i2 = df[df["item_id"] == "2"]
    assert i2.iloc[0]["source_layer"] == "presentation"
