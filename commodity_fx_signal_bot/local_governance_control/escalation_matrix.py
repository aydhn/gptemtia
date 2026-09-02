import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile
from .governance_control_models import EscalationItem, build_escalation_item_id, escalation_item_to_dict

def build_default_escalation_items(profile: LocalGovernanceControlProfile) -> list[EscalationItem]:
    return [
        EscalationItem(
            escalation_id=build_escalation_item_id("Safety Breach Attempt"),
            escalation_area="Safety",
            escalation_label="escalation_blocked_by_no_go",
            trigger_condition="Model output contains live trading claim.",
            recommended_manual_action="Halt operation and review logs.",
            warnings=["Bu otomatik bir süreç değildir."]
        ),
        EscalationItem(
            escalation_id=build_escalation_item_id("External API Request"),
            escalation_area="Network",
            escalation_label="escalation_external_approval_not_allowed",
            trigger_condition="Attempt to connect external service.",
            recommended_manual_action="Block request manually.",
            warnings=["External approval not allowed."]
        )
    ]

def build_escalation_matrix_registry(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_escalation_items(profile)
    df = pd.DataFrame([escalation_item_to_dict(i) for i in items])
    return df, summarize_escalation_matrix(df)

def summarize_escalation_matrix(escalation_df: pd.DataFrame) -> dict:
    if escalation_df is None or escalation_df.empty:
        return {"total": 0}
    return {"total": len(escalation_df)}
