"""Phase 126: Regime State Taxonomy.

Defines canonical regime state specifications with mandatory regime_state_ prefix.
States represent environmental context, never trade signals or target labels.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

REGIME_STATES: List[Dict[str, Any]] = [
    {
        "state_id": "state_01_trend",
        "regime_state_name": "regime_state_trend_context",
        "regime_family": "regime_family_trend",
        "state_description": "Market environment exhibiting consistent moving average alignment and directional persistence",
        "source_feature_contract": "contract_trend_features",
        "validation_dependency": "val_trend_no_lookahead",
        "quality_dependency": "qual_trend_factor_drift",
        "non_signal": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "state_id": "state_02_range",
        "regime_state_name": "regime_state_range_context",
        "regime_family": "regime_family_range",
        "state_description": "Market environment exhibiting mean-reversion characteristics bounded within volatility channels",
        "source_feature_contract": "contract_range_features",
        "validation_dependency": "val_range_no_lookahead",
        "quality_dependency": "qual_range_factor_drift",
        "non_signal": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "state_id": "state_03_vol_high",
        "regime_state_name": "regime_state_volatility_high_context",
        "regime_family": "regime_family_volatility",
        "state_description": "Market environment with realized volatility in the top historical quintile",
        "source_feature_contract": "contract_volatility_features",
        "validation_dependency": "val_vol_no_lookahead",
        "quality_dependency": "qual_vol_factor_drift",
        "non_signal": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "state_id": "state_04_vol_low",
        "regime_state_name": "regime_state_volatility_low_context",
        "regime_family": "regime_family_volatility",
        "state_description": "Market environment with realized volatility in the bottom historical quintile",
        "source_feature_contract": "contract_volatility_features",
        "validation_dependency": "val_vol_no_lookahead",
        "quality_dependency": "qual_vol_factor_drift",
        "non_signal": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "state_id": "state_05_vol_expansion",
        "regime_state_name": "regime_state_volatility_expansion_context",
        "regime_family": "regime_family_volatility",
        "state_description": "Market environment characterized by opening volatility envelopes and increasing true range",
        "source_feature_contract": "contract_volatility_features",
        "validation_dependency": "val_vol_no_lookahead",
        "quality_dependency": "qual_vol_factor_drift",
        "non_signal": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "state_id": "state_06_vol_compression",
        "regime_state_name": "regime_state_volatility_compression_context",
        "regime_family": "regime_family_volatility",
        "state_description": "Market environment characterized by narrowing Bollinger bandwidth and compressed price action",
        "source_feature_contract": "contract_volatility_features",
        "validation_dependency": "val_vol_no_lookahead",
        "quality_dependency": "qual_vol_factor_drift",
        "non_signal": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "state_id": "state_07_macro_event",
        "regime_state_name": "regime_state_macro_event_context",
        "regime_family": "regime_family_event_context",
        "state_description": "Market environment during high-impact scheduled economic releases or monetary policy announcements",
        "source_feature_contract": "contract_macro_event_features",
        "validation_dependency": "val_event_window_alignment",
        "quality_dependency": "qual_calendar_staleness",
        "non_signal": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "state_id": "state_08_news_attention",
        "regime_state_name": "regime_state_news_attention_context",
        "regime_family": "regime_family_news_metadata_context",
        "state_description": "Market environment with elevated metadata-only news item count and topic concentration",
        "source_feature_contract": "contract_news_metadata_features",
        "validation_dependency": "val_news_metadata_only",
        "quality_dependency": "qual_news_staleness",
        "non_signal": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "state_id": "state_09_cross_asset",
        "regime_state_name": "regime_state_cross_asset_context",
        "regime_family": "regime_family_cross_asset_context",
        "state_description": "Market environment influenced by macro benchmarks (DXY, US10Y, SPX) alignment",
        "source_feature_contract": "contract_cross_asset_features",
        "validation_dependency": "val_cross_asset_alignment",
        "quality_dependency": "qual_cross_asset_drift",
        "non_signal": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "status": "regime_ready",
    },
    {
        "state_id": "state_10_transition",
        "regime_state_name": "regime_state_transition_placeholder",
        "regime_family": "regime_family_composite_placeholder",
        "state_description": "Placeholder state indicating boundary shift or regime breakdown between trend and range",
        "source_feature_contract": "contract_composite_features",
        "validation_dependency": "val_transition_alignment",
        "quality_dependency": "qual_stability_score",
        "non_signal": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "status": "regime_placeholder_only",
    },
    {
        "state_id": "state_11_uncertain",
        "regime_state_name": "regime_state_uncertain_placeholder",
        "regime_family": "regime_family_composite_placeholder",
        "state_description": "Placeholder state indicating insufficient factor consensus or elevated missingness",
        "source_feature_contract": "contract_composite_features",
        "validation_dependency": "val_uncertain_diagnostics",
        "quality_dependency": "qual_missingness_score",
        "non_signal": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "status": "regime_placeholder_only",
    },
]


def build_regime_state_taxonomy_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime state taxonomy."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(REGIME_STATES)

    # Validate all regime state names start with regime_state_
    invalid_names = [name for name in df["regime_state_name"] if not name.startswith("regime_state_")]
    if invalid_names:
        raise ValueError(f"Regime state names must start with 'regime_state_': {invalid_names}")

    summary = {
        "active_profile": active_profile.profile_name,
        "total_states": len(df),
        "all_prefixed_correctly": len(invalid_names) == 0,
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "no_targets_or_predictions": bool((df["contains_target_or_prediction"] == False).all()),
        "no_trading_recommendations": bool((df["contains_trading_recommendation"] == False).all()),
        "ready_states": len(df[df["status"] == "regime_ready"]),
        "placeholder_states": len(df[df["status"] == "regime_placeholder_only"]),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_regime_state_taxonomy(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime state taxonomy DataFrame."""
    return {
        "total_items": len(df),
        "state_names": list(df["regime_state_name"].unique()) if "regime_state_name" in df.columns else [],
        "families": list(df["regime_family"].unique()) if "regime_family" in df.columns else [],
        "all_non_signal": True,
    }
