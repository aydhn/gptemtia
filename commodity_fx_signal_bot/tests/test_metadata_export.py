import pandas as pd
import pytest
from artifact_metadata.metadata_export import build_metadata_export_index, validate_metadata_export_safety
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile

def test_build_metadata_export_index():
    df = pd.DataFrame([{"artifact_id": "a1"}])
    profile = get_default_artifact_metadata_profile()

    idx_df = build_metadata_export_index(df, {}, profile)
    assert len(idx_df) == 1
    assert bool(idx_df.iloc[0]["local_only"]) is True

    val = validate_metadata_export_safety({}, idx_df, profile)
    assert val["safe"] is True
