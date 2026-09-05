"""Long-term domain registry."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile
from .longterm_models import LongTermDomain, build_longterm_domain_id, longterm_domain_to_dict

def build_default_longterm_domains(profile: LocalLongTermOperationsProfile) -> list[LongTermDomain]:
    labels = [
        "longterm_operations_binder_domain",
        "review_calendar_domain",
        "lifecycle_maintenance_domain",
        "maintenance_cadence_domain",
        "retention_review_domain",
        "quality_safety_review_domain",
        "incident_redteam_governance_review_domain",
        "deprecation_rehearsal_domain",
        "migration_readiness_domain",
        "roadmap_governance_domain",
        "feature_intake_domain",
        "change_control_domain",
        "quality_validation_domain"
    ]
    domains = []
    for lbl in labels:
        domains.append(LongTermDomain(
            domain_id=build_longterm_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"Local/offline {lbl.replace('_', ' ')} rehearsal.",
            required_outputs=["rehearsal_report.md"],
            warnings=["Bu domain official operations scope değildir."]
        ))
    return domains

def build_longterm_domain_registry(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_longterm_domains(profile)
    df = pd.DataFrame([longterm_domain_to_dict(d) for d in domains])
    summary = summarize_longterm_domains(df)
    return df, summary

def summarize_longterm_domains(domain_df: pd.DataFrame) -> dict:
    return {
        "total_domains": len(domain_df),
        "domain_labels": domain_df["domain_label"].tolist() if not domain_df.empty else []
    }
