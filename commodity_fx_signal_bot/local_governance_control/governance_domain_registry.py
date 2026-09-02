import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile
from .governance_control_models import GovernanceDomain, build_governance_domain_id, governance_domain_to_dict
from .governance_control_labels import list_governance_domain_labels

def build_default_governance_domains(profile: LocalGovernanceControlProfile) -> list[GovernanceDomain]:
    domains = []
    labels = list_governance_domain_labels()
    for lbl in labels:
        if lbl == "unknown_governance_domain":
            continue
        dom = GovernanceDomain(
            domain_id=build_governance_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"Local/offline {lbl.replace('_', ' ')} for rehearsal.",
            required_outputs=["document"],
            warnings=["Bu domain official governance scope değildir."]
        )
        domains.append(dom)
    return domains

def build_governance_domain_registry(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_governance_domains(profile)
    df = pd.DataFrame([governance_domain_to_dict(d) for d in domains])
    summary = summarize_governance_domains(df)
    return df, summary

def summarize_governance_domains(domain_df: pd.DataFrame) -> dict:
    if domain_df is None or domain_df.empty:
        return {"total": 0}
    return {
        "total": len(domain_df),
        "domains": domain_df["domain_label"].tolist()
    }
