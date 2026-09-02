import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_escalation_decisions(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"decision": "Escalate to L2", "criteria": "Mock criteria."}]
    return pd.DataFrame(data)

def build_escalation_decision_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_escalation_decisions(profile)
    summary = summarize_escalation_decisions(df)
    return df, summary

def summarize_escalation_decisions(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df),
        "note": "Does not automatically escalate."
    }
