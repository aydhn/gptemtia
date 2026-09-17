# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
ML artifact disabled contracts.

Prohibits model artifact persistence, model registry writes, and dataset materialization.
"""

from typing import Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_default_advanced_ml_dataset_profile,
)

FORBIDDEN_ARTIFACT_KEYWORDS = [
    "fit",
    "train",
    "predict",
    "inference",
    "transform",
    "materialize",
    "save_model",
    "model_registry",
    "target",
    "label",
    "future_return",
    "forward_return",
    "next_return",
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "backtest",
    "optimize",
]

ARTIFACT_DISABLED_CONTRACTS = [
    {
        "contract_key": "no_model_registry_write_contract",
        "description": "Strict prohibition of registering or publishing trained model weights",
        "enforced": True,
        "current_phase": 137,
        "next_phase": 138,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "contract_key": "no_dataset_materialization_contract",
        "description": "Strict prohibition of materializing physical parquet/csv training tables",
        "enforced": True,
        "current_phase": 137,
        "next_phase": 138,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "contract_key": "no_feature_snapshot_materialization_contract",
        "description": "Strict prohibition of writing materialized feature snapshot stores",
        "enforced": True,
        "current_phase": 137,
        "next_phase": 138,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "contract_key": "no_binary_model_artifact_contract",
        "description": "Strict prohibition of generating pickle, joblib, onnx, or torchpt artifacts",
        "enforced": True,
        "current_phase": 137,
        "next_phase": 138,
        "non_signal": True,
        "manual_review_required": True,
    },
]


def build_ml_artifact_disabled_contract_registry(
    profile: Optional[AdvancedMlDatasetProfile] = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary for artifact disabled contracts."""
    p = profile or get_default_advanced_ml_dataset_profile()
    df = pd.DataFrame(ARTIFACT_DISABLED_CONTRACTS)
    summary = summarize_artifact_disabled_contracts(df)
    return df, summary


def validate_artifact_disabled_request(request: Union[Dict, str]) -> Dict:
    """Validate that an incoming request does not violate artifact disabled policies.

    Returns dict with 'valid' (bool), 'blocked' (bool), and 'detected_violations' (list).
    """
    req_str = ""
    if isinstance(request, dict):
        req_str = " ".join(f"{k} {v}" for k, v in request.items()).lower()
    else:
        req_str = str(request).lower()

    detected = [kw for kw in FORBIDDEN_ARTIFACT_KEYWORDS if kw in req_str]
    is_blocked = len(detected) > 0

    return {
        "valid": not is_blocked,
        "blocked": is_blocked,
        "detected_violations": detected,
        "message": "Artifact/materialization action blocked by Phase 137 contract" if is_blocked else "Request clean",
        "non_signal": True,
    }


def summarize_artifact_disabled_contracts(df: pd.DataFrame) -> Dict:
    """Summarize artifact disabled contracts."""
    return {
        "total_contracts": len(df),
        "all_enforced": bool((df["enforced"] == True).all()),
        "artifact_persistence_blocked": True,
        "model_registry_write_blocked": True,
        "dataset_materialization_blocked": True,
        "non_signal": True,
        "manual_review_required": True,
    }
