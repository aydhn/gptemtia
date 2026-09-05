
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderDomain, build_macro_provider_domain_id

def build_default_macro_provider_domains(profile: MacroProviderProfile) -> list[MacroProviderDomain]:
    return [
        MacroProviderDomain(
            domain_id=build_macro_provider_domain_id("macro_provider_profile"),
            domain_label="macro_provider_profile_domain",
            domain_name="Macro Provider Profile",
            description="Profile configuration",
            required_outputs=[],
            warnings=[]
        )
    ]

def build_macro_provider_domain_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_provider_domains(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_provider_domains(df)

def summarize_macro_provider_domains(df: pd.DataFrame) -> dict:
    return {"total_domains": len(df)}
