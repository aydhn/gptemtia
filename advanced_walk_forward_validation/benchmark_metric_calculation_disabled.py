# -*- coding: utf-8 -*-
"""Phase 147: Benchmark Metric Calculation Disabled Report.

Documents and strictly enforces the disabled state of benchmark metric calculations.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_benchmark_metric_calculation_disabled_report(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled benchmark metric calculation."""
    rows = [
        {
            "calculation_target": "alpha_calculation_engine",
            "is_blocked": True,
            "reason": "Gercek alfa hesaplamasi Phase 147 sozlesme fazinda devre disidir.",
            "enforced": True,
            "non_signal": True,
        },
        {
            "calculation_target": "information_ratio_engine",
            "is_blocked": True,
            "reason": "Information ratio ve tracking error hesaplamasi devre disidir.",
            "enforced": True,
            "non_signal": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_blocked_calculations": len(df),
        "all_blocked": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_benchmark_metric_calculation_request(
    request: Union[Dict[str, Any], str],
) -> Dict[str, Any]:
    """Validate that request does not attempt benchmark metric calculation."""
    req_str = request if isinstance(request, str) else str(request.get("command", ""))
    req_lower = req_str.lower()
    blocked_keywords = ["calculate_alpha", "calculate_sharpe", "calculate_benchmark"]
    is_blocked = any(k in req_lower for k in blocked_keywords)
    return {
        "request": req_str,
        "is_safe": not is_blocked,
        "is_blocked": is_blocked,
        "message": "Metrik hesaplama istegi engellendi." if is_blocked else "Talep guvenli.",
        "non_signal": True,
    }
