
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_interfaces import BaseMacroProvider
from .macro_provider_registry import MacroProviderRegistry
from .macro_provider_models import MacroProviderRequest

def resolve_macro_provider_for_request(
    request: MacroProviderRequest,
    registry: MacroProviderRegistry,
    profile: MacroProviderProfile,
) -> BaseMacroProvider | None:
    return registry.get_provider(request.provider_name)

def build_macro_provider_resolver_map(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"request_type": "all", "resolved_to": "registry"}])
    return df, summarize_macro_provider_resolver_map(df)

def summarize_macro_provider_resolver_map(df: pd.DataFrame) -> dict:
    return {"total_mappings": len(df)}
