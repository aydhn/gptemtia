
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_models import CommodityItem, build_commodity_id

def build_precious_metals(profile: CommodityProviderProfile) -> list[CommodityItem]:
    return [
        CommodityItem(build_commodity_id("XAU/USD"), "Gold", "XAU/USD", "commodity_precious_metals", ["GOLD", "GC continuous placeholder"], "USD", "troy ounce", "commodity_data_continuous_contract_placeholder", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("XAG/USD"), "Silver", "XAG/USD", "commodity_precious_metals", ["SILVER", "SI continuous placeholder"], "USD", "troy ounce", "commodity_data_continuous_contract_placeholder", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("PLATINUM_PLACEHOLDER"), "Platinum", "PLATINUM_PLACEHOLDER", "commodity_precious_metals", ["PLATINUM"], "USD", "troy ounce", "commodity_data_spot", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("PALLADIUM_PLACEHOLDER"), "Palladium", "PALLADIUM_PLACEHOLDER", "commodity_precious_metals", ["PALLADIUM"], "USD", "troy ounce", "commodity_data_spot", "commodity_provider_ready", [])
    ]

def build_energy_commodities(profile: CommodityProviderProfile) -> list[CommodityItem]:
    return [
        CommodityItem(build_commodity_id("WTI_CRUDE"), "WTI Crude Oil", "WTI_CRUDE", "commodity_energy", ["CL continuous placeholder"], "USD", "barrel", "commodity_data_continuous_contract_placeholder", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("BRENT_CRUDE"), "Brent Crude Oil", "BRENT_CRUDE", "commodity_energy", ["BRN", "BZ continuous placeholder"], "USD", "barrel", "commodity_data_continuous_contract_placeholder", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("NATURAL_GAS"), "Natural Gas", "NATURAL_GAS", "commodity_energy", ["NG continuous placeholder"], "USD", "MMBtu", "commodity_data_continuous_contract_placeholder", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("HEATING_OIL_PLACEHOLDER"), "Heating Oil", "HEATING_OIL_PLACEHOLDER", "commodity_energy", [], "USD", "gallon", "commodity_data_spot", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("GASOLINE_PLACEHOLDER"), "Gasoline", "GASOLINE_PLACEHOLDER", "commodity_energy", [], "USD", "gallon", "commodity_data_spot", "commodity_provider_ready", [])
    ]

def build_industrial_metals(profile: CommodityProviderProfile) -> list[CommodityItem]:
    return [
        CommodityItem(build_commodity_id("COPPER"), "Copper", "COPPER", "commodity_industrial_metals", ["HG continuous placeholder"], "USD", "pound", "commodity_data_continuous_contract_placeholder", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("ALUMINUM_PLACEHOLDER"), "Aluminum", "ALUMINUM_PLACEHOLDER", "commodity_industrial_metals", [], "USD", "tonne", "commodity_data_spot", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("NICKEL_PLACEHOLDER"), "Nickel", "NICKEL_PLACEHOLDER", "commodity_industrial_metals", [], "USD", "tonne", "commodity_data_spot", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("ZINC_PLACEHOLDER"), "Zinc", "ZINC_PLACEHOLDER", "commodity_industrial_metals", [], "USD", "tonne", "commodity_data_spot", "commodity_provider_ready", [])
    ]

def build_agriculture_commodities(profile: CommodityProviderProfile) -> list[CommodityItem]:
    return [
        CommodityItem(build_commodity_id("WHEAT_PLACEHOLDER"), "Wheat", "WHEAT_PLACEHOLDER", "commodity_agriculture", [], "USD", "bushel", "commodity_data_spot", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("CORN_PLACEHOLDER"), "Corn", "CORN_PLACEHOLDER", "commodity_agriculture", [], "USD", "bushel", "commodity_data_spot", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("SOYBEANS_PLACEHOLDER"), "Soybeans", "SOYBEANS_PLACEHOLDER", "commodity_agriculture", [], "USD", "bushel", "commodity_data_spot", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("COFFEE_PLACEHOLDER"), "Coffee", "COFFEE_PLACEHOLDER", "commodity_agriculture", [], "USD", "pound", "commodity_data_spot", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("SUGAR_PLACEHOLDER"), "Sugar", "SUGAR_PLACEHOLDER", "commodity_agriculture", [], "USD", "pound", "commodity_data_spot", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("COTTON_PLACEHOLDER"), "Cotton", "COTTON_PLACEHOLDER", "commodity_agriculture", [], "USD", "pound", "commodity_data_spot", "commodity_provider_ready", []),
        CommodityItem(build_commodity_id("COCOA_PLACEHOLDER"), "Cocoa", "COCOA_PLACEHOLDER", "commodity_agriculture", [], "USD", "tonne", "commodity_data_spot", "commodity_provider_ready", [])
    ]

def build_default_commodities(profile: CommodityProviderProfile) -> list[CommodityItem]:
    items = []
    if profile.enable_precious_metals: items.extend(build_precious_metals(profile))
    if profile.enable_energy: items.extend(build_energy_commodities(profile))
    if profile.enable_industrial_metals: items.extend(build_industrial_metals(profile))
    if profile.enable_agriculture: items.extend(build_agriculture_commodities(profile))
    return items

def build_commodity_universe_registry(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_commodities(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_commodity_universe(df)

def summarize_commodity_universe(df: pd.DataFrame) -> dict:
    return {"total_commodities": len(df)}
