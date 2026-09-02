import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_rollback_boundaries(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"boundary": "Config", "allowed": False}]
    return pd.DataFrame(data)

def build_default_non_rollback_boundaries(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"boundary": "Database", "allowed": False}]
    return pd.DataFrame(data)

def build_rollback_boundary_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_rollback_boundaries(profile)
    summary = summarize_rollback_boundaries(df, pd.DataFrame())
    return df, summary

def build_non_rollback_boundary_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_non_rollback_boundaries(profile)
    summary = summarize_rollback_boundaries(pd.DataFrame(), df)
    return df, summary

def summarize_rollback_boundaries(rollback_df: pd.DataFrame, non_rollback_df: pd.DataFrame) -> Dict:
    return {
        "rollback_count": len(rollback_df) if not rollback_df.empty else 0,
        "non_rollback_count": len(non_rollback_df) if not non_rollback_df.empty else 0,
        "note": "Offline boundaries."
    }
