import pandas as pd
from .provider_config import DataProviderAbstractionProfile
from .provider_interfaces import BaseDataProvider
from .provider_models import ProviderMetadata, ProviderCapability, ProviderRequest, ProviderResponse

class LocalCacheProviderPlaceholder(BaseDataProvider):
    provider_name = "local_cache_provider_placeholder"
    provider_type = "provider_local_cache"

    def metadata(self) -> ProviderMetadata:
        from .provider_metadata import build_default_provider_metadata
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
            status_label="provider_placeholder_only",
            output_ref=f"local_cache://{request.data_type}",
            row_count=0,
            manual_review_required=True
        )

    def health_check(self) -> dict:
        return {"status": "healthy", "mode": "local-cache placeholder"}

def build_local_cache_provider_placeholder(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"provider": "local_cache_provider_placeholder", "status": "placeholder_ready"}])
    return df, {"total": len(df)}
