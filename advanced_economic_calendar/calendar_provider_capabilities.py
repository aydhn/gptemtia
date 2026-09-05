import pandas as pd
from typing import Tuple, Dict, List
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_models import CalendarProviderCapability, build_calendar_provider_capability_id

def build_default_calendar_provider_capabilities(profile: CalendarProviderProfile) -> List[CalendarProviderCapability]:
    caps = [
        ("calendar_dry_run_fixture", "provider_dry_run_fixture", ["event_central_bank_policy", "event_inflation"], ["calendar_data_event_schedule", "calendar_data_release_event"]),
        ("calendar_manual_file_provider", "provider_manual_file", ["event_central_bank_policy"], ["calendar_data_event_schedule", "calendar_data_release_event"]),
        ("calendar_local_cache_provider", "provider_local_cache", ["event_central_bank_policy"], ["calendar_data_event_schedule", "calendar_data_release_event"]),
        ("calendar_official_api_placeholder", "provider_official_api", ["event_central_bank_policy", "event_inflation", "event_labor", "event_growth", "event_pmi_sentiment", "event_energy_inventory"], ["calendar_data_event_schedule", "calendar_data_release_event"]),
        ("calendar_licensed_placeholder", "provider_licensed", ["event_central_bank_policy"], ["calendar_data_event_schedule", "calendar_data_release_event"]),
        ("calendar_public_dataset_placeholder", "provider_public_dataset", ["event_central_bank_policy"], ["calendar_data_event_schedule"])
    ]
    
    return [CalendarProviderCapability(
        capability_id=build_calendar_provider_capability_id(c[0], c[3][0]),
        provider_name=c[0],
        provider_type=c[1],
        event_categories=c[2],
        data_types=c[3],
        region_support=["GLOBAL"],
        requires_network=False,
        requires_credentials=False,
        supports_local_cache=True,
        no_scraping_compliant=True,
        status_label="calendar_provider_ready",
        warnings=[]
    ) for c in caps]

def build_calendar_provider_capability_registry(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_calendar_provider_capabilities(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_calendar_provider_capabilities(df)
    return df, summary

def summarize_calendar_provider_capabilities(df: pd.DataFrame) -> Dict:
    return {
        "total_capabilities": len(df)
    }
