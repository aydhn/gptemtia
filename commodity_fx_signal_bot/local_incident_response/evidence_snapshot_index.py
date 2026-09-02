import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from local_incident_response.incident_config import LocalIncidentResponseProfile

def map_safety_event_evidence_sources(project_root: Path, profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"evidence_source": "mock_source", "description": "Mock evidence mapping."}]
    return pd.DataFrame(data)

def build_safety_event_evidence_snapshot_index(project_root: Path, profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = map_safety_event_evidence_sources(project_root, profile)
    summary = summarize_evidence_snapshot_index(df)
    return df, summary

def summarize_evidence_snapshot_index(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df),
        "note": "Not an audit proof."
    }
