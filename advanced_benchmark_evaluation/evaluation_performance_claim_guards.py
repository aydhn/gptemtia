# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Performance Claim Guards Module.

Guards against commercial, promotional, or unverified performance claims.
"""

import re
from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_CLAIM_GUARD_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

FORBIDDEN_PERFORMANCE_PATTERNS = [
    r"high_performance_guarantee",
    r"superior_alpha_proven",
    r"market_beating_guarantee",
    r"zero_drawdown_claim",
    r"actual_win_rate",
    r"commercial_ready",
    r"institutional_grade_approval",
    r"production_alpha",
    r"live_ready",
    r"performance_claim",
]

PERFORMANCE_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_PROMOTIONAL_CLAIM",
        "guard_name": "Promotional Performance Claim Guard",
        "detection_target": "market_beating_or_superior_alpha_claims",
        "description": "Modeli üstün veya piyasayı yenen kesin bir strateji gibi lanse eden iddiaları engelleyen muhafız.",
    },
    {
        "guard_id": "GUARD_UNVERIFIED_WIN_RATE",
        "guard_name": "Unverified Win-Rate Claim Guard",
        "detection_target": "actual_win_rate_assertions",
        "description": "Örneklem dışı doğrulanmamış kazanma oranı iddialarını engelleyen muhafız.",
    },
]


def build_evaluation_performance_claim_guard_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of performance claim guards."""
    rows: List[Dict[str, Any]] = []

    for g in PERFORMANCE_GUARDS:
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


def validate_evaluation_performance_claim_request(request: Dict[str, Any] | str) -> Dict[str, Any]:
    """Validate request to ensure no forbidden performance claim is present."""
    text_to_check = ""
    if isinstance(request, str):
        text_to_check = request
    elif isinstance(request, dict):
        text_to_check = " ".join(str(v) for v in request.values()) + " " + " ".join(request.keys())

    text_lower = text_to_check.lower()
    matched_patterns: List[str] = []

    for pat in FORBIDDEN_PERFORMANCE_PATTERNS:
        if re.search(pat, text_lower):
            matched_patterns.append(pat)

    is_clean = len(matched_patterns) == 0
    return {
        "is_clean": is_clean,
        "claim_detected": not is_clean,
        "matched_patterns": matched_patterns,
        "status": "PASS" if is_clean else "BLOCKED_BY_PERFORMANCE_CLAIM_GUARD",
        "policy_action": "ALLOW" if is_clean else "CLAIM_BLOCKED_BY_POLICY",
        "non_signal": True,
    }
