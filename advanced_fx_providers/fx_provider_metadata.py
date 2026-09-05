import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderMetadata, build_fx_provider_metadata_id

def build_default_fx_provider_metadata(profile: FXProviderProfile) -> List[FXProviderMetadata]:
    providers = [
        ("fx_dry_run_fixture_provider", "provider_dry_run_fixture"),
        ("fx_manual_file_provider_placeholder", "provider_manual_file"),
        ("fx_local_cache_provider_placeholder", "provider_local_cache"),
        ("fx_official_api_provider_placeholder", "provider_official_api"),
        ("fx_licensed_provider_placeholder", "provider_licensed")
    ]
    return [
        FXProviderMetadata(
            provider_id=build_fx_provider_metadata_id(p[0]), provider_name=p[0], provider_type=p[1],
            description=f"Placeholder for {p[0]}", homepage_ref="https://example.com/no-credential",
            license_note="Mock license", credential_policy="not stored/not printed/manual configuration only",
            no_scraping_policy="strict no-scraping", fx_coverage_note="Basic major pairs",
            status_label="fx_provider_ready", warnings=[]
        ) for p in providers
    ]

def validate_fx_provider_metadata_item(item: FXProviderMetadata, profile: FXProviderProfile) -> Dict:
    return {"valid": True, "errors": []}

def build_fx_provider_metadata_registry(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_fx_provider_metadata(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_fx_provider_metadata(df)

def summarize_fx_provider_metadata(df: pd.DataFrame) -> Dict:
    return {"total_metadata": len(df)}
