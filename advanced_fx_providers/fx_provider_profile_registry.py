import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderProfileItem, build_fx_provider_profile_id

def build_default_fx_provider_profile_items(profile: FXProviderProfile) -> List[FXProviderProfileItem]:
    return [
        FXProviderProfileItem(
            profile_id=build_fx_provider_profile_id(profile.name),
            profile_name=profile.name,
            current_phase=profile.current_phase,
            target_final_phase=profile.target_final_phase,
            next_phase=profile.next_phase,
            local_only=profile.local_only,
            non_production=profile.non_production,
            research_only=profile.research_only,
            no_scraping=not profile.allow_web_scraping,
            status_label="fx_provider_ready",
            warnings=[]
        )
    ]

def build_fx_provider_profile_registry(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_fx_provider_profile_items(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_fx_provider_profile_registry(df)

def summarize_fx_provider_profile_registry(df: pd.DataFrame) -> Dict:
    return {
        "total_profiles": len(df),
        "profiles": df["profile_name"].tolist() if not df.empty else []
    }
