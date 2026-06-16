import pandas as pd
import pytest
from artifact_metadata.dataset_cards import build_dataset_card_registry
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile

def test_build_dataset_card_registry():
    df = pd.DataFrame([{
        "artifact_id": "art_1",
        "artifact_type": "dataset_artifact",
        "title": "d1",
        "relative_path": "path/synthetic/data.csv"
    }])

    profile = get_default_artifact_metadata_profile()
    res_df, summary = build_dataset_card_registry(df, profile)

    assert len(res_df) == 1
    card = res_df.iloc[0]
    assert card["card_type"] == "dataset_card"
    assert "synthetic" in card["summary"].lower()
