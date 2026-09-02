import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_incident_no_go_conditions(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [
        {"condition": "real incident response claim"},
        {"condition": "real rollback claim"},
        {"condition": "forensic analysis claim"},
        {"condition": "production recovery claim"},
        {"condition": "live halt/broker halt claim"},
        {"condition": "compliance/legal sign-off claim"},
        {"condition": "live/broker/deploy claim"},
        {"condition": "investment advice wording"},
        {"condition": "telemetry/dashboard claim"},
        {"condition": "raw secret output"},
        {"condition": "file deletion/move/overwrite claim"},
        {"condition": "cloud upload/package publish claim"}
    ]
    return pd.DataFrame(data)

def build_incident_safe_go_conditions(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [
        {"condition": "offline safety event register available"},
        {"condition": "rollback decision playbook documented"},
        {"condition": "non-rollback boundaries documented"},
        {"condition": "containment/recovery rehearsal documented"},
        {"condition": "post-incident review templates available"},
        {"condition": "no real rollback"},
        {"condition": "no production recovery"},
        {"condition": "manual review required"}
    ]
    return pd.DataFrame(data)

def build_incident_no_go_safe_go_summary(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    no_go_df = build_incident_no_go_conditions(profile)
    safe_go_df = build_incident_safe_go_conditions(profile)
    
    summary_df = pd.DataFrame([
        {"type": "no_go", "count": len(no_go_df)},
        {"type": "safe_go", "count": len(safe_go_df)}
    ])
    summary = summarize_incident_no_go_safe_go(summary_df)
    return summary_df, summary

def summarize_incident_no_go_safe_go(summary_df: pd.DataFrame) -> Dict:
    return {
        "rows": len(summary_df),
        "note": "Safe-go is not real incident response approval."
    }
