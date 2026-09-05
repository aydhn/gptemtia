import pandas as pd
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def build_preservation_no_go_conditions(profile: LocalPostCompletionPreservationProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"cond": "real archive seal claim"},
        {"cond": "immutable lock claim"},
        {"cond": "chmod/permission change claim"},
        {"cond": "git tag claim"},
        {"cond": "release publish claim"},
        {"cond": "package publish claim"},
        {"cond": "docker build/push claim"},
        {"cond": "cloud upload claim"},
        {"cond": "deployment claim"},
        {"cond": "official archive approval claim"},
        {"cond": "legal/compliance sign-off claim"},
        {"cond": "live/broker/deploy claim"},
        {"cond": "investment advice wording"},
        {"cond": "telemetry/dashboard claim"},
        {"cond": "raw secret output"},
        {"cond": "file deletion/move/overwrite claim"}
    ])

def build_preservation_safe_go_conditions(profile: LocalPostCompletionPreservationProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"cond": "archive seal rehearsal documented"},
        {"cond": "immutable README rehearsal documented"},
        {"cond": "evidence vault index available"},
        {"cond": "knowledge capsule available"},
        {"cond": "preservation binder available"},
        {"cond": "preservation inventories available"},
        {"cond": "fingerprint rehearsal available"},
        {"cond": "restore notes rehearsal available"},
        {"cond": "non-goals documented"},
        {"cond": "manual review required"},
        {"cond": "no file locking/chmod/release/deploy/live/broker/advice"}
    ])

def build_preservation_no_go_safe_go_summary(profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    nogo = build_preservation_no_go_conditions(profile)
    safego = build_preservation_safe_go_conditions(profile)
    df = pd.concat([nogo, safego], ignore_index=True)
    return df, summarize_preservation_no_go_safe_go(df)

def summarize_preservation_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"count": len(summary_df)}
