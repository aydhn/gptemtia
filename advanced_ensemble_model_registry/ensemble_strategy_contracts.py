# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Strategy Contracts Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)

ENSEMBLE_STRATEGIES: List[Dict[str, Any]] = [
    {
        "strategy_name": "simple_voting_ensemble_contract",
        "strategy_type": "voting",
        "description": "Unweighted majority or mean voting ensemble strategy contract placeholder.",
    },
    {
        "strategy_name": "weighted_voting_ensemble_contract",
        "strategy_type": "voting",
        "description": "Validation-metric-weighted voting ensemble strategy contract placeholder.",
    },
    {
        "strategy_name": "averaging_ensemble_contract",
        "strategy_type": "averaging",
        "description": "Arithmetic probability averaging ensemble contract placeholder.",
    },
    {
        "strategy_name": "blending_ensemble_contract",
        "strategy_type": "blending",
        "description": "Hold-out validation split blending ensemble strategy contract placeholder.",
    },
    {
        "strategy_name": "stacking_ensemble_contract",
        "strategy_type": "stacking",
        "description": "Out-of-fold cross-validated meta-feature stacking ensemble contract placeholder.",
    },
    {
        "strategy_name": "rank_aggregation_ensemble_contract",
        "strategy_type": "rank_aggregation",
        "description": "Rank-based candidate output aggregation contract placeholder.",
    },
    {
        "strategy_name": "meta_model_ensemble_contract",
        "strategy_type": "meta_model",
        "description": "Secondary level meta-learner model contract placeholder.",
    },
]


def build_ensemble_strategy_contract_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build ensemble strategy contract registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for strat in ENSEMBLE_STRATEGIES:
        rows.append(
            {
                "ensemble_strategy_name": strat["strategy_name"],
                "strategy_type": strat["strategy_type"],
                "description": strat["description"],
                "required_candidate_contract_refs": [
                    "logistic_regression_candidate_contract",
                    "random_forest_candidate_contract",
                    "gradient_boosting_candidate_contract",
                ],
                "required_candidate_eligibility_refs": [
                    "dataset_contract_present_gate",
                    "baseline_contract_present_gate",
                    "no_lookahead_guard_present_gate",
                ],
                "required_compatibility_matrix_ref": "candidate_compatibility_matrix_v140",
                "required_resource_policy_ref": "gpu_training_resource_policy_v139",
                "required_no_lookahead_guard_ref": "ensemble_no_lookahead_guard",
                "required_metadata_only_news_guard_ref": "ensemble_metadata_only_news_guard",
                "ensemble_execution_allowed": False,
                "voting_execution_allowed": False,
                "blending_execution_allowed": False,
                "stacking_execution_allowed": False,
                "calibration_allowed": False,
                "prediction_allowed": False,
                "signal_generation_allowed": False,
                "artifact_persistence_allowed": False,
                "non_signal_required": True,
                "manual_review_required": True,
                "status": "ensemble_contract_placeholder_only",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_ensemble_strategy_contracts(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_ensemble_strategy_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate an ensemble strategy contract ensuring zero execution and non-signal compliance."""
    violations = []
    if contract.get("ensemble_execution_allowed", False):
        violations.append("ensemble_execution_allowed must be False")
    if contract.get("voting_execution_allowed", False):
        violations.append("voting_execution_allowed must be False")
    if contract.get("blending_execution_allowed", False):
        violations.append("blending_execution_allowed must be False")
    if contract.get("stacking_execution_allowed", False):
        violations.append("stacking_execution_allowed must be False")
    if contract.get("calibration_allowed", False):
        violations.append("calibration_allowed must be False")
    if contract.get("prediction_allowed", False):
        violations.append("prediction_allowed must be False")
    if contract.get("signal_generation_allowed", False):
        violations.append("signal_generation_allowed must be False")
    if contract.get("artifact_persistence_allowed", False):
        violations.append("artifact_persistence_allowed must be False")
    if not contract.get("non_signal_required", True):
        violations.append("non_signal_required must be True")

    is_valid = len(violations) == 0
    return {
        "ensemble_strategy_name": contract.get("ensemble_strategy_name", "unknown_strategy"),
        "is_valid": is_valid,
        "violations": violations,
        "status": "VALID_STRATEGY_CONTRACT" if is_valid else "INVALID_STRATEGY_CONTRACT",
        "non_signal": True,
        "manual_review_required": True,
    }


def summarize_ensemble_strategy_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize ensemble strategy contracts DataFrame."""
    if df.empty:
        return {
            "total_strategies": 0,
            "all_execution_disabled": True,
            "all_voting_disabled": True,
            "all_blending_disabled": True,
            "all_stacking_disabled": True,
            "non_signal": True,
        }
    return {
        "total_strategies": len(df),
        "all_execution_disabled": not bool(df["ensemble_execution_allowed"].any()),
        "all_voting_disabled": not bool(df["voting_execution_allowed"].any()),
        "all_blending_disabled": not bool(df["blending_execution_allowed"].any()),
        "all_stacking_disabled": not bool(df["stacking_execution_allowed"].any()),
        "all_calibration_disabled": not bool(df["calibration_allowed"].any()),
        "all_prediction_disabled": not bool(df["prediction_allowed"].any()),
        "all_signal_disabled": not bool(df["signal_generation_allowed"].any()),
        "all_non_signal_required": bool(df["non_signal_required"].all()),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
        "production_ready": False,
        "broker_ready": False,
    }


def validate_ensemble_strategy_contracts(contracts: Any, summary: Optional[Dict[str, Any]] = None) -> bool:
    """Validate ensemble strategy contracts."""
    if isinstance(contracts, tuple):
        df = contracts[0]
    elif isinstance(contracts, pd.DataFrame):
        df = contracts
    elif isinstance(contracts, dict):
        return all(validate_ensemble_strategy_contract(c).get("is_valid", False) for c in contracts.values())
    else:
        return False
    if df.empty:
        return False
    if df["ensemble_execution_allowed"].any() or df["voting_execution_allowed"].any():
        return False
    if df["blending_execution_allowed"].any() or df["stacking_execution_allowed"].any():
        return False
    if not df["non_signal_required"].all():
        return False
    return True


build_ensemble_strategy_contracts = build_ensemble_strategy_contract_registry

