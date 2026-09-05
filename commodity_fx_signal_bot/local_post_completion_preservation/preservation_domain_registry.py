import pandas as pd
from local_post_completion_preservation.preservation_models import PreservationDomain, build_preservation_domain_id, preservation_domain_to_dict
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile
from local_post_completion_preservation.preservation_labels import list_preservation_domain_labels

def build_default_preservation_domains(profile: LocalPostCompletionPreservationProfile) -> list[PreservationDomain]:
    labels = list_preservation_domain_labels()
    return [
        PreservationDomain(
            domain_id=build_preservation_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description="Offline/local rehearsal domain",
            required_outputs=["rehearsal_report"],
            warnings=["Not official archive scope"]
        ) for lbl in labels
    ]

def build_preservation_domain_registry(profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_preservation_domains(profile)
    df = pd.DataFrame([preservation_domain_to_dict(d) for d in domains])
    summary = summarize_preservation_domains(df)
    return df, summary

def summarize_preservation_domains(domain_df: pd.DataFrame) -> dict:
    return {"total_domains": len(domain_df)}
