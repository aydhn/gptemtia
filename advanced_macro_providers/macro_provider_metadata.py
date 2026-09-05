
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderMetadata, build_macro_provider_metadata_id

def build_default_macro_provider_metadata(profile: MacroProviderProfile) -> list[MacroProviderMetadata]:
    meta = [
        MacroProviderMetadata(
            provider_id=build_macro_provider_metadata_id("macro_dry_run_fixture_provider"),
            provider_name="macro_dry_run_fixture_provider",
            provider_type="provider_dry_run_fixture",
            description="Dry run fixture for macro",
            homepage_ref="local://dry_run",
            license_note="local",
            credential_policy="not stored/not printed/manual configuration only",
            no_scraping_policy="compliant",
            macro_coverage_note="synthetic",
            status_label="macro_provider_ready",
            warnings=[]
        )
    ]
    return meta

def validate_macro_provider_metadata_item(item: MacroProviderMetadata, profile: MacroProviderProfile) -> dict:
    return {"valid": True}

def build_macro_provider_metadata_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_provider_metadata(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_provider_metadata(df)

def summarize_macro_provider_metadata(df: pd.DataFrame) -> dict:
    return {"total_metadata": len(df)}
