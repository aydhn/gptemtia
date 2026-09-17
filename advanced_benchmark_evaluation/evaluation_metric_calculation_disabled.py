# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Metric Calculation Disabled Module.

Documents and enforces prohibition against actual Sharpe, return, win-rate, alpha, or drawdown calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DISABLED_EXECUTION_DOMAIN,
    EXEC_BLOCKED_NO_METRIC_CALCULATION,
    STATUS_EVALUATION_CONTRACT_READY,
)

FORBIDDEN_METRIC_CALCULATION_TERMS = [
    "calculate_sharpe",
    "calculate_win_rate",
    "calculate_alpha",
    "calculate_beta",
    "calculate_return",
    "calculate_drawdown",
    "compute_metrics",
    "calculate_metrics",
    "compute_sharpe",
    "compute_alpha",
]


def build_evaluation_metric_calculation_disabled_report(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame report certifying metric calculation is disabled."""
    rows = [
        {
            "operation": "metric_calculation",
            "is_disabled": True,
            "policy_code": EXEC_BLOCKED_NO_METRIC_CALCULATION,
            "reason": "Phase 151 provides uncalculated metric placeholders only.",
            "status": STATUS_EVALUATION_CONTRACT_READY,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DISABLED_EXECUTION_DOMAIN,
        "operation": "metric_calculation",
        "is_disabled": True,
        "status": EXEC_BLOCKED_NO_METRIC_CALCULATION,
        "non_signal": True,
    }
    return df, summary


def validate_no_evaluation_metric_calculation_request(request: Dict[str, Any] | str) -> Dict[str, Any]:
    """Validate request to ensure no metric calculation was requested."""
    text_to_check = request if isinstance(request, str) else " ".join(str(v) for v in request.values())
    text_lower = text_to_check.lower()

    detected = [term for term in FORBIDDEN_METRIC_CALCULATION_TERMS if term in text_lower]
    is_blocked = len(detected) > 0

    return {
        "is_permitted": not is_blocked,
        "is_blocked": is_blocked,
        "detected_terms": detected,
        "status": "PASS" if not is_blocked else EXEC_BLOCKED_NO_METRIC_CALCULATION,
        "policy_action": "ALLOW" if not is_blocked else "CALCULATION_BLOCKED_BY_POLICY",
        "non_signal": True,
    }
