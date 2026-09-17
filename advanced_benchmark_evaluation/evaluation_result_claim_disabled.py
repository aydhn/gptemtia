# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Result Claim Disabled Module.

Documents and enforces prohibition against generating result or performance claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DISABLED_EXECUTION_DOMAIN,
    EXEC_BLOCKED_NO_RESULT_CLAIM,
    STATUS_EVALUATION_CONTRACT_READY,
)

FORBIDDEN_CLAIM_TERMS = [
    "performance_claim",
    "result_claim",
    "guaranteed_return",
    "proven_strategy",
    "market_beating",
    "risk_free_profit",
]


def build_evaluation_result_claim_disabled_report(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame report certifying result claims are disabled."""
    rows = [
        {
            "operation": "result_claim_generation",
            "is_disabled": True,
            "policy_code": EXEC_BLOCKED_NO_RESULT_CLAIM,
            "reason": "Phase 151 prohibits promotional or definitive result claims.",
            "status": STATUS_EVALUATION_CONTRACT_READY,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DISABLED_EXECUTION_DOMAIN,
        "operation": "result_claim_generation",
        "is_disabled": True,
        "status": EXEC_BLOCKED_NO_RESULT_CLAIM,
        "non_signal": True,
    }
    return df, summary


def validate_no_evaluation_result_claim_request(request: Dict[str, Any] | str) -> Dict[str, Any]:
    """Validate request to ensure no result claim generation was requested."""
    text_to_check = request if isinstance(request, str) else " ".join(str(v) for v in request.values())
    text_lower = text_to_check.lower()

    detected = [term for term in FORBIDDEN_CLAIM_TERMS if term in text_lower]
    is_blocked = len(detected) > 0

    return {
        "is_permitted": not is_blocked,
        "is_blocked": is_blocked,
        "detected_terms": detected,
        "status": "PASS" if not is_blocked else EXEC_BLOCKED_NO_RESULT_CLAIM,
        "policy_action": "ALLOW" if not is_blocked else "CLAIM_BLOCKED_BY_POLICY",
        "non_signal": True,
    }
