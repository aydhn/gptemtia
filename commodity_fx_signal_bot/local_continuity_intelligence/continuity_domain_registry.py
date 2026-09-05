import pandas as pd
from .continuity_models import ContinuityDomain, build_continuity_domain_id
from .continuity_labels import list_continuity_domain_labels

def build_continuity_domain_registry(profile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_continuity_domains(profile)
    df = pd.DataFrame([d.__dict__ for d in domains])
    summary = summarize_continuity_domains(df)
    return df, summary

def build_default_continuity_domains(profile) -> list[ContinuityDomain]:
    labels = list_continuity_domain_labels()
    return [ContinuityDomain(
        domain_id=build_continuity_domain_id(l),
        domain_label=l,
        domain_name=f"Domain {l}",
        description="Local offline domain",
        required_outputs=["none"],
        warnings=["Not official scope"]
    ) for l in labels]

def summarize_continuity_domains(domain_df: pd.DataFrame) -> dict:
    return {"total": len(domain_df)}