import pandas as pd
from local_delivery.delivery_config import LocalDeliveryProfile
from local_delivery.delivery_models import DeliveryDomain, build_delivery_domain_id, delivery_domain_to_dict

def build_default_delivery_domains(profile: LocalDeliveryProfile) -> list[DeliveryDomain]:
    domains = []
    labels = [
        "bundle_manifest_domain", "handoff_index_domain", "reviewer_guide_domain",
        "transfer_checklist_domain", "evidence_map_domain", "delivery_rehearsal_domain",
        "recipient_orientation_domain", "safety_boundary_domain", "readiness_scoring_domain",
        "quality_validation_domain"
    ]
    for lbl in labels:
        domains.append(DeliveryDomain(
            domain_id=build_delivery_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"Local/offline {lbl.replace('_', ' ')} for delivery rehearsal",
            required_items=["README.md", "SAFE_USAGE_GUIDE.md"],
            warnings=[]
        ))
    return domains

def build_delivery_domain_registry(profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_delivery_domains(profile)
    df = pd.DataFrame([delivery_domain_to_dict(d) for d in domains])
    return df, summarize_delivery_domains(df)

def summarize_delivery_domains(domain_df: pd.DataFrame) -> dict:
    if domain_df is None or domain_df.empty:
        return {"total_domains": 0}
    return {
        "total_domains": len(domain_df),
        "domains_listed": domain_df["domain_label"].tolist()
    }
