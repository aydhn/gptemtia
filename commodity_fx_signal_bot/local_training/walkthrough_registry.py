import pandas as pd
from .training_config import LocalTrainingProfile

def build_default_walkthroughs(profile: LocalTrainingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"name": "repo ilk okuma", "desc": "Walkthrough"},
        {"name": "kurulum dokümanını okuma", "desc": "Walkthrough"},
        {"name": "status report okuma", "desc": "Walkthrough"},
        {"name": "quality report okuma", "desc": "Walkthrough"},
        {"name": "DataLake klasörlerini gezme", "desc": "Walkthrough"},
        {"name": "local graph query çıktısını okuma", "desc": "Walkthrough"},
        {"name": "timeline event report okuma", "desc": "Walkthrough"},
        {"name": "consistency gap report okuma", "desc": "Walkthrough"},
        {"name": "readiness binder okuma", "desc": "Walkthrough"},
        {"name": "maintenance runbook okuma", "desc": "Walkthrough"},
        {"name": "archive manifest okuma", "desc": "Walkthrough"},
        {"name": "DR tabletop report okuma", "desc": "Walkthrough"}
    ])

def build_guided_walkthrough_registry(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_walkthroughs(profile)
    return df, summarize_guided_walkthroughs(df)

def summarize_guided_walkthroughs(walkthrough_df: pd.DataFrame) -> dict:
    if walkthrough_df is None or walkthrough_df.empty: return {"count": 0}
    return {"count": len(walkthrough_df)}
