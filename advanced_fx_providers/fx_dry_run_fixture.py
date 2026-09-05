import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_interfaces import BaseFXProvider
from .fx_provider_models import FXProviderMetadata, FXProviderCapability, FXProviderRequest, FXProviderResponse, build_fx_provider_metadata_id, build_fx_provider_capability_id
from .fx_provider_response import create_fx_provider_response

class FXDryRunFixtureProvider(BaseFXProvider):
    provider_name = "fx_dry_run_fixture_provider"
    provider_type = "provider_dry_run_fixture"

    def metadata(self) -> FXProviderMetadata:
        return FXProviderMetadata(
            provider_id=build_fx_provider_metadata_id(self.provider_name),
            provider_name=self.provider_name, provider_type=self.provider_type,
            description="Dry-run fixture for FX", homepage_ref="", license_note="",
            credential_policy="not stored", no_scraping_policy="strict no-scraping",
            fx_coverage_note="Mock coverage", status_label="fx_provider_ready", warnings=[]
        )

    def capabilities(self) -> List[FXProviderCapability]:
        return [
            FXProviderCapability(
                capability_id=build_fx_provider_capability_id(self.provider_name, "fx_data_ohlcv"),
                provider_name=self.provider_name, provider_type=self.provider_type,
                pair_groups=["fx_major_pair", "fx_minor_pair"], data_types=["fx_data_ohlcv", "fx_data_quote"],
                timeframe_support=["1d"], requires_network=False, requires_credentials=False,
                supports_local_cache=True, no_scraping_compliant=True, status_label="fx_provider_ready", warnings=[]
            )
        ]

    def validate_request(self, request: FXProviderRequest) -> Dict:
        return {"valid": True, "errors": []}

    def fetch_fx(self, request: FXProviderRequest) -> FXProviderResponse:
        return create_fx_provider_response(
            request_id=request.request_id, provider_name=self.provider_name,
            data_type=request.data_type, status_label="fx_provider_ready",
            output_ref=f"dry_run://fx_provider_fixture/{request.data_type}/{request.timeframe}",
            row_count=10, schema_ref="fx_ohlcv_schema"
        )

    def health_check(self) -> Dict:
        return {"status": "healthy", "type": "dry_run"}

def build_fx_dry_run_fixture_report(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame([{"fixture": "fx_dry_run_fixture_provider", "status": "active"}])
    return df, summarize_fx_dry_run_fixture(df)

def run_fx_dry_run_examples(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    return pd.DataFrame([{"example": "1", "result": "success"}]), {"ran": 1}

def summarize_fx_dry_run_fixture(df: pd.DataFrame) -> Dict:
    return {"fixtures": len(df)}
