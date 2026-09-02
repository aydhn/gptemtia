import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_governance_no_go_conditions(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    conditions = [
        "real approval claim",
        "committee approval claim",
        "legal/compliance signoff claim",
        "production approval claim",
        "live/broker/deploy claim",
        "investment advice wording",
        "dashboard/telemetry claim",
        "raw secret output",
        "file deletion/move/overwrite claim",
        "cloud upload/package publish claim"
    ]
    data = [{"condition": c, "type": "NO-GO"} for c in conditions]
    return pd.DataFrame(data)

def build_governance_safe_go_conditions(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    conditions = [
        "governance rehearsal documented",
        "manual approval ledger present",
        "non-approval boundaries documented",
        "no-go/safe-go present",
        "escalation matrix present",
        "executive oversight packet present",
        "operator supervision guide present",
        "manual review required"
    ]
    data = [{"condition": c, "type": "SAFE-GO"} for c in conditions]
    return pd.DataFrame(data)

def build_governance_no_go_safe_go_summary(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    no_go = build_governance_no_go_conditions(profile)
    safe_go = build_governance_safe_go_conditions(profile)
    df = pd.concat([no_go, safe_go], ignore_index=True)
    return df, summarize_governance_no_go_safe_go(df)

def summarize_governance_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    if summary_df is None or summary_df.empty:
        return {"total": 0}
    return {
        "no_go_count": len(summary_df[summary_df["type"] == "NO-GO"]),
        "safe_go_count": len(summary_df[summary_df["type"] == "SAFE-GO"])
    }
