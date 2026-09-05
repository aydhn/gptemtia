import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderDomain, build_fx_provider_domain_id
from .fx_provider_labels import list_fx_domain_labels

def build_default_fx_provider_domains(profile: FXProviderProfile) -> List[FXProviderDomain]:
    return [
        FXProviderDomain(
            domain_id=build_fx_provider_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"Domain for {lbl}",
            required_outputs=["schema", "registry"],
            warnings=[]
        ) for lbl in list_fx_domain_labels() if lbl != "unknown_fx_domain"
    ]

def build_fx_provider_domain_registry(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_fx_provider_domains(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_fx_provider_domains(df)

def summarize_fx_provider_domains(df: pd.DataFrame) -> Dict:
    return {
        "total_domains": len(df),
        "domains": df["domain_label"].tolist() if not df.empty else []
    }
