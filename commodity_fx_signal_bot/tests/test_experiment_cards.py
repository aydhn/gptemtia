import pandas as pd
import pytest
from artifact_metadata.experiment_cards import build_experiment_card_registry
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile

def test_build_experiment_card_registry():
    df = pd.DataFrame([{
        "artifact_id": "art_1",
        "artifact_type": "experiment_artifact",
        "title": "e1",
        "relative_path": "path"
    }])

    profile = get_default_artifact_metadata_profile()
    res_df, summary = build_experiment_card_registry(df, profile)

    assert len(res_df) == 1
    card = res_df.iloc[0]
    assert card["card_type"] == "experiment_card"
    assert "yatirim tavsiyesi icin kullanilamaz" in card["non_use_policy"].lower()
