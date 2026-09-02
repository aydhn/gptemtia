import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def build_delivery_no_go_conditions(profile: LocalDeliveryProfile) -> pd.DataFrame:
    conditions = [
        "raw secret included", ".env included", "live/broker/deploy claim",
        "investment advice wording", "official handoff claim", "compliance certification claim",
        "production handoff claim", "destructive command safe-listed", "package publish/cloud upload claim"
    ]
    return pd.DataFrame([{"condition": c, "type": "no-go"} for c in conditions])

def build_delivery_safe_go_conditions(profile: LocalDeliveryProfile) -> pd.DataFrame:
    conditions = [
        "local-only delivery documented", "no-use boundary documented",
        "final delivery manifest present", "handoff index present", "reviewer guide present",
        "transfer checklist present", "acceptance evidence available", "manual review register present"
    ]
    return pd.DataFrame([{"condition": c, "type": "safe-go"} for c in conditions])

def build_delivery_no_go_safe_go_summary(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    no_go = build_delivery_no_go_conditions(profile)
    safe_go = build_delivery_safe_go_conditions(profile)
    df = pd.concat([no_go, safe_go], ignore_index=True)
    return df, summarize_delivery_no_go_safe_go(df)

def summarize_delivery_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"total_conditions": len(summary_df)}
