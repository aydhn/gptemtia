"""Phase 127: Regime State Dataset Contracts.

Defines non-signal dataset contracts for regime state research, candidate contexts,
and preparation for Phase 128 unsupervised learning and rule-free labeling.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

CORE_STATE_DATASET_CONTRACTS: List[Dict[str, Any]] = [
    {
        "dataset_name": "regime_state_research_dataset_contract",
        "dataset_purpose": "Offline descriptive market state research without labels or signals.",
        "entity_keys": ["fx_pair", "commodity_symbol"],
        "timestamp_field": "timestamp_utc",
        "regime_state_namespace": "regime_state_research",
        "candidate_context_fields": ["trend_context_candidate", "volatility_context_candidate", "range_context_candidate"],
        "forbidden_fields": ["target", "label", "prediction", "signal", "buy", "sell", "long", "short", "position", "recommendation"],
        "no_target_label_prediction": True,
        "model_training_allowed": False,
        "clustering_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "dataset_name": "regime_state_candidate_context_dataset_contract",
        "dataset_purpose": "Multi-dimensional candidate context mapping for structural behavior characterization.",
        "entity_keys": ["fx_pair", "commodity_symbol", "macro_indicator"],
        "timestamp_field": "timestamp_utc",
        "regime_state_namespace": "regime_state_candidate_context",
        "candidate_context_fields": [
            "volatility_expansion_context_candidate",
            "volatility_compression_context_candidate",
            "macro_event_context_candidate",
            "cross_asset_context_candidate",
        ],
        "forbidden_fields": ["target", "label", "prediction", "signal", "buy", "sell", "future_return", "forward_return"],
        "no_target_label_prediction": True,
        "model_training_allowed": False,
        "clustering_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "dataset_name": "regime_state_taxonomy_mapping_dataset_contract",
        "dataset_purpose": "Maps Phase 126 regime state taxonomies to aligned matrix candidate records.",
        "entity_keys": ["regime_family", "regime_state_candidate_context"],
        "timestamp_field": "timestamp_utc",
        "regime_state_namespace": "regime_state_taxonomy_mapping",
        "candidate_context_fields": ["taxonomy_category_candidate", "transition_context_candidate", "uncertain_context_candidate"],
        "forbidden_fields": ["target", "label", "prediction", "signal", "recommendation"],
        "no_target_label_prediction": True,
        "model_training_allowed": False,
        "clustering_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "dataset_name": "regime_state_future_unsupervised_prep_contract",
        "dataset_purpose": "Dataset schema freeze preparing inputs for Phase 128 unsupervised learning and rule-free labeling.",
        "entity_keys": ["fx_pair", "commodity_symbol"],
        "timestamp_field": "timestamp_utc",
        "regime_state_namespace": "regime_state_unsupervised_prep",
        "candidate_context_fields": ["unsupervised_feature_pool_candidate", "standardized_context_candidate"],
        "forbidden_fields": ["target", "label", "prediction", "signal", "cluster_id_prediction", "trained_model_weights"],
        "no_target_label_prediction": True,
        "model_training_allowed": False,
        "clustering_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    },
]


def build_regime_state_dataset_contract_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the state dataset contract registry."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for c in CORE_STATE_DATASET_CONTRACTS:
        c_copy = c.copy()
        c_copy["current_phase"] = p.current_phase
        c_copy["target_final_phase"] = p.target_final_phase
        c_copy["next_phase"] = p.next_phase
        c_copy["source_preserved"] = True
        c_copy["official_approval"] = False
        c_copy["production_ready"] = False
        c_copy["broker_ready"] = False
        c_copy["model_training_executed"] = False
        c_copy["clustering_executed"] = False
        c_copy["unsupervised_execution"] = False
        c_copy["status"] = "matrix_ready"
        rows.append(c_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_state_dataset_contracts(df)
    return df, summary


def validate_regime_state_dataset_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a regime state dataset contract against non-signal and zero-label rules."""
    name = contract.get("dataset_name", "")
    forbidden = contract.get("forbidden_fields", [])
    candidate_fields = contract.get("candidate_context_fields", [])

    # Check that candidate fields do not contain forbidden words
    invalid_candidate_fields = []
    for f in candidate_fields:
        f_lower = f.lower()
        if any(term in f_lower for term in ["target", "label", "prediction", "signal", "buy", "sell"]):
            invalid_candidate_fields.append(f)

    is_valid = (
        len(invalid_candidate_fields) == 0
        and contract.get("no_target_label_prediction", False) is True
        and contract.get("model_training_allowed", True) is False
        and contract.get("clustering_allowed", True) is False
        and contract.get("non_signal", False) is True
    )

    return {
        "dataset_name": name,
        "is_valid": is_valid,
        "invalid_candidate_fields": invalid_candidate_fields,
        "no_target_label_prediction": contract.get("no_target_label_prediction", False),
        "model_training_allowed": contract.get("model_training_allowed", True),
        "clustering_allowed": contract.get("clustering_allowed", True),
        "non_signal": contract.get("non_signal", False),
    }


def summarize_regime_state_dataset_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize state dataset contracts registry."""
    return {
        "total_dataset_contracts": len(df),
        "total_contracts": len(df),
        "dataset_names": df["dataset_name"].tolist() if not df.empty else [],
        "all_no_target_label_prediction": bool(df["no_target_label_prediction"].all()) if not df.empty else True,
        "all_model_training_disallowed": bool((~df["model_training_allowed"]).all()) if not df.empty else True,
        "all_clustering_disallowed": bool((~df["clustering_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "any_target_or_prediction": False,
        "phase_128_prep_ready": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }


build_regime_state_dataset_contracts = build_regime_state_dataset_contract_registry
