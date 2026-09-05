"""Phase 122 Factor Dependency Registry.

Tracks upstream feature and data dependencies across Phases 116–121 for each factor.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_READY
from advanced_factor_metadata.factor_metadata_models import (
    FactorDependency,
    build_factor_dependency_id,
)

FACTOR_DEPENDENCY_ENTRIES: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_trend_multi_window_context",
        "dependency_type": "moving_average_grid",
        "dependency_ref": "advanced_feature_grid.moving_average_window_grid",
        "source_phase": "Phase 118",
        "dependency_note": "Requires multi-window SMA/EMA curves.",
        "mandatory": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_trend_multi_window_context",
        "dependency_type": "validation_guard",
        "dependency_ref": "advanced_feature_validation.no_lookahead_rules",
        "source_phase": "Phase 121",
        "dependency_note": "Requires verified zero shift(-1) operations.",
        "mandatory": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_momentum_rsi_roc_context",
        "dependency_type": "momentum_grid",
        "dependency_ref": "advanced_feature_grid.momentum_window_grid",
        "source_phase": "Phase 118",
        "dependency_note": "Requires RSI and ROC multi-window features.",
        "mandatory": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_momentum_rsi_roc_context",
        "dependency_type": "validation_guard",
        "dependency_ref": "advanced_feature_validation.feature_numeric_sanity_validation",
        "source_phase": "Phase 121",
        "dependency_note": "Requires bounded oscillator sanity checks.",
        "mandatory": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_volatility_atr_realized_context",
        "dependency_type": "volatility_grid",
        "dependency_ref": "advanced_feature_grid.volatility_window_grid",
        "source_phase": "Phase 118",
        "dependency_note": "Requires ATR and rolling realized volatility series.",
        "mandatory": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_volatility_atr_realized_context",
        "dependency_type": "validation_guard",
        "dependency_ref": "advanced_feature_validation.feature_infinite_value_validation",
        "source_phase": "Phase 121",
        "dependency_note": "Requires zero infinite values in volatility features.",
        "mandatory": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_mean_reversion_zscore_context",
        "dependency_type": "mean_reversion_grid",
        "dependency_ref": "advanced_feature_grid.mean_reversion_window_grid",
        "source_phase": "Phase 118",
        "dependency_note": "Requires rolling z-score and distance-to-MA features.",
        "mandatory": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_return_multi_horizon_context",
        "dependency_type": "return_grid",
        "dependency_ref": "advanced_feature_grid.return_window_grid",
        "source_phase": "Phase 118",
        "dependency_note": "Requires trailing backward-only return grids.",
        "mandatory": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_quote_spread_context_placeholder",
        "dependency_type": "quote_features",
        "dependency_ref": "advanced_technical_indicators.quote_microstructure_features",
        "source_phase": "Phase 117",
        "dependency_note": "Requires microstructure bid-ask spread quotes.",
        "mandatory": False,
        "manual_review_required": True,
    },
    {
        "factor_name": "factor_macro_inflation_rate_context",
        "dependency_type": "macro_fusion",
        "dependency_ref": "advanced_feature_fusion.macro_calendar_fusion",
        "source_phase": "Phase 120",
        "dependency_note": "Requires point-in-time inflation rates.",
        "mandatory": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_macro_inflation_rate_context",
        "dependency_type": "validation_guard",
        "dependency_ref": "advanced_feature_validation.macro_release_lag_validation",
        "source_phase": "Phase 121",
        "dependency_note": "Guarantees release lag causality.",
        "mandatory": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_event_release_context",
        "dependency_type": "calendar_event_windows",
        "dependency_ref": "advanced_feature_fusion.calendar_event_window_features",
        "source_phase": "Phase 120",
        "dependency_note": "Requires pre- and post-release event windows.",
        "mandatory": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_news_attention_context",
        "dependency_type": "news_metadata_fusion",
        "dependency_ref": "advanced_feature_fusion.news_topic_feature_fusion",
        "source_phase": "Phase 120",
        "dependency_note": "Requires metadata topic and entity count aggregations.",
        "mandatory": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_news_attention_context",
        "dependency_type": "validation_guard",
        "dependency_ref": "advanced_feature_validation.news_metadata_only_validation",
        "source_phase": "Phase 121",
        "dependency_note": "Guarantees zero full text or web scraping.",
        "mandatory": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_cross_asset_context",
        "dependency_type": "cross_asset_alignment",
        "dependency_ref": "advanced_cross_asset_alignment.cross_domain_matrix",
        "source_phase": "Phase 119",
        "dependency_note": "Requires aligned FX and commodity feature matrices.",
        "mandatory": True,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_regime_prep_placeholder",
        "dependency_type": "multi_domain_grid",
        "dependency_ref": "advanced_feature_grid.volatility_window_grid",
        "source_phase": "Phase 118",
        "dependency_note": "Feeds candidate features for Phase 126+ regime classification.",
        "mandatory": False,
        "manual_review_required": True,
    },
    {
        "factor_name": "factor_composite_context_placeholder",
        "dependency_type": "cross_domain_fusion",
        "dependency_ref": "advanced_feature_fusion.cross_domain_context_fusion",
        "source_phase": "Phase 120",
        "dependency_note": "Aggregates technical, macro, and event features for research.",
        "mandatory": False,
        "manual_review_required": True,
    },
]


def build_factor_dependency_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Factor Dependency Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    items: List[Dict[str, Any]] = []
    for entry in FACTOR_DEPENDENCY_ENTRIES:
        dep = FactorDependency(
            dependency_id=build_factor_dependency_id(entry["factor_name"], entry["dependency_ref"]),
            factor_name=entry["factor_name"],
            dependency_type=entry["dependency_type"],
            dependency_ref=entry["dependency_ref"],
            source_phase=entry["source_phase"],
            dependency_note=entry["dependency_note"],
            mandatory=entry["mandatory"],
            manual_review_required=entry["manual_review_required"],
        )
        items.append(dep.to_dict())

    df = pd.DataFrame(items)
    summary = {
        "active_profile": active_profile.name,
        "total_dependencies": len(items),
        "mandatory_dependencies": sum(1 for i in items if i["mandatory"]),
        "optional_dependencies": sum(1 for i in items if not i["mandatory"]),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_READY,
    }
    return df, summary


def summarize_factor_dependency_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize factor dependency registry DataFrame."""
    return {
        "total_dependencies": len(df),
        "factors_covered": int(df["factor_name"].nunique()) if "factor_name" in df else 0,
        "source_phases": list(df["source_phase"].unique()) if "source_phase" in df else [],
        "non_signal": True,
    }
