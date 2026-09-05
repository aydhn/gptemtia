import pandas as pd
from .completion_models import CompletionDomain, build_completion_domain_id, completion_domain_to_dict
from .completion_config import LocalProjectCompletionProfile
from .completion_labels import list_completion_domain_labels

def build_default_completion_domains(profile: LocalProjectCompletionProfile) -> list[CompletionDomain]:
    domains = []
    labels = list_completion_domain_labels()
    for lbl in labels:
        if lbl == "unknown_completion_domain": continue
        domains.append(CompletionDomain(
            domain_id=build_completion_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"Local/offline {lbl.replace('_', ' ')}",
            required_outputs=[f"{lbl}_report.md"],
            warnings=["Offline system closure context only. No raw secrets."]
        ))
    return domains

def build_completion_domain_registry(profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_completion_domains(profile)
    df = pd.DataFrame([completion_domain_to_dict(d) for d in domains])
    return df, summarize_completion_domains(df)

def summarize_completion_domains(domain_df: pd.DataFrame) -> dict:
    return {
        "total_domains": len(domain_df),
        "note": "Domain registry is not official completion scope."
    }
