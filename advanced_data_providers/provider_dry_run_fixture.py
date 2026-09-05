import pandas as pd
from .provider_config import DataProviderAbstractionProfile
from .provider_interfaces import BaseDataProvider
from .provider_models import ProviderMetadata, ProviderCapability, ProviderRequest, ProviderResponse

class DryRunFixtureProvider(BaseDataProvider):
    provider_name = "dry_run_fixture_provider"
    provider_type = "provider_dry_run_fixture"

    def metadata(self) -> ProviderMetadata:
        from .provider_metadata import build_default_provider_metadata
        # mock profile just to satisfy
        return build_default_provider_metadata(DataProviderAbstractionProfile("mock", "mock"))[0]

    def capabilities(self) -> list[ProviderCapability]:
        from .provider_capabilities import build_default_provider_capabilities
        caps = build_default_provider_capabilities(DataProviderAbstractionProfile("mock", "mock"))
        return [c for c in caps if c.provider_type == self.provider_type]

    def validate_request(self, request: ProviderRequest) -> dict:
        return {"valid": True, "errors": []}

    def fetch(self, request: ProviderRequest) -> ProviderResponse:
        from .provider_response import create_provider_response
        return create_provider_response(
            request_id=request.request_id,
            provider_name=self.provider_name,
            data_type=request.data_type,
            status_label="provider_ready",
            output_ref=f"dry_run://provider_fixture/{request.data_type}/{request.timeframe}",
            row_count=100, # sample fake count
            schema_ref="dry_run_schema",
            manual_review_required=True
        )

    def health_check(self) -> dict:
        return {"status": "healthy", "mode": "local-only dry-run"}

def build_provider_dry_run_fixture_report(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"fixture": "dry_run_fixture_provider", "status": "available"}])
    return df, summarize_provider_dry_run_fixture(df)

def run_provider_dry_run_examples(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"example": "ohlcv", "status": "success"}])
    return df, summarize_provider_dry_run_fixture(df)

def summarize_provider_dry_run_fixture(df: pd.DataFrame) -> dict:
    return {"total_fixtures": len(df)}
