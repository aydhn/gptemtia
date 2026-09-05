import pandas as pd
from typing import Tuple, Dict, List
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_models import CalendarProviderMetadata, CalendarProviderCapability, CalendarProviderRequest, CalendarProviderResponse

class BaseCalendarProvider:
    provider_name: str
    provider_type: str

    def metadata(self) -> CalendarProviderMetadata:
        raise NotImplementedError

    def capabilities(self) -> List[CalendarProviderCapability]:
        raise NotImplementedError

    def validate_request(self, request: CalendarProviderRequest) -> Dict:
        raise NotImplementedError

    def fetch_calendar(self, request: CalendarProviderRequest) -> CalendarProviderResponse:
        raise NotImplementedError

    def health_check(self) -> Dict:
        raise NotImplementedError

def build_calendar_provider_interface_contract(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    methods = [
        {"method_name": "metadata", "return_type": "CalendarProviderMetadata"},
        {"method_name": "capabilities", "return_type": "List[CalendarProviderCapability]"},
        {"method_name": "validate_request", "return_type": "Dict"},
        {"method_name": "fetch_calendar", "return_type": "CalendarProviderResponse"},
        {"method_name": "health_check", "return_type": "Dict"}
    ]
    df = pd.DataFrame(methods)
    summary = summarize_calendar_provider_interface_contract(df)
    return df, summary

def summarize_calendar_provider_interface_contract(df: pd.DataFrame) -> Dict:
    return {
        "total_methods": len(df)
    }
