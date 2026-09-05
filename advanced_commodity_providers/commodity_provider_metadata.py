
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_models import CommodityProviderMetadata, build_commodity_provider_metadata_id

def build_default_commodity_provider_metadata(profile: CommodityProviderProfile) -> list[CommodityProviderMetadata]:
    return [
        CommodityProviderMetadata(build_commodity_provider_metadata_id("commodity_dry_run_fixture_provider"), "commodity_dry_run_fixture_provider", "fixture", "Dry-run provider", "local://", "Open", "not stored", "compliant", "All", "commodity_provider_ready", []),
        CommodityProviderMetadata(build_commodity_provider_metadata_id("commodity_manual_file_provider_placeholder"), "commodity_manual_file_provider_placeholder", "manual", "Manual file provider", "local://", "Open", "not stored", "compliant", "Selected", "commodity_provider_ready", []),
        CommodityProviderMetadata(build_commodity_provider_metadata_id("commodity_local_cache_provider_placeholder"), "commodity_local_cache_provider_placeholder", "local", "Local cache provider", "local://", "Open", "not stored", "compliant", "Selected", "commodity_provider_ready", []),
        CommodityProviderMetadata(build_commodity_provider_metadata_id("commodity_official_api_provider_placeholder"), "commodity_official_api_provider_placeholder", "official", "Official API provider placeholder", "https://official-api.example.com", "Requires Review", "manual configuration only", "compliant", "Broad", "commodity_provider_ready", []),
        CommodityProviderMetadata(build_commodity_provider_metadata_id("commodity_licensed_provider_placeholder"), "commodity_licensed_provider_placeholder", "licensed", "Licensed API provider placeholder", "https://licensed-api.example.com", "Commercial License", "manual configuration only", "compliant", "Futures, Options", "commodity_provider_ready", ["Futures data licensing özel risk notu"])
    ]

def validate_commodity_provider_metadata_item(item: CommodityProviderMetadata, profile: CommodityProviderProfile) -> dict:
    return {"valid": True, "errors": []}

def build_commodity_provider_metadata_registry(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_commodity_provider_metadata(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_commodity_provider_metadata(df)

def summarize_commodity_provider_metadata(df: pd.DataFrame) -> dict:
    return {"total_metadata": len(df)}
