# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Deployment Disabled Module.

Documents and enforces prohibition against production deployment or live serving.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DISABLED_EXECUTION_DOMAIN,
    EXEC_CONTRACT_ONLY,
    STATUS_EVALUATION_CONTRACT_READY,
)

FORBIDDEN_DEPLOYMENT_TERMS = [
    "deploy_to_production",
    "production_deploy",
    "publish_prod",
    "go_live",
    "live_release",
]


def build_evaluation_deployment_disabled_report(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame report certifying deployment is disabled."""
    rows = [
        {
            "operation": "production_deployment",
            "is_disabled": True,
            "policy_code": EXEC_CONTRACT_ONLY,
            "reason": "Phase 151 is non-production research only; deployments are prohibited.",
            "status": STATUS_EVALUATION_CONTRACT_READY,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DISABLED_EXECUTION_DOMAIN,
        "operation": "production_deployment",
        "is_disabled": True,
        "status": EXEC_CONTRACT_ONLY,
        "non_signal": True,
    }
    return df, summary


def validate_no_evaluation_deployment_request(request: Dict[str, Any] | str) -> Dict[str, Any]:
    """Validate request to ensure no deployment was requested."""
    text_to_check = request if isinstance(request, str) else " ".join(str(v) for v in request.values())
    text_lower = text_to_check.lower()

    detected = [term for term in FORBIDDEN_DEPLOYMENT_TERMS if term in text_lower]
    is_blocked = len(detected) > 0

    return {
        "is_permitted": not is_blocked,
        "is_blocked": is_blocked,
        "detected_terms": detected,
        "status": "PASS" if not is_blocked else "DEPLOYMENT_BLOCKED",
        "policy_action": "ALLOW" if not is_blocked else "DEPLOYMENT_BLOCKED_BY_POLICY",
        "non_signal": True,
    }
