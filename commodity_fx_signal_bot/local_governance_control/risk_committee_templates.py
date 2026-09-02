import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_risk_committee_agenda_templates(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [
        {"agenda_item": "Review no-go conditions", "duration_mins": 15},
        {"agenda_item": "Review quality warnings", "duration_mins": 20},
        {"agenda_item": "Check manual approval ledger", "duration_mins": 15}
    ]
    return pd.DataFrame(data)

def build_default_risk_committee_decisions(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [
        {"decision_id": "DEC-001", "decision": "Rehearsal completed", "status": "rehearsal_only"}
    ]
    return pd.DataFrame(data)

def build_risk_committee_agenda_template_registry(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_risk_committee_agenda_templates(profile)
    return df, {"total_items": len(df)}

def build_risk_committee_decision_rehearsal_ledger(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_risk_committee_decisions(profile)
    return df, {"total_decisions": len(df)}

def summarize_risk_committee_templates(agenda_df: pd.DataFrame, decision_df: pd.DataFrame) -> dict:
    return {
        "agenda_items": len(agenda_df) if agenda_df is not None else 0,
        "decisions": len(decision_df) if decision_df is not None else 0
    }
