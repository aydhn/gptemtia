
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_models import CommodityProviderDomain, build_commodity_provider_domain_id
from .commodity_provider_labels import list_commodity_domain_labels

def build_default_commodity_provider_domains(profile: CommodityProviderProfile) -> list[CommodityProviderDomain]:
    return [
        CommodityProviderDomain(
            domain_id=build_commodity_provider_domain_id(label),
            domain_label=label,
            domain_name=label.replace('_', ' ').title(),
            description=f"Domain for {label}",
            required_outputs=[],
            warnings=[]
        ) for label in list_commodity_domain_labels() if label != "unknown_commodity_domain"
    ]

def build_commodity_provider_domain_registry(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_commodity_provider_domains(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_commodity_provider_domains(df)

def summarize_commodity_provider_domains(df: pd.DataFrame) -> dict:
    return {"total_domains": len(df)}
