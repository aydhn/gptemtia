import pandas as pd
from typing import Tuple, Dict, List
from local_incident_response.incident_config import LocalIncidentResponseProfile
from local_incident_response.incident_models import IncidentDomain, build_incident_domain_id, incident_domain_to_dict

def build_default_incident_domains(profile: LocalIncidentResponseProfile) -> List[IncidentDomain]:
    labels = [
        "incident_rehearsal_domain", "safety_event_domain", "incident_taxonomy_domain",
        "incident_triage_domain", "incident_classification_domain", "rollback_rehearsal_domain",
        "containment_rehearsal_domain", "degraded_mode_domain", "recovery_rehearsal_domain",
        "resilience_supervision_domain", "post_incident_review_domain", "corrective_action_domain",
        "escalation_domain", "quality_validation_domain"
    ]
    domains = []
    for lbl in labels:
        domains.append(IncidentDomain(
            domain_id=build_incident_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"Local/offline mock domain for {lbl}",
            required_outputs=["mock_report"],
            warnings=["Offline context only."]
        ))
    return domains

def build_incident_domain_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    domains = build_default_incident_domains(profile)
    df = pd.DataFrame([incident_domain_to_dict(d) for d in domains])
    summary = summarize_incident_domains(df)
    return df, summary

def summarize_incident_domains(domain_df: pd.DataFrame) -> Dict:
    return {
        "total_domains": len(domain_df) if domain_df is not None else 0,
        "note": "This is not an official incident response scope."
    }
