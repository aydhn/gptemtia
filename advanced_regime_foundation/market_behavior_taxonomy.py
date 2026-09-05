"""Phase 126: Market Behavior Taxonomy.

Defines canonical market behavior classifications without directional bias or trade signals.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

MARKET_BEHAVIORS: List[Dict[str, Any]] = [
    {
        "behavior_id": "beh_01_trending",
        "behavior_name": "trending_behavior",
        "behavior_category": "directional_persistence",
        "description": "Persistent directional price movement across moving average and channel indicators without trade recommendation",
        "associated_regime_family": "regime_family_trend",
        "key_characteristics": "ma_slope_high, channel_penetration_sustained, persistence_high",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "behavior_id": "beh_02_ranging",
        "behavior_name": "ranging_behavior",
        "behavior_category": "mean_reversion_envelope",
        "description": "Oscillating price behavior bounded between support and resistance envelopes",
        "associated_regime_family": "regime_family_range",
        "key_characteristics": "bounded_envelope, zscore_reversion, flat_ma_slope",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "behavior_id": "beh_03_high_volatility",
        "behavior_name": "high_volatility_behavior",
        "behavior_category": "dispersion_level",
        "description": "Elevated realized volatility and wide true range relative to historical baseline",
        "associated_regime_family": "regime_family_volatility",
        "key_characteristics": "atr_elevated, realized_vol_upper_quartile, wide_candle_bodies",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "behavior_id": "beh_04_low_volatility",
        "behavior_name": "low_volatility_behavior",
        "behavior_category": "dispersion_level",
        "description": "Subdued realized dispersion and narrow true range relative to historical baseline",
        "associated_regime_family": "regime_family_volatility",
        "key_characteristics": "atr_subdued, realized_vol_lower_quartile, narrow_candle_bodies",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "behavior_id": "beh_05_volatility_expansion",
        "behavior_name": "volatility_expansion_behavior",
        "behavior_category": "dispersion_dynamics",
        "description": "Rapid widening of Bollinger bandwidth and accelerating true range",
        "associated_regime_family": "regime_family_volatility",
        "key_characteristics": "bollinger_bandwidth_widening, atr_acceleration_positive",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "behavior_id": "beh_06_volatility_compression",
        "behavior_name": "volatility_compression_behavior",
        "behavior_category": "dispersion_dynamics",
        "description": "Squeezing of volatility bands and decelerating realized dispersion",
        "associated_regime_family": "regime_family_volatility",
        "key_characteristics": "bollinger_bandwidth_squeeze, atr_acceleration_negative",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "behavior_id": "beh_07_event_sensitive",
        "behavior_name": "event_sensitive_behavior",
        "behavior_category": "catalyst_sensitivity",
        "description": "Heightened sensitivity surrounding scheduled economic calendar events and announcements",
        "associated_regime_family": "regime_family_event_context",
        "key_characteristics": "event_window_active, surprise_reaction_amplified",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "behavior_id": "beh_08_macro_sensitive",
        "behavior_name": "macro_sensitive_behavior",
        "behavior_category": "macro_factor_alignment",
        "description": "Asset dynamics driven primarily by rate differential, inflation, and growth revisions",
        "associated_regime_family": "regime_family_macro_context",
        "key_characteristics": "rate_diff_correlation, inflation_surprise_alignment",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "behavior_id": "beh_09_cross_asset_sensitive",
        "behavior_name": "cross_asset_sensitive_behavior",
        "behavior_category": "intermarket_coupling",
        "description": "Behavior governed by macro benchmarks such as DXY, US10Y, SPX, or commodity spreads",
        "associated_regime_family": "regime_family_cross_asset_context",
        "key_characteristics": "dxy_coupling_high, us10y_coupling_high, brent_wti_spread_impact",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "behavior_id": "beh_10_liquidity_sensitive",
        "behavior_name": "liquidity_sensitive_placeholder",
        "behavior_category": "microstructure_placeholder",
        "description": "Placeholder behavior for spread widening, session transition, and quote staleness",
        "associated_regime_family": "regime_family_liquidity_placeholder",
        "key_characteristics": "spread_widening_placeholder, off_session_staleness_placeholder",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_placeholder_only",
    },
    {
        "behavior_id": "beh_11_transition_behavior",
        "behavior_name": "transition_behavior_placeholder",
        "behavior_category": "regime_shift_placeholder",
        "description": "Regime boundary transition placeholder indicating state instability or boundary crossing",
        "associated_regime_family": "regime_family_composite_placeholder",
        "key_characteristics": "mixed_indicators, trend_breakdown, volatility_shift",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_placeholder_only",
    },
    {
        "behavior_id": "beh_12_uncertain_behavior",
        "behavior_name": "uncertain_behavior_placeholder",
        "behavior_category": "diagnostics_placeholder",
        "description": "Uncertain behavior classification where contradictory factor metrics prevent clear attribution",
        "associated_regime_family": "regime_family_composite_placeholder",
        "key_characteristics": "insufficient_quality_score, conflicting_factor_readings",
        "non_signal": True,
        "contains_trading_recommendation": False,
        "status": "regime_placeholder_only",
    },
]


def build_market_behavior_taxonomy_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for market behavior taxonomy."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(MARKET_BEHAVIORS)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_behaviors": len(df),
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "no_trading_recommendations": bool((df["contains_trading_recommendation"] == False).all()),
        "ready_behaviors": len(df[df["status"] == "regime_ready"]),
        "placeholder_behaviors": len(df[df["status"] == "regime_placeholder_only"]),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_market_behavior_taxonomy(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize market behavior taxonomy DataFrame."""
    return {
        "total_items": len(df),
        "behavior_names": list(df["behavior_name"].unique()) if "behavior_name" in df.columns else [],
        "categories": list(df["behavior_category"].unique()) if "behavior_category" in df.columns else [],
        "all_non_signal": True,
    }
