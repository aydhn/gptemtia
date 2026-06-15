import pandas as pd
import pytest
from artifact_metadata.research_report_cards import build_research_report_card_registry
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile

def test_build_research_report_card_registry():
    df = pd.DataFrame([{
        "artifact_id": "art_1",
        "artifact_type": "research_report_artifact",
        "title": "rr1",
        "relative_path": "path"
    }])
    profile = get_default_artifact_metadata_profile()
    res_df, _ = build_research_report_card_registry(df, profile)
    assert len(res_df) == 1
    assert "documentation_use_only" in res_df.iloc[0]["intended_use"]
