
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_models import CommodityProviderMetadata, CommodityProviderCapability, CommodityProviderRequest, CommodityProviderResponse

class BaseCommodityProvider:
    provider_name: str = "base"
    provider_type: str = "base"

    def metadata(self) -> CommodityProviderMetadata:
        raise NotImplementedError

    def capabilities(self) -> list[CommodityProviderCapability]:
        raise NotImplementedError

    def validate_request(self, request: CommodityProviderRequest) -> dict:
        raise NotImplementedError

    def fetch_commodity(self, request: CommodityProviderRequest) -> CommodityProviderResponse:
        raise NotImplementedError

    def health_check(self) -> dict:
        raise NotImplementedError

def build_commodity_provider_interface_contract(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"method": "metadata"}, {"method": "capabilities"}, {"method": "validate_request"}, {"method": "fetch_commodity"}, {"method": "health_check"}])
    return df, summarize_commodity_provider_interface_contract(df)

def summarize_commodity_provider_interface_contract(df: pd.DataFrame) -> dict:
    return {"total_methods": len(df)}
