import pandas as pd
from .usability_config import LocalUsabilityProfile
from .usability_models import UsabilityDomain, build_usability_domain_id

def build_default_usability_domains(profile: LocalUsabilityProfile) -> list[UsabilityDomain]:
    return [
        UsabilityDomain(
            domain_id=build_usability_domain_id("usability_review_domain"),
            domain_label="usability_review_domain",
            domain_name="Usability Review Domain",
            description="Local/offline usability review domain.",
            required_outputs=["final_local_usability_review"],
            warnings=["Official UX scope değildir."]
        ),
        UsabilityDomain(
            domain_id=build_usability_domain_id("friction_map_domain"),
            domain_label="friction_map_domain",
            domain_name="Friction Map Domain",
            description="Operator friction map domain.",
            required_outputs=["operator_friction_map"],
            warnings=[]
        )
    ]

def build_usability_domain_registry(profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_usability_domains(profile)
    df = pd.DataFrame([d.__dict__ for d in domains])
    summary = {"total_domains": len(domains)}
    return df, summary

def summarize_usability_domains(domain_df: pd.DataFrame) -> dict:
    return {"total": len(domain_df)}
