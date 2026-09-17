# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Prediction Disabled Module.

Documents and enforces prohibition against generating predictions or target labels.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DISABLED_EXECUTION_DOMAIN,
    EXEC_BLOCKED_NO_PREDICTION,
    STATUS_EVALUATION_CONTRACT_READY,
)

FORBIDDEN_PREDICTION_TERMS = [
    "generate_prediction",
    "model_predict",
    "target_label",
    "run_inference",
    "forward_prediction",
]


def build_evaluation_prediction_disabled_report(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame report certifying prediction generation is disabled."""
    rows = [
        {
            "operation": "prediction_generation",
            "is_disabled": True,
            "policy_code": EXEC_BLOCKED_NO_PREDICTION,
            "reason": "Phase 151 defines evaluation contracts only; prediction generation is prohibited.",
            "status": STATUS_EVALUATION_CONTRACT_READY,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DISABLED_EXECUTION_DOMAIN,
        "operation": "prediction_generation",
        "is_disabled": True,
        "status": EXEC_BLOCKED_NO_PREDICTION,
        "non_signal": True,
    }
    return df, summary


def validate_no_evaluation_prediction_request(request: Dict[str, Any] | str) -> Dict[str, Any]:
    """Validate request to ensure no prediction generation was requested."""
    text_to_check = request if isinstance(request, str) else " ".join(str(v) for v in request.values())
    text_lower = text_to_check.lower()

    detected = [term for term in FORBIDDEN_PREDICTION_TERMS if term in text_lower]
    is_blocked = len(detected) > 0

    return {
        "is_permitted": not is_blocked,
        "is_blocked": is_blocked,
        "detected_terms": detected,
        "status": "PASS" if not is_blocked else EXEC_BLOCKED_NO_PREDICTION,
        "policy_action": "ALLOW" if not is_blocked else "PREDICTION_BLOCKED_BY_POLICY",
        "non_signal": True,
    }
