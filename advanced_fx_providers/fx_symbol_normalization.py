import pandas as pd
from typing import Tuple, Dict, List, Optional
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import (
    FXSymbolNormalizationRule,
    build_fx_symbol_normalization_rule_id,
)
import re


def build_default_fx_symbol_normalization_rules(
    profile: FXProviderProfile,
) -> List[FXSymbolNormalizationRule]:
    return [
        FXSymbolNormalizationRule(
            rule_id=build_fx_symbol_normalization_rule_id("generic", "compact"),
            canonical_pair="generic",
            provider_name="generic",
            provider_symbol_pattern="compact",
            normalized_symbol="compact",
            notes="E.g. EURUSD",
            manual_review_required=False,
        ),
        FXSymbolNormalizationRule(
            rule_id=build_fx_symbol_normalization_rule_id("generic", "slash"),
            canonical_pair="generic",
            provider_name="generic",
            provider_symbol_pattern="slash",
            normalized_symbol="slash",
            notes="E.g. EUR/USD",
            manual_review_required=False,
        ),
    ]


def normalize_fx_pair_symbol(symbol: str, provider_name: Optional[str] = None) -> str:
    # Basic heuristic for normalization to XXX/YYY
    symbol = symbol.strip().upper()

    # First, check if it already has a common separator
    match = re.match(r"^([A-Z]{2,5})[-_./]([A-Z]{2,5})$", symbol)
    if match:
        return f"{match.group(1)}/{match.group(2)}"

    clean_symbol = re.sub(r"[^A-Z]", "", symbol)

    # Standard 6-char FX
    if len(clean_symbol) == 6:
        return f"{clean_symbol[:3]}/{clean_symbol[3:]}"

    # Non-standard lengths
    quote_currencies = ["USDT", "USDC", "USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF"]
    for quote in quote_currencies:
        if clean_symbol.endswith(quote):
            base = clean_symbol[: -len(quote)]
            if len(base) >= 2:
                return f"{base}/{quote}"

    return clean_symbol  # Graceful fallback


def denormalize_fx_pair_symbol(canonical_pair: str, provider_name: str) -> str:
    # Mock denormalization for placeholder
    if provider_name == "generic_compact":
        return canonical_pair.replace("/", "")
    return canonical_pair


def build_fx_symbol_normalization_map(
    profile: FXProviderProfile,
) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_fx_symbol_normalization_rules(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_fx_symbol_normalization(df)


def summarize_fx_symbol_normalization(df: pd.DataFrame) -> Dict:
    return {"total_rules": len(df)}
