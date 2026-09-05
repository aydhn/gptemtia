import os
from pathlib import Path

def generate_modules_6():
    base_dir = Path("advanced_commodity_providers")
    
    code = """
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_models import CommodityProviderContractItem, build_commodity_provider_contract_id

def build_default_commodity_adapter_contract_items(profile: CommodityProviderProfile) -> list[CommodityProviderContractItem]:
    forbidden = ["no scraping", "no browser automation", "no hidden API reverse engineering", "no paywall bypass", "no credential output", "no broker/live/order", "no futures broker execution", "no investment advice", "no futures advice", "no deployment", "no destructive file action"]
    areas = [
        "Commodity metadata contract", "Commodity capability contract", "Commodity symbol normalization contract", 
        "Commodity request validation contract", "Commodity fetch response contract", "Commodity error handling contract",
        "Commodity manual file contract", "Commodity local cache contract", "Commodity official API placeholder contract",
        "Commodity licensed placeholder contract", "Commodity dry-run fixture contract", "Commodity spot schema contract",
        "Commodity OHLCV schema contract", "Futures contract metadata contract", "Continuous contract requirement contract",
        "Roll adjustment requirement contract", "Commodity output validation contract", "Commodity safety contract"
    ]
    return [
        CommodityProviderContractItem(build_commodity_provider_contract_id(a.replace(' ', '_').lower()), a, "valid input", "valid output", forbidden, True)
        for a in areas
    ]

def build_commodity_adapter_contract(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_commodity_adapter_contract_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_commodity_adapter_contract(df)

def summarize_commodity_adapter_contract(df: pd.DataFrame) -> dict:
    return {"total_contracts": len(df)}
"""
    (base_dir / "commodity_adapter_contracts.py").write_text(code, encoding="utf-8")

    code = """
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_interfaces import BaseCommodityProvider
from .commodity_provider_models import CommodityProviderCapability

class CommodityProviderRegistry:
    def __init__(self):
        self._providers = {}
    
    def register(self, provider: BaseCommodityProvider) -> None:
        self._providers[provider.provider_name] = provider

    def list_providers(self) -> list[str]:
        return list(self._providers.keys())

    def get_provider(self, provider_name: str) -> BaseCommodityProvider | None:
        return self._providers.get(provider_name)

    def list_capabilities(self) -> list[CommodityProviderCapability]:
        caps = []
        for p in self._providers.values():
            caps.extend(p.capabilities())
        return caps

    def to_dataframe(self) -> pd.DataFrame:
        data = []
        for k, v in self._providers.items():
            data.append({"provider_name": k, "provider_type": v.provider_type})
        return pd.DataFrame(data)

def build_default_commodity_provider_registry(profile: CommodityProviderProfile) -> CommodityProviderRegistry:
    from .commodity_dry_run_fixture import CommodityDryRunFixtureProvider
    from .commodity_manual_file_provider import CommodityManualFileProviderPlaceholder
    from .commodity_local_cache_provider import CommodityLocalCacheProviderPlaceholder
    from .commodity_official_api_provider import CommodityOfficialApiProviderPlaceholder
    from .commodity_licensed_provider import CommodityLicensedProviderPlaceholder
    registry = CommodityProviderRegistry()
    registry.register(CommodityDryRunFixtureProvider())
    registry.register(CommodityManualFileProviderPlaceholder())
    registry.register(CommodityLocalCacheProviderPlaceholder())
    registry.register(CommodityOfficialApiProviderPlaceholder())
    registry.register(CommodityLicensedProviderPlaceholder())
    return registry

def build_commodity_provider_registry(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    registry = build_default_commodity_provider_registry(profile)
    df = registry.to_dataframe()
    return df, summarize_commodity_provider_registry(df)

def summarize_commodity_provider_registry(df: pd.DataFrame) -> dict:
    return {"total_providers": len(df)}
"""
    (base_dir / "commodity_provider_registry.py").write_text(code, encoding="utf-8")

    code = """
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_interfaces import BaseCommodityProvider
from .commodity_provider_models import CommodityProviderRequest
from .commodity_provider_registry import CommodityProviderRegistry

def resolve_commodity_provider_for_request(
    request: CommodityProviderRequest,
    registry: CommodityProviderRegistry,
    profile: CommodityProviderProfile,
) -> BaseCommodityProvider | None:
    return registry.get_provider(request.provider_name)

def build_commodity_provider_resolver_map(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"request_type": "all", "resolved_provider": "dry_run"}])
    return df, summarize_commodity_provider_resolver_map(df)

def summarize_commodity_provider_resolver_map(df: pd.DataFrame) -> dict:
    return {"total_mappings": len(df)}
"""
    (base_dir / "commodity_provider_resolver.py").write_text(code, encoding="utf-8")

    code = """
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile

def resolve_commodity_provider_preferences_from_config_profiles(profile: CommodityProviderProfile) -> pd.DataFrame:
    data = [
        {"preference": "no_scraping_public_api_preferred", "enabled": not profile.allow_web_scraping},
        {"preference": "local_cache_preferred", "enabled": profile.enable_local_cache_provider},
        {"preference": "manual_file_import_preferred", "enabled": profile.enable_manual_file_provider},
        {"preference": "official_provider_preferred", "enabled": profile.enable_official_api_placeholder},
        {"preference": "precious_metals", "enabled": profile.enable_precious_metals},
        {"preference": "energy_commodities", "enabled": profile.enable_energy},
        {"preference": "industrial_metals", "enabled": profile.enable_industrial_metals},
        {"preference": "agriculture_commodities", "enabled": profile.enable_agriculture},
        {"preference": "broad_commodities_research", "enabled": True},
        {"preference": "gold_macro_research", "enabled": True},
        {"preference": "oil_macro_research", "enabled": True}
    ]
    return pd.DataFrame(data)

def build_commodity_provider_preference_resolver_report(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = resolve_commodity_provider_preferences_from_config_profiles(profile)
    return df, summarize_commodity_provider_preference_resolver(df)

def summarize_commodity_provider_preference_resolver(df: pd.DataFrame) -> dict:
    return {"total_preferences": len(df)}
"""
    (base_dir / "commodity_provider_preference_resolver.py").write_text(code, encoding="utf-8")

    code = """
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile

def match_commodity_provider_capabilities(
    requested_data_type: str,
    requested_category: str,
    timeframe: str,
    capability_df: pd.DataFrame,
) -> pd.DataFrame:
    if capability_df.empty: return pd.DataFrame()
    def match_row(row):
        return (requested_data_type in row.get("data_types", []) and 
                requested_category in row.get("commodity_categories", []) and
                timeframe in row.get("timeframe_support", []))
    matched = capability_df[capability_df.apply(match_row, axis=1)]
    return matched

def build_commodity_provider_capability_matcher_report(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"match_status": "ok"}])
    return df, summarize_commodity_provider_capability_matcher(df)

def summarize_commodity_provider_capability_matcher(df: pd.DataFrame) -> dict:
    return {"total_matches": len(df)}
"""
    (base_dir / "commodity_provider_capability_matcher.py").write_text(code, encoding="utf-8")

if __name__ == "__main__":
    generate_modules_6()
    print("Modules 6 generated.")
