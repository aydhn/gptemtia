
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_models import CommodityProviderCapability, build_commodity_provider_capability_id

def build_default_commodity_provider_capabilities(profile: CommodityProviderProfile) -> list[CommodityProviderCapability]:
    return [
        CommodityProviderCapability(build_commodity_provider_capability_id("commodity_dry_run_fixture_provider", "spot"), "commodity_dry_run_fixture_provider", "fixture", ["commodity_precious_metals", "commodity_energy", "commodity_industrial_metals", "commodity_agriculture"], ["spot"], ["1d"], False, False, True, True, "commodity_provider_ready", []),
        CommodityProviderCapability(build_commodity_provider_capability_id("commodity_dry_run_fixture_provider", "ohlcv"), "commodity_dry_run_fixture_provider", "fixture", ["commodity_precious_metals", "commodity_energy", "commodity_industrial_metals", "commodity_agriculture"], ["ohlcv"], ["1d"], False, False, True, True, "commodity_provider_ready", []),
        CommodityProviderCapability(build_commodity_provider_capability_id("commodity_dry_run_fixture_provider", "futures_metadata"), "commodity_dry_run_fixture_provider", "fixture", ["commodity_energy", "commodity_agriculture"], ["futures_metadata"], ["1d"], False, False, True, True, "commodity_provider_ready", []),
        CommodityProviderCapability(build_commodity_provider_capability_id("commodity_manual_file_provider_placeholder", "spot"), "commodity_manual_file_provider_placeholder", "manual", ["commodity_precious_metals"], ["spot"], ["1d"], False, False, True, True, "commodity_provider_ready", []),
        CommodityProviderCapability(build_commodity_provider_capability_id("commodity_manual_file_provider_placeholder", "ohlcv"), "commodity_manual_file_provider_placeholder", "manual", ["commodity_precious_metals"], ["ohlcv"], ["1d"], False, False, True, True, "commodity_provider_ready", []),
        CommodityProviderCapability(build_commodity_provider_capability_id("commodity_local_cache_provider_placeholder", "spot"), "commodity_local_cache_provider_placeholder", "local", ["commodity_energy"], ["spot"], ["1d"], False, False, True, True, "commodity_provider_ready", []),
        CommodityProviderCapability(build_commodity_provider_capability_id("commodity_local_cache_provider_placeholder", "ohlcv"), "commodity_local_cache_provider_placeholder", "local", ["commodity_energy"], ["ohlcv"], ["1d"], False, False, True, True, "commodity_provider_ready", []),
        CommodityProviderCapability(build_commodity_provider_capability_id("commodity_official_api_provider_placeholder", "precious_metals"), "commodity_official_api_provider_placeholder", "official", ["commodity_precious_metals"], ["ohlcv"], ["1d"], False, False, False, True, "commodity_provider_ready", []),
        CommodityProviderCapability(build_commodity_provider_capability_id("commodity_official_api_provider_placeholder", "energy"), "commodity_official_api_provider_placeholder", "official", ["commodity_energy"], ["ohlcv"], ["1d"], False, False, False, True, "commodity_provider_ready", []),
        CommodityProviderCapability(build_commodity_provider_capability_id("commodity_official_api_provider_placeholder", "industrial_metals"), "commodity_official_api_provider_placeholder", "official", ["commodity_industrial_metals"], ["ohlcv"], ["1d"], False, False, False, True, "commodity_provider_ready", []),
        CommodityProviderCapability(build_commodity_provider_capability_id("commodity_official_api_provider_placeholder", "agriculture"), "commodity_official_api_provider_placeholder", "official", ["commodity_agriculture"], ["ohlcv"], ["1d"], False, False, False, True, "commodity_provider_ready", []),
        CommodityProviderCapability(build_commodity_provider_capability_id("commodity_licensed_provider_placeholder", "ohlcv"), "commodity_licensed_provider_placeholder", "licensed", ["commodity_precious_metals", "commodity_energy"], ["ohlcv"], ["1d"], False, False, False, True, "commodity_provider_ready", []),
        CommodityProviderCapability(build_commodity_provider_capability_id("commodity_licensed_provider_placeholder", "futures_metadata"), "commodity_licensed_provider_placeholder", "licensed", ["commodity_energy"], ["futures_metadata"], ["1d"], False, False, False, True, "commodity_provider_ready", [])
    ]

def build_commodity_provider_capability_registry(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_commodity_provider_capabilities(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_commodity_provider_capabilities(df)

def summarize_commodity_provider_capabilities(df: pd.DataFrame) -> dict:
    return {"total_capabilities": len(df)}
