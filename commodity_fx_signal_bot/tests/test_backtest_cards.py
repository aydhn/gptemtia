import pandas as pd
import pytest
from artifact_metadata.backtest_cards import build_backtest_card_registry
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile

def test_build_backtest_card_registry():
    df = pd.DataFrame([{
        "artifact_id": "art_1",
        "artifact_type": "backtest_artifact",
        "title": "b1",
        "relative_path": "path"
    }])
    profile = get_default_artifact_metadata_profile()
    res_df, _ = build_backtest_card_registry(df, profile)
    assert len(res_df) == 1
    assert "offline/local only" in res_df.iloc[0]["limitations"]
