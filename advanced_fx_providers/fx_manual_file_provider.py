import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_interfaces import BaseFXProvider
from .fx_provider_models import FXProviderMetadata, FXProviderCapability, FXProviderRequest, FXProviderResponse, build_fx_provider_metadata_id
from .fx_provider_response import create_fx_provider_response

class FXManualFileProviderPlaceholder(BaseFXProvider):
    provider_name = "fx_manual_file_provider_placeholder"
    provider_type = "provider_manual_file"

    def metadata(self) -> FXProviderMetadata:
        return FXProviderMetadata(
            provider_id=build_fx_provider_metadata_id(self.provider_name),
            provider_name=self.provider_name, provider_type=self.provider_type,
            description="Placeholder for fx_manual_file_provider_placeholder", homepage_ref="", license_note="",
            credential_policy="not stored", no_scraping_policy="strict no-scraping",
            fx_coverage_note="Placeholder", status_label="fx_provider_placeholder_only", warnings=[]
        )

    def capabilities(self) -> List[FXProviderCapability]: return []
    def validate_request(self, request: FXProviderRequest) -> Dict: return {"valid": True, "errors": []}
    def fetch_fx(self, request: FXProviderRequest) -> FXProviderResponse:
        return create_fx_provider_response(
            request_id=request.request_id, provider_name=self.provider_name,
            data_type=request.data_type, status_label="fx_provider_placeholder_only",
            output_ref="placeholder_ref", row_count=0
        )
    def health_check(self) -> Dict: return {"status": "healthy", "type": "placeholder"}

def build_fx_manual_file_provider_placeholder(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame([{"provider": "fx_manual_file_provider_placeholder", "status": "placeholder_active"}])
    return df, {"status": "ok"}
