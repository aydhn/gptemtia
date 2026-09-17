# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Model Training Disabled Module.

Documents and enforces prohibition against fitting or training machine learning models.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DISABLED_EXECUTION_DOMAIN,
    EXEC_BLOCKED_NO_MODEL_TRAINING,
    STATUS_EVALUATION_CONTRACT_READY,
)

FORBIDDEN_TRAINING_TERMS = [
    "train_model",
    "model_fit",
    "fit_model",
    "retrain",
    "fine_tune",
]


def build_evaluation_model_training_disabled_report(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame report certifying model training is disabled."""
    rows = [
        {
            "operation": "model_training",
            "is_disabled": True,
            "policy_code": EXEC_BLOCKED_NO_MODEL_TRAINING,
            "reason": "Phase 151 is strictly an evaluation report contract layer; model training is prohibited.",
            "status": STATUS_EVALUATION_CONTRACT_READY,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DISABLED_EXECUTION_DOMAIN,
        "operation": "model_training",
        "is_disabled": True,
        "status": EXEC_BLOCKED_NO_MODEL_TRAINING,
        "non_signal": True,
    }
    return df, summary


def validate_no_evaluation_model_training_request(request: Dict[str, Any] | str) -> Dict[str, Any]:
    """Validate request to ensure no model training was requested."""
    text_to_check = request if isinstance(request, str) else " ".join(str(v) for v in request.values())
    text_lower = text_to_check.lower()

    detected = [term for term in FORBIDDEN_TRAINING_TERMS if term in text_lower]
    is_blocked = len(detected) > 0

    return {
        "is_permitted": not is_blocked,
        "is_blocked": is_blocked,
        "detected_terms": detected,
        "status": "PASS" if not is_blocked else EXEC_BLOCKED_NO_MODEL_TRAINING,
        "policy_action": "ALLOW" if not is_blocked else "TRAINING_BLOCKED_BY_POLICY",
        "non_signal": True,
    }
