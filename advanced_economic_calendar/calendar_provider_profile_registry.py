import pandas as pd
from typing import Tuple, Dict, List
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile, list_calendar_provider_profiles
from advanced_economic_calendar.calendar_provider_models import CalendarProviderProfileItem, build_calendar_provider_profile_id
from advanced_economic_calendar.calendar_provider_labels import list_calendar_provider_status_labels

def build_default_calendar_provider_profile_items(profile: CalendarProviderProfile) -> List[CalendarProviderProfileItem]:
    items = []
    for p in list_calendar_provider_profiles(enabled_only=True):
        items.append(CalendarProviderProfileItem(
            profile_id=build_calendar_provider_profile_id(p.name),
            profile_name=p.name,
            current_phase=p.current_phase,
            target_final_phase=p.target_final_phase,
            next_phase=p.next_phase,
            local_only=p.local_only,
            non_production=p.non_production,
            research_only=p.research_only,
            no_scraping=not p.allow_web_scraping,
            status_label="calendar_provider_ready",
            warnings=[]
        ))
    return items

def build_economic_calendar_provider_profile_registry(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_calendar_provider_profile_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_calendar_provider_profile_registry(df)
    return df, summary

def summarize_calendar_provider_profile_registry(df: pd.DataFrame) -> Dict:
    return {
        "total_profiles": len(df),
        "profiles": df["profile_name"].tolist() if not df.empty else []
    }
