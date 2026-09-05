"""Phase 127: Regime Matrix Input Feature Registry.

Catalogs features sourced from upstream Phases 117-124 entering the regime matrix.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

INPUT_FEATURES_CATALOG: List[Dict[str, Any]] = [
    {
        "feature_key": "regime_matrix__tech__sma_ratio",
        "feature_name": "sma_fast_slow_ratio",
        "source_phase": 117,
        "source_module": "advanced_technical_indicators",
        "feature_family": "trend",
        "entity_type": "fx_or_commodity",
        "validation_dependency_ref": "rule_no_lookahead_ts_order",
        "quality_dependency_ref": "qual_missingness_max_5pct",
    },
    {
        "feature_key": "regime_matrix__tech__atr_realized_vol",
        "feature_name": "atr_normalized_volatility",
        "source_phase": 117,
        "source_module": "advanced_technical_indicators",
        "feature_family": "volatility",
        "entity_type": "fx_or_commodity",
        "validation_dependency_ref": "rule_no_lookahead_ts_order",
        "quality_dependency_ref": "qual_drift_psi_max_025",
    },
    {
        "feature_key": "regime_matrix__grid__rolling_return_w20",
        "feature_name": "rolling_return_window_20",
        "source_phase": 118,
        "source_module": "advanced_feature_grid",
        "feature_family": "returns",
        "entity_type": "fx_or_commodity",
        "validation_dependency_ref": "rule_warmup_nan_boundary",
        "quality_dependency_ref": "qual_missingness_max_5pct",
    },
    {
        "feature_key": "regime_matrix__grid__range_channel_w50",
        "feature_name": "channel_position_window_50",
        "source_phase": 118,
        "source_module": "advanced_feature_grid",
        "feature_family": "range",
        "entity_type": "fx_or_commodity",
        "validation_dependency_ref": "rule_no_lookahead_ts_order",
        "quality_dependency_ref": "qual_drift_psi_max_025",
    },
    {
        "feature_key": "regime_matrix__cross__fx_cmd_spread",
        "feature_name": "fx_commodity_relative_spread",
        "source_phase": 119,
        "source_module": "advanced_cross_asset_alignment",
        "feature_family": "cross_asset",
        "entity_type": "cross_asset_context",
        "validation_dependency_ref": "rule_asof_backward_only",
        "quality_dependency_ref": "qual_staleness_max_1day",
    },
    {
        "feature_key": "regime_matrix__fusion__macro_release_lag",
        "feature_name": "macro_indicator_release_lag",
        "source_phase": 120,
        "source_module": "advanced_feature_fusion",
        "feature_family": "macro_fusion",
        "entity_type": "macro_indicator",
        "validation_dependency_ref": "rule_macro_release_delay",
        "quality_dependency_ref": "qual_missingness_max_5pct",
    },
    {
        "feature_key": "regime_matrix__fusion__event_surprise",
        "feature_name": "calendar_event_surprise_zscore",
        "source_phase": 120,
        "source_module": "advanced_feature_fusion",
        "feature_family": "event_fusion",
        "entity_type": "calendar_event",
        "validation_dependency_ref": "rule_asof_backward_only",
        "quality_dependency_ref": "qual_missingness_max_5pct",
    },
    {
        "feature_key": "regime_matrix__fusion__news_attention",
        "feature_name": "news_metadata_attention_volume",
        "source_phase": 120,
        "source_module": "advanced_feature_fusion",
        "feature_family": "news_metadata",
        "entity_type": "news_metadata_tag",
        "validation_dependency_ref": "rule_news_metadata_only_boundary",
        "quality_dependency_ref": "qual_zero_full_text_guarantee",
    },
    {
        "feature_key": "regime_matrix__val__integrity_score",
        "feature_name": "feature_validation_integrity_score",
        "source_phase": 121,
        "source_module": "advanced_feature_validation",
        "feature_family": "validation",
        "entity_type": "validation_record",
        "validation_dependency_ref": "rule_validation_pass_required",
        "quality_dependency_ref": "qual_validation_readiness",
    },
    {
        "feature_key": "regime_matrix__qual__drift_score_psi",
        "feature_name": "population_stability_index_psi",
        "source_phase": 123,
        "source_module": "advanced_feature_quality_drift",
        "feature_family": "quality_drift",
        "entity_type": "quality_record",
        "validation_dependency_ref": "rule_drift_under_threshold",
        "quality_dependency_ref": "qual_drift_psi_max_025",
    },
    {
        "feature_key": "regime_matrix__store__lineage_pointer",
        "feature_name": "feature_store_lineage_pointer",
        "source_phase": 124,
        "source_module": "advanced_feature_store_integration",
        "feature_family": "store_metadata",
        "entity_type": "store_record",
        "validation_dependency_ref": "rule_source_preservation_enforced",
        "quality_dependency_ref": "qual_lineage_provenance_valid",
    },
]


def build_regime_matrix_input_feature_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the input features registry for Phase 127."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for feat in INPUT_FEATURES_CATALOG:
        f_copy = feat.copy()
        f_copy["current_phase"] = p.current_phase
        f_copy["target_final_phase"] = p.target_final_phase
        f_copy["next_phase"] = p.next_phase
        f_copy["non_signal"] = True
        f_copy["source_preserved"] = True
        f_copy["status"] = "matrix_ready"
        rows.append(f_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_matrix_input_features(df)
    return df, summary


def summarize_regime_matrix_input_features(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize input features registry."""
    return {
        "total_input_features": len(df),
        "total_features": len(df),
        "source_phases": sorted(df["source_phase"].unique().tolist()) if not df.empty else [],
        "feature_families": df["feature_family"].unique().tolist() if not df.empty else [],
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "status": "matrix_ready",
    }


build_regime_matrix_input_features_registry = build_regime_matrix_input_feature_registry
