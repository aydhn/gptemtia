import pandas as pd
from .provider_config import DataProviderAbstractionProfile
from .provider_models import ProviderMetadata, build_provider_metadata_id
from dataclasses import asdict

def build_default_provider_metadata(profile: DataProviderAbstractionProfile) -> list[ProviderMetadata]:
    return [
        ProviderMetadata(
            provider_id=build_provider_metadata_id("dry_run_fixture"),
            provider_name="dry_run_fixture",
            provider_type="provider_dry_run_fixture",
            description="Dry run fixture provider",
            homepage_ref="N/A",
            license_note="Local Only",
            credential_policy="not stored/not printed/manual configuration only",
            no_scraping_policy="Compliant",
            status_label="provider_ready",
            warnings=[]
        )
    ]

def build_provider_metadata_schema(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    schema = {
        "field": ["provider_id", "provider_name", "provider_type", "description", "homepage_ref", "license_note", "credential_policy", "no_scraping_policy", "status_label", "warnings"],
        "type": ["str", "str", "str", "str", "str", "str", "str", "str", "str", "list[str]"]
    }
    df = pd.DataFrame(schema)
    return df, {"total_fields": len(df)}

def build_provider_metadata_registry(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_provider_metadata(profile)
    df = pd.DataFrame([asdict(item) for item in items])
    return df, summarize_provider_metadata(df)

def validate_provider_metadata_item(item: ProviderMetadata, profile: DataProviderAbstractionProfile) -> dict:
    return {"valid": True, "errors": []}

def summarize_provider_metadata(df: pd.DataFrame) -> dict:
    return {"total_metadata_records": len(df)}
