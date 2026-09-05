import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderCapability, build_fx_provider_capability_id

def build_default_fx_provider_capabilities(profile: FXProviderProfile) -> List[FXProviderCapability]:
    caps = [
        ("fx_dry_run_fixture_provider", "provider_dry_run_fixture", ["fx_major_pair", "fx_minor_pair"], ["fx_data_ohlcv", "fx_data_quote"]),
        ("fx_manual_file_provider_placeholder", "provider_manual_file", ["fx_major_pair"], ["fx_data_ohlcv"]),
        ("fx_local_cache_provider_placeholder", "provider_local_cache", ["fx_major_pair"], ["fx_data_ohlcv"]),
        ("fx_official_api_provider_placeholder", "provider_official_api", ["fx_major_pair", "fx_minor_pair", "fx_exotic_pair"], ["fx_data_ohlcv", "fx_data_quote"]),
        ("fx_licensed_provider_placeholder", "provider_licensed", ["fx_major_pair"], ["fx_data_ohlcv"])
    ]
    return [
        FXProviderCapability(
            capability_id=build_fx_provider_capability_id(c[0], c[3][0]), provider_name=c[0], provider_type=c[1],
            pair_groups=c[2], data_types=c[3], timeframe_support=["1d", "1h", "1m"], requires_network=False,
            requires_credentials=False, supports_local_cache=True, no_scraping_compliant=True,
            status_label="fx_provider_ready", warnings=[]
        ) for c in caps
    ]

def build_fx_provider_capability_registry(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_fx_provider_capabilities(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_fx_provider_capabilities(df)

def summarize_fx_provider_capabilities(df: pd.DataFrame) -> Dict:
    return {"total_capabilities": len(df)}
