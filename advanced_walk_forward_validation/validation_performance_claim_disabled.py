# -*- coding: utf-8 -*-
"""Phase 147: Validation Performance Claim Disabled Report.

Documents and strictly enforces the prohibition against generating performance guarantees,
Sharpe claims, win-rate promises, or production-ready marketing.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_validation_performance_claim_disabled_report(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for prohibited performance claims."""
    rows = [
        {
            "prohibited_claim": "guaranteed_future_return",
            "is_blocked": True,
            "reason": "Gelecek getiri veya kesin kazanc garantisi iddiasi kanunen ve sistemce yasaktir.",
            "enforced": True,
            "non_signal": True,
        },
        {
            "prohibited_claim": "production_or_broker_readiness_approval",
            "is_blocked": True,
            "reason": "Sozlesme katmani basarili diye sisteme canli/broker onayi verilemez.",
            "enforced": True,
            "non_signal": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_prohibited_claims": len(df),
        "all_blocked": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_validation_performance_claim_request(
    request: Union[Dict[str, Any], str],
) -> Dict[str, Any]:
    """Validate that text or request does not contain prohibited performance claims."""
    req_str = request if isinstance(request, str) else str(request.get("text", ""))
    req_lower = req_str.lower()
    blocked_keywords = [
        "guaranteed_return",
        "sharpe_claim",
        "win_rate_claim",
        "production_ready",
        "broker_ready",
        "official_approval",
    ]
    is_blocked = any(k in req_lower for k in blocked_keywords)
    return {
        "request": req_str,
        "is_safe": not is_blocked,
        "is_blocked": is_blocked,
        "message": "Yasakli performans iddiasi engellendi." if is_blocked else "Icerik guvenli.",
        "non_signal": True,
    }
