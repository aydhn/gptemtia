import pandas as pd
from typing import Tuple, Dict, List, Optional
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_interfaces import BaseCalendarProvider
from advanced_economic_calendar.calendar_provider_models import CalendarProviderCapability

class CalendarProviderRegistry:
    def __init__(self):
        self._providers = {}

    def register(self, provider: BaseCalendarProvider) -> None:
        self._providers[provider.provider_name] = provider

    def list_providers(self) -> List[str]:
        return list(self._providers.keys())

    def get_provider(self, provider_name: str) -> Optional[BaseCalendarProvider]:
        return self._providers.get(provider_name)

    def list_capabilities(self) -> List[CalendarProviderCapability]:
        caps = []
        for p in self._providers.values():
            caps.extend(p.capabilities())
        return caps

    def to_dataframe(self) -> pd.DataFrame:
        data = []
        for p in self._providers.values():
            meta = p.metadata()
            data.append(vars(meta))
        return pd.DataFrame(data)

def build_default_calendar_provider_registry(profile: CalendarProviderProfile) -> CalendarProviderRegistry:
    from advanced_economic_calendar.calendar_dry_run_fixture import CalendarDryRunFixtureProvider
    from advanced_economic_calendar.calendar_manual_file_provider import CalendarManualFileProviderPlaceholder
    from advanced_economic_calendar.calendar_local_cache_provider import CalendarLocalCacheProviderPlaceholder
    from advanced_economic_calendar.calendar_official_api_provider import CalendarOfficialApiProviderPlaceholder
    from advanced_economic_calendar.calendar_licensed_provider import CalendarLicensedProviderPlaceholder
    from advanced_economic_calendar.calendar_public_dataset_provider import CalendarPublicDatasetProviderPlaceholder

    registry = CalendarProviderRegistry()
    registry.register(CalendarDryRunFixtureProvider())
    registry.register(CalendarManualFileProviderPlaceholder())
    registry.register(CalendarLocalCacheProviderPlaceholder())
    registry.register(CalendarOfficialApiProviderPlaceholder())
    registry.register(CalendarLicensedProviderPlaceholder())
    registry.register(CalendarPublicDatasetProviderPlaceholder())
    
    return registry

def build_calendar_provider_registry(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    registry = build_default_calendar_provider_registry(profile)
    df = registry.to_dataframe()
    summary = summarize_calendar_provider_registry(df)
    return df, summary

def summarize_calendar_provider_registry(df: pd.DataFrame) -> Dict:
    return {
        "total_registered_providers": len(df)
    }
