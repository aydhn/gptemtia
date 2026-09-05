import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile
from local_review_governance.review_models import ReviewDomain, build_review_domain_id, review_domain_to_dict
from local_review_governance.review_labels import list_review_domain_labels

def build_default_review_domains(profile: LocalReviewGovernanceProfile) -> list[ReviewDomain]:
    labels = list_review_domain_labels()
    domains = []
    for label in labels:
        if label == "unknown_review_domain":
            continue
        domains.append(
            ReviewDomain(
                domain_id=build_review_domain_id(label),
                domain_label=label,
                domain_name=label.replace("_", " ").title(),
                description=f"Local/offline {label.replace('_', ' ')} for rehearsal purposes.",
                required_outputs=[f"{label}_output_1", f"{label}_output_2"],
                warnings=["Not a real approval workflow", "No official sign-off"]
            )
        )
    return domains

def build_review_governance_domain_registry(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_review_domains(profile)
    df = pd.DataFrame([review_domain_to_dict(d) for d in domains])
    summary = summarize_review_domains(df)
    return df, summary

def summarize_review_domains(domain_df: pd.DataFrame) -> dict:
    return {
        "total_domains": len(domain_df),
        "domains": domain_df["domain_name"].tolist() if not domain_df.empty else []
    }
