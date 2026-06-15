import pandas as pd
import pytest
from artifact_metadata.reproducibility_cards import build_reproducibility_card_registry, build_reproducibility_checklist
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile

def test_reproducibility_cards_and_checklist():
    df = pd.DataFrame([{
        "artifact_id": "art_1",
        "artifact_type": "model_artifact",
        "title": "m1",
        "relative_path": "path"
    }])

    profile = get_default_artifact_metadata_profile()
    r_df, r_sum = build_reproducibility_card_registry(df, profile)
    c_df, c_sum = build_reproducibility_checklist(df, profile)

    assert len(r_df) == 1
    assert r_df.iloc[0]["reproducibility"] == "reproducible_with_warnings"

    assert len(c_df) == 3 # 3 checks
