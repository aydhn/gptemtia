# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Strategy Approval Disabled Module.

Documents and enforces prohibition against approving strategies or allocating capital.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DISABLED_EXECUTION_DOMAIN,
    EXEC_BLOCKED_NO_STRATEGY_APPROVAL,
    STATUS_EVALUATION_CONTRACT_READY,
)

FORBIDDEN_APPROVAL_TERMS = [
    "approve_strategy",
    "strategy_approved",
    "allocate_capital",
    "position_size",
    "portfolio_construct",
    "production_ready",
    "broker_ready",
]


def build_evaluation_strategy_approval_disabled_report(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame report certifying strategy approval is disabled."""
    rows = [
        {
            "operation": "strategy_approval",
            "is_disabled": True,
            "policy_code": EXEC_BLOCKED_NO_STRATEGY_APPROVAL,
            "reason": "Phase 151 does not grant commercial or trading approvals.",
            "status": STATUS_EVALUATION_CONTRACT_READY,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DISABLED_EXECUTION_DOMAIN,
        "operation": "strategy_approval",
        "is_disabled": True,
        "status": EXEC_BLOCKED_NO_STRATEGY_APPROVAL,
        "non_signal": True,
    }
    return df, summary


def validate_no_strategy_approval_request(request: Dict[str, Any] | str) -> Dict[str, Any]:
    """Validate request to ensure no strategy approval was requested."""
    text_to_check = request if isinstance(request, str) else " ".join(str(v) for v in request.values())
    text_lower = text_to_check.lower()

    detected = [term for term in FORBIDDEN_APPROVAL_TERMS if term in text_lower]
    is_blocked = len(detected) > 0

    return {
        "is_permitted": not is_blocked,
        "is_blocked": is_blocked,
        "detected_terms": detected,
        "status": "PASS" if not is_blocked else EXEC_BLOCKED_NO_STRATEGY_APPROVAL,
        "policy_action": "ALLOW" if not is_blocked else "APPROVAL_BLOCKED_BY_POLICY",
        "non_signal": True,
    }
