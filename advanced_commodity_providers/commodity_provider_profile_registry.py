
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_models import CommodityProviderProfileItem, build_commodity_provider_profile_id

def build_default_commodity_provider_profile_items(profile: CommodityProviderProfile) -> list[CommodityProviderProfileItem]:
    return [
        CommodityProviderProfileItem(
            profile_id=build_commodity_provider_profile_id(profile.name),
            profile_name=profile.name,
            current_phase=profile.current_phase,
            target_final_phase=profile.target_final_phase,
            next_phase=profile.next_phase,
            local_only=profile.local_only,
            non_production=profile.non_production,
            research_only=profile.research_only,
            no_scraping=not profile.allow_web_scraping,
            status_label="commodity_provider_ready",
            warnings=[]
        )
    ]

def build_commodity_provider_profile_registry(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_commodity_provider_profile_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_commodity_provider_profile_registry(df)

def summarize_commodity_provider_profile_registry(df: pd.DataFrame) -> dict:
    return {"total_profiles": len(df), "columns": list(df.columns)}
