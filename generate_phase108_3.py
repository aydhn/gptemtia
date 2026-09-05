import os
from pathlib import Path

def generate_modules_3():
    base_dir = Path("advanced_commodity_providers")
    
    code = """
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_models import CommodityMetadata, build_commodity_metadata_id
from .commodity_universe import build_default_commodities

def build_default_commodity_metadata(profile: CommodityProviderProfile) -> list[CommodityMetadata]:
    items = []
    universe = build_default_commodities(profile)
    for c in universe:
        items.append(CommodityMetadata(
            commodity_id=build_commodity_metadata_id(c.canonical_symbol),
            canonical_symbol=c.canonical_symbol,
            commodity_name=c.commodity_name,
            category_label=c.category_label,
            unit_note=c.unit_note,
            contract_note="manual review gerektirebilir",
            liquidity_note="Placeholder liquidity note",
            data_availability_note="dry-run uyumlu",
            warnings=["Metadata yatırım tavsiyesi değildir."]
        ))
    return items

def build_commodity_metadata_registry(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_commodity_metadata(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_commodity_metadata(df)

def summarize_commodity_metadata(df: pd.DataFrame) -> dict:
    return {"total_metadata": len(df)}
"""
    (base_dir / "commodity_metadata.py").write_text(code, encoding="utf-8")

    code = """
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
"""
    (base_dir / "commodity_symbol_normalization.py").write_text(code, encoding="utf-8")

    code = """
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile

def build_commodity_spot_schema_contract(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [
        {"field": "symbol", "type": "str"},
        {"field": "timestamp", "type": "datetime"},
        {"field": "spot_price", "type": "float"},
        {"field": "quote_currency", "type": "str"},
        {"field": "unit", "type": "str"},
        {"field": "provider_name", "type": "str"},
        {"field": "retrieval_mode", "type": "str"},
        {"field": "data_quality_status", "type": "str"},
        {"field": "manual_review_required", "type": "bool"}
    ]
    df = pd.DataFrame(schema)
    return df, summarize_commodity_spot_schema(df)

def summarize_commodity_spot_schema(df: pd.DataFrame) -> dict:
    return {"total_fields": len(df)}
"""
    (base_dir / "commodity_spot_schema.py").write_text(code, encoding="utf-8")

    code = """
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile

def build_commodity_ohlcv_schema_contract(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [
        {"field": "symbol", "type": "str"},
        {"field": "timestamp", "type": "datetime"},
        {"field": "open", "type": "float"},
        {"field": "high", "type": "float"},
        {"field": "low", "type": "float"},
        {"field": "close", "type": "float"},
        {"field": "volume", "type": "float"},
        {"field": "open_interest", "type": "float"},
        {"field": "provider_name", "type": "str"},
        {"field": "retrieval_mode", "type": "str"},
        {"field": "contract_type", "type": "str"},
        {"field": "adjusted_flag", "type": "bool"},
        {"field": "data_quality_status", "type": "str"},
        {"field": "manual_review_required", "type": "bool"}
    ]
    df = pd.DataFrame(schema)
    return df, summarize_commodity_ohlcv_schema(df)

def summarize_commodity_ohlcv_schema(df: pd.DataFrame) -> dict:
    return {"total_fields": len(df)}
"""
    (base_dir / "commodity_ohlcv_schema.py").write_text(code, encoding="utf-8")

if __name__ == "__main__":
    generate_modules_3()
    print("Modules 3 generated.")
