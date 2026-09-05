"""Phase 126: Liquidity Regime Placeholders.

Registers placeholder definitions for market microstructure, spread, and session availability.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

LIQUIDITY_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "placeholder_id": "liq_ph_01_spread",
        "placeholder_name": "quote_spread_context_placeholder",
        "regime_family": "regime_family_liquidity_placeholder",
        "description": "Placeholder for relative quote spread widening or narrowing across trading sessions",
        "primary_features": "quote_spread_pct, bid_ask_spread_zscore",
        "underlying_factors": "factor_liquidity_spread_placeholder",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_placeholder_only",
    },
    {
        "placeholder_id": "liq_ph_02_staleness",
        "placeholder_name": "quote_staleness_context_placeholder",
        "regime_family": "regime_family_liquidity_placeholder",
        "description": "Placeholder tracking time delta since last quote update or stale price ticks",
        "primary_features": "quote_staleness_seconds, tick_update_frequency",
        "underlying_factors": "factor_liquidity_staleness_placeholder",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_placeholder_only",
    },
    {
        "placeholder_id": "liq_ph_03_session",
        "placeholder_name": "market_session_liquidity_placeholder",
        "regime_family": "regime_family_liquidity_placeholder",
        "description": "Placeholder for London/NY session overlap versus Asian/off-hours session depth",
        "primary_features": "session_overlap_flag, typical_session_volume_ratio",
        "underlying_factors": "factor_liquidity_session_placeholder",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_placeholder_only",
    },
    {
        "placeholder_id": "liq_ph_04_availability",
        "placeholder_name": "data_availability_liquidity_placeholder",
        "regime_family": "regime_family_liquidity_placeholder",
        "description": "Placeholder measuring data feed availability and missing bar ratios during market closure",
        "primary_features": "data_gap_ratio, missing_feed_seconds",
        "underlying_factors": "factor_liquidity_availability_placeholder",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_placeholder_only",
    },
]


def build_liquidity_regime_placeholder_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for liquidity regime placeholder registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(LIQUIDITY_PLACEHOLDERS)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_placeholders": len(df),
        "regime_family": "regime_family_liquidity_placeholder",
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "no_trading_recommendations": bool((df["contains_trading_recommendation"] == False).all()),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_liquidity_regime_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize liquidity regime placeholders DataFrame."""
    return {
        "total_placeholders": len(df),
        "placeholder_names": list(df["placeholder_name"].unique()) if "placeholder_name" in df.columns else [],
        "non_signal": True,
    }
