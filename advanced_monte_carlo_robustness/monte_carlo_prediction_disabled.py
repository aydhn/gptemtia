# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Prediction Disabled Report Module.

Provides audit trail and request validator confirming model prediction and inference is disabled.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISABLED_EXECUTION_DOMAIN,
    EXECUTION_BLOCKED_NO_PREDICTION,
    MONTE_CARLO_CONTRACT_READY,
)


def validate_no_monte_carlo_prediction_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming requests do not attempt model inference or prediction."""
    req_str = str(request).lower()
    prohibited = ["predict", "inference", "target", "label", "generate_prediction"]
    for p in prohibited:
        if p in req_str:
            return {
                "execution_allowed": False,
                "reason": f"Prohibited prediction command detected: {p}",
                "status": EXECUTION_BLOCKED_NO_PREDICTION,
            }
    return {
        "execution_allowed": False,
        "reason": "Model prediction disabled under Phase 149 contract layer.",
        "status": EXECUTION_BLOCKED_NO_PREDICTION,
    }


def build_monte_carlo_prediction_disabled_report(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the prediction disabled report DataFrame and summary."""
    rows: List[Dict[str, Any]] = [
        {
            "capability": "model_inference_and_prediction",
            "execution_allowed": profile.allow_model_predict,
            "policy_reference": "POLICY_PHASE_149_ZERO_PREDICTION",
            "status": EXECUTION_BLOCKED_NO_PREDICTION,
            "description": "Prohibits generating forward return forecasts, direction predictions, or target labels.",
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
