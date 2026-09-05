"""Phase 126: Volatility Regime Families.

Registers volatility regime sub-families, indicators, and non-signal contracts.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

VOLATILITY_FAMILIES: List[Dict[str, Any]] = [
    {
        "sub_family_id": "vol_fam_01_level",
        "sub_family_name": "volatility_level_context",
        "regime_family": "regime_family_volatility",
        "description": "Baseline dispersion context classifying market into low, normal, or high volatility tiers",
        "primary_features": "realized_volatility_20, realized_volatility_60, atr_pct_14",
        "underlying_factors": "factor_volatility_realized, factor_volatility_atr",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "sub_family_id": "vol_fam_02_expansion",
        "sub_family_name": "volatility_expansion_context",
        "regime_family": "regime_family_volatility",
        "description": "Volatility expansion context capturing explosive bandwidth opening or volatility breakouts",
        "primary_features": "bollinger_bandwidth_slope, atr_acceleration_5_20",
        "underlying_factors": "factor_volatility_expansion, factor_volatility_breakout",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "sub_family_id": "vol_fam_03_compression",
        "sub_family_name": "volatility_compression_context",
        "regime_family": "regime_family_volatility",
        "description": "Volatility compression context identifying band squeezes and reduced price movement envelopes",
        "primary_features": "bollinger_bandwidth_percentile, true_range_ratio",
        "underlying_factors": "factor_volatility_compression, factor_volatility_squeeze",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "sub_family_id": "vol_fam_04_atr_realized",
        "sub_family_name": "atr_realized_volatility_context",
        "regime_family": "regime_family_volatility",
        "description": "Cross-measurement of ATR range versus close-to-close realized dispersion",
        "primary_features": "atr_14, realized_vol_20, parkinson_vol_20",
        "underlying_factors": "factor_volatility_atr, factor_volatility_parkinson",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "sub_family_id": "vol_fam_05_bollinger_width",
        "sub_family_name": "bollinger_width_context",
        "regime_family": "regime_family_volatility",
        "description": "Standardized Bollinger bandwidth relative to rolling 100-bar percentile rank",
        "primary_features": "bollinger_bandwidth_20_2, bandwidth_percentile_100",
        "underlying_factors": "factor_volatility_bollinger_width",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
]


def build_volatility_regime_family_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for volatility regime family registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(VOLATILITY_FAMILIES)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_sub_families": len(df),
        "regime_family": "regime_family_volatility",
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


def summarize_volatility_regime_families(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize volatility regime families DataFrame."""
    return {
        "total_sub_families": len(df),
        "sub_family_names": list(df["sub_family_name"].unique()) if "sub_family_name" in df.columns else [],
        "non_signal": True,
    }
