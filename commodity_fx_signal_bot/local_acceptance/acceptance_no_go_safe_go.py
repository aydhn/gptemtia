import pandas as pd
from pathlib import Path
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def build_acceptance_no_go_register(project_root: Path, profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    nogo = [
        "raw secret present",
        "live/broker/deploy claim",
        "investment advice wording",
        "official sign-off claim",
        "compliance certification claim",
        "production release claim",
        "destructive command safe-listed",
        "package publish claim"
    ]
    df = pd.DataFrame([{"condition": c, "action": "manual review"} for c in nogo])
    return df, {"total_nogo": len(df)}

def build_acceptance_safe_go_register(project_root: Path, profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    safego = [
        "local/offline use only",
        "dry-run outputs available",
        "manual review register present",
        "no-use policy present",
        "evidence trace available",
        "reviewer pack available"
    ]
    df = pd.DataFrame([{"condition": c, "action": "proceed offline"} for c in safego])
    return df, {"total_safego": len(df)}

def build_acceptance_no_go_safe_go_summary(no_go_df: pd.DataFrame, safe_go_df: pd.DataFrame, profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    summary = [{"type": "no_go", "count": len(no_go_df)}, {"type": "safe_go", "count": len(safe_go_df)}]
    df = pd.DataFrame(summary)
    return df, summarize_acceptance_no_go_safe_go(df)

def summarize_acceptance_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"summary": summary_df.to_dict("records")}
