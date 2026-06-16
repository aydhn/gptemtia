import pandas as pd
import pytest
from artifact_metadata.intended_use_cards import build_intended_use_cards
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile

def test_build_intended_use_cards():
    df = pd.DataFrame([{
        "artifact_id": "art_1",
        "artifact_type": "model_artifact",
        "title": "l1",
        "relative_path": "path"
    }])
    profile = get_default_artifact_metadata_profile()
    res_df, _ = build_intended_use_cards(df, profile)
    assert len(res_df) == 1
    assert "offline research review" in res_df.iloc[0]["intended_use"]
