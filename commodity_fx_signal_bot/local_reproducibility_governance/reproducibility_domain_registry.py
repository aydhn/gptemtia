"""Reproducibility domain registry."""
import pandas as pd
from .reproducibility_config import LocalReproducibilityGovernanceProfile
from .reproducibility_models import ReproducibilityDomain, build_reproducibility_domain_id, reproducibility_domain_to_dict
from .reproducibility_labels import list_reproducibility_domain_labels

def build_default_reproducibility_domains(profile: LocalReproducibilityGovernanceProfile) -> list[ReproducibilityDomain]:
    domains = []
    labels = list_reproducibility_domain_labels()
    for lbl in labels:
        domains.append(ReproducibilityDomain(
            domain_id=build_reproducibility_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"{lbl} domain for offline/local context.",
            required_outputs=["no_raw_secret_here"],
            warnings=["Domain registry official reproducibility scope degildir."]
        ))
    return domains

def build_reproducibility_domain_registry(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_reproducibility_domains(profile)
    df = pd.DataFrame([reproducibility_domain_to_dict(d) for d in domains])
    summary = summarize_reproducibility_domains(df)
    return df, summary

def summarize_reproducibility_domains(domain_df: pd.DataFrame) -> dict:
    return {
        "total_domains": len(domain_df),
        "note": "Domain registry official reproducibility scope degildir."
    }
