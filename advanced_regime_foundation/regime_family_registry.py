"""Phase 126: Master Regime Family Registry.

Registers all canonical regime families and connects them to indicator and factor prerequisites.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

MASTER_REGIME_FAMILIES: List[Dict[str, Any]] = [
    {
        "family_id": "fam_01_volatility",
        "family_name": "regime_family_volatility",
        "family_category": "dispersion_analysis",
        "description": "Volatility regime family analyzing realized volatility, ATR, and Bollinger bandwidth envelopes",
        "primary_indicators": "atr, realized_volatility, bollinger_bandwidth, rolling_std",
        "source_phases": [117, 118, 122, 124],
        "non_signal": True,
        "model_training_executed": False,
        "clustering_executed": False,
        "status": "regime_ready",
    },
    {
        "family_id": "fam_02_trend",
        "family_name": "regime_family_trend",
        "family_category": "directional_alignment",
        "description": "Trend regime family evaluating moving average slopes, Donchian channels, and trend persistence",
        "primary_indicators": "sma_slope, ema_alignment, donchian_channel, adx_dmi",
        "source_phases": [117, 118, 122, 124],
        "non_signal": True,
        "model_training_executed": False,
        "clustering_executed": False,
        "status": "regime_ready",
    },
    {
        "family_id": "fam_03_range",
        "family_name": "regime_family_range",
        "family_category": "mean_reversion",
        "description": "Range regime family assessing mean-reversion, zscore bounds, and channel envelope positions",
        "primary_indicators": "rolling_zscore, bollinger_percent_b, channel_position, range_zscore",
        "source_phases": [117, 118, 122, 124],
        "non_signal": True,
        "model_training_executed": False,
        "clustering_executed": False,
        "status": "regime_ready",
    },
    {
        "family_id": "fam_04_liquidity",
        "family_name": "regime_family_liquidity_placeholder",
        "family_category": "microstructure_placeholder",
        "description": "Liquidity regime placeholder tracking spread, staleness, and trading session alignment",
        "primary_indicators": "quote_spread, quote_staleness, session_status",
        "source_phases": [117, 122, 124],
        "non_signal": True,
        "model_training_executed": False,
        "clustering_executed": False,
        "status": "regime_placeholder_only",
    },
    {
        "family_id": "fam_05_macro",
        "family_name": "regime_family_macro_context",
        "family_category": "macroeconomic_environment",
        "description": "Macro regime context family analyzing inflation trends, rate differentials, and growth revisions",
        "primary_indicators": "inflation_trend, rate_differential, growth_revisions",
        "source_phases": [109, 120, 122, 124],
        "non_signal": True,
        "model_training_executed": False,
        "clustering_executed": False,
        "status": "regime_ready",
    },
    {
        "family_id": "fam_06_event",
        "family_name": "regime_family_event_context",
        "family_category": "scheduled_catalysts",
        "description": "Event regime context family evaluating pre/post event windows, release delays, and event importance",
        "primary_indicators": "event_window_minutes, importance_score, release_delay_minutes",
        "source_phases": [110, 120, 122, 124],
        "non_signal": True,
        "model_training_executed": False,
        "clustering_executed": False,
        "status": "regime_ready",
    },
    {
        "family_id": "fam_07_news",
        "family_name": "regime_family_news_metadata_context",
        "family_category": "news_metadata_attention",
        "description": "News metadata regime context analyzing count, topic concentration, and freshness without text/embeddings",
        "primary_indicators": "news_item_count_1h, topic_entropy, news_freshness_minutes",
        "source_phases": [111, 120, 122, 124],
        "non_signal": True,
        "model_training_executed": False,
        "clustering_executed": False,
        "status": "regime_ready",
    },
    {
        "family_id": "fam_08_cross_asset",
        "family_name": "regime_family_cross_asset_context",
        "family_category": "intermarket_dynamics",
        "description": "Cross-asset regime context evaluating DXY, US10Y, SPX coupling and commodity cross-spreads",
        "primary_indicators": "dxy_rolling_corr, us10y_rolling_corr, brent_wti_spread",
        "source_phases": [119, 122, 124],
        "non_signal": True,
        "model_training_executed": False,
        "clustering_executed": False,
        "status": "regime_ready",
    },
    {
        "family_id": "fam_09_composite",
        "family_name": "regime_family_composite_placeholder",
        "family_category": "multi_factor_synthesis",
        "description": "Composite regime placeholder for multi-family cross-checks, stability analysis, and transition detection",
        "primary_indicators": "consensus_score, stability_index, transition_flag",
        "source_phases": [122, 123, 124, 125],
        "non_signal": True,
        "model_training_executed": False,
        "clustering_executed": False,
        "status": "regime_placeholder_only",
    },
]


def build_regime_family_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for master regime family registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(MASTER_REGIME_FAMILIES)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_families": len(df),
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "model_training_executed": False,
        "clustering_executed": False,
        "ready_families": len(df[df["status"] == "regime_ready"]),
        "placeholder_families": len(df[df["status"] == "regime_placeholder_only"]),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_regime_family_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime family registry DataFrame."""
    return {
        "total_families": len(df),
        "family_names": list(df["family_name"].unique()) if "family_name" in df.columns else [],
        "categories": list(df["family_category"].unique()) if "family_category" in df.columns else [],
        "non_signal": True,
    }
