# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
ML prediction disabled contracts.

Prohibits model inference, predictions, transforms, forward returns, and signal generation.
"""

from typing import Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_default_advanced_ml_dataset_profile,
)

FORBIDDEN_PREDICTION_KEYWORDS = [
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

PREDICTION_DISABLED_CONTRACTS = [
    {
        "contract_key": "no_prediction_inference_contract",
        "description": "Strict prohibition of all forward pass predictions and batch inference",
        "enforced": True,
        "current_phase": 137,
        "next_phase": 138,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "contract_key": "no_directional_signal_contract",
        "description": "Strict prohibition of generating buy/sell/long/short or directional trade signals",
        "enforced": True,
        "current_phase": 137,
        "next_phase": 138,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "contract_key": "no_forward_return_contract",
        "description": "Strict prohibition of forward returns, future return labels, or target variables",
        "enforced": True,
        "current_phase": 137,
        "next_phase": 138,
        "non_signal": True,
        "manual_review_required": True,
    },
    {
        "contract_key": "no_sentiment_score_contract",
        "description": "Strict prohibition of NLP sentiment prediction and model-based scoring",
        "enforced": True,
        "current_phase": 137,
        "next_phase": 138,
        "non_signal": True,
        "manual_review_required": True,
    },
]


def build_ml_prediction_disabled_contract_registry(
    profile: Optional[AdvancedMlDatasetProfile] = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary for prediction disabled contracts."""
    p = profile or get_default_advanced_ml_dataset_profile()
    df = pd.DataFrame(PREDICTION_DISABLED_CONTRACTS)
    summary = summarize_prediction_disabled_contracts(df)
    return df, summary


def validate_prediction_disabled_request(request: Union[Dict, str]) -> Dict:
    """Validate that an incoming request does not violate prediction disabled policies.

    Returns dict with 'valid' (bool), 'blocked' (bool), and 'detected_violations' (list).
    """
    req_str = ""
    if isinstance(request, dict):
        req_str = " ".join(f"{k} {v}" for k, v in request.items()).lower()
    else:
        req_str = str(request).lower()

    detected = [kw for kw in FORBIDDEN_PREDICTION_KEYWORDS if kw in req_str]
    is_blocked = len(detected) > 0

    return {
        "valid": not is_blocked,
        "blocked": is_blocked,
        "detected_violations": detected,
        "message": "Prediction/inference action blocked by Phase 137 contract" if is_blocked else "Request clean",
        "non_signal": True,
    }


def summarize_prediction_disabled_contracts(df: pd.DataFrame) -> Dict:
    """Summarize prediction disabled contracts."""
    return {
        "total_contracts": len(df),
        "all_enforced": bool((df["enforced"] == True).all()),
        "prediction_blocked": True,
        "inference_blocked": True,
        "signal_generation_blocked": True,
        "non_signal": True,
        "manual_review_required": True,
    }
