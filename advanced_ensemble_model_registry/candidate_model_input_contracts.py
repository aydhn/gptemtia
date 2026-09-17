# -*- coding: utf-8 -*-
"""Phase 140: Candidate Model Input Contracts Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)
from advanced_ensemble_model_registry.candidate_model_families import CANDIDATE_MODEL_FAMILIES


def build_candidate_model_input_contract_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build candidate model input contract registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for fam in CANDIDATE_MODEL_FAMILIES:
        rows.append(
            {
                "input_contract_name": f"{fam['family_id']}_input_contract",
                "candidate_family": fam["family_id"],
                "dataset_source_ref": "advanced_ml_dataset_registry_phase_137",
                "baseline_contract_ref": fam["baseline_contract_ref"],
                "gpu_resource_policy_ref": "advanced_gpu_training_governance_phase_139",
                "featurestore_catalog_ref": "featurestore_catalog_phase_134",
                "regime_acceptance_ref": "regime_acceptance_phase_135",
                "no_lookahead_validation_ref": "no_lookahead_validation_phase_133",
                "quality_drift_ref": "quality_drift_metadata_phase_123_124",
                "input_feature_count": 48,
                "no_lookahead_guaranteed": True,
                "metadata_only_news_guaranteed": True,
                "source_preserved": True,
                "contains_target": False,
                "contains_signal": False,
                "non_signal": True,
                "manual_review_required": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_candidate_model_input_contracts(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_candidate_model_input_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize candidate model input contracts DataFrame."""
    if df.empty:
        return {
            "total_input_contracts": 0,
            "all_no_lookahead_guaranteed": True,
            "all_metadata_only_news_guaranteed": True,
            "zero_targets_contained": True,
            "zero_signals_contained": True,
            "non_signal": True,
        }
    return {
        "total_input_contracts": len(df),
        "all_no_lookahead_guaranteed": bool(df["no_lookahead_guaranteed"].all()),
        "all_metadata_only_news_guaranteed": bool(df["metadata_only_news_guaranteed"].all()),
        "all_source_preserved": bool(df["source_preserved"].all()),
        "zero_targets_contained": not bool(df["contains_target"].any()),
        "zero_signals_contained": not bool(df["contains_signal"].any()),
        "non_signal": bool(df["non_signal"].all()),
        "production_ready": False,
        "broker_ready": False,
    }


def validate_candidate_model_input_contracts(contracts: Any, summary: Optional[Dict[str, Any]] = None) -> bool:
    """Validate candidate model input contracts."""
    if isinstance(contracts, tuple):
        df = contracts[0]
    elif isinstance(contracts, pd.DataFrame):
        df = contracts
    elif isinstance(contracts, dict):
        return all(c.get("non_signal", False) for c in contracts.values())
    else:
        return False
    if df.empty:
        return False
    if not df["no_lookahead_guaranteed"].all() or not df["metadata_only_news_guaranteed"].all():
        return False
    if df["contains_target"].any() or df["contains_signal"].any():
        return False
    if not df["non_signal"].all():
        return False
    return True


build_candidate_model_input_contracts = build_candidate_model_input_contract_registry

