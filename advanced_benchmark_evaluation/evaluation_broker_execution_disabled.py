# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Broker Execution Disabled Module.

Documents and enforces prohibition against broker integration and order routing.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DISABLED_EXECUTION_DOMAIN,
    EXEC_BLOCKED_NO_BROKER,
    STATUS_EVALUATION_CONTRACT_READY,
)

FORBIDDEN_BROKER_TERMS = [
    "broker_order",
    "broker_api",
    "connect_broker",
    "transmit_order",
    "fix_gateway",
    "interactive_brokers",
]


def build_evaluation_broker_execution_disabled_report(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame report certifying broker execution is disabled."""
    rows = [
        {
            "operation": "broker_execution",
            "is_disabled": True,
            "policy_code": EXEC_BLOCKED_NO_BROKER,
            "reason": "Phase 151 operates strictly offline; broker connections are prohibited.",
            "status": STATUS_EVALUATION_CONTRACT_READY,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DISABLED_EXECUTION_DOMAIN,
        "operation": "broker_execution",
        "is_disabled": True,
        "status": EXEC_BLOCKED_NO_BROKER,
        "non_signal": True,
    }
    return df, summary


def validate_no_evaluation_broker_execution_request(request: Dict[str, Any] | str) -> Dict[str, Any]:
    """Validate request to ensure no broker connection or order routing was requested."""
    text_to_check = request if isinstance(request, str) else " ".join(str(v) for v in request.values())
    text_lower = text_to_check.lower()

    detected = [term for term in FORBIDDEN_BROKER_TERMS if term in text_lower]
    is_blocked = len(detected) > 0

    return {
        "is_permitted": not is_blocked,
        "is_blocked": is_blocked,
        "detected_terms": detected,
        "status": "PASS" if not is_blocked else EXEC_BLOCKED_NO_BROKER,
        "policy_action": "ALLOW" if not is_blocked else "BROKER_BLOCKED_BY_POLICY",
        "non_signal": True,
    }
