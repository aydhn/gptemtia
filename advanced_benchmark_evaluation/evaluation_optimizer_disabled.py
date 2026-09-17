# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Optimizer Disabled Module.

Documents and enforces prohibition against parameter optimization and curve-fitting sweeps.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DISABLED_EXECUTION_DOMAIN,
    EXEC_BLOCKED_NO_OPTIMIZER,
    STATUS_EVALUATION_CONTRACT_READY,
)

FORBIDDEN_OPTIMIZER_TERMS = [
    "optimize",
    "parameter_sweep",
    "grid_search",
    "genetic_optimizer",
    "curve_fit",
]


def build_evaluation_optimizer_disabled_report(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame report certifying optimizer execution is disabled."""
    rows = [
        {
            "operation": "optimizer_execution",
            "is_disabled": True,
            "policy_code": EXEC_BLOCKED_NO_OPTIMIZER,
            "reason": "Phase 151 evaluates pre-registered hypotheses; optimizer sweeps are prohibited.",
            "status": STATUS_EVALUATION_CONTRACT_READY,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DISABLED_EXECUTION_DOMAIN,
        "operation": "optimizer_execution",
        "is_disabled": True,
        "status": EXEC_BLOCKED_NO_OPTIMIZER,
        "non_signal": True,
    }
    return df, summary


def validate_no_evaluation_optimizer_request(request: Dict[str, Any] | str) -> Dict[str, Any]:
    """Validate request to ensure no optimizer execution was requested."""
    text_to_check = request if isinstance(request, str) else " ".join(str(v) for v in request.values())
    text_lower = text_to_check.lower()

    detected = [term for term in FORBIDDEN_OPTIMIZER_TERMS if term in text_lower]
    is_blocked = len(detected) > 0

    return {
        "is_permitted": not is_blocked,
        "is_blocked": is_blocked,
        "detected_terms": detected,
        "status": "PASS" if not is_blocked else EXEC_BLOCKED_NO_OPTIMIZER,
        "policy_action": "ALLOW" if not is_blocked else "OPTIMIZER_BLOCKED_BY_POLICY",
        "non_signal": True,
    }
