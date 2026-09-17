# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Model Training Disabled Report Module.

Provides audit trail and request validator confirming model training and fitting is disabled.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISABLED_EXECUTION_DOMAIN,
    EXECUTION_BLOCKED_NO_MODEL_TRAINING,
    MONTE_CARLO_CONTRACT_READY,
)


def validate_no_monte_carlo_model_training_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming requests do not attempt model training or fitting."""
    req_str = str(request).lower()
    prohibited = ["train", "fit", "model_train", "fit_model", "retrain"]
    for p in prohibited:
        if p in req_str:
            return {
                "execution_allowed": False,
                "reason": f"Prohibited model training command detected: {p}",
                "status": EXECUTION_BLOCKED_NO_MODEL_TRAINING,
            }
    return {
        "execution_allowed": False,
        "reason": "Model training disabled under Phase 149 contract layer.",
        "status": EXECUTION_BLOCKED_NO_MODEL_TRAINING,
    }


def build_monte_carlo_model_training_disabled_report(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the model training disabled report DataFrame and summary."""
    rows: List[Dict[str, Any]] = [
        {
            "capability": "ml_model_training",
            "execution_allowed": profile.allow_model_training,
            "policy_reference": "POLICY_PHASE_149_ZERO_TRAINING",
            "status": EXECUTION_BLOCKED_NO_MODEL_TRAINING,
            "description": "Prohibits fitting supervised, unsupervised, or RL models during robustness evaluations.",
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": DISABLED_EXECUTION_DOMAIN,
        "total_capabilities": len(df),
        "all_executions_blocked": bool((~df["execution_allowed"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
