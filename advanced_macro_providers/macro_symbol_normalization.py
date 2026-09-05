
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroSymbolNormalizationRule, build_macro_symbol_normalization_rule_id

def build_default_macro_symbol_normalization_rules(profile: MacroProviderProfile) -> list[MacroSymbolNormalizationRule]:
    return [
        MacroSymbolNormalizationRule(
            rule_id=build_macro_symbol_normalization_rule_id("US_10Y_YIELD", "generic"),
            canonical_indicator="US_10Y_YIELD",
            provider_name="generic",
            provider_symbol_pattern="US10Y",
            normalized_symbol="US_10Y_YIELD",
            notes="",
            manual_review_required=False
        ),
        MacroSymbolNormalizationRule(
            rule_id=build_macro_symbol_normalization_rule_id("FED_POLICY_RATE", "generic"),
            canonical_indicator="FED_POLICY_RATE",
            provider_name="generic",
            provider_symbol_pattern="FEDFUNDS",
            normalized_symbol="FED_POLICY_RATE",
            notes="",
            manual_review_required=False
        )
    ]

def normalize_macro_indicator_symbol(symbol: str, provider_name: str | None = None) -> str:
    if symbol == "US10Y": return "US_10Y_YIELD"
    if symbol == "FEDFUNDS": return "FED_POLICY_RATE"
    return symbol

def denormalize_macro_indicator_symbol(canonical_indicator: str, provider_name: str) -> str:
    return canonical_indicator

def build_macro_symbol_normalization_map(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_symbol_normalization_rules(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_symbol_normalization(df)

def summarize_macro_symbol_normalization(df: pd.DataFrame) -> dict:
    return {"total_rules": len(df)}
