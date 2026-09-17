# -*- coding: utf-8 -*-
"""Phase 147: Validation Broker Execution Disabled Report.

Documents and strictly enforces the disabled state of broker integration and execution.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_validation_broker_execution_disabled_report(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled broker execution."""
    rows = [
        {
            "execution_target": "broker_api_client",
            "is_blocked": True,
            "reason": "Broker API entegrasyonu ve otomatik hesap islemleri kesinlikle yasaktir.",
            "enforced": True,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_blocked_broker": len(df),
        "all_blocked": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_validation_broker_execution_request(
    request: Union[Dict[str, Any], str],
) -> Dict[str, Any]:
    """Validate that request does not attempt broker operations."""
    req_str = request if isinstance(request, str) else str(request.get("command", ""))
    req_lower = req_str.lower()
    blocked_keywords = ["broker_order", "broker_connect", "broker_auth", "place_order"]
    is_blocked = any(k in req_lower for k in blocked_keywords)
    return {
        "request": req_str,
        "is_safe": not is_blocked,
        "is_blocked": is_blocked,
        "message": "Broker islemi istegi engellendi." if is_blocked else "Talep guvenli.",
        "non_signal": True,
    }
