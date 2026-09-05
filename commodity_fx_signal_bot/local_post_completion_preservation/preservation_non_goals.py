import pandas as pd
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def build_default_preservation_non_goals(profile: LocalPostCompletionPreservationProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"goal": "no real archive seal"},
        {"goal": "no file locking"},
        {"goal": "no chmod"},
        {"goal": "no git tag"},
        {"goal": "no release publish"},
        {"goal": "no cloud archive"},
        {"goal": "no package publish"},
        {"goal": "no deployment"},
        {"goal": "no official approval"},
        {"goal": "no live trading"},
        {"goal": "no broker execution"},
        {"goal": "no investment advice"}
    ])

def build_preservation_non_goals_registry(profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_preservation_non_goals(profile)
    return df, summarize_preservation_non_goals(df)

def summarize_preservation_non_goals(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
