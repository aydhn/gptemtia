import pandas as pd
import pytest
from artifact_metadata.model_cards import build_model_card_registry
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile

def test_build_model_card_registry():
    df = pd.DataFrame([{
        "artifact_id": "art_1",
        "artifact_type": "model_artifact",
        "title": "m1",
        "relative_path": "path"
    }])

    profile = get_default_artifact_metadata_profile()
    res_df, summary = build_model_card_registry(df, profile)

    assert len(res_df) == 1
    assert summary["total_model_cards"] == 1

    card = res_df.iloc[0]
    assert card["card_type"] == "model_card"
    assert "deployment onayi degildir" in card["non_use_policy"].lower()
    assert "unknown/not available" in card["metrics"]
