
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_interfaces import BaseCommodityProvider
from .commodity_provider_models import CommodityProviderMetadata, CommodityProviderCapability, CommodityProviderRequest, CommodityProviderResponse
from .commodity_provider_response import create_commodity_provider_response

class CommodityManualFileProviderPlaceholder(BaseCommodityProvider):
    provider_name = "commodity_manual_file_provider_placeholder"
    provider_type = "manual"

    def metadata(self) -> CommodityProviderMetadata:
        from .commodity_provider_models import build_commodity_provider_metadata_id
        return CommodityProviderMetadata(build_commodity_provider_metadata_id(self.provider_name), self.provider_name, self.provider_type, "Manual file provider", "local://", "Open", "not stored", "compliant", "Selected", "commodity_provider_ready", [])

    def capabilities(self) -> list[CommodityProviderCapability]:
        from .commodity_provider_capabilities import build_default_commodity_provider_capabilities
        caps = build_default_commodity_provider_capabilities(CommodityProviderProfile("default", ""))
        return [c for c in caps if c.provider_name == self.provider_name]

    def validate_request(self, request: CommodityProviderRequest) -> dict:
        return {"valid": True}

    def fetch_commodity(self, request: CommodityProviderRequest) -> CommodityProviderResponse:
        return create_commodity_provider_response(request.request_id, self.provider_name, request.data_type, "commodity_provider_placeholder_only")

    def health_check(self) -> dict:
        return {"status": "healthy"}

def build_commodity_manual_file_provider_placeholder(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"placeholder": "ok"}])
    return df, {"total": len(df)}
