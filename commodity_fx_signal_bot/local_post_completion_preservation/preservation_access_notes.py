import pandas as pd
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def build_default_preservation_access_notes(profile: LocalPostCompletionPreservationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"note": "Access notes permission management degildir."}])

def build_preservation_access_note_registry(profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_preservation_access_notes(profile)
    return df, summarize_preservation_access_notes(df)

def summarize_preservation_access_notes(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
