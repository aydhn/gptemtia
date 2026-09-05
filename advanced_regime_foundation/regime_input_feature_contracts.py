"""Phase 126: Regime Input Feature Contracts.

Defines input feature and factor contracts required to construct downstream regime state datasets.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

INPUT_FEATURE_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "contract_volatility_features",
        "regime_family": "regime_family_volatility",
        "required_feature_families": "volatility_indicators, multi_window_volatility, atr_features",
        "required_factor_families": "factor_volatility_realized, factor_volatility_expansion",
        "source_phase_refs": [117, 118, 122, 124],
        "validation_required": True,
        "quality_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": True,
        "status": "regime_ready",
    },
    {
        "contract_name": "contract_trend_features",
        "regime_family": "regime_family_trend",
        "required_feature_families": "moving_averages, multi_window_trend, donchian_channels",
        "required_factor_families": "factor_trend_ma_slope, factor_trend_alignment",
        "source_phase_refs": [117, 118, 122, 124],
        "validation_required": True,
        "quality_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": True,
        "status": "regime_ready",
    },
    {
        "contract_name": "contract_range_features",
        "regime_family": "regime_family_range",
        "required_feature_families": "mean_reversion_indicators, multi_window_range, bollinger_bands",
        "required_factor_families": "factor_mean_reversion, factor_zscore_bounds",
        "source_phase_refs": [117, 118, 122, 124],
        "validation_required": True,
        "quality_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": True,
        "status": "regime_ready",
    },
    {
        "contract_name": "contract_liquidity_features",
        "regime_family": "regime_family_liquidity_placeholder",
        "required_feature_families": "quote_spread_features, quote_staleness_features",
        "required_factor_families": "factor_liquidity_placeholder",
        "source_phase_refs": [117, 122, 124],
        "validation_required": True,
        "quality_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": True,
        "status": "regime_placeholder_only",
    },
    {
        "contract_name": "contract_macro_features",
        "regime_family": "regime_family_macro_context",
        "required_feature_families": "macro_indicator_features, yield_spread_features",
        "required_factor_families": "factor_macro_differential, factor_macro_trend",
        "source_phase_refs": [109, 120, 122, 124],
        "validation_required": True,
        "quality_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": True,
        "status": "regime_ready",
    },
    {
        "contract_name": "contract_macro_event_features",
        "regime_family": "regime_family_event_context",
        "required_feature_families": "calendar_window_features, surprise_indicators",
        "required_factor_families": "factor_calendar_event, factor_event_window",
        "source_phase_refs": [110, 120, 122, 124],
        "validation_required": True,
        "quality_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": True,
        "status": "regime_ready",
    },
    {
        "contract_name": "contract_news_metadata_features",
        "regime_family": "regime_family_news_metadata_context",
        "required_feature_families": "news_volume_features, topic_entropy_features",
        "required_factor_families": "factor_news_attention, factor_news_tag_density",
        "source_phase_refs": [111, 120, 122, 124],
        "validation_required": True,
        "quality_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": True,
        "status": "regime_ready",
    },
    {
        "contract_name": "contract_cross_asset_features",
        "regime_family": "regime_family_cross_asset_context",
        "required_feature_families": "cross_asset_returns, benchmark_correlations",
        "required_factor_families": "factor_cross_asset_coupling, factor_intermarket_spread",
        "source_phase_refs": [119, 120, 122, 124],
        "validation_required": True,
        "quality_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": True,
        "status": "regime_ready",
    },
    {
        "contract_name": "contract_composite_features",
        "regime_family": "regime_family_composite_placeholder",
        "required_feature_families": "all_validated_features",
        "required_factor_families": "all_validated_factors",
        "source_phase_refs": [121, 122, 123, 124, 125],
        "validation_required": True,
        "quality_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": True,
        "status": "regime_placeholder_only",
    },
]


def build_regime_input_feature_contract_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime input feature contracts."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(INPUT_FEATURE_CONTRACTS)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_contracts": len(df),
        "all_validation_required": bool((df["validation_required"] == True).all()),
        "all_quality_required": bool((df["quality_required"] == True).all()),
        "all_no_lookahead_required": bool((df["no_lookahead_required"] == True).all()),
        "all_non_signal_required": bool((df["non_signal_required"] == True).all()),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def validate_regime_input_feature_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate an individual regime input feature contract."""
    issues = []
    required_keys = [
        "contract_name",
        "regime_family",
        "required_feature_families",
        "required_factor_families",
        "source_phase_refs",
    ]
    for key in required_keys:
        if key not in contract or not contract[key]:
            issues.append(f"Missing required contract field: {key}")

    if not contract.get("no_lookahead_required", False):
        issues.append("Contract must require no-lookahead guarantee")
    if not contract.get("non_signal_required", False):
        issues.append("Contract must require non-signal guarantee")

    return {
        "contract_name": contract.get("contract_name", "UNKNOWN"),
        "is_valid": len(issues) == 0,
        "issues": issues,
        "non_signal": True,
    }


def summarize_regime_input_feature_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime input feature contracts DataFrame."""
    return {
        "total_contracts": len(df),
        "contract_names": list(df["contract_name"].unique()) if "contract_name" in df.columns else [],
        "all_non_signal": True,
    }
