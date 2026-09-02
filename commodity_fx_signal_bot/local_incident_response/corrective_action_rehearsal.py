import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_corrective_actions(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"action": "Update Config", "description": "Mock action."}]
    return pd.DataFrame(data)

def build_corrective_action_rehearsal_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_corrective_actions(profile)
    summary = summarize_corrective_actions(df)
    return df, summary

def summarize_corrective_actions(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df),
        "note": "Not an auto-fix."
    }
