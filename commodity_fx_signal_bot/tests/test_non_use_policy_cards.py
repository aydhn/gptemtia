import pandas as pd
import pytest
from artifact_metadata.non_use_policy_cards import build_non_use_policy_cards, build_global_non_use_policy
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile

def test_build_non_use_policy_cards():
    df = pd.DataFrame([{
        "artifact_id": "art_1",
        "artifact_type": "model_artifact",
        "title": "l1",
        "relative_path": "path"
    }])
    profile = get_default_artifact_metadata_profile()
    res_df, _ = build_non_use_policy_cards(df, profile)
    assert len(res_df) == 1
    assert "canli emir" in res_df.iloc[0]["non_use_policy"].lower()

    global_pol = build_global_non_use_policy(profile)
    assert "broker talimati" in global_pol
