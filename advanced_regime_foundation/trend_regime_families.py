"""Phase 126: Trend Regime Families.

Registers trend regime sub-families, indicators, and non-signal contracts.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

TREND_FAMILIES: List[Dict[str, Any]] = [
    {
        "sub_family_id": "trend_fam_01_ma",
        "sub_family_name": "moving_average_trend_context",
        "regime_family": "regime_family_trend",
        "description": "Multi-window moving average alignment (SMA 20/50/200) measuring directional slope consistency",
        "primary_features": "sma_20_slope, sma_50_slope, ma_alignment_score",
        "underlying_factors": "factor_trend_ma_slope, factor_trend_alignment",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "sub_family_id": "trend_fam_02_macd",
        "sub_family_name": "macd_context_placeholder",
        "regime_family": "regime_family_trend",
        "description": "MACD histogram and line differential context without using forbidden signal line terms",
        "primary_features": "macd_line, macd_smooth, macd_histogram",
        "underlying_factors": "factor_trend_macd",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_placeholder_only",
    },
    {
        "sub_family_id": "trend_fam_03_donchian",
        "sub_family_name": "donchian_trend_context",
        "regime_family": "regime_family_trend",
        "description": "Donchian channel breakout and continuous boundary hugging measurement",
        "primary_features": "donchian_upper_dist, donchian_lower_dist, channel_position",
        "underlying_factors": "factor_trend_donchian_breakout",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "sub_family_id": "trend_fam_04_persistence",
        "sub_family_name": "trend_persistence_placeholder",
        "regime_family": "regime_family_trend",
        "description": "Trend duration and autocorrelation persistence measuring longevity of the directional state",
        "primary_features": "trend_bar_count, return_autocorr_lag1",
        "underlying_factors": "factor_trend_persistence",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_placeholder_only",
    },
    {
        "sub_family_id": "trend_fam_05_transition",
        "sub_family_name": "trend_transition_placeholder",
        "regime_family": "regime_family_trend",
        "description": "Trend exhaustion or momentum divergence placeholder identifying potential breakdown into range",
        "primary_features": "rsi_divergence_metric, adx_decay_slope",
        "underlying_factors": "factor_trend_exhaustion",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_placeholder_only",
    },
]


def build_trend_regime_family_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for trend regime family registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(TREND_FAMILIES)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_sub_families": len(df),
        "regime_family": "regime_family_trend",
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


def summarize_trend_regime_families(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize trend regime families DataFrame."""
    return {
        "total_sub_families": len(df),
        "sub_family_names": list(df["sub_family_name"].unique()) if "sub_family_name" in df.columns else [],
        "non_signal": True,
    }
