"""Phase 127: Regime State Candidate Context Registry.

Defines candidate context indicators for research and dataset preparation.
Enforces that candidate contexts are strictly NOT targets, labels, predictions, or signals.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

CANDIDATE_CONTEXT_ENTRIES: List[Dict[str, Any]] = [
    {
        "candidate_name": "volatility_expansion_context",
        "context_name": "volatility_expansion_context",
        "regime_family": "volatility",
        "underlying_features": ["bollinger_expansion_ratio", "atr_slope"],
        "underlying_factors": ["volatility_expansion_factor"],
        "context_type": "volatility_dynamics",
        "description": "Indicates accelerating dispersion of price action across observation windows.",
    },
    {
        "candidate_name": "trend_strong_bull_context",
        "context_name": "trend_strong_bull_context",
        "regime_family": "trend",
        "underlying_features": ["sma_fast_slow_ratio", "macd_histogram_norm"],
        "underlying_factors": ["trend_persistence_factor"],
        "context_type": "trend_state",
        "description": "Indicates persistent directional slope without long/short trade recommendation.",
    },
    {
        "candidate_name": "range_tight_compression_context",
        "context_name": "range_tight_compression_context",
        "regime_family": "range",
        "underlying_features": ["channel_position_w50", "mean_reversion_zscore"],
        "underlying_factors": ["channel_distance_zscore_factor"],
        "context_type": "range_state",
        "description": "Indicates bounded price oscillation between support/resistance envelopes.",
    },
    {
        "candidate_name": "liquidity_stress_context",
        "context_name": "liquidity_stress_context",
        "regime_family": "liquidity",
        "underlying_features": ["spread_bid_ask_proxy", "turnover_dispersion"],
        "underlying_factors": ["market_liquidity_factor"],
        "context_type": "liquidity_state",
        "description": "Indicates constrained liquidity environment without execution recommendation.",
    },
    {
        "candidate_name": "volatility_low_context_candidate",
        "context_name": "volatility_low_context_candidate",
        "regime_family": "volatility",
        "underlying_features": ["atr_normalized_volatility", "historical_variance"],
        "underlying_factors": ["volatility_compression_factor"],
        "context_type": "volatility_level",
        "description": "Indicates subdued realized volatility context without directional bias.",
    },
    {
        "candidate_name": "macro_event_context_candidate",
        "context_name": "macro_event_context_candidate",
        "regime_family": "macro_event",
        "underlying_features": ["event_release_lag", "event_surprise_zscore"],
        "underlying_factors": ["scheduled_event_window_factor"],
        "context_type": "event_backdrop",
        "description": "Indicates proximity to high-salience macroeconomic data announcements.",
    },
    {
        "candidate_name": "news_attention_context_candidate",
        "context_name": "news_attention_context_candidate",
        "regime_family": "news_metadata",
        "underlying_features": ["news_metadata_attention_volume", "topic_intensity_score"],
        "underlying_factors": ["news_volume_frequency_factor"],
        "context_type": "attention_backdrop",
        "description": "Indicates elevated news frequency/tag volume (zero full text, zero sentiment models).",
    },
    {
        "candidate_name": "cross_asset_context_candidate",
        "context_name": "cross_asset_context_candidate",
        "regime_family": "cross_asset",
        "underlying_features": ["fx_commodity_relative_spread", "intermarket_correlation"],
        "underlying_factors": ["intermarket_relative_strength_factor"],
        "context_type": "coupling_state",
        "description": "Indicates divergent or coupled movements across asset classes.",
    },
    {
        "candidate_name": "transition_context_candidate",
        "context_name": "transition_context_candidate",
        "regime_family": "transition",
        "underlying_features": ["trend_break_ratio", "volatility_inflection"],
        "underlying_factors": ["transition_persistence_factor"],
        "context_type": "transition_phase",
        "description": "Indicates structural shift between regimes without predicting destination.",
    },
    {
        "candidate_name": "uncertain_context_candidate",
        "context_name": "uncertain_context_candidate",
        "regime_family": "uncertain",
        "underlying_features": ["conflicting_indicator_score", "dispersion_high"],
        "underlying_factors": ["data_reliability_factor"],
        "context_type": "low_confidence",
        "description": "Indicates conflicting indicators where no single regime profile dominates.",
    },
]


def is_valid_regime_state_candidate_context(name: str) -> bool:
    """Check whether context name is a registered non-signal candidate context."""
    valid_names = {c["context_name"] for c in CANDIDATE_CONTEXT_ENTRIES} | {c["candidate_name"] for c in CANDIDATE_CONTEXT_ENTRIES}
    return name in valid_names


def build_regime_state_candidate_context_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the regime state candidate context registry."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for cand in CANDIDATE_CONTEXT_ENTRIES:
        c_copy = cand.copy()
        c_copy["current_phase"] = p.current_phase
        c_copy["target_final_phase"] = p.target_final_phase
        c_copy["next_phase"] = p.next_phase
        c_copy["is_target_or_label"] = False
        c_copy["is_prediction"] = False
        c_copy["is_trade_signal"] = False
        c_copy["candidate_contexts_as_targets"] = False
        c_copy["is_research_only"] = True
        c_copy["non_signal"] = True
        c_copy["source_preserved"] = True
        c_copy["status"] = "matrix_ready"
        rows.append(c_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_state_candidate_context(df)
    return df, summary


def summarize_regime_state_candidate_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize candidate context registry."""
    return {
        "total_candidate_contexts": len(df),
        "candidate_names": df["candidate_name"].tolist() if not df.empty else [],
        "context_names": df["context_name"].tolist() if not df.empty and "context_name" in df.columns else [],
        "candidate_contexts_as_targets": False,
        "all_research_only": True,
        "all_zero_target_or_label": bool((~df["is_target_or_label"]).all()) if not df.empty else True,
        "all_zero_prediction": bool((~df["is_prediction"]).all()) if not df.empty else True,
        "all_zero_trade_signal": bool((~df["is_trade_signal"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "status": "matrix_ready",
    }


build_regime_state_candidate_contexts = build_regime_state_candidate_context_registry

