import pandas as pd
from typing import Tuple, Dict, List
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_interfaces import BaseCalendarProvider
from advanced_economic_calendar.calendar_provider_response import create_calendar_provider_response
from advanced_economic_calendar.calendar_provider_models import CalendarProviderMetadata, CalendarProviderCapability, CalendarProviderRequest, CalendarProviderResponse

class CalendarDryRunFixtureProvider(BaseCalendarProvider):
    provider_name = "calendar_dry_run_fixture_provider"
    provider_type = "provider_dry_run_fixture"

    def metadata(self) -> CalendarProviderMetadata:
        from advanced_economic_calendar.calendar_provider_metadata import build_default_calendar_provider_metadata
        for m in build_default_calendar_provider_metadata(CalendarProviderProfile("temp", "")):
            if m.provider_name == self.provider_name:
                return m
        return CalendarProviderMetadata(self.provider_name, self.provider_name, self.provider_type, "", "none", "none", "none", "compliant", "none", "calendar_provider_ready", [])

    def capabilities(self) -> List[CalendarProviderCapability]:
        from advanced_economic_calendar.calendar_provider_capabilities import build_default_calendar_provider_capabilities
        for c in build_default_calendar_provider_capabilities(CalendarProviderProfile("temp", "")):
            if c.provider_name == self.provider_name:
                return [c]
        return []

    def validate_request(self, request: CalendarProviderRequest) -> Dict:
        return {"valid": True, "errors": []}

    def fetch_calendar(self, request: CalendarProviderRequest) -> CalendarProviderResponse:
        return create_calendar_provider_response(
            request_id=request.request_id,
            provider_name=self.provider_name,
            data_type=request.data_type,
            status_label="success",
            output_ref=f"dry_run://calendar_provider_fixture/{request.data_type}/{request.region or 'ALL'}",
            row_count=5,
            schema_ref="dry_run_schema",
            warnings=["Dry run output"],
            manual_review_required=True
        )

    def health_check(self) -> Dict:
        return {"status": "healthy", "mode": "local-only dry-run"}

def build_calendar_dry_run_fixture_report(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    return run_calendar_dry_run_examples(profile)

def run_calendar_dry_run_examples(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    provider = CalendarDryRunFixtureProvider()
    from advanced_economic_calendar.calendar_provider_request import create_calendar_provider_request
    
    req1 = create_calendar_provider_request(provider.provider_name, "calendar_data_release_event", ["US_CPI_RELEASE"], "US")
    res1 = provider.fetch_calendar(req1)
    
    df = pd.DataFrame([vars(res1)])
    summary = summarize_calendar_dry_run_fixture(df)
    return df, summary

def summarize_calendar_dry_run_fixture(df: pd.DataFrame) -> Dict:
    return {
        "total_requests": len(df)
    }
