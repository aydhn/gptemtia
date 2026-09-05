import pandas as pd
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def build_default_evidence_vault_limitations(profile: LocalPostCompletionPreservationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"limit": "Not legal/audit evidence vault"}])

def build_evidence_vault_limitation_register(profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_evidence_vault_limitations(profile)
    return df, summarize_evidence_vault_limitations(df)

def summarize_evidence_vault_limitations(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
