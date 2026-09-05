
import pandas as pd
from .macro_provider_interfaces import BaseMacroProvider
from .macro_provider_models import MacroProviderMetadata, MacroProviderCapability, MacroProviderRequest, MacroProviderResponse, build_macro_provider_metadata_id
from .macro_provider_config import MacroProviderProfile

class MacroPublicDatasetProviderPlaceholder(BaseMacroProvider):
    provider_name = "macro_public_dataset_provider_placeholder"
    provider_type = "provider_public_dataset"
    
    def metadata(self) -> MacroProviderMetadata:
        return MacroProviderMetadata(
            provider_id=build_macro_provider_metadata_id(self.provider_name),
            provider_name=self.provider_name,
            provider_type=self.provider_type,
            description="Placeholder",
            homepage_ref="local://placeholder",
            license_note="local",
            credential_policy="not stored",
            no_scraping_policy="compliant",
            macro_coverage_note="placeholder",
            status_label="macro_provider_placeholder_only",
            warnings=[]
        )
        
    def capabilities(self) -> list[MacroProviderCapability]:
        return []
        
    def validate_request(self, request: MacroProviderRequest) -> dict:
        return {"valid": True}
        
    def fetch_macro(self, request: MacroProviderRequest) -> MacroProviderResponse:
        return MacroProviderResponse(
            response_id="placeholder",
            request_id=request.request_id,
            provider_name=self.provider_name,
            data_type=request.data_type,
            status_label="macro_provider_placeholder_only",
            output_ref="local://placeholder",
            row_count=0,
            schema_ref="",
            warnings=[],
            manual_review_required=True
        )
        
    def health_check(self) -> dict:
        return {"status": "healthy", "local_only": True}

def build_macro_public_dataset_provider_placeholder(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame([{"provider": "macro_public_dataset_provider_placeholder"}]), {"status": "placeholder"}
