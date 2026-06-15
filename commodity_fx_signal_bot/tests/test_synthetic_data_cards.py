import pandas as pd
import pytest
from artifact_metadata.synthetic_data_cards import build_synthetic_data_card_registry
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile

def test_build_synthetic_data_card_registry():
    df = pd.DataFrame([{
        "artifact_id": "art_1",
        "artifact_type": "synthetic_data_artifact",
        "title": "sy1",
        "relative_path": "path"
    }])
    profile = get_default_artifact_metadata_profile()
    res_df, _ = build_synthetic_data_card_registry(df, profile)
    assert len(res_df) == 1
    assert "not real market data" in res_df.iloc[0]["limitations"]
