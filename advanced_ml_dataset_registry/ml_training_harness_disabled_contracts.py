# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
ML training harness disabled contracts.

Prohibits model training, fit, optimizer execution, and backtest execution in Phase 137.
"""

from typing import Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_default_advanced_ml_dataset_profile,
)

FORBIDDEN_TRAINING_KEYWORDS = [
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

TRAINING_DISABLED_CONTRACTS = [
    {
        "contract_key": "no_model_training_contract",
        "description": "Strict prohibition of all model training routines (fit, train, step, epochs)",
        "enforced": True,
        "current_phase": 137,
        "next_phase": 138,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "contract_key": "no_backtest_optimizer_contract",
        "description": "Strict prohibition of strategy backtesting, grid search, and hyperparameter optimizers",
        "enforced": True,
        "current_phase": 137,
        "next_phase": 138,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "contract_key": "no_clustering_unsupervised_contract",
        "description": "Strict prohibition of unsupervised clustering, manifold learning, and centroid updates",
        "enforced": True,
        "current_phase": 137,
        "next_phase": 138,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "contract_key": "no_weights_persistence_contract",
        "description": "Strict prohibition of saving trained model checkpoints or weights to storage",
        "enforced": True,
        "current_phase": 137,
        "next_phase": 138,
        "non_signal": True,
        "manual_review_required": True,
    },
]


def build_ml_training_harness_disabled_contract_registry(
    profile: Optional[AdvancedMlDatasetProfile] = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary for training harness disabled contracts."""
    p = profile or get_default_advanced_ml_dataset_profile()
    df = pd.DataFrame(TRAINING_DISABLED_CONTRACTS)
    summary = summarize_training_harness_disabled_contracts(df)
    return df, summary


def validate_training_harness_disabled_request(request: Union[Dict, str]) -> Dict:
    """Validate that an incoming request does not violate training disabled policies.

    Returns dict with 'valid' (bool), 'blocked' (bool), and 'detected_violations' (list).
    """
    req_str = ""
    if isinstance(request, dict):
        req_str = " ".join(f"{k} {v}" for k, v in request.items()).lower()
    else:
        req_str = str(request).lower()

    detected = [kw for kw in FORBIDDEN_TRAINING_KEYWORDS if kw in req_str]
    is_blocked = len(detected) > 0

    return {
        "valid": not is_blocked,
        "blocked": is_blocked,
        "detected_violations": detected,
        "message": "Training action blocked by Phase 137 contract" if is_blocked else "Request clean",
        "non_signal": True,
    }


def summarize_training_harness_disabled_contracts(df: pd.DataFrame) -> Dict:
    """Summarize training harness disabled contracts."""
    return {
        "total_contracts": len(df),
        "all_enforced": bool((df["enforced"] == True).all()),
        "model_training_blocked": True,
        "optimizer_blocked": True,
        "backtest_blocked": True,
        "non_signal": True,
        "manual_review_required": True,
    }
