"""Phase 127: Regime Feature Matrix Contracts.

Defines formal contracts for regime feature matrices across technical, factor,
macro, event, news metadata, cross-asset, and quality dimensions.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

CORE_FEATURE_MATRIX_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "regime_technical_feature_matrix_contract",
        "matrix_family": "technical",
        "required_entity_keys": ["fx_pair", "commodity_symbol"],
        "timestamp_field": "timestamp_utc",
        "symbol_field": "symbol",
        "required_feature_families": ["trend", "momentum", "volatility", "range", "volume_liquidity_placeholder"],
        "required_factor_families": ["technical", "trend", "momentum", "volatility"],
        "required_context_inputs": ["trend_context", "volatility_context", "range_context"],
        "required_quality_inputs": ["missingness", "drift_ks", "staleness"],
        "validation_required": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": False,
        "non_signal_required": True,
        "manual_review_required": True,
    },
    {
        "contract_name": "regime_factor_feature_matrix_contract",
        "matrix_family": "factor",
        "required_entity_keys": ["fx_pair", "commodity_symbol"],
        "timestamp_field": "timestamp_utc",
        "symbol_field": "symbol",
        "required_feature_families": ["technical_factors", "macro_factors", "cross_asset_factors"],
        "required_factor_families": ["mean_reversion", "volatility_regime", "trend_continuation", "event_importance"],
        "required_context_inputs": ["volatility_expansion", "range_bound", "trend_persistence"],
        "required_quality_inputs": ["factor_availability", "drift_psi", "validation_status"],
        "validation_required": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": False,
        "non_signal_required": True,
        "manual_review_required": True,
    },
    {
        "contract_name": "regime_macro_event_context_matrix_contract",
        "matrix_family": "macro_event",
        "required_entity_keys": ["macro_indicator", "calendar_event"],
        "timestamp_field": "timestamp_utc",
        "symbol_field": "indicator_or_event_id",
        "required_feature_families": ["macro_growth", "macro_inflation", "event_release_lag", "event_surprise"],
        "required_factor_families": ["macro_policy", "event_window_context"],
        "required_context_inputs": ["pre_event_window", "post_event_window", "macro_regime_state"],
        "required_quality_inputs": ["release_lag_integrity", "timestamp_monotonicity"],
        "validation_required": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": False,
        "non_signal_required": True,
        "manual_review_required": True,
    },
    {
        "contract_name": "regime_news_metadata_context_matrix_contract",
        "matrix_family": "news_metadata",
        "required_entity_keys": ["news_metadata_tag", "fx_pair", "commodity_symbol"],
        "timestamp_field": "timestamp_utc",
        "symbol_field": "asset_tag",
        "required_feature_families": ["news_volume_count", "topic_intensity", "asset_tag_frequency"],
        "required_factor_families": ["news_attention_factor"],
        "required_context_inputs": ["breaking_attention_window", "metadata_freshness_score"],
        "required_quality_inputs": ["metadata_only_verification", "zero_full_text_audit"],
        "validation_required": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": True,
        "non_signal_required": True,
        "manual_review_required": True,
    },
    {
        "contract_name": "regime_cross_asset_context_matrix_contract",
        "matrix_family": "cross_asset",
        "required_entity_keys": ["fx_pair", "commodity_symbol", "macro_indicator"],
        "timestamp_field": "timestamp_utc",
        "symbol_field": "pair_or_cross_key",
        "required_feature_families": ["fx_commodity_correlation", "macro_currency_coupling", "intermarket_spread"],
        "required_factor_families": ["cross_asset_alignment_factor"],
        "required_context_inputs": ["risk_on_off_context", "cross_asset_divergence_context"],
        "required_quality_inputs": ["session_overlap_check", "joint_missingness"],
        "validation_required": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": False,
        "non_signal_required": True,
        "manual_review_required": True,
    },
    {
        "contract_name": "regime_quality_drift_context_matrix_contract",
        "matrix_family": "quality_drift",
        "required_entity_keys": ["fx_pair", "commodity_symbol"],
        "timestamp_field": "timestamp_utc",
        "symbol_field": "symbol",
        "required_feature_families": ["staleness_flags", "drift_ks_scores", "missing_ratio_rolling"],
        "required_factor_families": ["data_reliability_factor"],
        "required_context_inputs": ["degraded_data_context", "high_drift_context"],
        "required_quality_inputs": ["manual_review_blocker_status"],
        "validation_required": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": False,
        "non_signal_required": True,
        "manual_review_required": True,
    },
    {
        "contract_name": "regime_combined_research_matrix_contract",
        "matrix_family": "combined_research",
        "required_entity_keys": ["fx_pair", "commodity_symbol", "macro_indicator", "calendar_event", "news_metadata_tag"],
        "timestamp_field": "timestamp_utc",
        "symbol_field": "symbol",
        "required_feature_families": ["technical", "factors", "macro", "event", "news_metadata", "cross_asset", "quality"],
        "required_factor_families": ["composite_regime_factor_set"],
        "required_context_inputs": ["multi_domain_regime_candidate_context"],
        "required_quality_inputs": ["full_pipeline_validation_pass"],
        "validation_required": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": True,
        "non_signal_required": True,
        "manual_review_required": True,
    },
]


def build_regime_feature_matrix_contract_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the feature matrix contract registry."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for c in CORE_FEATURE_MATRIX_CONTRACTS:
        c_copy = c.copy()
        c_copy["current_phase"] = p.current_phase
        c_copy["target_final_phase"] = p.target_final_phase
        c_copy["next_phase"] = p.next_phase
        c_copy["non_signal"] = True
        c_copy["source_preserved"] = True
        c_copy["official_approval"] = False
        c_copy["production_ready"] = False
        c_copy["broker_ready"] = False
        c_copy["model_training_executed"] = False
        c_copy["clustering_executed"] = False
        c_copy["unsupervised_execution"] = False
        c_copy["destructive_action_allowed"] = False
        c_copy["auto_fix_allowed"] = False
        c_copy["auto_drop_allowed"] = False
        c_copy["status"] = "matrix_ready"
        rows.append(c_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_feature_matrix_contracts(df)
    return df, summary


def validate_regime_feature_matrix_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Audit single feature matrix contract for Phase 127 requirements."""
    name = contract.get("contract_name", "")
    req_keys = [
        "contract_name",
        "matrix_family",
        "required_entity_keys",
        "timestamp_field",
        "symbol_field",
        "required_feature_families",
        "required_factor_families",
        "required_context_inputs",
        "required_quality_inputs",
        "validation_required",
        "no_lookahead_required",
        "non_signal_required",
        "manual_review_required",
    ]
    missing = [k for k in req_keys if k not in contract]

    # Validate forbidden terms in contract name or family
    forbidden_terms = ["signal", "buy", "sell", "long", "short", "position", "target", "label", "prediction", "recommendation"]
    forbidden_hits = [term for term in forbidden_terms if term in name.lower()]

    is_valid = (len(missing) == 0) and (len(forbidden_hits) == 0)
    return {
        "contract_name": name,
        "is_valid": is_valid,
        "missing_fields": missing,
        "forbidden_hits": forbidden_hits,
        "non_signal": True,
        "source_preserved": True,
    }


def summarize_regime_feature_matrix_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize feature matrix contracts registry."""
    return {
        "total_contracts": len(df),
        "ready_contracts": len(df),
        "contract_names": df["contract_name"].tolist() if not df.empty else [],
        "matrix_families": df["matrix_family"].unique().tolist() if not df.empty else [],
        "all_validation_required": bool(df["validation_required"].all()) if not df.empty else True,
        "all_no_lookahead_required": bool(df["no_lookahead_required"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "any_target_or_prediction": False,
        "model_training_executed": False,
        "clustering_executed": False,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }


build_regime_feature_matrix_contracts = build_regime_feature_matrix_contract_registry
