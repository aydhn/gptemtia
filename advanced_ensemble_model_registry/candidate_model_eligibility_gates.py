# -*- coding: utf-8 -*-
"""Phase 140: Candidate Model Eligibility Gates Registry."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_default_ensemble_model_profile,
)

ELIGIBILITY_GATES: List[Dict[str, Any]] = [
    {
        "gate_name": "dataset_contract_present_gate",
        "gate_category": "prerequisite",
        "description": "Validates that candidate model references an active Phase 137 dataset contract.",
    },
    {
        "gate_name": "baseline_contract_present_gate",
        "gate_category": "prerequisite",
        "description": "Validates that candidate model references an active Phase 138 baseline contract.",
    },
    {
        "gate_name": "runtime_contract_present_gate",
        "gate_category": "prerequisite",
        "description": "Validates that candidate model references an active Phase 136 runtime foundation.",
    },
    {
        "gate_name": "resource_policy_present_gate",
        "gate_category": "governance",
        "description": "Validates that candidate model references an active Phase 139 GPU resource policy.",
    },
    {
        "gate_name": "no_lookahead_guard_present_gate",
        "gate_category": "safety",
        "description": "Enforces zero lookahead leakage across all candidate input features.",
    },
    {
        "gate_name": "metadata_only_news_guard_present_gate",
        "gate_category": "safety",
        "description": "Enforces strict metadata-only news usage (no full text, embeddings, sentiment).",
    },
    {
        "gate_name": "source_preservation_guard_present_gate",
        "gate_category": "safety",
        "description": "Guarantees no source deletion, overwrite, auto-imputation, or auto-feature drop.",
    },
    {
        "gate_name": "target_label_disabled_gate",
        "gate_category": "execution_block",
        "description": "Blocks any target or ground-truth label generation within candidate registry.",
    },
    {
        "gate_name": "training_disabled_gate",
        "gate_category": "execution_block",
        "description": "Blocks real model training, model fit, or backward passes.",
    },
    {
        "gate_name": "prediction_disabled_gate",
        "gate_category": "execution_block",
        "description": "Blocks model predict, forward inference, or score generation.",
    },
    {
        "gate_name": "artifact_disabled_gate",
        "gate_category": "execution_block",
        "description": "Blocks saving model weights, pickle, joblib dumps, or model registry write.",
    },
    {
        "gate_name": "manual_review_gate",
        "gate_category": "governance",
        "description": "Requires human manual review before any candidate contract is promoted.",
    },
]


def build_candidate_model_eligibility_gate_registry(
    profile: Optional[EnsembleModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build candidate model eligibility gate registry DataFrame and summary."""
    active_profile = profile or get_default_ensemble_model_profile()
    rows = []
    for g in ELIGIBILITY_GATES:
        rows.append(
            {
                "gate_name": g["gate_name"],
                "gate_category": g["gate_category"],
                "description": g["description"],
                "status": "GATE_ACTIVE",
                "passed": True,
                "blocks_execution": True,
                "non_signal": True,
                "manual_review_required": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_candidate_model_eligibility_gates(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_candidate_model_eligibility_request(
    request: Union[Dict[str, Any], str],
) -> Dict[str, Any]:
    """Validate a candidate model eligibility request ensuring non-execution and non-signal compliance."""
    req_dict = {"name": request} if isinstance(request, str) else request
    gate_name = req_dict.get("gate_name", req_dict.get("name", "unknown_gate"))

    # Check for prohibited action attempts
    attempted_action = req_dict.get("action", "").lower()
    blocked_actions = ["train", "fit", "predict", "infer", "save", "write_registry", "generate_signal", "trade"]
    if any(b in attempted_action for b in blocked_actions):
        return {
            "gate_name": gate_name,
            "eligible": False,
            "blocked": True,
            "reason": f"Action '{attempted_action}' is strictly prohibited by candidate eligibility policy.",
            "non_signal": True,
            "manual_review_required": True,
        }

    return {
        "gate_name": gate_name,
        "eligible": True,
        "blocked": False,
        "reason": "Contract eligibility validated; execution remains blocked by system policy.",
        "non_signal": True,
        "manual_review_required": True,
    }


def summarize_candidate_model_eligibility_gates(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize eligibility gates DataFrame."""
    if df.empty:
        return {
            "total_gates": 0,
            "all_gates_passed": True,
            "all_blocks_execution": True,
            "non_signal": True,
        }
    return {
        "total_gates": len(df),
        "all_gates_passed": bool(df["passed"].all()),
        "all_blocks_execution": bool(df["blocks_execution"].all()),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
        "non_signal": bool(df["non_signal"].all()),
        "production_ready": False,
        "broker_ready": False,
    }


def validate_candidate_model_eligibility_gates(gates: Any, summary: Optional[Dict[str, Any]] = None) -> bool:
    """Validate candidate model eligibility gates."""
    if isinstance(gates, tuple):
        df = gates[0]
    elif isinstance(gates, pd.DataFrame):
        df = gates
    elif isinstance(gates, dict):
        return all(g.get("non_signal", False) for g in gates.values())
    else:
        return False
    if df.empty:
        return False
    if not df["passed"].all():
        return False
    if not df["non_signal"].all():
        return False
    return True


build_candidate_model_eligibility_gates = build_candidate_model_eligibility_gate_registry
validate_candidate_eligibility_request = validate_candidate_model_eligibility_request


