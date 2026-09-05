import pandas as pd
from .completion_config import LocalProjectCompletionProfile

def build_completion_no_go_conditions(profile: LocalProjectCompletionProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "real project closure claim"},
        {"condition": "official completion approval claim"},
        {"condition": "production approval claim"},
        {"condition": "official acceptance claim"},
        {"condition": "legal/compliance sign-off claim"},
        {"condition": "package publish claim"},
        {"condition": "docker build/push claim"},
        {"condition": "git tag claim"},
        {"condition": "cloud upload claim"},
        {"condition": "deployment claim"},
        {"condition": "live/broker/deploy claim"},
        {"condition": "investment advice wording"},
        {"condition": "telemetry/dashboard claim"},
        {"condition": "raw secret output"},
        {"condition": "file deletion/move/overwrite claim"}
    ])

def build_completion_safe_go_conditions(profile: LocalProjectCompletionProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "offline system closure dossier documented", "manual_review_required": True},
        {"condition": "terminal handoff pack documented", "manual_review_required": True},
        {"condition": "knowledge freeze rehearsal documented", "manual_review_required": True},
        {"condition": "last-mile audit binder documented", "manual_review_required": True},
        {"condition": "completion evidence map available", "manual_review_required": True},
        {"condition": "final inventories available", "manual_review_required": True},
        {"condition": "final recaps available", "manual_review_required": True},
        {"condition": "manual review required", "manual_review_required": True},
        {"condition": "no real closure approval", "manual_review_required": True},
        {"condition": "no deployment/publish/live/broker/advice", "manual_review_required": True}
    ])

def build_completion_no_go_safe_go_summary(profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    no_go = build_completion_no_go_conditions(profile)
    safe_go = build_completion_safe_go_conditions(profile)
    df = pd.concat([no_go, safe_go], ignore_index=True)
    return df, summarize_completion_no_go_safe_go(df)

def summarize_completion_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"items": len(summary_df), "note": "Safe-go gerçek closure approval değildir."}
