"""Phase 122 Factor Input Feature Sets Registry.

Maps factor inputs to upstream feature specifications from Phases 116–121.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import (
    FACTOR_FAMILY_CALENDAR_EVENT,
    FACTOR_FAMILY_COMPOSITE,
    FACTOR_FAMILY_CROSS_ASSET_CONTEXT,
    FACTOR_FAMILY_MACRO_CONTEXT,
    FACTOR_FAMILY_MEAN_REVERSION,
    FACTOR_FAMILY_MOMENTUM,
    FACTOR_FAMILY_NEWS_ATTENTION,
    FACTOR_FAMILY_QUOTE_MICROSTRUCTURE,
    FACTOR_FAMILY_REGIME_PREP,
    FACTOR_FAMILY_RETURN,
    FACTOR_FAMILY_TREND,
    FACTOR_FAMILY_VOLATILITY,
    FACTOR_READY,
)
from advanced_factor_metadata.factor_metadata_models import (
    FactorInputFeatureSet,
    build_factor_input_feature_set_id,
)

FACTOR_INPUT_FEATURE_SET_SPECS: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_trend_multi_window_context",
        "factor_family": FACTOR_FAMILY_TREND,
        "required_features": ["trend__sma_20", "trend__sma_50", "trend__donchian_high_20"],
        "optional_features": ["trend__ema_12", "trend__ema_26"],
        "source_phase_refs": ["Phase 117", "Phase 118"],
        "validation_required": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_momentum_rsi_roc_context",
        "factor_family": FACTOR_FAMILY_MOMENTUM,
        "required_features": ["momentum__rsi_14", "momentum__roc_10"],
        "optional_features": ["momentum__stoch_k_14_3", "momentum__stoch_d_14_3"],
        "source_phase_refs": ["Phase 117", "Phase 118"],
        "validation_required": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_volatility_atr_realized_context",
        "factor_family": FACTOR_FAMILY_VOLATILITY,
        "required_features": ["volatility__atr_14", "volatility__realized_vol_20"],
        "optional_features": ["volatility__bb_bandwidth_20"],
        "source_phase_refs": ["Phase 117", "Phase 118"],
        "validation_required": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_mean_reversion_zscore_context",
        "factor_family": FACTOR_FAMILY_MEAN_REVERSION,
        "required_features": ["mean_reversion__rolling_zscore_20", "mean_reversion__dist_sma_50"],
        "optional_features": ["mean_reversion__percentile_rank_100"],
        "source_phase_refs": ["Phase 117", "Phase 118"],
        "validation_required": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_return_multi_horizon_context",
        "factor_family": FACTOR_FAMILY_RETURN,
        "required_features": ["return__simple_1d", "return__simple_5d", "return__simple_20d"],
        "optional_features": ["return__log_1d"],
        "source_phase_refs": ["Phase 117", "Phase 118"],
        "validation_required": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_quote_spread_context_placeholder",
        "factor_family": FACTOR_FAMILY_QUOTE_MICROSTRUCTURE,
        "required_features": ["quote__spread_bps", "quote__bid_ask_ratio"],
        "optional_features": ["quote__staleness_seconds"],
        "source_phase_refs": ["Phase 117"],
        "validation_required": True,
        "manual_review_required": True,
    },
    {
        "factor_name": "factor_macro_inflation_rate_context",
        "factor_family": FACTOR_FAMILY_MACRO_CONTEXT,
        "required_features": ["fusion__macro_cpi_rate", "fusion__macro_policy_rate"],
        "optional_features": ["fusion__macro_revision_flag"],
        "source_phase_refs": ["Phase 120", "Phase 121"],
        "validation_required": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_event_release_context",
        "factor_family": FACTOR_FAMILY_CALENDAR_EVENT,
        "required_features": ["fusion__event_pre_release_window", "fusion__event_post_release_window"],
        "optional_features": ["fusion__event_importance_weight"],
        "source_phase_refs": ["Phase 120", "Phase 121"],
        "validation_required": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_news_attention_context",
        "factor_family": FACTOR_FAMILY_NEWS_ATTENTION,
        "required_features": ["fusion__news_topic_attention_count", "fusion__news_asset_tag_count"],
        "optional_features": ["fusion__news_event_linkage_flag"],
        "source_phase_refs": ["Phase 120", "Phase 121"],
        "validation_required": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_cross_asset_context",
        "factor_family": FACTOR_FAMILY_CROSS_ASSET_CONTEXT,
        "required_features": ["cross__usd_try_gold_corr_30", "cross__eur_usd_wti_corr_30"],
        "optional_features": ["cross__asset_dispersion_index"],
        "source_phase_refs": ["Phase 119", "Phase 121"],
        "validation_required": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_regime_prep_placeholder",
        "factor_family": FACTOR_FAMILY_REGIME_PREP,
        "required_features": ["volatility__realized_vol_20", "trend__sma_slope_50"],
        "optional_features": ["fusion__macro_cpi_rate"],
        "source_phase_refs": ["Phase 118", "Phase 120"],
        "validation_required": True,
        "manual_review_required": True,
    },
    {
        "factor_name": "factor_composite_context_placeholder",
        "factor_family": FACTOR_FAMILY_COMPOSITE,
        "required_features": ["trend__sma_20", "fusion__macro_cpi_rate"],
        "optional_features": ["cross__usd_try_gold_corr_30"],
        "source_phase_refs": ["Phase 118", "Phase 119", "Phase 120"],
        "validation_required": True,
        "manual_review_required": True,
    },
]


def build_factor_input_feature_set_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Factor Input Feature Set Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    items: List[Dict[str, Any]] = []
    total_required = 0
    total_optional = 0

    for spec in FACTOR_INPUT_FEATURE_SET_SPECS:
        fset = FactorInputFeatureSet(
            feature_set_id=build_factor_input_feature_set_id(spec["factor_name"]),
            factor_name=spec["factor_name"],
            factor_family=spec["factor_family"],
            required_features=spec["required_features"],
            optional_features=spec["optional_features"],
            source_phase_refs=spec["source_phase_refs"],
            validation_required=spec["validation_required"],
            non_signal=True,
            manual_review_required=spec["manual_review_required"],
        )
        total_required += len(spec["required_features"])
        total_optional += len(spec["optional_features"])
        items.append(fset.to_dict())

    df = pd.DataFrame(items)
    summary = {
        "active_profile": active_profile.name,
        "total_feature_sets": len(items),
        "total_required_features": total_required,
        "total_optional_features": total_optional,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_READY,
    }
    return df, summary


def summarize_factor_input_feature_sets(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize factor input feature set registry DataFrame."""
    return {
        "total_feature_sets": len(df),
        "total_factors": int(df["factor_name"].nunique()) if "factor_name" in df else 0,
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df else 0,
        "non_signal": True,
    }
