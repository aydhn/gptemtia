import pandas as pd
from typing import Tuple, Dict, Optional
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_models import CalendarProviderRequest
from advanced_economic_calendar.calendar_provider_registry import CalendarProviderRegistry
from advanced_economic_calendar.calendar_provider_interfaces import BaseCalendarProvider

def resolve_calendar_provider_for_request(
    request: CalendarProviderRequest,
    registry: CalendarProviderRegistry,
    profile: CalendarProviderProfile,
) -> Optional[BaseCalendarProvider]:
    
    if profile.enable_dry_run_fixture_provider:
        p = registry.get_provider("calendar_dry_run_fixture_provider")
        if p:
            return p
            
    return None

def build_calendar_provider_resolver_map(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    rules = [
        {"rule_id": "rule_1", "condition": "dry_run_enabled", "resolved_provider": "calendar_dry_run_fixture_provider"},
        {"rule_id": "rule_2", "condition": "manual_file", "resolved_provider": "calendar_manual_file_provider_placeholder"}
    ]
    df = pd.DataFrame(rules)
    summary = summarize_calendar_provider_resolver_map(df)
    return df, summary

def summarize_calendar_provider_resolver_map(df: pd.DataFrame) -> Dict:
    return {
        "total_rules": len(df)
    }
