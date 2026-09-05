import pandas as pd
from .provider_config import DataProviderAbstractionProfile
from .provider_models import ProviderProfileItem, build_provider_profile_id
from dataclasses import asdict

def build_default_provider_profile_items(profile: DataProviderAbstractionProfile) -> list[ProviderProfileItem]:
    return [
        ProviderProfileItem(
            profile_id=build_provider_profile_id(profile.name),
            profile_name=profile.name,
            current_phase=106,
            target_final_phase=160,
            next_phase=107,
            local_only=True,
            non_production=True,
            research_only=True,
            no_scraping=True,
            status_label="provider_ready",
            warnings=[]
        )
    ]

def build_data_provider_abstraction_profile_registry(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_provider_profile_items(profile)
    df = pd.DataFrame([asdict(item) for item in items])
    return df, summarize_provider_profile_registry(df)

def summarize_provider_profile_registry(df: pd.DataFrame) -> dict:
    return {"total_profiles": len(df)}
