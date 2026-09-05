"""Phase 127: Regime State Dataset Metadata Registry.

Catalogs comprehensive dataset metadata linking state candidate records to source phases,
taxonomies, contracts, and Phase 128 preparation flags.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

STATE_DATASET_METADATA_ENTRIES: List[Dict[str, Any]] = [
    {
        "dataset_name": "regime_state_research_dataset",
        "source_phase_refs": [126, 127],
        "state_taxonomy_ref": "regime_state_taxonomy_v1",
        "matrix_contract_ref": "regime_technical_feature_matrix_contract",
        "no_lookahead_policy_ref": "asof_policy_backward_only",
        "quality_dependency_ref": "qual_missingness_max_5pct",
        "validation_dependency_ref": "rule_no_lookahead_ts_order",
        "phase_128_ready": True,
        "manual_review_required": True,
        "non_signal": True,
    },
    {
        "dataset_name": "regime_state_candidate_context_dataset",
        "source_phase_refs": [120, 126, 127],
        "state_taxonomy_ref": "regime_candidate_context_taxonomy_v1",
        "matrix_contract_ref": "regime_macro_event_context_matrix_contract",
        "no_lookahead_policy_ref": "ts_rule_macro_release_lag",
        "quality_dependency_ref": "qual_drift_psi_max_025",
        "validation_dependency_ref": "rule_macro_release_delay",
        "phase_128_ready": True,
        "manual_review_required": True,
        "non_signal": True,
    },
    {
        "dataset_name": "regime_state_taxonomy_mapping_dataset",
        "source_phase_refs": [126, 127],
        "state_taxonomy_ref": "market_behavior_taxonomy_v1",
        "matrix_contract_ref": "regime_combined_research_matrix_contract",
        "no_lookahead_policy_ref": "asof_policy_backward_only",
        "quality_dependency_ref": "qual_validation_readiness",
        "validation_dependency_ref": "rule_validation_pass_required",
        "phase_128_ready": True,
        "manual_review_required": True,
        "non_signal": True,
    },
    {
        "dataset_name": "regime_state_future_unsupervised_prep_dataset",
        "source_phase_refs": [117, 118, 119, 120, 122, 126, 127],
        "state_taxonomy_ref": "unsupervised_prep_taxonomy_v1",
        "matrix_contract_ref": "regime_combined_research_matrix_contract",
        "no_lookahead_policy_ref": "asof_policy_backward_only",
        "quality_dependency_ref": "qual_missingness_max_5pct",
        "validation_dependency_ref": "rule_source_preservation_enforced",
        "phase_128_ready": True,
        "manual_review_required": True,
        "non_signal": True,
    },
    {
        "dataset_name": "unsupervised_clustering_input_dataset",
        "source_phase_refs": [126, 127],
        "state_taxonomy_ref": "unsupervised_prep_taxonomy_v1",
        "matrix_contract_ref": "regime_state_candidate_context_matrix_contract",
        "no_lookahead_policy_ref": "asof_policy_backward_only",
        "quality_dependency_ref": "qual_missingness_max_5pct",
        "validation_dependency_ref": "rule_no_target_label_prediction",
        "phase_128_ready": True,
        "manual_review_required": True,
        "non_signal": True,
    },
]


def is_valid_regime_state_dataset(name: str) -> bool:
    """Check whether a dataset name is a valid Phase 127 state dataset."""
    valid_names = {entry["dataset_name"] for entry in STATE_DATASET_METADATA_ENTRIES}
    return name in valid_names


def build_regime_state_dataset_metadata_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the state dataset metadata registry."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for m in STATE_DATASET_METADATA_ENTRIES:
        m_copy = m.copy()
        m_copy["current_phase"] = p.current_phase
        m_copy["target_final_phase"] = p.target_final_phase
        m_copy["next_phase"] = p.next_phase
        m_copy["source_preserved"] = True
        m_copy["contains_target_or_prediction"] = False
        m_copy["status"] = "matrix_ready"
        rows.append(m_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_state_dataset_metadata(df)
    return df, summary


def summarize_regime_state_dataset_metadata(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize state dataset metadata registry."""
    return {
        "total_datasets": len(df),
        "dataset_names": df["dataset_name"].tolist() if not df.empty else [],
        "all_phase_128_ready": bool(df["phase_128_ready"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "any_target_or_prediction": bool(df["contains_target_or_prediction"].any()) if not df.empty and "contains_target_or_prediction" in df.columns else False,
        "status": "matrix_ready",
    }
