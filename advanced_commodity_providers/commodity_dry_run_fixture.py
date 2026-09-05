
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_interfaces import BaseCommodityProvider
from .commodity_provider_models import CommodityProviderMetadata, CommodityProviderCapability, CommodityProviderRequest, CommodityProviderResponse
from .commodity_provider_metadata import build_default_commodity_provider_metadata
from .commodity_provider_capabilities import build_default_commodity_provider_capabilities
from .commodity_provider_response import create_commodity_provider_response

class CommodityDryRunFixtureProvider(BaseCommodityProvider):
    provider_name = "commodity_dry_run_fixture_provider"
    provider_type = "provider_dry_run_fixture"

    def metadata(self) -> CommodityProviderMetadata:
        from .commodity_provider_models import build_commodity_provider_metadata_id
        return CommodityProviderMetadata(build_commodity_provider_metadata_id(self.provider_name), self.provider_name, self.provider_type, "Dry-run provider", "local://", "Open", "not stored", "compliant", "All", "commodity_provider_ready", [])

    def capabilities(self) -> list[CommodityProviderCapability]:
        caps = build_default_commodity_provider_capabilities(CommodityProviderProfile("default", ""))
        return [c for c in caps if c.provider_name == self.provider_name]

    def validate_request(self, request: CommodityProviderRequest) -> dict:
        return {"valid": True}

    def fetch_commodity(self, request: CommodityProviderRequest) -> CommodityProviderResponse:
        out_ref = f"dry_run://commodity_provider_fixture/{request.data_type}/{request.timeframe}"
        return create_commodity_provider_response(request.request_id, self.provider_name, request.data_type, "commodity_provider_ready", output_ref=out_ref, row_count=100)

    def health_check(self) -> dict:
        return {"status": "healthy", "local_only": True}

def build_commodity_dry_run_fixture_report(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"fixture": "ok"}])
    return df, summarize_commodity_dry_run_fixture(df)

def run_commodity_dry_run_examples(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def summarize_commodity_dry_run_fixture(df: pd.DataFrame) -> dict:
    return {"total": len(df)}
