import pandas as pd
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def build_default_immutable_readme_boundaries(profile: LocalPostCompletionPreservationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"boundary": "chmod/read-only", "desc": "no chmod/lock"}])

def build_immutable_readme_boundary_registry(profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_immutable_readme_boundaries(profile)
    return df, summarize_immutable_readme_boundaries(df)

def summarize_immutable_readme_boundaries(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
