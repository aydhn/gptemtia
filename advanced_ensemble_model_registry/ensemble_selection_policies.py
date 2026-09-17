# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Selection Policies Registry."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)

SELECTION_POLICIES = [
    {
        "policy_name": "diversity_based_selection_policy",
        "description": "Candidate selection policy requiring model family diversity (execution blocked).",
    },
    {
        "policy_name": "stability_based_selection_policy",
        "description": "Candidate selection policy evaluating cross-validation stability (execution blocked).",
    },
    {
        "policy_name": "resource_constrained_selection_policy",
        "description": "Candidate selection policy bounded by Phase 139 GPU memory limits (execution blocked).",
    },
]


def build_ensemble_selection_policy_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build ensemble selection policy registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for sp in SELECTION_POLICIES:
        rows.append(
            {
                "policy_name": sp["policy_name"],
                "description": sp["description"],
                "selection_executed": False,
                "execution_blocked": True,
                "score_is_signal": False,
                "score_is_performance": False,
                "non_signal": True,
                "source_preserved": True,
                "manual_review_required": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_ensemble_selection_policies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_ensemble_selection_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate an ensemble selection request ensuring zero real selection and non-signal output."""
    req_dict = {"policy_name": request} if isinstance(request, str) else request
    policy_name = req_dict.get("policy_name", "unknown_policy")

    # If action is actual selection execution or trading recommendation
    action = req_dict.get("action", "").lower()
    if any(k in action for k in ["select", "pick", "optimize", "trade", "signal"]):
        return {
            "policy_name": policy_name,
            "selection_allowed": False,
            "blocked": True,
            "reason": f"Execution of selection action '{action}' is strictly blocked by safety policy.",
            "non_signal": True,
            "manual_review_required": True,
        }

    return {
        "policy_name": policy_name,
        "selection_allowed": False,
        "blocked": False,
        "reason": "Selection policy registered as metadata contract; execution blocked by design.",
        "non_signal": True,
        "manual_review_required": True,
    }


def summarize_ensemble_selection_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize ensemble selection policies DataFrame."""
    if df.empty:
        return {
            "total_policies": 0,
            "all_selection_blocked": True,
            "zero_selection_executed": True,
            "non_signal": True,
        }
    return {
        "total_policies": len(df),
        "all_selection_blocked": bool(df["execution_blocked"].all()),
        "zero_selection_executed": not bool(df["selection_executed"].any()),
        "all_scores_non_signal": not bool(df["score_is_signal"].any()),
        "all_scores_non_performance": not bool(df["score_is_performance"].any()),
        "non_signal": bool(df["non_signal"].all()),
        "production_ready": False,
        "broker_ready": False,
    }


def validate_ensemble_selection_policies(policies: Any, summary: Optional[Dict[str, Any]] = None) -> bool:
    """Validate ensemble selection policies."""
    if isinstance(policies, tuple):
        df = policies[0]
    elif isinstance(policies, pd.DataFrame):
        df = policies
    elif isinstance(policies, dict):
        return all(not p.get("selection_executed", False) for p in policies.values())
    else:
        return False
    if df.empty:
        return False
    if df["selection_executed"].any():
        return False
    if not df["non_signal"].all():
        return False
    return True


build_ensemble_selection_policies = build_ensemble_selection_policy_registry

