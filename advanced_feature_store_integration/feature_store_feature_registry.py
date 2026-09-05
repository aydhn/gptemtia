"""Phase 124 Feature Store Feature Registry.

Aggregates features across Phases 116-123 into a validation-aware,
quality/drift metadata referenced feature store registry.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

CORE_STORE_FEATURES = [
    {
        "store_key": "fx__eurusd__technical__sma__20",
        "feature_name": "sma_20",
        "feature_family": "technical_moving_average",
        "entity_type": "entity_fx_pair",
        "source_phase": 117,
        "data_type": "float64",
        "namespace": "fx.eurusd.technical",
        "validation_status": "validation_pass",
        "quality_score_ref": 0.98,
        "drift_score_ref": 0.05,
        "lineage_ref": "LIN_117_SMA_20",
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "contains_full_article_text": False,
    },
    {
        "store_key": "fx__eurusd__technical__ema__50",
        "feature_name": "ema_50",
        "feature_family": "technical_moving_average",
        "entity_type": "entity_fx_pair",
        "source_phase": 117,
        "data_type": "float64",
        "namespace": "fx.eurusd.technical",
        "validation_status": "validation_pass",
        "quality_score_ref": 0.97,
        "drift_score_ref": 0.04,
        "lineage_ref": "LIN_117_EMA_50",
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "contains_full_article_text": False,
    },
    {
        "store_key": "fx__eurusd__momentum__rsi__14",
        "feature_name": "rsi_14",
        "feature_family": "technical_momentum",
        "entity_type": "entity_fx_pair",
        "source_phase": 117,
        "data_type": "float64",
        "namespace": "fx.eurusd.momentum",
        "validation_status": "validation_pass",
        "quality_score_ref": 0.95,
        "drift_score_ref": 0.08,
        "lineage_ref": "LIN_117_RSI_14",
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "contains_full_article_text": False,
    },
    {
        "store_key": "commodity__brent__volatility__atr__14",
        "feature_name": "atr_14",
        "feature_family": "technical_volatility",
        "entity_type": "entity_commodity_symbol",
        "source_phase": 117,
        "data_type": "float64",
        "namespace": "commodity.brent.volatility",
        "validation_status": "validation_pass",
        "quality_score_ref": 0.96,
        "drift_score_ref": 0.07,
        "lineage_ref": "LIN_117_ATR_14",
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "contains_full_article_text": False,
    },
    {
        "store_key": "commodity__brent__grid__rolling_mean__20",
        "feature_name": "rolling_mean_20",
        "feature_family": "multi_window_grid",
        "entity_type": "entity_commodity_symbol",
        "source_phase": 118,
        "data_type": "float64",
        "namespace": "commodity.brent.grid",
        "validation_status": "validation_pass",
        "quality_score_ref": 0.99,
        "drift_score_ref": 0.03,
        "lineage_ref": "LIN_118_GRID_RM_20",
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "contains_full_article_text": False,
    },
    {
        "store_key": "cross_asset__brent_eurusd__correlation__30",
        "feature_name": "brent_eurusd_corr_30",
        "feature_family": "cross_asset_alignment",
        "entity_type": "entity_cross_asset_context",
        "source_phase": 119,
        "data_type": "float64",
        "namespace": "cross_asset.correlation",
        "validation_status": "validation_pass_with_warnings",
        "quality_score_ref": 0.91,
        "drift_score_ref": 0.12,
        "lineage_ref": "LIN_119_CORR_30",
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "contains_full_article_text": False,
    },
    {
        "store_key": "fusion__macro_news__energy_headline_sentiment_placeholder",
        "feature_name": "energy_event_attention_score",
        "feature_family": "macro_news_fusion",
        "entity_type": "entity_news_metadata",
        "source_phase": 120,
        "data_type": "float64",
        "namespace": "fusion.news_attention",
        "validation_status": "validation_pass",
        "quality_score_ref": 0.88,
        "drift_score_ref": 0.14,
        "lineage_ref": "LIN_120_ATTN_SCORE",
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "contains_full_article_text": False,
    },
    {
        "store_key": "validation__no_lookahead__audit_flag",
        "feature_name": "no_lookahead_compliance_flag",
        "feature_family": "feature_validation",
        "entity_type": "entity_factor_family",
        "source_phase": 121,
        "data_type": "int64",
        "namespace": "validation.guards",
        "validation_status": "validation_pass",
        "quality_score_ref": 1.00,
        "drift_score_ref": 0.00,
        "lineage_ref": "LIN_121_NO_LOOKAHEAD",
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "contains_full_article_text": False,
    },
    {
        "store_key": "quality_drift__staleness__consecutive_unchanged",
        "feature_name": "feature_staleness_metric",
        "feature_family": "feature_quality_drift",
        "entity_type": "entity_factor_family",
        "source_phase": 123,
        "data_type": "float64",
        "namespace": "quality_drift.diagnostics",
        "validation_status": "validation_pass",
        "quality_score_ref": 0.94,
        "drift_score_ref": 0.06,
        "lineage_ref": "LIN_123_STALENESS",
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "contains_full_article_text": False,
    },
]


def build_feature_store_feature_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of feature store features."""
    prof = profile or get_default_feature_store_integration_profile()
    records = []
    for f in CORE_STORE_FEATURES:
        item = dict(f)
        item["current_phase"] = prof.current_phase
        item["target_final_phase"] = prof.target_final_phase
        records.append(item)

    df = pd.DataFrame(records)
    summary = {
        "total_features": len(records),
        "source_phases": sorted(list(set(r["source_phase"] for r in records))),
        "feature_families": sorted(list(set(r["feature_family"] for r in records))),
        "non_signal": True,
        "source_preserved": True,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
        "contains_full_article_text": False,
    }
    return df, summary


def summarize_feature_store_feature_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize feature registry."""
    if df.empty:
        return {"total_features": 0, "non_signal": True, "source_preserved": True}
    return {
        "total_features": len(df),
        "source_phases": sorted(list(set(df["source_phase"]))) if "source_phase" in df.columns else [],
        "all_non_signal": bool(all(df.get("non_signal", [True]))),
        "all_source_preserved": bool(all(df.get("source_preserved", [True]))),
    }
