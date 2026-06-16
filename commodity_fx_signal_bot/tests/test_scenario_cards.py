import pandas as pd
import pytest
from artifact_metadata.scenario_cards import build_scenario_card_registry
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile

def test_build_scenario_card_registry():
    df = pd.DataFrame([{
        "artifact_id": "art_1",
        "artifact_type": "scenario_artifact",
        "title": "s1",
        "relative_path": "path"
    }])
    profile = get_default_artifact_metadata_profile()
    res_df, _ = build_scenario_card_registry(df, profile)
    assert len(res_df) == 1
    assert "synthetic scenario demo" in res_df.iloc[0]["intended_use"]
