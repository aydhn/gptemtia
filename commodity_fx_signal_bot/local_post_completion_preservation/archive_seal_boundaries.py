import pandas as pd
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def build_default_archive_seal_boundaries(profile: LocalPostCompletionPreservationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"boundary": "seal", "desc": "Offline rehearsal only"}])

def build_default_non_seal_boundaries(profile: LocalPostCompletionPreservationProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"boundary": "no chmod", "desc": "no chmod"},
        {"boundary": "no read-only lock", "desc": "no lock"},
        {"boundary": "no git tag", "desc": "no tag"},
        {"boundary": "no release publish", "desc": "no release"},
        {"boundary": "no package publish", "desc": "no package"},
        {"boundary": "no cloud upload", "desc": "no cloud"},
        {"boundary": "no deployment", "desc": "no deploy"},
        {"boundary": "no official archive approval", "desc": "no approval"},
        {"boundary": "no legal/compliance sign-off", "desc": "no signoff"}
    ])

def build_archive_seal_boundary_registry(profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_archive_seal_boundaries(profile)
    return df, {"count": len(df)}

def build_non_seal_boundary_registry(profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_non_seal_boundaries(profile)
    return df, {"count": len(df)}

def summarize_archive_seal_boundaries(seal_df: pd.DataFrame, non_seal_df: pd.DataFrame) -> dict:
    return {"seal": len(seal_df), "non_seal": len(non_seal_df)}
