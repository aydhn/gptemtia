import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def detect_incident_exceptions(event_df: pd.DataFrame, rollback_df: pd.DataFrame, no_go_df: pd.DataFrame) -> pd.DataFrame:
    data = [{"exception": "Mock exception", "description": "Mock description"}]
    return pd.DataFrame(data)

def build_incident_exception_register(event_df: pd.DataFrame, rollback_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = detect_incident_exceptions(event_df, rollback_df, no_go_df)
    summary = summarize_incident_exceptions(df)
    return df, summary

def summarize_incident_exceptions(exception_df: pd.DataFrame) -> Dict:
    return {
        "count": len(exception_df),
        "note": "Does not perform real rollback."
    }
