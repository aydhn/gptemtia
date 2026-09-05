
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderProfileItem, build_macro_provider_profile_id

def build_default_macro_provider_profile_items(profile: MacroProviderProfile) -> list[MacroProviderProfileItem]:
    return [
        MacroProviderProfileItem(
            profile_id=build_macro_provider_profile_id(profile.name),
            profile_name=profile.name,
            current_phase=profile.current_phase,
            target_final_phase=profile.target_final_phase,
            next_phase=profile.next_phase,
            local_only=profile.local_only,
            non_production=profile.non_production,
            research_only=profile.research_only,
            no_scraping=True,
            status_label="macro_provider_ready",
            warnings=[]
        )
    ]

def build_macro_provider_profile_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_provider_profile_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_provider_profile_registry(df)

def summarize_macro_provider_profile_registry(df: pd.DataFrame) -> dict:
    return {"total_profiles": len(df)}
