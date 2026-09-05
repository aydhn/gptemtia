
import pandas as pd
from .macro_provider_interfaces import BaseMacroProvider
from .macro_provider_models import MacroProviderMetadata, MacroProviderCapability, MacroProviderRequest, MacroProviderResponse, build_macro_provider_metadata_id, build_macro_provider_capability_id, build_macro_provider_response_id
from .macro_provider_config import MacroProviderProfile

class MacroDryRunFixtureProvider(BaseMacroProvider):
    provider_name = "macro_dry_run_fixture_provider"
    provider_type = "provider_dry_run_fixture"
    
    def metadata(self) -> MacroProviderMetadata:
        return MacroProviderMetadata(
            provider_id=build_macro_provider_metadata_id(self.provider_name),
            provider_name=self.provider_name,
            provider_type=self.provider_type,
            description="Dry run fixture",
            homepage_ref="local://dry_run",
            license_note="local",
            credential_policy="not stored",
            no_scraping_policy="compliant",
            macro_coverage_note="synthetic",
            status_label="macro_provider_ready",
            warnings=[]
        )
        
    def capabilities(self) -> list[MacroProviderCapability]:
        return [
            MacroProviderCapability(
                capability_id=build_macro_provider_capability_id(self.provider_name, "timeseries"),
                provider_name=self.provider_name,
                provider_type=self.provider_type,
                macro_categories=["macro_rates_and_yields"],
                data_types=["macro_data_timeseries", "macro_data_release_metadata"],
                frequency_support=["daily"],
                region_support=["US"],
                requires_network=False,
                requires_credentials=False,
                supports_local_cache=True,
                no_scraping_compliant=True,
                status_label="macro_provider_ready",
                warnings=[]
            )
        ]
        
    def validate_request(self, request: MacroProviderRequest) -> dict:
        return {"valid": True}
        
    def fetch_macro(self, request: MacroProviderRequest) -> MacroProviderResponse:
        return MacroProviderResponse(
            response_id=build_macro_provider_response_id(request.request_id, self.provider_name),
            request_id=request.request_id,
            provider_name=self.provider_name,
            data_type=request.data_type,
            status_label="macro_provider_ready",
            output_ref=f"dry_run://macro_provider_fixture/{request.data_type}/{request.frequency}",
            row_count=100,
            schema_ref="macro_timeseries_schema",
            warnings=[],
            manual_review_required=True
        )
        
    def health_check(self) -> dict:
        return {"status": "healthy", "local_only": True}

def run_macro_dry_run_examples(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame([{"run": "success"}]), {"status": "success"}

def build_macro_dry_run_fixture_report(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    return run_macro_dry_run_examples(profile)

def summarize_macro_dry_run_fixture(df: pd.DataFrame) -> dict:
    return {"total": len(df)}
