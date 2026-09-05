import pandas as pd
from typing import Tuple, Dict, List
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_models import CalendarProviderMetadata, build_calendar_provider_metadata_id

def build_default_calendar_provider_metadata(profile: CalendarProviderProfile) -> List[CalendarProviderMetadata]:
    providers = [
        ("calendar_dry_run_fixture_provider", "provider_dry_run_fixture"),
        ("calendar_manual_file_provider_placeholder", "provider_manual_file"),
        ("calendar_local_cache_provider_placeholder", "provider_local_cache"),
        ("calendar_official_api_provider_placeholder", "provider_official_api"),
        ("calendar_licensed_provider_placeholder", "provider_licensed"),
        ("calendar_public_dataset_provider_placeholder", "provider_public_dataset")
    ]
    
    return [CalendarProviderMetadata(
        provider_id=build_calendar_provider_metadata_id(p[0]),
        provider_name=p[0],
        provider_type=p[1],
        description=f"{p[0]} metadata",
        homepage_ref="none",
        license_note="manual review required",
        credential_policy="not stored/not printed/manual configuration only",
        no_scraping_policy="compliant",
        calendar_coverage_note="coverage placeholder",
        status_label="calendar_provider_ready",
        warnings=[]
    ) for p in providers]

def validate_calendar_provider_metadata_item(item: CalendarProviderMetadata, profile: CalendarProviderProfile) -> Dict:
    return {"valid": True, "errors": []}

def build_calendar_provider_metadata_registry(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_calendar_provider_metadata(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_calendar_provider_metadata(df)
    return df, summary

def summarize_calendar_provider_metadata(df: pd.DataFrame) -> Dict:
    return {
        "total_metadata": len(df)
    }
