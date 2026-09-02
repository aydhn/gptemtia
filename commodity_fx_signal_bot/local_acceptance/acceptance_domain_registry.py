import pandas as pd
from local_acceptance.acceptance_config import LocalAcceptanceProfile
from local_acceptance.acceptance_models import AcceptanceDomain, build_acceptance_domain_id, acceptance_domain_to_dict
from local_acceptance.acceptance_labels import list_acceptance_domain_labels

def build_default_acceptance_domains(profile: LocalAcceptanceProfile) -> list[AcceptanceDomain]:
    domains = []
    labels = list_acceptance_domain_labels()
    for lbl in labels:
        if lbl == "unknown_acceptance_domain":
            continue
        d = AcceptanceDomain(
            domain_id=build_acceptance_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"Local/offline {lbl.replace('_', ' ')}",
            required_evidence=["docs/README.md"],
            warnings=["Bu domain resmi acceptance scope değildir."]
        )
        domains.append(d)
    return domains

def build_acceptance_domain_registry(profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_acceptance_domains(profile)
    df = pd.DataFrame([acceptance_domain_to_dict(d) for d in domains])
    summary = summarize_acceptance_domains(df)
    return df, summary

def summarize_acceptance_domains(domain_df: pd.DataFrame) -> dict:
    return {
        "total_domains": len(domain_df),
        "domain_labels": domain_df["domain_label"].tolist() if not domain_df.empty else []
    }
