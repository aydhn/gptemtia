# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Strategy Approval Guards Module.

Guards against premature strategy approval, capital allocation,
portfolio construction, and position sizing during evaluation.
"""

import re
from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_STRATEGY_APPROVAL_GUARD_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

FORBIDDEN_APPROVAL_PATTERNS = [
    r"approve_strategy",
    r"strategy_approved",
    r"approved_strategy",
    r"allocate_capital",
    r"capital_allocation",
    r"portfolio_construction",
    r"portfolio_construct",
    r"position_size",
    r"position_sizing",
    r"production_ready",
    r"broker_ready",
    r"live_trading_approval",
    r"official_approval",
]

STRATEGY_APPROVAL_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_STRATEGY_APPROVAL_LOCK",
        "guard_name": "Zero Strategy Approval Enforcement Guard",
        "detection_target": "strategy_approval_requests",
        "description": "Değerlendirme raporu hazır diye stratejiye otomatik onay verilmesini engelleyen muhafız.",
    },
    {
        "guard_id": "GUARD_CAPITAL_ALLOCATION_LOCK",
        "guard_name": "Zero Capital Allocation Enforcement Guard",
        "detection_target": "capital_allocation_and_sizing_requests",
        "description": "Değerlendirme skorlarına dayanarak fon tahsisi veya lot büyüklüğü belirlenmesini engelleyen muhafız.",
    },
]


def build_evaluation_strategy_approval_guard_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of strategy approval guards."""
    rows: List[Dict[str, Any]] = []

    for g in STRATEGY_APPROVAL_GUARDS:
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
        "domain": LABEL_STRATEGY_APPROVAL_GUARD_DOMAIN,
        "total_guards": len(df),
        "all_active": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary


def validate_evaluation_strategy_approval_request(request: Dict[str, Any] | str) -> Dict[str, Any]:
    """Validate request to ensure no strategy approval or capital allocation is attempted."""
    text_to_check = ""
    if isinstance(request, str):
        text_to_check = request
    elif isinstance(request, dict):
        text_to_check = " ".join(str(v) for v in request.values()) + " " + " ".join(request.keys())

    text_lower = text_to_check.lower()
    matched_patterns: List[str] = []

    for pat in FORBIDDEN_APPROVAL_PATTERNS:
        if re.search(pat, text_lower):
            matched_patterns.append(pat)

    is_clean = len(matched_patterns) == 0
    return {
        "is_clean": is_clean,
        "approval_detected": not is_clean,
        "matched_patterns": matched_patterns,
        "status": "PASS" if is_clean else "BLOCKED_BY_APPROVAL_GUARD",
        "policy_action": "ALLOW" if is_clean else "APPROVAL_BLOCKED_BY_POLICY",
        "non_signal": True,
    }
