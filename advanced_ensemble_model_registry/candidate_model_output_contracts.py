# -*- coding: utf-8 -*-
"""Phase 140: Candidate Model Output Contracts Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)
from advanced_ensemble_model_registry.candidate_model_families import CANDIDATE_MODEL_FAMILIES


def build_candidate_model_output_contract_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build candidate model output contract registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for fam in CANDIDATE_MODEL_FAMILIES:
        rows.append(
            {
                "output_contract_name": f"{fam['family_id']}_output_contract",
                "candidate_family": fam["family_id"],
                "prediction_output_allowed": False,
                "probability_output_allowed": False,
                "class_label_allowed": False,
                "regression_output_allowed": False,
                "ensemble_vote_allowed": False,
                "trade_signal_allowed": False,
                "performance_metric_allowed": False,
                "candidate_contract_status": "contract_registered",
                "eligibility_status": "candidate_metadata_ready",
                "compatibility_status": "compatible_contract_only",
                "blocked_reason": "execution_blocked_by_policy",
                "manual_review_required": True,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_candidate_model_output_contracts(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_candidate_model_output_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize candidate model output contracts DataFrame."""
    if df.empty:
        return {
            "total_output_contracts": 0,
            "all_predictions_prohibited": True,
            "all_probabilities_prohibited": True,
            "all_signals_prohibited": True,
            "non_signal": True,
        }
    return {
        "total_output_contracts": len(df),
        "all_predictions_prohibited": not bool(df["prediction_output_allowed"].any()),
        "all_probabilities_prohibited": not bool(df["probability_output_allowed"].any()),
        "all_classes_prohibited": not bool(df["class_label_allowed"].any()),
        "all_signals_prohibited": not bool(df["trade_signal_allowed"].any()),
        "all_metrics_prohibited": not bool(df["performance_metric_allowed"].any()),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
        "non_signal": bool(df["non_signal"].all()),
        "production_ready": False,
        "broker_ready": False,
    }


def validate_candidate_model_output_contracts(contracts: Any, summary: Optional[Dict[str, Any]] = None) -> bool:
    """Validate candidate model output contracts."""
    if isinstance(contracts, tuple):
        df = contracts[0]
    elif isinstance(contracts, pd.DataFrame):
        df = contracts
    elif isinstance(contracts, dict):
        return all(not c.get("prediction_output_allowed", True) for c in contracts.values())
    else:
        return False
    if df.empty:
        return False
    if df["prediction_output_allowed"].any() or df["trade_signal_allowed"].any() or df["probability_output_allowed"].any():
        return False
    if not df["non_signal"].all():
        return False
    return True


build_candidate_model_output_contracts = build_candidate_model_output_contract_registry

