"""Phase 134: Regime FeatureStore Contracts.

Defines the formal read/write/query contracts governing all regime components
stored in the FeatureStore / DataLake architecture.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    REGIME_FEATURESTORE_CONTRACT_DOMAIN,
    REGIME_STORE_READY,
    STORE_ENTITY_CANDIDATE_STATE,
    STORE_ENTITY_CROSS_ASSET_CONTEXT,
    STORE_ENTITY_MACRO_EVENT_NEWS_CONTEXT,
    STORE_ENTITY_PSEUDO_STATE,
    STORE_ENTITY_REGIME_MATRIX,
    STORE_ENTITY_REGIME_TAXONOMY,
    STORE_ENTITY_TRANSITION,
    STORE_ENTITY_VALIDATION_ACCEPTANCE,
)

CANONICAL_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "regime_taxonomy_store_contract",
        "store_entity_type": STORE_ENTITY_REGIME_TAXONOMY,
        "entity_keys": ["taxonomy_id", "family_id"],
        "timestamp_field": "timestamp_utc",
        "namespace_policy_ref": "regime_store_taxonomy_namespace",
        "schema_policy_ref": "regime_taxonomy_schema_v1",
        "validation_acceptance_required": True,
        "no_lookahead_acceptance_required": True,
        "metadata_only_news_acceptance_required": False,
        "source_preservation_required": True,
        "non_signal_required": True,
        "quality_dependency_required": True,
        "lineage_required": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "contract_name": "regime_matrix_store_contract",
        "store_entity_type": STORE_ENTITY_REGIME_MATRIX,
        "entity_keys": ["matrix_id", "feature_set_id"],
        "timestamp_field": "timestamp_utc",
        "namespace_policy_ref": "regime_store_matrix_namespace",
        "schema_policy_ref": "regime_matrix_schema_v1",
        "validation_acceptance_required": True,
        "no_lookahead_acceptance_required": True,
        "metadata_only_news_acceptance_required": False,
        "source_preservation_required": True,
        "non_signal_required": True,
        "quality_dependency_required": True,
        "lineage_required": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "contract_name": "candidate_state_store_contract",
        "store_entity_type": STORE_ENTITY_CANDIDATE_STATE,
        "entity_keys": ["candidate_state_id", "cluster_prep_id"],
        "timestamp_field": "timestamp_utc",
        "namespace_policy_ref": "regime_store_candidate_state_namespace",
        "schema_policy_ref": "candidate_state_schema_v1",
        "validation_acceptance_required": True,
        "no_lookahead_acceptance_required": True,
        "metadata_only_news_acceptance_required": False,
        "source_preservation_required": True,
        "non_signal_required": True,
        "quality_dependency_required": True,
        "lineage_required": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "contract_name": "pseudo_state_store_contract",
        "store_entity_type": STORE_ENTITY_PSEUDO_STATE,
        "entity_keys": ["pseudo_state_id", "prep_label_id"],
        "timestamp_field": "timestamp_utc",
        "namespace_policy_ref": "regime_store_pseudo_state_namespace",
        "schema_policy_ref": "pseudo_state_schema_v1",
        "validation_acceptance_required": True,
        "no_lookahead_acceptance_required": True,
        "metadata_only_news_acceptance_required": False,
        "source_preservation_required": True,
        "non_signal_required": True,
        "quality_dependency_required": True,
        "lineage_required": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "contract_name": "transition_store_contract",
        "store_entity_type": STORE_ENTITY_TRANSITION,
        "entity_keys": ["transition_id", "matrix_state_id"],
        "timestamp_field": "timestamp_utc",
        "namespace_policy_ref": "regime_store_transition_namespace",
        "schema_policy_ref": "transition_schema_v1",
        "validation_acceptance_required": True,
        "no_lookahead_acceptance_required": True,
        "metadata_only_news_acceptance_required": False,
        "source_preservation_required": True,
        "non_signal_required": True,
        "quality_dependency_required": True,
        "lineage_required": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "contract_name": "cross_asset_regime_context_store_contract",
        "store_entity_type": STORE_ENTITY_CROSS_ASSET_CONTEXT,
        "entity_keys": ["cross_asset_id", "pair_symbol"],
        "timestamp_field": "timestamp_utc",
        "namespace_policy_ref": "regime_store_cross_asset_namespace",
        "schema_policy_ref": "cross_asset_schema_v1",
        "validation_acceptance_required": True,
        "no_lookahead_acceptance_required": True,
        "metadata_only_news_acceptance_required": False,
        "source_preservation_required": True,
        "non_signal_required": True,
        "quality_dependency_required": True,
        "lineage_required": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "contract_name": "macro_event_news_context_store_contract",
        "store_entity_type": STORE_ENTITY_MACRO_EVENT_NEWS_CONTEXT,
        "entity_keys": ["macro_context_id", "event_id"],
        "timestamp_field": "timestamp_utc",
        "namespace_policy_ref": "regime_store_macro_news_namespace",
        "schema_policy_ref": "macro_news_schema_v1",
        "validation_acceptance_required": True,
        "no_lookahead_acceptance_required": True,
        "metadata_only_news_acceptance_required": True,
        "source_preservation_required": True,
        "non_signal_required": True,
        "quality_dependency_required": True,
        "lineage_required": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "contract_name": "regime_validation_acceptance_store_contract",
        "store_entity_type": STORE_ENTITY_VALIDATION_ACCEPTANCE,
        "entity_keys": ["acceptance_id", "gate_id"],
        "timestamp_field": "timestamp_utc",
        "namespace_policy_ref": "regime_store_validation_namespace",
        "schema_policy_ref": "validation_acceptance_schema_v1",
        "validation_acceptance_required": True,
        "no_lookahead_acceptance_required": True,
        "metadata_only_news_acceptance_required": True,
        "source_preservation_required": True,
        "non_signal_required": True,
        "quality_dependency_required": True,
        "lineage_required": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "contract_name": "regime_acceptance_manifest_store_contract",
        "store_entity_type": "acceptance_manifest_entity",
        "entity_keys": ["manifest_id"],
        "timestamp_field": "timestamp_utc",
        "namespace_policy_ref": "regime_store_manifest_namespace",
        "schema_policy_ref": "manifest_schema_v1",
        "validation_acceptance_required": True,
        "no_lookahead_acceptance_required": True,
        "metadata_only_news_acceptance_required": True,
        "source_preservation_required": True,
        "non_signal_required": True,
        "quality_dependency_required": True,
        "lineage_required": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "contract_name": "phase_135_handoff_store_contract",
        "store_entity_type": "phase_135_handoff_entity",
        "entity_keys": ["handoff_id", "prerequisite_id"],
        "timestamp_field": "timestamp_utc",
        "namespace_policy_ref": "regime_store_handoff_namespace",
        "schema_policy_ref": "handoff_schema_v1",
        "validation_acceptance_required": True,
        "no_lookahead_acceptance_required": True,
        "metadata_only_news_acceptance_required": True,
        "source_preservation_required": True,
        "non_signal_required": True,
        "quality_dependency_required": True,
        "lineage_required": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
]


def build_regime_featurestore_contract_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary dictionary of all FeatureStore contracts."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_CONTRACTS)
    summary = {
        "domain": REGIME_FEATURESTORE_CONTRACT_DOMAIN,
        "total_contracts": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "all_non_signal_required": bool((df["non_signal_required"] == True).all()),
        "all_source_preservation_required": bool((df["source_preservation_required"] == True).all()),
        "all_no_lookahead_required": bool((df["no_lookahead_acceptance_required"] == True).all()),
        "production_ready": False,
        "broker_ready": False,
        "status": REGIME_STORE_READY,
    }
    return df, summary


def validate_regime_featurestore_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate that a single contract dictionary satisfies all non-signal invariants."""
    errors = []
    if not contract.get("contract_name"):
        errors.append("Missing contract_name")
    if not contract.get("non_signal_required", False):
        errors.append("Contract must enforce non_signal_required=True")
    if not contract.get("source_preservation_required", False):
        errors.append("Contract must enforce source_preservation_required=True")
    if not contract.get("no_lookahead_acceptance_required", False):
        errors.append("Contract must enforce no_lookahead_acceptance_required=True")
    if contract.get("production_ready", False):
        errors.append("Contract must NOT declare production_ready=True")
    if contract.get("broker_ready", False):
        errors.append("Contract must NOT declare broker_ready=True")

    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "is_valid": len(errors) == 0,
        "errors": errors,
        "non_signal": True,
    }


def summarize_regime_featurestore_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the contract registry DataFrame."""
    return {
        "total_contracts": len(df),
        "contract_names": df["contract_name"].tolist() if not df.empty else [],
        "entities_covered": df["store_entity_type"].unique().tolist() if not df.empty else [],
        "all_non_signal": bool((df["non_signal_required"] == True).all()) if not df.empty else True,
        "all_production_false": bool((df["production_ready"] == False).all()) if not df.empty else True,
    }
