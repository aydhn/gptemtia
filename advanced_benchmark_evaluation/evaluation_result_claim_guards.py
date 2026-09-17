# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Result Claim Guards Module.

Guards against premature, unproven, or misleading backtest and benchmark result claims.
"""

import re
from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_CLAIM_GUARD_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

FORBIDDEN_RESULT_CLAIM_PATTERNS = [
    r"guaranteed_return",
    r"proven_alpha",
    r"actual_sharpe",
    r"realized_win_rate",
    r"live_profit",
    r"risk_free_profit",
    r"claim_return",
    r"proven_strategy",
    r"guaranteed_profit",
    r"risk_free_return",
    r"result_claim",
    r"performance_claim",
]

RESULT_CLAIM_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_RESULT_CLAIM_INTERCEPT",
        "guard_name": "Unproven Result Claim Interceptor",
        "detection_target": "guaranteed_or_actual_return_claims",
        "description": "Geçmiş simülasyonları kesin başarı veya ampirik kazanç gibi sunan ifadeleri engelleyen muhafız.",
    },
    {
        "guard_id": "GUARD_SHARPE_CLAIM_INTERCEPT",
        "guard_name": "Uncalculated Sharpe Ratio Claim Interceptor",
        "detection_target": "actual_sharpe_claims",
        "description": "Hesaplanmamış Sharpe veya risk metriklerinin kesin iddia olarak sunulmasını engelleyen muhafız.",
    },
]


def build_evaluation_result_claim_guard_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of result claim guards."""
    rows: List[Dict[str, Any]] = []

    for g in RESULT_CLAIM_GUARDS:
        rows.append(
            {
                "guard_id": g["guard_id"],
                "guard_name": g["guard_name"],
                "detection_target": g["detection_target"],
                "description": g["description"],
                "is_active": True,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_CLAIM_GUARD_DOMAIN,
        "total_guards": len(df),
        "all_active": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary


def validate_evaluation_result_claim_request(request: Dict[str, Any] | str) -> Dict[str, Any]:
    """Validate a request text or dictionary to ensure no forbidden result claim is present."""
    text_to_check = ""
    if isinstance(request, str):
        text_to_check = request
    elif isinstance(request, dict):
        text_to_check = " ".join(str(v) for v in request.values()) + " " + " ".join(request.keys())

    text_lower = text_to_check.lower()
    matched_patterns: List[str] = []

    for pat in FORBIDDEN_RESULT_CLAIM_PATTERNS:
        if re.search(pat, text_lower):
            matched_patterns.append(pat)

    is_clean = len(matched_patterns) == 0
    return {
        "is_clean": is_clean,
        "claim_detected": not is_clean,
        "matched_patterns": matched_patterns,
        "status": "PASS" if is_clean else "BLOCKED_BY_CLAIM_GUARD",
        "policy_action": "ALLOW" if is_clean else "CLAIM_BLOCKED_BY_POLICY",
        "non_signal": True,
    }
