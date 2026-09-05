"""Phase 130: Regime State Sequence Contracts.

Defines state sequence dataset contracts governing structure, entity keys,
timestamp continuity, source traceability, and non-signal compliance.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

EXPECTED_SEQUENCE_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "candidate_state_sequence_contract",
        "sequence_family": "candidate_state",
        "entity_keys": ["entity_type", "entity_id"],
        "timestamp_field": "timestamp_utc",
        "state_context_field": "candidate_state_context",
        "source_phase_refs": ["Phase 128", "Phase 129"],
        "required_validation_refs": ["val_no_lookahead", "val_chronological_order"],
        "required_quality_refs": ["qual_missingness", "qual_coverage"],
        "no_lookahead_required": True,
        "metadata_only_news_required": True,
        "non_signal_required": True,
        "model_training_allowed": False,
        "clustering_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "pseudo_state_sequence_contract",
        "sequence_family": "pseudo_state",
        "entity_keys": ["entity_type", "entity_id"],
        "timestamp_field": "timestamp_utc",
        "state_context_field": "pseudo_state_context",
        "source_phase_refs": ["Phase 128"],
        "required_validation_refs": ["val_no_lookahead", "val_zero_ml"],
        "required_quality_refs": ["qual_pseudo_stability"],
        "no_lookahead_required": True,
        "metadata_only_news_required": True,
        "non_signal_required": True,
        "model_training_allowed": False,
        "clustering_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "regime_family_sequence_contract",
        "sequence_family": "regime_family",
        "entity_keys": ["entity_type", "entity_id"],
        "timestamp_field": "timestamp_utc",
        "state_context_field": "regime_family_context",
        "source_phase_refs": ["Phase 126", "Phase 127", "Phase 129"],
        "required_validation_refs": ["val_family_consistency"],
        "required_quality_refs": ["qual_family_quality"],
        "no_lookahead_required": True,
        "metadata_only_news_required": True,
        "non_signal_required": True,
        "model_training_allowed": False,
        "clustering_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "volatility_state_sequence_contract",
        "sequence_family": "volatility_state",
        "entity_keys": ["entity_type", "entity_id"],
        "timestamp_field": "timestamp_utc",
        "state_context_field": "volatility_state_context",
        "source_phase_refs": ["Phase 117", "Phase 126", "Phase 129"],
        "required_validation_refs": ["val_no_lookahead"],
        "required_quality_refs": ["qual_volatility_coverage"],
        "no_lookahead_required": True,
        "metadata_only_news_required": True,
        "non_signal_required": True,
        "model_training_allowed": False,
        "clustering_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "trend_state_sequence_contract",
        "sequence_family": "trend_state",
        "entity_keys": ["entity_type", "entity_id"],
        "timestamp_field": "timestamp_utc",
        "state_context_field": "trend_state_context",
        "source_phase_refs": ["Phase 117", "Phase 126", "Phase 129"],
        "required_validation_refs": ["val_no_lookahead"],
        "required_quality_refs": ["qual_trend_coverage"],
        "no_lookahead_required": True,
        "metadata_only_news_required": True,
        "non_signal_required": True,
        "model_training_allowed": False,
        "clustering_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "range_state_sequence_contract",
        "sequence_family": "range_state",
        "entity_keys": ["entity_type", "entity_id"],
        "timestamp_field": "timestamp_utc",
        "state_context_field": "range_state_context",
        "source_phase_refs": ["Phase 117", "Phase 126", "Phase 129"],
        "required_validation_refs": ["val_no_lookahead"],
        "required_quality_refs": ["qual_range_coverage"],
        "no_lookahead_required": True,
        "metadata_only_news_required": True,
        "non_signal_required": True,
        "model_training_allowed": False,
        "clustering_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "macro_event_context_sequence_contract",
        "sequence_family": "macro_event_context",
        "entity_keys": ["country_code", "event_id"],
        "timestamp_field": "release_timestamp_utc",
        "state_context_field": "event_window_context",
        "source_phase_refs": ["Phase 120", "Phase 129"],
        "required_validation_refs": ["val_release_lag", "val_no_lookahead"],
        "required_quality_refs": ["qual_macro_quality"],
        "no_lookahead_required": True,
        "metadata_only_news_required": True,
        "non_signal_required": True,
        "model_training_allowed": False,
        "clustering_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "news_metadata_context_sequence_contract",
        "sequence_family": "news_metadata_context",
        "entity_keys": ["news_id", "asset_tag"],
        "timestamp_field": "published_timestamp_utc",
        "state_context_field": "topic_metadata_context",
        "source_phase_refs": ["Phase 120", "Phase 129"],
        "required_validation_refs": ["val_metadata_only_boundary"],
        "required_quality_refs": ["qual_news_quality"],
        "no_lookahead_required": True,
        "metadata_only_news_required": True,
        "non_signal_required": True,
        "model_training_allowed": False,
        "clustering_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "cross_asset_context_sequence_contract",
        "sequence_family": "cross_asset_context",
        "entity_keys": ["base_asset_id", "cross_asset_id"],
        "timestamp_field": "timestamp_utc",
        "state_context_field": "cross_asset_state_context",
        "source_phase_refs": ["Phase 119", "Phase 126", "Phase 129"],
        "required_validation_refs": ["val_cross_asset_alignment"],
        "required_quality_refs": ["qual_alignment_quality"],
        "no_lookahead_required": True,
        "metadata_only_news_required": True,
        "non_signal_required": True,
        "model_training_allowed": False,
        "clustering_allowed": False,
        "manual_review_required": True,
    },
]


def build_regime_state_sequence_contract_registry(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry dataframe and summary of state sequence contracts."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    rows = []
    for c in EXPECTED_SEQUENCE_CONTRACTS:
        rows.append(
            {
                "contract_name": c["contract_name"],
                "sequence_family": c["sequence_family"],
                "entity_keys": ",".join(c["entity_keys"]),
                "timestamp_field": c["timestamp_field"],
                "state_context_field": c["state_context_field"],
                "source_phase_refs": ",".join(c["source_phase_refs"]),
                "required_validation_refs": ",".join(c["required_validation_refs"]),
                "required_quality_refs": ",".join(c["required_quality_refs"]),
                "no_lookahead_required": c["no_lookahead_required"],
                "metadata_only_news_required": c["metadata_only_news_required"],
                "non_signal_required": c["non_signal_required"],
                "model_training_allowed": c["model_training_allowed"],
                "clustering_allowed": c["clustering_allowed"],
                "manual_review_required": c["manual_review_required"],
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_state_sequence_contracts(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def validate_state_sequence_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a single sequence contract conforms to non-signal invariants."""
    required_keys = [
        "contract_name",
        "sequence_family",
        "entity_keys",
        "timestamp_field",
        "state_context_field",
        "non_signal_required",
        "no_lookahead_required",
    ]
    for key in required_keys:
        if key not in contract:
            return {"is_valid": False, "error": f"Missing contract key: {key}"}

    if contract.get("model_training_allowed", False):
        return {"is_valid": False, "error": "model_training_allowed must be False"}
    if contract.get("clustering_allowed", False):
        return {"is_valid": False, "error": "clustering_allowed must be False"}
    if not contract.get("non_signal_required", False):
        return {"is_valid": False, "error": "non_signal_required must be True"}

    return {"is_valid": True, "contract_name": contract["contract_name"]}


def summarize_state_sequence_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize state sequence contracts dataframe."""
    return {
        "total_contracts": len(df),
        "contract_names": df["contract_name"].tolist() if not df.empty else [],
        "all_non_signal_required": bool(df["non_signal_required"].all()) if not df.empty else True,
        "all_no_lookahead_required": bool(df["no_lookahead_required"].all()) if not df.empty else True,
        "zero_model_training_allowed": bool(not df["model_training_allowed"].any()) if not df.empty else True,
        "zero_clustering_allowed": bool(not df["clustering_allowed"].any()) if not df.empty else True,
    }
