"""Phase 126: Range Regime Families.

Registers range and mean-reversion regime sub-families, indicators, and non-signal contracts.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

RANGE_FAMILIES: List[Dict[str, Any]] = [
    {
        "sub_family_id": "range_fam_01_bound",
        "sub_family_name": "range_bound_context",
        "regime_family": "regime_family_range",
        "description": "Price oscillation confined within established horizontal bounds without breakout",
        "primary_features": "rolling_range_pct_20, range_stability_score",
        "underlying_factors": "factor_range_boundedness",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "sub_family_id": "range_fam_02_mean_reversion",
        "sub_family_name": "mean_reversion_context",
        "regime_family": "regime_family_range",
        "description": "Degree of pull toward rolling mean measured across multiple time horizons",
        "primary_features": "distance_to_sma_20, distance_to_ema_20, mean_reversion_speed",
        "underlying_factors": "factor_mean_reversion_distance",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "sub_family_id": "range_fam_03_zscore",
        "sub_family_name": "zscore_context",
        "regime_family": "regime_family_range",
        "description": "Rolling normalized standard deviation z-score measuring extreme deviations from central tendency",
        "primary_features": "rolling_zscore_20, rolling_zscore_60",
        "underlying_factors": "factor_zscore_deviation",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "sub_family_id": "range_fam_04_channel_position",
        "sub_family_name": "channel_position_context",
        "regime_family": "regime_family_range",
        "description": "Relative location of price within Bollinger percent_b and Keltner channels (0.0 - 1.0)",
        "primary_features": "bollinger_percent_b_20_2, keltner_channel_position",
        "underlying_factors": "factor_channel_relative_position",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "sub_family_id": "range_fam_05_compression_range",
        "sub_family_name": "compression_range_context",
        "regime_family": "regime_family_range",
        "description": "Narrow range contraction context indicating consolidation prior to volatility expansion",
        "primary_features": "rolling_range_zscore_20, candle_body_pct_mean",
        "underlying_factors": "factor_range_compression",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
]


def build_range_regime_family_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for range regime family registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(RANGE_FAMILIES)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_sub_families": len(df),
        "regime_family": "regime_family_range",
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


def summarize_range_regime_families(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize range regime families DataFrame."""
    return {
        "total_sub_families": len(df),
        "sub_family_names": list(df["sub_family_name"].unique()) if "sub_family_name" in df.columns else [],
        "non_signal": True,
    }
