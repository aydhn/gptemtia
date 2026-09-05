import pandas as pd
from typing import Tuple, Dict, List
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_interfaces import BaseCalendarProvider
from advanced_economic_calendar.calendar_provider_response import create_calendar_provider_response
from advanced_economic_calendar.calendar_provider_models import CalendarProviderMetadata, CalendarProviderCapability, CalendarProviderRequest, CalendarProviderResponse

class CalendarLocalCacheProviderPlaceholder(BaseCalendarProvider):
    provider_name = "calendar_local_cache_provider_placeholder"
    provider_type = "provider_local_cache"

    def metadata(self) -> CalendarProviderMetadata:
        return CalendarProviderMetadata(self.provider_name, self.provider_name, self.provider_type, "", "none", "none", "none", "compliant", "none", "calendar_provider_ready", [])

    def capabilities(self) -> List[CalendarProviderCapability]:
        return []

    def validate_request(self, request: CalendarProviderRequest) -> Dict:
        return {"valid": True, "errors": []}

    def fetch_calendar(self, request: CalendarProviderRequest) -> CalendarProviderResponse:
        return create_calendar_provider_response(request.request_id, self.provider_name, request.data_type, "placeholder_success")

    def health_check(self) -> Dict:
        return {"status": "healthy"}

def build_calendar_local_cache_provider_placeholder(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame([vars(CalendarLocalCacheProviderPlaceholder().metadata())])
    return df, {"total": len(df)}
