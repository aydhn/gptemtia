import pandas as pd
from typing import Tuple, Dict, Optional
from .fx_provider_config import FXProviderProfile
from .fx_provider_registry import FXProviderRegistry
from .fx_provider_interfaces import BaseFXProvider
from .fx_provider_models import FXProviderRequest

def resolve_fx_provider_for_request(
    request: FXProviderRequest,
    registry: FXProviderRegistry,
    profile: FXProviderProfile,
) -> Optional[BaseFXProvider]:
    # graceful degradation without scraping/network
    if request.dry_run:
        return registry.get_provider("fx_dry_run_fixture_provider")
    return registry.get_provider("fx_manual_file_provider_placeholder")

def build_fx_provider_resolver_map(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    data = [{"request_type": "dry_run", "resolved_provider": "fx_dry_run_fixture_provider"}]
    df = pd.DataFrame(data)
    return df, summarize_fx_provider_resolver_map(df)

def summarize_fx_provider_resolver_map(df: pd.DataFrame) -> Dict:
    return {"total_rules": len(df)}
