
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_models import CommoditySymbolNormalizationRule, build_commodity_symbol_normalization_rule_id

def build_default_commodity_symbol_normalization_rules(profile: CommodityProviderProfile) -> list[CommoditySymbolNormalizationRule]:
    return [
        CommoditySymbolNormalizationRule(build_commodity_symbol_normalization_rule_id("XAU/USD", "default"), "XAU/USD", "default", "XAUUSD|GOLD|GC", "XAU/USD", "Gold normalization", False),
        CommoditySymbolNormalizationRule(build_commodity_symbol_normalization_rule_id("XAG/USD", "default"), "XAG/USD", "default", "XAGUSD|SILVER|SI", "XAG/USD", "Silver normalization", False),
        CommoditySymbolNormalizationRule(build_commodity_symbol_normalization_rule_id("WTI_CRUDE", "default"), "WTI_CRUDE", "default", "WTI|CL", "WTI_CRUDE_CONTINUOUS_PLACEHOLDER", "WTI normalization", False),
        CommoditySymbolNormalizationRule(build_commodity_symbol_normalization_rule_id("BRENT_CRUDE", "default"), "BRENT_CRUDE", "default", "BRENT|BRN|BZ", "BRENT_CRUDE", "Brent normalization", False),
        CommoditySymbolNormalizationRule(build_commodity_symbol_normalization_rule_id("NATURAL_GAS", "default"), "NATURAL_GAS", "default", "NG", "NATURAL_GAS_CONTINUOUS_PLACEHOLDER", "NG normalization", False),
        CommoditySymbolNormalizationRule(build_commodity_symbol_normalization_rule_id("COPPER", "default"), "COPPER", "default", "HG", "COPPER_CONTINUOUS_PLACEHOLDER", "Copper normalization", False)
    ]

def normalize_commodity_symbol(symbol: str, provider_name: str | None = None) -> str:
    s = symbol.upper().replace(' ', '')
    if s in ["XAUUSD", "GOLD", "GC"]: return "XAU/USD" # Or GOLD_CONTINUOUS_PLACEHOLDER depending on requirement
    if s in ["XAGUSD", "SILVER", "SI"]: return "XAG/USD"
    if s in ["WTI", "CL"]: return "WTI_CRUDE_CONTINUOUS_PLACEHOLDER"
    if s in ["BRENT", "BRN", "BZ"]: return "BRENT_CRUDE"
    if s == "NG": return "NATURAL_GAS_CONTINUOUS_PLACEHOLDER"
    if s == "HG": return "COPPER_CONTINUOUS_PLACEHOLDER"
    return symbol

def denormalize_commodity_symbol(canonical_symbol: str, provider_name: str) -> str:
    return canonical_symbol

def build_commodity_symbol_normalization_map(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_commodity_symbol_normalization_rules(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_commodity_symbol_normalization(df)

def summarize_commodity_symbol_normalization(df: pd.DataFrame) -> dict:
    return {"total_rules": len(df)}
