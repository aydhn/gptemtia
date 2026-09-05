from typing import Tuple, Dict, Any, List
import pandas as pd
import re

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)
from advanced_cross_asset_alignment.cross_asset_alignment_models import (
    AssetSymbolMapping,
    build_asset_symbol_mapping_id,
)


SYMBOL_NORMALIZATION_MAP: Dict[str, str] = {
    # FX
    "EURUSD": "EUR/USD",
    "EUR/USD": "EUR/USD",
    "EUR-USD": "EUR/USD",
    "USDTRY": "USD/TRY",
    "USD/TRY": "USD/TRY",
    "USD-TRY": "USD/TRY",
    "GBPUSD": "GBP/USD",
    "GBP/USD": "GBP/USD",
    "USDJPY": "USD/JPY",
    "USD/JPY": "USD/JPY",
    "DXY": "DXY_PLACEHOLDER",
    "DXY_PLACEHOLDER": "DXY_PLACEHOLDER",
    # Commodities
    "GOLD": "XAU/USD",
    "XAUUSD": "XAU/USD",
    "XAU/USD": "XAU/USD",
    "SILVER": "XAG/USD",
    "XAGUSD": "XAG/USD",
    "XAG/USD": "XAG/USD",
    "CL": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
    "WTI": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
    "WTI_CRUDE": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
    "WTI_CRUDE_CONTINUOUS_PLACEHOLDER": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
    "NG": "NATURAL_GAS_CONTINUOUS_PLACEHOLDER",
    "NATURAL_GAS": "NATURAL_GAS_CONTINUOUS_PLACEHOLDER",
    "NATURAL_GAS_CONTINUOUS_PLACEHOLDER": "NATURAL_GAS_CONTINUOUS_PLACEHOLDER",
    # Macro
    "US10Y": "US_10Y_YIELD",
    "US_10Y_YIELD": "US_10Y_YIELD",
    "FEDFUNDS": "FED_POLICY_RATE",
    "FED_POLICY_RATE": "FED_POLICY_RATE",
    "ECBRATE": "ECB_POLICY_RATE",
    "ECB_POLICY_RATE": "ECB_POLICY_RATE",
    "CBRTRATE": "CBRT_POLICY_RATE",
    "CBRT_POLICY_RATE": "CBRT_POLICY_RATE",
}

DEFAULT_MAPPINGS: List[Dict[str, Any]] = [
    {
        "source_domain": "fx",
        "target_domain": "macro",
        "source_symbol": "EUR/USD",
        "canonical_symbol": "EUR/USD",
        "target_reference": "FED_POLICY_RATE",
        "mapping_type": "economic_driver",
        "confidence_label": "high",
        "manual_review_required": False,
    },
    {
        "source_domain": "fx",
        "target_domain": "calendar",
        "source_symbol": "EUR/USD",
        "canonical_symbol": "EUR/USD",
        "target_reference": "FOMC_RATE_DECISION",
        "mapping_type": "event_driver",
        "confidence_label": "high",
        "manual_review_required": False,
    },

    {
        "source_domain": "fx",
        "target_domain": "commodity",
        "source_symbol": "EUR/USD",
        "canonical_symbol": "EUR/USD",
        "target_reference": "XAU/USD",
        "mapping_type": "cross_asset_context",
        "confidence_label": "medium",
        "manual_review_required": False,
    },
    {
        "source_domain": "fx",
        "target_domain": "macro",
        "source_symbol": "USD/TRY",
        "canonical_symbol": "USD/TRY",
        "target_reference": "CBRT_POLICY_RATE",
        "mapping_type": "economic_driver",
        "confidence_label": "high",
        "manual_review_required": False,
    },
    {
        "source_domain": "commodity",
        "target_domain": "macro",
        "source_symbol": "XAU/USD",
        "canonical_symbol": "XAU/USD",
        "target_reference": "US_10Y_YIELD",
        "mapping_type": "rate_inverse_driver",
        "confidence_label": "high",
        "manual_review_required": False,
    },
    {
        "source_domain": "commodity",
        "target_domain": "fx",
        "source_symbol": "XAU/USD",
        "canonical_symbol": "XAU/USD",
        "target_reference": "DXY_PLACEHOLDER",
        "mapping_type": "dollar_index_context",
        "confidence_label": "high",
        "manual_review_required": False,
    },
    {
        "source_domain": "commodity",
        "target_domain": "calendar",
        "source_symbol": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
        "canonical_symbol": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
        "target_reference": "EIA_CRUDE_INVENTORY_RELEASE",
        "mapping_type": "event_inventory_driver",
        "confidence_label": "high",
        "manual_review_required": False,
    },
    {
        "source_domain": "commodity",
        "target_domain": "calendar",
        "source_symbol": "NATURAL_GAS_CONTINUOUS_PLACEHOLDER",
        "canonical_symbol": "NATURAL_GAS_CONTINUOUS_PLACEHOLDER",
        "target_reference": "EIA_NATURAL_GAS_STORAGE_RELEASE",
        "mapping_type": "event_storage_driver",
        "confidence_label": "high",
        "manual_review_required": False,
    },
]


def normalize_cross_asset_symbol(value: str) -> str:
    cleaned = value.strip().upper()
    if cleaned in SYMBOL_NORMALIZATION_MAP:
        return SYMBOL_NORMALIZATION_MAP[cleaned]
    # Check if 7 char with underscore like EUR_USD
    if "_" in cleaned and len(cleaned) == 7 and cleaned.replace("_", "").isalpha():
        return cleaned.replace("_", "/")
    # Check if 6 character FX pair without slash
    if len(cleaned) == 6 and cleaned.isalpha():
        return f"{cleaned[:3]}/{cleaned[3:]}"
    return cleaned


def map_symbol_to_related_domains(symbol: str) -> Dict[str, Any]:
    norm = normalize_cross_asset_symbol(symbol)
    matches = [m for m in DEFAULT_MAPPINGS if m["canonical_symbol"] == norm]
    target_domains = list(set(m["target_domain"] for m in matches))
    return {
        "symbol": symbol,
        "canonical_symbol": norm,
        "mappings_count": len(matches),
        "target_references": [m["target_reference"] for m in matches],
        "target_domains": target_domains,
        "related_domains": target_domains,
    }



def build_asset_symbol_mapping_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()

    rows = []
    for item_data in DEFAULT_MAPPINGS:
        item = AssetSymbolMapping(
            mapping_id=build_asset_symbol_mapping_id(item_data["source_symbol"], item_data["target_reference"]),
            source_domain=item_data["source_domain"],
            target_domain=item_data["target_domain"],
            source_symbol=item_data["source_symbol"],
            canonical_symbol=item_data["canonical_symbol"],
            target_reference=item_data["target_reference"],
            mapping_type=item_data["mapping_type"],
            confidence_label=item_data["confidence_label"],
            manual_review_required=item_data["manual_review_required"],
        )
        rows.append(item.to_dict())

    df = pd.DataFrame(rows)
    summary = summarize_asset_symbol_mapping(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_asset_symbol_mapping(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_mappings": 0, "status": "EMPTY"}

    return {
        "total_mappings": len(df),
        "unique_source_symbols": int(df["canonical_symbol"].nunique()) if "canonical_symbol" in df.columns else 0,
        "unique_target_domains": list(df["target_domain"].unique()) if "target_domain" in df.columns else [],
        "asset_types": list(df["source_domain"].unique()) if "source_domain" in df.columns else [],
        "high_confidence_count": int((df["confidence_label"] == "high").sum()) if "confidence_label" in df.columns else 0,
        "non_signal": True,
        "status": "READY",
    }

