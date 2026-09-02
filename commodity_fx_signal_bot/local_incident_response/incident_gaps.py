import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def detect_missing_incident_domains(domain_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing_domain"}]) if domain_df is None or domain_df.empty else pd.DataFrame()

def detect_missing_safety_events(event_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing_event"}]) if event_df is None or event_df.empty else pd.DataFrame()

def detect_missing_triage_items(triage_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing_triage"}]) if triage_df is None or triage_df.empty else pd.DataFrame()

def detect_missing_recovery_items(recovery_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing_recovery"}]) if recovery_df is None or recovery_df.empty else pd.DataFrame()

def build_incident_gap_register(
    domain_df: pd.DataFrame,
    event_df: pd.DataFrame,
    triage_df: pd.DataFrame,
    recovery_df: pd.DataFrame,
    profile: LocalIncidentResponseProfile,
) -> Tuple[pd.DataFrame, Dict]:
    gaps = pd.concat([
        detect_missing_incident_domains(domain_df),
        detect_missing_safety_events(event_df),
        detect_missing_triage_items(triage_df),
        detect_missing_recovery_items(recovery_df)
    ], ignore_index=True)
    
    summary = summarize_incident_gaps(gaps)
    return gaps, summary

def summarize_incident_gaps(gap_df: pd.DataFrame) -> Dict:
    return {
        "count": len(gap_df),
        "note": "No auto-fix provided."
    }
