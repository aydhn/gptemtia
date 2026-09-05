import pandas as pd
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def build_default_preservation_handoff_items(profile: LocalPostCompletionPreservationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"item": "gercek onay degildir."}])

def build_preservation_handoff_checklist(profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_preservation_handoff_items(profile)
    return df, summarize_preservation_handoff(df)

def summarize_preservation_handoff(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
