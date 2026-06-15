import pandas as pd
import pytest
from artifact_metadata.feature_set_cards import build_feature_set_card_registry
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile

def test_build_feature_set_card_registry():
    df = pd.DataFrame([{
        "artifact_id": "art_1",
        "artifact_type": "feature_set_artifact",
        "title": "f1",
        "relative_path": "path"
    }])
    profile = get_default_artifact_metadata_profile()
    res_df, _ = build_feature_set_card_registry(df, profile)
    assert len(res_df) == 1
    assert "feature leakage risk" in res_df.iloc[0]["limitations"]
