"""Phase 126: Cross-Asset Regime Context Registry.

Registers intermarket coupling contexts across FX, commodities, macro rates, and benchmarks.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

CROSS_ASSET_CONTEXTS: List[Dict[str, Any]] = [
    {
        "context_id": "cross_ctx_01_fx_comm",
        "context_name": "fx_commodity_context",
        "regime_family": "regime_family_cross_asset_context",
        "description": "Intermarket dynamics between USD pairs and gold/oil (e.g. XAU/USD vs USD/TRY, WTI vs DXY)",
        "coupled_assets": "EUR_USD, USD_TRY, XAU_USD, WTI_CRUDE",
        "source_phases": [119, 122],
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "cross_ctx_02_fx_macro",
        "context_name": "fx_macro_context",
        "regime_family": "regime_family_cross_asset_context",
        "description": "Sensitivity of foreign exchange pairs to rate differential expectations and DXY index",
        "coupled_assets": "EUR_USD, USD_TRY, DXY_INDEX, US10Y_YIELD",
        "source_phases": [119, 120, 122],
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "cross_ctx_03_comm_macro",
        "context_name": "commodity_macro_context",
        "regime_family": "regime_family_cross_asset_context",
        "description": "Sensitivity of commodities (gold, energy) to real yields, breakeven inflation, and global PMI",
        "coupled_assets": "XAU_USD, BRENT_CRUDE, US_TIPS_10Y, GLOBAL_PMI",
        "source_phases": [119, 120, 122],
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "cross_ctx_04_macro_cal",
        "context_name": "macro_calendar_context",
        "regime_family": "regime_family_cross_asset_context",
        "description": "Coupling of cyclical economic releases with sovereign yield curve repositioning",
        "coupled_assets": "CALENDAR_EVENTS, US2Y_YIELD, US10Y_YIELD",
        "source_phases": [110, 120, 122],
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "cross_ctx_05_cal_news",
        "context_name": "calendar_news_context",
        "regime_family": "regime_family_cross_asset_context",
        "description": "Temporal alignment between scheduled event publication windows and surge in headline volume",
        "coupled_assets": "ECONOMIC_CALENDAR, NEWS_METADATA_STREAM",
        "source_phases": [110, 111, 120],
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "cross_ctx_06_cross_domain",
        "context_name": "cross_domain_context_placeholder",
        "regime_family": "regime_family_cross_asset_context",
        "description": "Placeholder for multi-asset composite spillover indexes and cross-correlation matrix eigenvalues",
        "coupled_assets": "FULL_CROSS_ASSET_UNIVERSE",
        "source_phases": [119, 122, 124],
        "non_signal": True,
        "status": "regime_placeholder_only",
    },
]


def build_cross_asset_regime_context_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for cross-asset regime context registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(CROSS_ASSET_CONTEXTS)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_contexts": len(df),
        "regime_family": "regime_family_cross_asset_context",
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_cross_asset_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize cross-asset regime context DataFrame."""
    return {
        "total_contexts": len(df),
        "context_names": list(df["context_name"].unique()) if "context_name" in df.columns else [],
        "non_signal": True,
    }
