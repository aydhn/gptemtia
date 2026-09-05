"""Phase 124 Feature Store Contract Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

STORE_CONTRACTS = [
    {
        "store_name": "technical_feature_store_contract",
        "entity_keys": ["fx_pair", "commodity_symbol"],
        "timestamp_field": "timestamp",
        "symbol_field": "symbol",
        "feature_namespace_policy": "entity__symbol__technical__indicator__window",
        "schema_policy": "strict_canonical_types",
        "validation_status_required": True,
        "quality_score_required": True,
        "drift_score_required": True,
        "lineage_reference_required": True,
        "manual_review_blocker_policy": "block_on_unresolved",
        "non_signal_required": True,
        "source_preserved_required": True,
        "source_phase": 117,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_name": "multi_window_feature_grid_store_contract",
        "entity_keys": ["fx_pair", "commodity_symbol"],
        "timestamp_field": "timestamp",
        "symbol_field": "symbol",
        "feature_namespace_policy": "entity__symbol__grid__window",
        "schema_policy": "strict_multi_window_grid",
        "validation_status_required": True,
        "quality_score_required": True,
        "drift_score_required": True,
        "lineage_reference_required": True,
        "manual_review_blocker_policy": "block_on_unresolved",
        "non_signal_required": True,
        "source_preserved_required": True,
        "source_phase": 118,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_name": "cross_asset_feature_store_contract",
        "entity_keys": ["cross_asset_context", "fx_pair", "commodity_symbol"],
        "timestamp_field": "timestamp",
        "symbol_field": "context_id",
        "feature_namespace_policy": "cross_asset__pair__metric__window",
        "schema_policy": "asof_backward_alignment_only",
        "validation_status_required": True,
        "quality_score_required": True,
        "drift_score_required": True,
        "lineage_reference_required": True,
        "manual_review_blocker_policy": "block_on_unresolved",
        "non_signal_required": True,
        "source_preserved_required": True,
        "source_phase": 119,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_name": "macro_calendar_news_fusion_store_contract",
        "entity_keys": ["macro_indicator", "calendar_event", "news_metadata_tag"],
        "timestamp_field": "timestamp",
        "symbol_field": "event_id",
        "feature_namespace_policy": "fusion__domain__feature__window",
        "schema_policy": "metadata_only_no_full_text",
        "validation_status_required": True,
        "quality_score_required": True,
        "drift_score_required": True,
        "lineage_reference_required": True,
        "manual_review_blocker_policy": "block_on_unresolved",
        "non_signal_required": True,
        "source_preserved_required": True,
        "source_phase": 120,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_name": "factor_metadata_store_contract",
        "entity_keys": ["factor_family"],
        "timestamp_field": "timestamp",
        "symbol_field": "factor_id",
        "feature_namespace_policy": "factor__family__asset__symbol__factor_name__window",
        "schema_policy": "canonical_factor_registry",
        "validation_status_required": True,
        "quality_score_required": True,
        "drift_score_required": True,
        "lineage_reference_required": True,
        "manual_review_blocker_policy": "block_on_unresolved",
        "non_signal_required": True,
        "source_preserved_required": True,
        "source_phase": 122,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_name": "quality_drift_metadata_store_contract",
        "entity_keys": ["fx_pair", "commodity_symbol", "factor_family"],
        "timestamp_field": "timestamp",
        "symbol_field": "feature_or_factor_id",
        "feature_namespace_policy": "quality_drift__metric__target_ref",
        "schema_policy": "diagnostic_bounds_zero_to_one",
        "validation_status_required": True,
        "quality_score_required": True,
        "drift_score_required": True,
        "lineage_reference_required": True,
        "manual_review_blocker_policy": "block_on_unresolved",
        "non_signal_required": True,
        "source_preserved_required": True,
        "source_phase": 123,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_name": "validation_status_store_contract",
        "entity_keys": ["fx_pair", "commodity_symbol", "macro_indicator", "calendar_event", "factor_family"],
        "timestamp_field": "timestamp",
        "symbol_field": "item_id",
        "feature_namespace_policy": "validation__status__item_ref",
        "schema_policy": "no_lookahead_and_leakage_audit",
        "validation_status_required": True,
        "quality_score_required": True,
        "drift_score_required": True,
        "lineage_reference_required": True,
        "manual_review_blocker_policy": "block_on_unresolved",
        "non_signal_required": True,
        "source_preserved_required": True,
        "source_phase": 121,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    },
]


def build_feature_store_contract_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of feature store contracts."""
    prof = profile or get_default_feature_store_integration_profile()
    records = []
    for c in STORE_CONTRACTS:
        item = dict(c)
        item["entity_keys_str"] = ",".join(item["entity_keys"])
        item["current_phase"] = prof.current_phase
        item["target_final_phase"] = prof.target_final_phase
        records.append(item)

    df = pd.DataFrame(records)
    summary = {
        "total_contracts": len(records),
        "all_non_signal": all(r["non_signal_required"] for r in records),
        "all_source_preserved": all(r["source_preserved_required"] for r in records),
        "all_validation_required": all(r["validation_status_required"] for r in records),
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_feature_store_contract_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize contract registry."""
    if df.empty:
        return {"total_contracts": 0, "all_non_signal": True, "all_source_preserved": True}
    return {
        "total_contracts": len(df),
        "all_non_signal": bool(all(df.get("non_signal_required", [True]))),
        "all_source_preserved": bool(all(df.get("source_preserved_required", [True]))),
        "all_validation_required": bool(all(df.get("validation_status_required", [True]))),
    }
